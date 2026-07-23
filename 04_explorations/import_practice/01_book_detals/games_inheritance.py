from book_details import (
    save_data, 
    load_data, 
    display_list, 
    choose_item
)

FILE = "games.json"

def get_games():
    return load_data(FILE)

def format_games(items):
    print(items['name'])
    print(f"    Category: {items['caterogy']}")
    print(f"    Rate: {items['rate']}")

def add_game():
    name = input("Game Name: ").strip()
    category = input("Game Category: ").strip()
    rate = 0

    games = get_games()
    games.append({
        "name": name,
        "caterogy": category,
        "rate": rate
    })
    save_data(FILE, games)
    print("Game added successfully.")

def view_games():
    games = get_games()
    display_list(games, format_games, "No games yet.")

def search_game():
    games = get_games()
    results = []

    keyword = input("Game Search: ").lower().strip()

    for game in games:
        if keyword in game['name'].lower():
            results.append(game)

    display_list(results, format_games, "No such game.")

def rate_game():
    games = get_games()
    index = choose_item(games, format_games)

    if index is None:
        return
    
    try:
        new_rate = int(input("Rate Game (1-10): "))
        if new_rate < 1 or new_rate > 10: 
            print("Rate must be between 1 and 10")
            return
    except ValueError:
        print("Invalid Input")
        return

    games[index]['rate'] = new_rate
    save_data(FILE, games)
    print("Rate updated successfully.")

def report():
    games = get_games()
    total_games = 0
    lower_rate_games = 0
    mid_rate_games = 0
    high_rate_games = 0

    for game in games:
        total_games += 1
        if game["rate"] < 5:   
            lower_rate_games += 1
        elif game["rate"] < 7:
            mid_rate_games += 1
        else:
            high_rate_games += 1

    print(f"Total Games: {total_games}")
    print(f"Low Rated Games: {lower_rate_games}")
    print(f"Mid Rated Games: {mid_rate_games}")
    print(f"High Rated Games: {high_rate_games}")

def load_game_menu():
    menu = {
        "1": ("Add Game", add_game),
        "2": ("View Games", view_games),
        "3": ("Search Games", search_game),
        "4": ("Rate Games", rate_game),
        "5": ("Report", report)
    }
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("6. Exit")

        choice = input("Choose: ")
        if choice == "6":
            print("Goodbye.")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid Input.")

load_game_menu()