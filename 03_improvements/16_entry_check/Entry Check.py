from datetime import datetime

FILE = "entry.txt"

def save_data(filename, data):
    with open(filename, "a") as file:
        file.write(f"{data}\n")

def save_update(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(item)

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def add_entry():
    task_name = input("Task Name: ").strip()
    task = input("Add Task: ").strip()
    entry_date = datetime.now()
    save_data(FILE, f"{task_name}|{task}|{entry_date}") 
    print("Entry added successfully.")

def display_list(items, formatter, empty_msg="No entry yet"):
    if not items:
        print(empty_msg)
        return
    
    for i, item in enumerate(items, start=1):
        print(f"{i}.", end=" ")
        formatter(item)

def format_entry(line):
    task_name, task, entry_date = line.strip().split("|")
    print(task_name)
    print(f"    Task: {task}")
    print(f"    Entry Date: {entry_date}")

def view_entries():
    entries = load_data(FILE)
    display_list(entries, format_entry, "No entries yet.")

def search_entries():  
    entries = load_data(FILE)
    results = []
    keyword = input("Search entry: ").strip()

    for entry in entries:
        task_name, _, _ = entry.strip().split("|")
        if keyword.lower() in task_name.lower():
            results.append(entry)

    display_list(results, format_entry, "No such entry")

def delete_entry():
    entries = load_data(FILE)
    display_list(entries, format_entry, "No entries yet.")

    if not entries:
        return

    try:
        choice = int(input("Which entry to delete: "))
    except ValueError:
        print("Invalid Input")
        return

    if choice < 1 or choice > len(entries):
        print("Invalid Option.")
        return

    entries.pop(choice - 1)
    save_update(FILE, entries)
    print("Entry deleted successfully.")

def view_new_entry():
    entries = load_data(FILE)

    if not entries:
        print("No entries yet.")
        return

    last = [entries[-1]]
    display_list(last, format_entry, "No entries yet.")

def load_menu():
    menu = {
        "1": ("Add Entry", add_entry),
        "2": ("View Entries", view_entries),
        "3": ("Search Entries", search_entries),
        "4": ("Delete Entry", delete_entry),
        "5": ("View Latest Entry", view_new_entry)
    }
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("6. Exit")

        choice = input("Choose: ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid Option.")

load_menu()