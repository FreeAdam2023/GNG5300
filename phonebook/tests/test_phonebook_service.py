"""
@Time ： 2024-09-16
@Auth ： Adam Lyu
"""
import unittest
from app.services.phonebook_service import PhoneBookService
from data.database import Database

class TestPhoneBookService(unittest.TestCase):

    def setUp(self):
        self.db = Database(':memory:')
        self.service = PhoneBookService(self.db)

    def tearDown(self):
        self.db.close()

    def test_add_contact(self):
        self.service.add_contact("John", "Doe", "123456789", "john@example.com")
        contacts = self.service.get_all_contacts()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]['first_name'], 'John')

    def test_update_contact(self):
        self.service.add_contact("Jane", "Doe", "987654321")
        self.service.update_contact("987654321", first_name="Janet")
        updated_contact = self.service.search_contact("987654321")[0]
        self.assertEqual(updated_contact['first_name'], 'Janet')

    def test_delete_contact(self):
        self.service.add_contact("Jake", "Smith", "1122334455")
        self.service.delete_contact("1122334455")
        contacts = self.service.get_all_contacts()
        self.assertEqual(len(contacts), 0)

if __name__ == '__main__':
    unittest.main()
