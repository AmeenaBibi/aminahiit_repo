contacts = {}


def main():
    # ask the user for an option
    while True:
        print("""
                press 1 to add contact
                press 2 to view contact
                press 3 to search contact
                press 4 to remove contact
                press 5 to exit program
                """)

        resp = input("Select an option: ")
        # checks the user response
        if resp == "1":
            add_cont()
            continue
        elif resp == "2":
            view_cont()
            continue
        elif resp == "3":
            search_cont()
            continue
        elif resp == "4":
            rem_cont()
            continue
        elif resp == "5":
            break
        else:
            print("You have not made a valid choice")
            continue


# adds contacts to the phonebook
def add_cont():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {'name': name, 'phone': phone, 'email': email}
    print(contacts[name])


# view contacts in the phonebook
def view_cont():
    for name, info in contacts.items():
        print("Name", info['name'])
        print("Phone", info['phone'])
        print("Email", info['email'])


# search contatcs in the phonebook
def search_cont():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print("Name", info['name'])
        print("Phone", info['phone'])
        print("Email", info['email'])
    else:
        print("Contact not found")


# removes contacts from the phonebook
def rem_cont():
    name = input("Enter contact name to remove: ")
    if name in contacts:
        del contacts[name]
        print("You have successfully removed contact")
    else:
        print("Contact not found")


main()
