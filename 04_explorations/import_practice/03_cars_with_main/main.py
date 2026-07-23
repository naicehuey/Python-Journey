import json

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)
    
def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def display_list(items, formatter, empty_msg="Database Empty."):
    if not items:
        print(empty_msg)
        return
    
    for i, item in enumerate(items, start=1):
        print(f"{i}.", end=" ")
        formatter(item)
    print()

def choose_item(items, formatter):
    display_list(items, formatter, "Database Empty")

    if not items:
        return None
    
    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Invalid Input")
        return None

    if choice < 1 or choice > len(items):
        print("Invalid Option")
        return None
    
    return choice - 1