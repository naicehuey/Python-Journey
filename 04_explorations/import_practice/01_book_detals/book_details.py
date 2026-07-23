import json

FILE = "bookss.json"

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def display_list(items, formatter, empty_msg="No data yet"):
    if not items:
        print(empty_msg)
        return
    
    for i, item in enumerate(items, start=1):
        print(f"{i}. ", end=" ")
        formatter(item)
    print()

def format_list(item):
    print(item["name"])
    print(f"        Author: {item['author']}")
    print(f"        Release Day: {item['date']}")

def choose_item(items, formatter):
    display_list(items, formatter, "No data yet")
    
    if not items:
        return None

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Invalid Input.")
        return None
    
    if choice < 1 or choice > len(items):
        return None

    return choice - 1

def add_book():
    name = input("Book Name: ").strip()
    author = input("Author Name: ").strip()
    date = input("Release year: ").strip()

    if len(date) != 4:
        print("Wrong year try again.")
        return

    books = load_data(FILE)
    books.append({
        "name": name,
        "author": author,
        "date": date
    })

    save_data(FILE, books)
    print("Book Successfully Added.")

def view_books():
    books = load_data(FILE)
    display_list(books, format_list, "No books yet")

def search_books():
    books = load_data(FILE)
    result = []
    
    keyword = input("Search book: ").strip().lower()

    for book in books:
        if keyword in book['name'].lower():
            result.append(book)

    display_list(result, format_list, "No such book.")
            
def delete_book():
    books = load_data(FILE)
    index = choose_item(books, format_list)

    if index is None:
        return
    
    books.pop(index)
    save_data(FILE, books)
    print("Book successfully deleted.")

def load_menu():
    menu = {
        "1": ("Add Book", add_book),
        "2": ("View Books", view_books),
        "3": ("Search Books", search_books),
        "4": ("Delete Books", delete_book)
    }
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("5. Exit")

        choice = input("Choose: ")
        if choice == "5":
            print("Goodbye.")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    load_menu()