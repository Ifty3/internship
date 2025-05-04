contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts yet.\n")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_name = input("Enter name to search: ")
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            return
    print("Contact not found.\n")

def update_contact():
    search_name = input("Enter name to update: ")
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    search_name = input("Enter name to delete: ")
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            contacts.remove(contact)
            print("Contact deleted!\n")
            return
    print("Contact not found.\n")

def main():
    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
