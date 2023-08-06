import types
from itertools import chain

from django.db.models.aggregates import Avg, Count, StdDev, Variance
from django.db.models.expressions import Exists, OrderBy, Ref, Value
from django.db.models.functions import ConcatPair, Greatest, Least, Length, StrIndex, Substr
from django.db.models.sql import compiler
from django.db.transaction import TransactionManagementError
from django.db.utils import DatabaseError, NotSupportedError


def _as_sql_agv(self, compiler, connection):
    return self.as_sql(compiler, connection, template='%(function)s(CONVERT(float, %(field)s))')

def _as_sql_concatpair(self, compiler, connection):
    return self.as_sql(compiler, connection)


def _as_sql_count(self, compiler, connection):
    return self.as_sql(compiler, connection, function='COUNT_BIG')

def _as_sql_greatest(self, compiler, connection):
    # SQL Server does not provide GREATEST function,
    # so we emulate it with a table value constructor
    # https://msdn.microsoft.com/en-us/library/dd776382.aspx
    template='(SELECT MAX(value) FROM (VALUES (%(expressions)s)) AS _%(function)s(value))'
    return self.as_sql(compiler, connection, arg_joiner='), (', template=template)

def _as_sql_least(self, compiler, connection):
    # SQL Server does not provide LEAST function,
    # so we emulate it with a table value constructor
    # https://msdn.microsoft.com/en-us/library/dd776382.aspx
    template='(SELECT MIN(value) FROM (VALUES (%(expressions)s)) AS _%(function)s(value))'
    return self.as_sql(compiler, connection, arg_joiner='), (', template=template)

def _as_sql_length(self, compiler, connection):
    return self.as_sql(compiler, connection, function='LEN')

def _as_sql_exists(self, compiler, connection, template=None, **extra_context):
    # MS SQL doesn't allow EXISTS() in the SELECT list, so wrap it with a
    # CASE WHEN expression. Change the template since the When expression
    # requires a left hand side (column) to compare against.
    sql, params = self.as_sql(compiler, connection, template, **extra_context)
    sql = 'CASE WHEN {} THEN 1 ELSE 0 END'.format(sql)
    return sql, params

def _as_sql_order_by(self, compiler, connection):
    template = None
    if self.nulls_last:
        template = 'CASE WHEN %(expression)s IS NULL THEN 1 ELSE 0 END, %(expression)s %(ordering)s'
    if self.nulls_first:
        template = 'CASE WHEN %(expression)s IS NULL THEN 0 ELSE 1 END, %(expression)s %(ordering)s'
    return self.as_sql(compiler, connection, template=template)

def _as_sql_stddev(self, compiler, connection):
    function = 'STDEV'
    if self.function == 'STDDEV_POP':
        function = '%sP' % function
    return self.as_sql(compiler, connection, function=function)

def _as_sql_strindex(self, compiler, connection):
    self.source_expressions.reverse()
    sql = self.as_sql(compiler, connection, function='CHARINDEX')
    self.source_expressions.reverse()
    return sql

def _as_sql_variance(self, compiler, connection):
    function = 'VAR'
    if self.function == 'VAR_POP':
        function = '%sP' % function
    return self.as_sql(compiler, connection, function=function)


class SQLCompiler(compiler.SQLCompiler):
    def as_sql(self, with_limits=True, with_col_aliases=False):
        if (with_limits and
            (self.query.high_mark is not None or self.query.low_mark) and
            not self.get_order_by()
        ):
            self.query.order_by = ['pk']
        return super().as_sql(with_limits, with_col_aliases)

    def compile(self, node, select_format=False):
        node = self._as_microsoft(node)
        return super().compile(node, select_format)

    def _as_microsoft(self, node):
        as_microsoft = None
        if isinstance(node, Avg):
            as_microsoft = _as_sql_agv
        elif isinstance(node, ConcatPair):
            as_microsoft = _as_sql_concatpair
        elif isinstance(node, Count):
            as_microsoft = _as_sql_count
        elif isinstance(node, Greatest):
            as_microsoft = _as_sql_greatest
        elif isinstance(node, Least):
            as_microsoft = _as_sql_least
        elif isinstance(node, Length):
            as_microsoft = _as_sql_length
        elif isinstance(node, Exists):
            as_microsoft = _as_sql_exists
        elif isinstance(node, OrderBy):
            as_microsoft = _as_sql_order_by
        elif isinstance(node, StdDev):
            as_microsoft = _as_sql_stddev
        elif isinstance(node, StrIndex):
            as_microsoft = _as_sql_strindex
        elif isinstance(node, Variance):
            as_microsoft = _as_sql_variance
        if as_microsoft:
            node = node.copy()
            node.as_microsoft = types.MethodType(as_microsoft, node)
        return node

class SQLInsertCompiler(compiler.SQLInsertCompiler, SQLCompiler):
    def as_sql(self):
        # We don't need quote_name_unless_alias() here, since these are all
        # going to be column names (so we can avoid the extra overhead).
        qn = self.connection.ops.quote_name
        opts = self.query.get_meta()
        result = ['INSERT INTO %s' % qn(opts.db_table)]

        has_fields = bool(self.query.fields)

        if has_fields:
            fields = self.query.fields
            result.append('(%s)' % ', '.join(qn(f.column) for f in fields))
            values_format = 'VALUES (%s)'
            value_rows = [
                [self.prepare_value(field, self.pre_save_val(field, obj)) for field in fields]
                for obj in self.query.objs
            ]
        else:
            values_format = '%s VALUES'
            # An empty object.
            value_rows = [[self.connection.ops.pk_default_value()] for _ in self.query.objs]
            fields = [None]

        # Currently the backends just accept values when generating bulk
        # queries and generate their own placeholders. Doing that isn't
        # necessary and it should be possible to use placeholders and
        # expressions in bulk inserts too.
        can_bulk = (not self.return_id and self.connection.features.has_bulk_insert) and has_fields

        placeholder_rows, param_rows = self.assemble_as_sql(fields, value_rows)

        if self.return_id and self.connection.features.can_return_id_from_insert:
            result.insert(0, 'SET NOCOUNT ON')
            result.append((values_format + ';') % ', '.join(placeholder_rows[0]))
            params = [param_rows[0]]
            result.append('SELECT CAST(SCOPE_IDENTITY() AS bigint)')
            return [(" ".join(result), tuple(chain.from_iterable(params)))]

        if can_bulk:
            result.append(self.connection.ops.bulk_insert_sql(fields, placeholder_rows))
            sql = [(" ".join(result), tuple(p for ps in param_rows for p in ps))]
        else:
            sql = [
                (" ".join(result + [values_format % ", ".join(p)]), vals)
                for p, vals in zip(placeholder_rows, param_rows)
            ]

        if has_fields:
            if opts.auto_field is not None:
                # db_column is None if not explicitly specified by model field
                auto_field_column = opts.auto_field.db_column or opts.auto_field.column
                columns = [f.column for f in fields]
                if auto_field_column in columns:
                    id_insert_sql = []
                    table = qn(opts.db_table)
                    sql_format = 'SET IDENTITY_INSERT %s ON; %s; SET IDENTITY_INSERT %s OFF'
                    for q, p in sql:
                        id_insert_sql.append((sql_format % (table, q, table), p))
                    sql = id_insert_sql

        return sql


class SQLDeleteCompiler(compiler.SQLDeleteCompiler, SQLCompiler):
    pass


class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler):
    pass


class SQLAggregateCompiler(compiler.SQLAggregateCompiler, SQLCompiler):
    pass
