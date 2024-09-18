"""
@Time ： 2024-09-16
@Auth ： Adam Lyu
"""
import unittest
from data.crud import CrudOperations
from data.database import Database

class TestCrudOperations(unittest.TestCase):

    def setUp(self):
        self.db = Database(':memory:')
        self.crud = CrudOperations(self.db, 'contacts')
        self.db.execute('''
        CREATE TABLE contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            email TEXT,
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')

    def tearDown(self):
        self.db.close()

    def test_add_contact(self):
        self.crud.add(first_name="John", last_name="Doe", phone="123456789", email="john@example.com")
        contacts = self.crud.fetch_all()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]['first_name'], 'John')

    def test_update_contact(self):
        self.crud.add(first_name="Jane", last_name="Doe", phone="987654321")
        self.crud.update(where={"phone": "987654321"}, first_name="Janet")
        updated_contact = self.crud.search("987654321")[0]
        self.assertEqual(updated_contact['first_name'], 'Janet')

    def test_delete_contact(self):
        self.crud.add(first_name="Jake", last_name="Smith", phone="1122334455")
        self.crud.delete(phone="1122334455")
        contacts = self.crud.fetch_all()
        self.assertEqual(len(contacts), 0)

if __name__ == '__main__':
    unittest.main()
