"""
@Time ： 2024-09-16
@Auth ： Adam Lyu
"""
from phonebook.app.services.phonebook_service import PhoneBookService


def main_menu():
    print("\nPhone Book Manager")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    return input("Choose an option: ")


def handle_add_contact(service):
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    phone = input("Phone number: ").strip()
    email = input("Email (optional): ").strip() or None
    address = input("Address (optional): ").strip() or None
    service.add_contact(first_name, last_name, phone, email, address)


def handle_view_contacts(service):
    contacts = service.get_all_contacts()
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")


def handle_search_contact(service):
    search_term = input("Enter search term (name or phone): ").strip()
    results = service.search_contact(search_term)
    if results:
        for contact in results:
            print(contact)
    else:
        print("No matching contacts found.")


def handle_update_contact(service):
    phone = input("Enter phone number of the contact to update: ").strip()
    if not phone:
        print("Phone number is required to update contact.")
        return
    first_name = input("New first name (leave empty to skip): ").strip() or None
    last_name = input("New last name (leave empty to skip): ").strip() or None
    email = input("New email (leave empty to skip): ").strip() or None
    address = input("New address (leave empty to skip): ").strip() or None
    service.update_contact(phone, first_name=first_name, last_name=last_name, email=email, address=address)


def handle_delete_contact(service):
    phone = input("Enter phone number of the contact to delete: ").strip()
    if phone:
        service.delete_contact(phone)
    else:
        print("Phone number is required to delete contact.")


def main():
    try:
        service = PhoneBookService()
        while True:
            option = main_menu()
            if option == "1":
                handle_add_contact(service)
            elif option == "2":
                handle_view_contacts(service)
            elif option == "3":
                handle_search_contact(service)
            elif option == "4":
                handle_update_contact(service)
            elif option == "5":
                handle_delete_contact(service)
            elif option == "6":
                break
            else:
                print("Invalid option")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
