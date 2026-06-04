class contact:
    def __inti__(self,name,phoneNumber,city):
        self.name = name
        self.phoneNumber = phoneNumber
        self.city = city
        
    def add_contact(self):
        name = input("Enter the name :")
        phoneNumber = input("Enter the phoneNumber ")
        city = input("Enter the city ")
        with open("contacts.txt","a") as f:
            f.write(f"{name},{phoneNumber},{city}\n")

    def view_contacts(self):
        with open("contacts.txt","r") as f:
            contacts = f.read()
            print(contacts)

    def search_contact(self):
        name = input("Enter the name to search: ")
        with open("contacts.txt","r") as f:
            contacts = f.readlines()
            for contact in contacts:
                if name in contact:
                    print(contact)
                    return
            print("Contact not found.")

    def update_contact(self):
        name = input("Enter the name to update: ")
        with open("contacts.txt","r") as f:
            contacts = f.readlines()
            print(contacts)
        with open("contacts.txt","w") as f:
            for contact in contacts:
                if name in contact:
                    new_phoneNumber = input("Enter the new phone number: ")
                    new_city = input("Enter the new city: ")
                    f.write(f"{name},{new_phoneNumber},{new_city}\n")
                    print("Contact updated successfully.")
                else:
                    f.write(contact)
    def delete_contact(self):
        name = input("Enter the name to delete: ")
        with open("contacts.txt","r") as f:
            contacts = f.readlines()
        with open("contacts.txt","w") as f:
            for i , contact in enumerate(contacts):
                if name in contact:
                    del contacts[i]
                    continue
        with open("contacts.txt","w") as f:
            for contact in contacts:
                f.write(contact)
            
        
def main():
    print("""
    1. Add Contact
    2. View Contacts
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Exit""")
    while True:
        choice = input("Enter your choice: ")
        const = contact()
        if choice == '1':
            const.add_contact()
        elif choice == '2':
            const.view_contacts()
        elif choice == '3':
            const.search_contact()
        elif choice == '4':
            const.update_contact()
        elif choice == '5':
            const.delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()


