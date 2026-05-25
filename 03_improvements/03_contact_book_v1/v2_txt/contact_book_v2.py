def save_contacts(contact):
    with open("contact.txt", "a") as file:
        file.write(f"{contact}\n")

def load_contacts():
    with open("contact.txt", "r") as file:
        contents = file.readlines()

    for i, content in enumerate(contents, start=1):
        name, number = content.strip().split("|")
        print(f"{i}. Name: {name}")
        print(f"       Mobile No: {number}")

def add_contact():
    name = input("Name: ")
    number = input(("Number: "))

    contact= f"{name}|{number}"

    save_contacts(contact)

def remove_contact():
    try:
        with open("contact.txt", "r") as file:
            contents =  file.readlines()

            if len(contents) == 0:
                print("No Content Yet!!!")
                return

            for i, content in enumerate(contents, start=1):
                name, number = content.strip().split("|")
                print(f"{i}. Name: {name}")
                print(f"       Mobile No: {number}")

            chose = int(input("Which Contact Do you wanna delete: "))
            index = chose - 1

            contents.pop(index)
            with open("contact.txt", "w") as file:
                for content in contents:
                    file.write(content)

            print("Contact deleted successfully")

    except FileNotFoundError:
        print("File is Missing.")
def edit_contact():
    try:
        with open("contact.txt", "r") as file:
            contents = file.readlines()
            if len(contents) == 0:
                print("No Contacts Yet!!")
                return

        for i, content in enumerate(contents, start=1):
            name, number = content.strip().split("|")
            print(f"{i}. Name: {name}")
            print(f"        Mobile No: {number}")

        choose = int(input("Which Contact You Wanna Edit: "))

        index = choose - 1

        name = input("Name: ").strip()
        number = input("Number: ").strip()

        if name == "" or number == "":
            print("Name and number cannot be empty")
            return

        contents[index] = f"{name}|{number}\n"

        with open("contact.txt", "w") as file:
            for content in contents:
                file.write(content)

        print("Edited Successfully")

    except FileNotFoundError:
        print("File Was Not Found")

def search_contact():
    with open("contact.txt", "r") as file:
        contents = file.readlines()

    keyword = input("Search: ").strip ()

    found = False

    for content in contents:
        name, number = content.strip().split("|")
        if keyword.lower() == name.lower():
            print(f"Name: {name}")
            print(f"  Mobile No: {number}")
            found = True

    if not found:
        print("Contact not found")

def load_menu():
    while True:
        try:
            menu = [
            "1. Add Contacts",
            "2. View Contacts",
            "3. Delete Contact",
            "4. Search",
            "5. Edit Contact",
            "6. Exit"
            ]
            for item in menu:
                print(item)

            chose = int(input("Choose Option: "))

            if chose not in [1,2,3,4,5,6]:
                print("Wrong Option")

            elif chose == 1:
                add_contact()

            elif chose == 2:
                load_contacts()

            elif chose == 3:
                remove_contact()

            elif chose == 4:
                search_contact()

            elif chose == 5:
                edit_contact()

            else:
                print("Thank you for saving contacts, Bye")
                break

        except ValueError:
            print("Invalid Option ")

load_menu()