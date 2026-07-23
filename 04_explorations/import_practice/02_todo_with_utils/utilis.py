FILE = "ToDo.txt"

def save_data(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(item)

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
    
def display_list(items, formatter, empty_msg="No Tasks Yet!!"):
    if not items:
        print(empty_msg)
        return
    
    for i, item in enumerate(items, start=1):
        print(f"{i}.", end=" ")
        formatter(item)

def choose():
    tasks = load_data(FILE)

    if not tasks:
        print("Nothing to choose from.")
        return None
    
    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Invalid Input")
        return None

    if choice < 1 or choice > len(tasks):
        print("Invalid Option")
        return None
    
    return choice - 1