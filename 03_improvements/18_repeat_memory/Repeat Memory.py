import json

FILE = "repeat_memory_books.json"

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def display_list(items, formatter, empty_msg="Nothing here"):
    if not items:
        print(empty_msg)
        return
    
    for i, item in enumerate(items, start=1):
        print(f"{i}.", end=" ")
        formatter(item)
    print()

def format_book(item):
    print(item['name'])
    print(f"    Author: {item['author']}")
    print(f"    Release Year: {item['date']}")

def add_book():
    books = load_data(FILE)
    name = input("Book Name: ").strip()
    author = input("Author Name: ").strip()
    date = input("Release Year: ").strip()

    books.append({
        "name": name,
        "author": author,
        "date": date
    })

    save_data(FILE, books)
    print("Book added successfully.")

def view_books():
    books = load_data(FILE)
    display_list(books, format_book, "No books!!")

def search_books():
    books = load_data(FILE)
    results = []
    keyword = input("Search Books: ").strip().lower()

    for book in books:
        if keyword in book['name'].lower():
            results.append(book)

    display_list(results, format_book, "No Results!!")

def delete_book():
    books = load_data(FILE)
    display_list(books, format_book, "No books!!")

    if not books:
        return

    try:
        item = int(input("Delete Book: "))
    except ValueError:
        print("Invalid Input")
        return

    if item < 1 or item > len(books):
        print("Invalid option")
        return

    books.pop(item - 1)
    save_data(FILE, books)
    print("Book has been deleted.")

def menu():
    options = {
        "1": ("Add Book", add_book),
        "2": ("View Books", view_books),
        "3": ("Search Book", search_books),
        "4": ("Delete Book", delete_book)
    }
    while True:
        for key, (label, _) in options.items():
            print(f"{key}. {label}")
        print("5. Exit")

        choice = input("Choose: ").strip()
        if choice == "5":
            print("Goodbye!!")
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid Option")

menu()