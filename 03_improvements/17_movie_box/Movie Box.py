import json

FILE = "Movies.json"

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def display_list(items, formatter, empty_msg="Nothing here yet!"):
    if not items:
        print(empty_msg)
        return
    
    for i, item in enumerate(items, start=1):
        print(f"{i}.", end=" ")
        formatter(item)
    print()

def format_list(items):
    print(items["mov_name"])
    print(f"     Rate: {items['mov_rate']}")
    print(f"     Category: {items['mov_caterogy']}")

def choose_movie():
    movies = load_data(FILE)
    display_list(movies, format_list, "No movies yet.")

    if not movies:
        return None, None
    
    try:
        choice = int(input("Choose movie: "))
    except ValueError:
        print("Invalid Choice")
        return None, None

    if choice < 1 or choice > len(movies):
        return None, None
    
    return movies, choice - 1

def add_movie():
    movies = load_data(FILE)
    mov_name = input("Movie Name: ").strip()
    mov_rate = 0
    mov_category = input("Movie Category: ").strip()

    movies.append({
        "mov_name": mov_name,
        "mov_rate": mov_rate,
        "mov_caterogy": mov_category
    })

    save_data(FILE, movies)
    print("Movie added successfully!")

def view_movies():
    movies = load_data(FILE)
    display_list(movies, format_list, "No movies yet.")

def search_movie():
    movies = load_data(FILE)
    results = []
    keyword = input("Movie search: ").strip()

    for movie in movies:
        if keyword.lower() in movie['mov_name'].lower():
            results.append(movie)

    display_list(results, format_list, "No movie found.")

def delete_movie():
    movies, index = choose_movie()
    if movies is None:
        return
    
    movies.pop(index)
    save_data(FILE, movies)
    print("Movie has been deleted.")

def rate_movie():
    movies, index = choose_movie()
    if movies is None:
        return
    
    try:
        rate_mov = int(input("Rate the movie out of 10: "))
        if rate_mov < 1 or rate_mov > 10:
            print("Rate must be between 1 and 10")
            return
    except ValueError:
        print("Invalid Input")
        return

    movies[index]["mov_rate"] = rate_mov
    save_data(FILE, movies)
    print("Rating updated!")
    display_list([movies[index]], format_list)

def report():
    movies = load_data(FILE)
    low_movie = 0
    high_movie = 0
    total = 0

    if not movies:
        print("Nothing to report yet.")
        return
    
    for movie in movies:
        total += 1
        if movie['mov_rate'] < 5:
            low_movie += 1
        else:
            high_movie += 1

    print("Here is the movie report: ")
    print(f"Total Movies: {total}")
    print(f"Low Rated Movies: {low_movie}")
    print(f"High Rated Movies: {high_movie}")

def load_menu():
    menu = {
        "1": ("Add Movie", add_movie),
        "2": ("View Movies", view_movies),
        "3": ("Search Movie", search_movie),
        "4": ("Delete Movie", delete_movie),
        "5": ("Rate Movie", rate_movie),
        "6": ("Report", report)
    }
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("7. Exit")

        choice = input("Choose: ").strip()
        if choice == "7":
            print("Goodbye.")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid Option.")

load_menu()