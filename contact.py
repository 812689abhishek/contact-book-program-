contacts = {}

def add_contact():
    """Add a new contact"""
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    
    contact = {
        "phone_number": phone_number,
        "email": email,
        "address": address
    }
    
    
    contacts[name] = contact
    
    print(f"Contact '{name}' added successfully!")

def view_contact_list():
    """Display a list of all saved contacts"""
    if not contacts:
        print("No contacts found!")
    else:
        print("Contact List:")
        for name, contact in contacts.items():
            print(f"{name}: {contact['phone_number']}")

def search_contact():
    """Search for a contact by name or phone number"""
    search_term = input("Enter name or phone number to search: ")
    
    for name, contact in contacts.items():
        if search_term.lower() in name.lower() or search_term in contact["phone_number"]:
            print(f"Contact found: {name} - {contact['phone_number']}")
            return
    
    print("Contact not found!")

def update_contact():
    """Update a contact's details"""
    name = input("Enter name of contact to update: ")
    
    if name in contacts:
        contact = contacts[name]
        print("Enter new details (press Enter to skip):")
        phone_number = input(f"Phone number ({contact['phone_number']}): ")
        email = input(f"Email ({contact['email']}): ")
        address = input(f"Address ({contact['address']}): ")
        
        if phone_number:
            contact["phone_number"] = phone_number
        if email:
            contact["email"] = email
        if address:
            contact["address"] = address
        
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    """Delete a contact"""
    name = input("Enter name of contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found!")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
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
            print("Invalid choice. Please try again.")
