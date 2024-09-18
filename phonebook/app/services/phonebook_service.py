import csv

from app.models.contact import Contacts

class PhoneBookService:

    def __init__(self, db):
        self.contacts = Contacts(db)

    def add_contact(self, first_name, last_name, phone, email=None, address=None):
        """Add a new contact."""
        self.contacts.add_contact(first_name, last_name, phone, email, address)

    def update_contact(self, phone, **fields):
        """Update contact information."""
        self.contacts.update_contact(phone, **fields)

    def delete_contact(self, phone):
        """Delete a contact."""
        self.contacts.delete_contact(phone)

    def search_contact(self, search_term):
        """Search contacts by name or phone number."""
        return self.contacts.search_contact(search_term)

    def get_all_contacts(self):
        """Get all contacts."""
        return self.contacts.get_all_contacts()

    def bulk_add_contacts(self, records):
        """Bulk add contacts."""
        self.contacts.bulk_add(records)

    def bulk_add_contacts_from_csv(self, csv_file_path):
        """Bulk add contacts from a CSV file."""
        records = []
        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    records.append({
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'phone': row['phone'],
                        'email': row.get('email'),
                        'address': row.get('address')
                    })
            self.bulk_add(records)
        except Exception as e:
            print(f"Error reading or processing CSV file: {e}")
