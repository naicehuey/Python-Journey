from datetime import datetime

def save_book(book):
    with open("books.txt", "a") as file:
        file.write(f"{book}\n")

def load_books():
    try:
        with open("books.txt", "r") as file:
            contents = file.readlines()

            if len(contents) == 0:
                print("No books yet")
                print()
                return

        for i, content in enumerate(contents, start=1):
            book, author, status, time = content.strip().split("|")
            print(f"{i}. {book}")
            print(f"        Author: {author}")
            print(f"        Status: {status}")
            if status == "Borrowed":
                print(f"        Time Borrowed: {time}")
            
            else:
                pass
    
            print()

    except FileNotFoundError:
        print("File Not Found")
        print()

def add_book():
    book = input("Book Name: ").strip()
    author = input("Author Name: ").strip()
    status = "Active"
    time = ""

    book = f"{book}|{author}|{status}|{time}"

    save_book(book)

    print("Book Successfully Added!")

def remove_book():
    with open("books.txt", "r") as file:
        contents = file.readlines()

        if len(contents) == 0:
            print("No books yet")
            print()
            return
        
    for i, content in enumerate(contents, start=1):
        book, _, _, _= content.strip().split("|")
        print(f"{i} Book: {book}")
        print()

    delete = int(input("Which book you wanna delete: "))

    if delete < 1 or delete > len(contents):
        print("Invalid choice")
        return
    
    index = delete - 1
    contents.pop(index)

    with open("books.txt", "w") as file:
        for content in contents:
            file.write(content)

    print("Book removed successfully.")
    print()

def clear():
    with open("books.txt", "w") as file:
        pass

    print("Library has been cleared.")

def search_book():
    with open("books.txt", "r") as file:
        contents = file.readlines()

        if len(contents) == 0:
            print("No books, Can't search")
            print()
            return

    search = int(input(
        "Search by \n"
        "1. Book Name\n"
        "2. Author\n"
        "Enter Option: "))
    
    found = False
    result_count = 1

    if search == 1:
        keyword = input("Search by book name: ").strip()
        print("Results: ")
        for content in contents:
            book, _, _, _ = content.strip().split("|")
            if keyword.lower() == book.lower():
                print(f"{result_count}. {book}")
                result_count += 1
                found = True
            
    if search == 2:
        keyword = input("Search by Author: ").strip()
        print(f"Results(Books by {keyword}) ")
        for content in contents:
            book, author, _, _ = content.strip().split("|")
            if keyword.lower() == author.lower():
                print(f"{result_count}. {book}")
                result_count += 1
                found = True

    print()
    if not found:
        print("Couldn't Found Your Book.")

def borrow_book():
    with open("books.txt", "r") as file:
        contents = file.readlines()

    for i, content in enumerate(contents, start=1):
        book, _, _, _ = content.strip().split("|")
        print(f"{i} Book: {book}")
        print()

    rent = int(input("Which book do you wanna borrow: "))

    if rent < 1 or rent > len(contents):
        print("Invalid Option")
        return

    index = rent - 1
    book, author, status, old_time = contents[index].strip().split("|")

    if status == "Borrowed":
        print(f"{book} is already borrowed!")
        return

    new_status = "Borrowed"
    time = datetime.now()
    updated = f"{book}|{author}|{new_status}|{time}\n"
    contents[index] = updated

    with open("books.txt", "w") as file:
        for content in contents:
            file.write(content)

    print("Book has been borrowed")
    print(f"{book} @ Time: {time}")
    print()

def return_book():
    with open("books.txt", "r") as file:
        contents = file.readlines()

    borrowed_exists = False
    for i, content in enumerate(contents, start=1):
        book, _, status, time = content.strip().split("|")
        if status == "Borrowed":
            print(f"{i} Book: {book}")
            print(f"        Borrowed On: {time}")
            borrowed_exists = True

    if not borrowed_exists:
        print("No borrowed books to return")
        return

    returned = int(input("Which book do you wanna return: "))

    if returned < 1 or returned > len(contents) :
        print("Invalid choice")
        return
    
    index = returned - 1
    book, author, status, old_time = contents[index].strip().split("|")

    if status != "Borrowed":
        print(f"{book} is available")
        return

    new_status = "Active"
    time = datetime.now()
    new_time = ""
    updated = f"{book}|{author}|{new_status}|{new_time}\n"
    contents[index] = updated

    with open("books.txt", "w") as file:
        for content in contents:
            file.write(content)

    print("Book has been returned")
    print(f"{book} @ Time: {time}")
    print()

def load_menu():
    while True:
        try:
            menu = [
                "1. Add book",
                "2. Search book",
                "3. View book",
                "4. Borrow book",
                "5. Return book",
                "6. Remove books",
                "7. Clear Libray",
                "8. Exit"
            ]

            for item in menu:
                print(item)

            chose = int(input("Choose Option: "))

            if chose not in [1, 2, 3, 4, 5, 6, 7, 8]:
                print("Not an option")
                print()

            elif chose == 1:
                add_book()

            elif chose == 2:
                search_book()

            elif chose == 3:
                load_books()

            elif chose == 4:
                borrow_book()

            elif chose == 5:
                return_book()

            elif chose == 6:
                remove_book()

            elif chose == 7:
                clear()

            else:
                print("Thank you for using the library app")
                break

        except ValueError:
            print("Invalid Option")

#clear()
load_menu()

