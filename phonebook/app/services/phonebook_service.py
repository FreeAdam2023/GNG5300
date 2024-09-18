import csv
from phonebook.app.models.contact import Contacts
from phonebook.utils.utils import error_reporter


class PhoneBookService:

    def __init__(self):
        self.contacts = Contacts()

    @error_reporter
    def add_contact(self, first_name, last_name, phone, email=None, address=None):
        """Add a new contact and display the result."""
        new_data = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.add(**new_data)

        # Display the newly added contact
        print("\nNew contact added successfully:")
        self._display_contact(new_data)

    @error_reporter
    def update_contact(self, phone, **fields):
        """Update contact information."""
        self.contacts.update(phone, **fields)

    @error_reporter
    def delete_contact(self, phone):
        """Delete a contact."""
        self.contacts.delete(phone)

    @error_reporter
    def search_contact(self, search_term):
        """Search contacts by name or phone number."""
        results = self.contacts.search_contact(search_term)
        if results:
            print("\nSearch Results:")
            for contact in results:
                self._display_contact(contact)
        else:
            print(f"No contacts found for search term: {search_term}")
        return results

    @error_reporter
    def get_all_contacts(self, limit=10, offset=0):
        """Get all contacts with pagination support and display them."""
        contacts = self.contacts.get_all_contacts(limit=limit, offset=offset)
        if contacts:
            print("\nAll contacts:")
            for contact in contacts:
                self._display_contact(contact)
        else:
            print("No contacts found.")
        return contacts

    @error_reporter
    def bulk_add_contacts(self, records):
        """Bulk add contacts."""
        self.contacts.bulk_add(records)

    @error_reporter
    def bulk_add_contacts_from_csv(self, csv_file_path):
        """Bulk add contacts from a CSV file with detailed error reporting."""
        records = self._parse_csv(csv_file_path)
        if records:
            self.bulk_add_contacts(records)
        else:
            print("No valid records found to add.")

    @error_reporter
    def _parse_csv(self, csv_file_path):
        """Helper method to parse CSV and validate records."""
        records = []
        required_fields = {'first_name', 'last_name', 'phone'}

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Validate CSV headers
            if not required_fields.issubset(reader.fieldnames):
                raise ValueError(f"CSV file is missing required headers: {required_fields - set(reader.fieldnames)}")

            for row in reader:
                # Ensure required fields are present in each row
                if not all(row[field] for field in required_fields):
                    print(f"Skipping row with missing required data: {row}")
                    continue

                records.append({
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'phone': row['phone'],
                    'email': row.get('email'),
                    'address': row.get('address')
                })

        return records

    def _display_contact(self, contact):
        """Helper to format and display a single contact."""
        print(f"Name: {contact['first_name']} {contact['last_name']}")
        print(f"Phone: {contact['phone']}")
        if contact['email']:
            print(f"Email: {contact['email']}")
        if contact['address']:
            print(f"Address: {contact['address']}")
        print("-" * 40)  # Separator for visual clarity
