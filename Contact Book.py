# Define the contact book dictionary to store contact details
contact_book = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter contact address: ")
    
    contact_book[name] = {
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    print(f"Contact '{name}' added successfully.")

# Function to view all contacts
def view_contacts():
    if contact_book:
        print("\n--- Contact List ---")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['Phone']}")
    else:
        print("No contacts available.")

# Function to search for a contact
def search_contact():
    search = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contact_book.items():
        if name == search or details['Phone'] == search:
            print(f"\n--- Contact Found ---")
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        print(f"\n--- Updating Contact '{name}' ---")
        phone = input("Enter new phone number (or press Enter to keep current): ")
        email = input("Enter new email address (or press Enter to keep current): ")
        address = input("Enter new address (or press Enter to keep current): ")

        if phone:
            contact_book[name]['Phone'] = phone
        if email:
            contact_book[name]['Email'] = email
        if address:
            contact_book[name]['Address'] = address

        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

# Main menu for the Contact Book
def contact_book_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the Contact Book application
contact_book_menu()
