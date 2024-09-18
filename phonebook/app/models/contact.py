from phonebook.data.crud import CrudOperations


class Contacts:

    def __init__(self):
        self.contacts = CrudOperations('contacts')
        self.create_contacts_table()

    def create_contacts_table(self):
        """
        Create contacts table if it does not exist.
        """
        query = '''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            email TEXT,
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        '''
        self.contacts.db.execute(query)

    def add_contact(self, first_name, last_name, phone, email=None, address=None):
        """
        Add a new contact to the table.
        """
        try:
            self.contacts.add(first_name=first_name, last_name=last_name, phone=phone, email=email, address=address)
        except Exception as e:
            print(f"Error adding contact: {e}")

    def update_contact(self, phone, **fields):
        """
        Update contact information based on phone number.
        """
        try:
            self.contacts.update(where={'phone': phone}, **fields)
        except Exception as e:
            print(f"Error updating contact: {e}")

    def delete_contact(self, phone):
        """
        Delete a contact by phone number.
        """
        try:
            self.contacts.delete(phone=phone)
        except Exception as e:
            print(f"Error deleting contact: {e}")

    def search_contact(self, search_term):
        """
        Search contacts by first name, last name, or phone number.
        """
        return self.contacts.search(search_term)

    def get_all_contacts(self):
        """
        Retrieve all contacts from the table.
        """
        return self.contacts.fetch_all()

    def bulk_add(self, records):
        """
        Bulk add multiple contact records in a single transaction.
        Args:
            records: List of dictionaries containing contact info.
        Example:
            [{'first_name': 'John', 'last_name': 'Doe', 'phone': '123456789', 'email': 'john@example.com'}]
        """
        if not records:
            return  # Return if no records

        try:
            self.contacts.db.conn.execute('BEGIN')

            columns = ['first_name', 'last_name', 'phone', 'email', 'address']
            query = f'''
            INSERT INTO contacts ({', '.join(columns)}, created_at)
            VALUES ({', '.join(['?' for _ in columns])}, CURRENT_TIMESTAMP)
            '''

            self.contacts.db.conn.executemany(query, [
                (record['first_name'], record['last_name'], record['phone'], record.get('email'), record.get('address'))
                for record in records
            ])

            self.contacts.db.conn.execute('COMMIT')
            print(f"Successfully added {len(records)} contacts.")

        except Exception as e:
            self.contacts.db.conn.execute('ROLLBACK')
            print(f"Error during bulk add: {e}")
