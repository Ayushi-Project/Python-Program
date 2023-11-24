class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        search_results = [
            contact for contact in self.contacts
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number
        ]

        if not search_results:
            print(f"No contacts found for '{search_term}'.")
        else:
            print("\nSearch Results:")
            for contact in search_results:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == old_name.lower():
                self.contacts[i] = new_contact
                print(f"Contact '{old_name}' updated successfully.")
                return

        print(f"No contact found with the name '{old_name}'.")

    def delete_contact(self, contact_name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != contact_name.lower()]
        print(f"Contact '{contact_name}' deleted successfully.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == "4":
            old_name = input("Enter the name of the contact to update: ")
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.update_contact(old_name, new_contact)

        elif choice == "5":
            contact_name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(contact_name)

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
