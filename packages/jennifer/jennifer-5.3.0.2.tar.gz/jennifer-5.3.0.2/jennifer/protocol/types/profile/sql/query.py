from ... import remote_call
from ..profile_data import ProfileDataType


class Query(ProfileDataType):
    TYPE_DB_UNKNOWN = remote_call.TYPE_UNKNOWN_SQL_DATABASE
    TYPE_DB_ORACLE = remote_call.TYPE_ORACLE
    TYPE_DB_DB2 = remote_call.TYPE_DB2
    TYPE_DB_MYSQL = remote_call.TYPE_MYSQL
    TYPE_DB_POSTGRESQL = remote_call.TYPE_POSTGRESQL
    TYPE_DB_CUBRID = remote_call.TYPE_CUBRID
    TYPE_DB_MSSQL = remote_call.TYPE_MSSQL
    TYPE_DB_SOAP = remote_call.TYPE_SOAP

    TYPE_SQL_PSTMT_QUERY = 5
    TYPE_SQL_QUERY = 11
    TYPE_SQL_EXECUTE = 12

    def __init__(
            self,
            host='',
            port='',
            db=TYPE_DB_UNKNOWN,
            method=TYPE_SQL_QUERY,
            query_hash=0,
            error_hash=0,
            bind_params=[],
            inline_params=[],
            query='',
    ):
        ProfileDataType.__init__(self)
        self.error_hash = error_hash
        self.db = db
        self.host = host
        self.port = port
        self.method = method
        self.query_hash = query_hash
        self.bind_params = bind_params
        self.inline_params = inline_params
        self.query = query

    def get_type(self):
        return ProfileDataType.TYPE_SQL_EXEC
