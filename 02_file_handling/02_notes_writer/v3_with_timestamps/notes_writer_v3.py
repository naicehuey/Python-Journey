from datetime import datetime

def lines():
    print("=" *30)

def save_note(notes):
    with open("notes.txt", "a") as file:
        file.write(f"{notes}\n")

def load_note():
    lines()
    print("     View Notes")
    lines()
    with open("notes.txt", "r") as file:
        contents = file.readlines()

        print("Here is the notes")

        for i, content in enumerate(contents, start=1):
            note, time = content.strip().split("|")
            print(f"{i}. {note}")
            print(f"     Added Time: {time}")

def add_notes():
    lines()
    print("     Add Note")
    lines()
    note = input("Add notes: ").strip()
    time = datetime.now()
    notes = f"{note}|{time}"
    save_note(notes)

def clear_notes():
    lines()
    print("     Clear Notes")
    lines()
    with open("notes.txt", "w") as file:
        pass
    print("Notes have been cleared.")

def remove_note():
    with open("notes.txt", "r") as file:
        contents = file.readlines()

        for i, content in enumerate(contents, start=1):
            note, _ = content.strip().split("|")
            print(f"{i}. {note}")

        delete = int(input("Which note do you wanna delete: "))
        index = delete - 1

        contents.pop(index)
        with open("notes.txt", "w") as file:
            for content in contents:
                file.write(content)

        print("Note has been removed successfully.")

def load_menu():
    lines()
    print("     Main Menu")
    lines()
    while True:
        try:
            menu = [
                "1. Add Notes",
                "2. View Notes",
                "3. Remove Note",
                "4. Clear All Notes",
                "5. Exit"
            ]

            for item in menu:
                print(item)

            chose = int(input("Choose Option: "))

            if chose not in [1, 2, 3, 4, 5]:
                print("Wrong input")

            elif chose == 1:
                add_notes()

            elif chose == 2:
                load_note()

            elif chose == 3:
                remove_note()

            elif chose == 4:
                clear_notes()

            else:
                print("Thanks for using notes.")
                break

        except ValueError:
            print("Invalid Option")

load_menu()