from phonebook.data.database import Database
from phonebook.utils.schema_parser import get_table_schema
from phonebook.utils.validators import validate_fields


class CrudOperations:
    def __init__(self, table: str):
        self.db = Database()
        self.table = table
        self.schema = get_table_schema(self.db, table)

    def transactional(func):
        """
        Transaction decorator to manage transaction lifecycle.
        """
        def wrapper(self, *args, **kwargs):
            try:
                self.db.connect()
                self.db.conn.execute('BEGIN TRANSACTION')
                result = func(self, *args, **kwargs)
                self.db.conn.commit()
                return result
            except Exception as e:
                self.db.conn.rollback()
                raise e
            finally:
                self.db.close()

        return wrapper

    @transactional
    def add(self, **fields):
        validate_fields(fields, self.schema)
        columns = ', '.join(fields.keys())
        placeholders = ', '.join('?' for _ in fields)
        query = f"INSERT INTO {self.table} ({columns}, created_at) VALUES ({placeholders}, CURRENT_TIMESTAMP)"
        self.db.execute(query, tuple(fields.values()))

    @transactional
    def update(self, where, **fields):
        validate_fields(fields, self.schema)
        set_clause = ', '.join(f"{k} = ?" for k in fields)
        where_clause = ' AND '.join(f"{k} = ?" for k in where)
        query = f"UPDATE {self.table} SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE {where_clause}"
        self.db.execute(query, tuple(fields.values()) + tuple(where.values()))

    @transactional
    def delete(self, **where):
        where_clause = ' AND '.join(f"{k} = ?" for k in where)
        query = f"DELETE FROM {self.table} WHERE {where_clause}"
        self.db.execute(query, tuple(where.values()))

    @transactional
    def bulk_add(self, records):
        if not records:
            return

        first_record = records[0]
        validate_fields(first_record, self.schema)

        columns = ', '.join(first_record.keys())
        placeholders = ', '.join('?' for _ in first_record)
        query = f"INSERT INTO {self.table} ({columns}, created_at) VALUES ({placeholders}, CURRENT_TIMESTAMP)"
        self.db.conn.executemany(query, [tuple(record.values()) for record in records])
