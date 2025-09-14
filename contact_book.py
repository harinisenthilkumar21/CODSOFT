import csv
import os

FILENAME = "contacts.csv"

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_list(self):
        return [self.name, self.phone, self.email]

def load_contacts():
    contacts = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    contacts.append(Contact(row[0], row[1], row[2]))
    return contacts

def save_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow(contact.to_list())

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = Contact(name, phone, email)
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contacts List ---")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact.name} | {contact.phone} | {contact.email}")

def search_contact(contacts):
    query = input("Enter name to search: ").lower()
    found = [c for c in contacts if query in c.name.lower()]
    if found:
        print("\n--- Search Results ---")
        for contact in found:
            print(f"{contact.name} | {contact.phone} | {contact.email}")
    else:
        print("No contact found.")

def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contacts[index] = Contact(name, phone, email)
            save_contacts(contacts)
            print("Contact updated!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"Contact '{removed.name}' deleted!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()