class ContactBook:
    def __init__(self,name,phoneNumber,city):
        self.name = name
        self.phoneNumber = phoneNumber
        self.city = city


class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def addContact(self):
        name = input("Enter the Name: ")
        phoneNumber = input("Enter the Phone Number: ")
        city = input("Enter the City: ")
        contact = ContactBook(name, phoneNumber, city)
        self.contacts.append(contact)

    def viewContacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phoneNumber}, City: {contact.city}")

    def deleteContact(self):
        name = input("Enter the Name to delete: ")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def updateContact(self):
        name = input("Enter the Name to update:")
        for contact in self.contacts:
            if contact.name == name:
                newPhoneNumber = input("Enter the new Phone Number: ")
                newName = input("Enter the new Name: ")
                newCity = input("Enter the new City: ")
                contact.name = newName
                contact.phoneNumber = newPhoneNumber
                contact.city = newCity
                print("Contact updated successfully.")
                return
        print("Contact not found.")


def main():
    manager = ContactManager()
    while True:
        print("""
        1. Add Contact
        2. View Contacts
        3. Update Contact
        4. Delete Contact
        5. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            manager.addContact()
        elif choice == '2':
            manager.viewContacts()
        elif choice == '3':
            manager.updateContact()
        elif choice == '4':
            manager.deleteContact()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()