def save_contacts(contact):
    with open("contact.txt", "a") as file:
        file.write(f"{contact}\n")

def load_contants():
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

    except FileNotFoundError:
        print("File is Missing.")

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
            "5. Exit"
            ]
            for item in menu:
                print(item)

            chose = int(input("Choose Option: "))

            if chose not in [1,2,3,4,5]:
                print("Wrong Option")

            elif chose == 1:
                add_contact()

            elif chose == 2:
                load_contants()

            elif chose == 3:
                remove_contact()

            elif chose == 4:
                search_contact()

            else:
                print("Thank you for saving contacts, Bye")
                break

        except ValueError:
            print("Invalid Option ")

load_menu()