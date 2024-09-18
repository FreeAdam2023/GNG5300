from data.database import Database
from utils.schema_parser import get_table_schema
from utils.validators import validate_fields

class CrudOperations:
    def __init__(self, db: Database, table: str):
        # Initialize with database instance and table name
        self.db = db
        self.table = table
        self.schema = get_table_schema(db, table)  # Get table schema for validation

    def transactional(self, func):
        """
        Transaction decorator to manage transaction lifecycle.
        """
        def wrapper(*args, **kwargs):
            try:
                self.db.connect()  # Ensure the database is connected
                self.db.conn.execute('BEGIN TRANSACTION')  # Start transaction
                result = func(self, *args, **kwargs)  # Execute the main function
                self.db.conn.commit()  # Commit transaction if no errors
                return result
            except Exception as e:
                self.db.conn.rollback()  # Rollback transaction on error
                raise e  # Re-raise exception
            finally:
                self.db.close()  # Close the connection after operation
        return wrapper

    @transactional
    def add(self, **fields):
        """
        Add a single record to the table.
        """
        validate_fields(fields, self.schema)  # Validate the fields against the schema
        columns = ', '.join(fields.keys())  # Prepare column names
        placeholders = ', '.join('?' for _ in fields)  # Prepare placeholders for query
        query = f"INSERT INTO {self.table} ({columns}, created_at) VALUES ({placeholders}, CURRENT_TIMESTAMP)"
        self.db.execute(query, tuple(fields.values()))  # Execute the insert query

    @transactional
    def update(self, where, **fields):
        """
        Update existing record(s) in the table based on condition.
        """
        validate_fields(fields, self.schema)  # Validate the fields against the schema
        set_clause = ', '.join(f"{k} = ?" for k in fields)  # Prepare SET clause for query
        where_clause = ' AND '.join(f"{k} = ?" for k in where)  # Prepare WHERE clause
        query = f"UPDATE {self.table} SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE {where_clause}"
        self.db.execute(query, tuple(fields.values()) + tuple(where.values()))  # Execute update query

    @transactional
    def delete(self, **where):
        """
        Delete record(s) from the table based on condition.
        """
        where_clause = ' AND '.join(f"{k} = ?" for k in where)  # Prepare WHERE clause
        query = f"DELETE FROM {self.table} WHERE {where_clause}"  # Prepare delete query
        self.db.execute(query, tuple(where.values()))  # Execute delete query

    @transactional
    def bulk_add(self, records):
        """
        Add multiple records to the table in a single transaction.
        """
        if not records:
            return  # Return if no records to insert

        first_record = records[0]
        validate_fields(first_record, self.schema)  # Validate the first record

        columns = ', '.join(first_record.keys())  # Prepare column names
        placeholders = ', '.join('?' for _ in first_record)  # Prepare placeholders for query
        query = f"INSERT INTO {self.table} ({columns}, created_at) VALUES ({placeholders}, CURRENT_TIMESTAMP)"
        self.db.conn.executemany(query, [tuple(record.values()) for record in records])  # Batch insert records

    def fetch_all(self):
        """
        Fetch all records from the table.
        """
        query = f"SELECT * FROM {self.table}"  # Select all query
        return self.db.fetchall(query)  # Execute fetch all query

    def search(self, search_term):
        """
        Search records in the table by first_name, last_name, or phone.
        """
        pattern = f"%{search_term}%"  # Prepare search pattern for LIKE clause
        query = f"SELECT * FROM {self.table} WHERE first_name LIKE ? OR last_name LIKE ? OR phone LIKE ?"
        return self.db.fetchall(query, (pattern, pattern, pattern))  # Execute search query
