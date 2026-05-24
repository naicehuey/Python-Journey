import json

print("Hello Welcome To Phone book Service")

def save_contact(contacts):
    with open("contacts.json", "w") as filex:
        json.dump(contacts, filex)

def load_contacts():
    try:
        with open("contacts.json", "r") as filex:
         contacts = json.load(filex)
         return contacts
    except (FileNotFoundError, json.JSONDecodeError):
        return []

contacts = load_contacts()

def lines():
    print("=" *40)

def storage(contacts):
    lines()
    print("       Edit Contact")
    lines()
    x = input("Enter Contact Name: ").strip()
    y = input("Enter Number: ").strip()
    new = {
        "name": x,
        "phone": y,
        "favorite": False
    }

    for i, contact in enumerate(contacts, start=1):
        if new in contacts:
            if new["name"].lower() == x.lower():
                print("We have a dublicated name")
                return

            if new["phone"] == y:
                print("This number already exist")
                return

        contacts.append(new)
        print("You Have Entered a New Contact")

    print("We already have a contact with the same name or number")

def search_contacts(contacts):
    lines()
    print("       Search For Contact")
    lines()
    try:
        ask = int(input("Wanna search by 1. Name or 2. Contact: "))

        if ask not in (1, 2):
            print("invalid Input")
            return

        keyword = input("Search Contact ").strip()
        if keyword == "":
            print("Can't search for the Unknown")
            return
    
        found = False

        for i, contact in enumerate(contacts, start=1):
            if ask == 1 and keyword.lower() in contact["name"].lower():
                    print("Contact found: ")
                    print(f"{i}. {contact['name']} - {contact['phone']}")
                    found = True

            elif ask == 2 and keyword in contact["phone"]:
                    print("contact found")
                    print(f"{i}. {contact['name']} - {contact['phone']}")
                    found = True

        if not found:
            print("Contact wasn't found")

    except ValueError:
        print("Invalid Input")

def toggle_favorites(contacts):
    lines()
    print("       Mark As Favorites")
    lines()
    view_contacts(contacts)

    if len(contacts) == 0:
        print("No contacts yet")
        return

    try:
        choose = int(input("Press 1 to mark as favorite or 2 to remove contact from favorite: "))
        
        if choose not in (1, 2):
            print("Invalid Option")
            return
        
        ask = int(input("Which number do you wanna mark as favorite: "))
        if ask < 1 or ask > len(contacts):
            print("Invalid Input")
            return
        
        index = ask - 1

        if choose == 1:
            contacts[index]["favorite"] = True
            print("Mark Successful")
            print()

        elif choose == 2:
            if not contacts[index]["favorite"]:
                print("This contact is already Marked as favorite")
                print()

            else:
                contacts[index]["favorite"] = False
                print("It has successfully been removed from favorite contacts")
                print()

    except (ValueError, IndexError) :
        print("Wrong input")

def show_stats(contacts):
    lines()
    print("     Contact Summary")
    lines()
    total_contacts = len(contacts)
    favorite = 0

    for contact in contacts:
        if contact["favorite"]:
            favorite += 1

    others = total_contacts - favorite

    print(f"Total Contacts: {total_contacts}")
    print(f"Favorite Contacts: {favorite}")
    print(f"Others: {others}")
    print()

def coming_soon(contacts):
    return

def view_contacts(contacts, filter=None, sort=False):
    lines()
    print("       View Contacts")
    lines()
    if len(contacts) ==0 :
        print( "No contacts yet")
        return
    
    total = len(contacts)
    print(f"Total contacts {total}")

    display_list = contacts
    if sort:
        display_list = sorted(
            contacts,
            key=lambda contact: contact["name"].lower()
        )

    for i, contact in enumerate(display_list, start=1):
        if filter == "favorite" and not contact["favorite"]:
            continue

        status = "⭐" if contact.get("favorite") else ""
        print(f"{i}. {status} {contact['name']} - {contact['phone']}")

    print()

def edit_contact(contacts):
    lines()
    print("       Edit Contact")
    lines()
    view_contacts(contacts)

    if len(contacts) == 0:
        print("There are no contacts yet")
        return
    
    try :
        edit = int(input("Which contact do you wanna edit: "))
        if edit < 1 or edit > len(contacts):
            print("Invalid Option")
            return

        index = edit - 1
        
        x = input("Edit name: ").strip()
        y = input("Now edit number: ").strip()
        new = {
            "name" : x,
            "phone" : y,
            "favorite": contacts[index].get("favorite", False) 
        }
        contacts[index] = new
        print("Contact has been updated")
        print(f"1. {new['name']} - {new['phone']}")
        print()
    
    except ValueError:
        print("Wrong Input.")
    

def delete(contacts):
    lines()
    print("       Delete Contact")
    lines()
    view_contacts(contacts)

    if len(contacts) == 0:
        return

    deletel = int(input("Which Contact You Wanna Delete: "))
    try:
            if deletel < 1 or deletel > len(contacts):
                print("Delete Contact Invalid")

            else:
                removed = contacts.pop(deletel - 1)
                print(f"Contact Has Been Deleted: {removed}")
                print()

    except ValueError:
            print("Option not valid")

while True:
    lines()
    print("      Main Menu")
    lines()
    try:
        menu = [
            "0. Mark/Unmark Favorite",
            "1. Search Contacts",
            "2. Show Contact Stats",
            "3. Coming Soon",
            "4. Enter a number",
            "5. View contacts",
            "6. Edit Contacts",
            "7. Delete Contacts",
            "8. Exit Contacts"
        ]
        for item in menu:
            print(item)
        
        lines()
        choice = int(input("CHoose Option: "))

        if choice == 0:
            toggle_favorites(contacts)
            save_contact(contacts)
        
        elif choice == 1:
            search_contacts(contacts)

        elif choice == 2:
            show_stats(contacts)

        elif choice == 3:
            coming_soon(contacts)

        elif choice == 4:
            storage(contacts)
            save_contact(contacts)
        
        elif choice == 5:
            view = int(input(
                "1. All Contacts\n"
                "2. Favorite Contatcs\n"
                "3. Sorted Conatcts\n"
                "4. Sorted Favorites\n"
                "Choose: "
            ))
            if view == 1:
                view_contacts(contacts)

            elif view == 2:
                view_contacts(contacts, "favorite")
            
            elif view == 3:
                view_contacts(contacts, sort=True)
            
            elif view == 4:
                view_contacts(contacts, "favorite", True)

            else:
                print("Invalid Input")

        elif choice == 6:
            edit_contact(contacts)
            save_contact(contacts)

        elif choice == 7:
            delete(contacts)
            save_contact(contacts)

        elif choice == 8:
            print("Thank You for Using This PhoneBook, Bye!")
            break

        else:
            print("Wrong Choice")

    except ValueError:
        print("Please Enter Your Option")