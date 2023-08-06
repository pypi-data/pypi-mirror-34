from django.db.backends.base.features import BaseDatabaseFeatures
from django.db.utils import InterfaceError


class DatabaseFeatures(BaseDatabaseFeatures):
    allow_sliced_subqueries = False
    can_introspect_small_integer_field = True
    can_return_id_from_insert = True
    can_use_chunked_reads = False
    for_update_after_from = True
    greatest_least_ignores_nulls = True
    has_real_datatype = True
    has_zoneinfo_database = False
    ignores_table_name_case = True
    ignores_quoted_identifier_case = True
    requires_literal_defaults = True
    requires_sqlparse_for_splitting = False
    supports_nullable_unique_constraints = False
    supports_paramstyle_pyformat = False
    supports_partially_nullable_unique_constraints = False
    supports_regex_backreferencing = False
    supports_sequence_reset = False
    supports_subqueries_in_group_by = False
    supports_temporal_subtraction = True
    supports_timezones = False
    supports_transactions = True

    uses_savepoints = True
    has_native_uuid_field = True
    has_select_for_update = False
    supports_table_check_constraints = False
    can_introspect_autofield = False
    supports_tablespaces = False
    supports_index_on_text_field = True
