import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split('|')
                contacts.append({"name": name, "phone": phone, "email": email})
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to show.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= choice < len(contacts):
            contacts[choice]['name'] = input("New name: ")
            contacts[choice]['phone'] = input("New phone number: ")
            contacts[choice]['email'] = input("New email address: ")
            print("Contact updated!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= choice < len(contacts):
            removed = contacts.pop(choice)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        option = input("Choose an option (1-5): ")

        if option == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif option == '2':
            view_contacts(contacts)
        elif option == '3':
            edit_contact(contacts)
            save_contacts(contacts)
        elif option == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif option == '5':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
