FILE = "workout.txt"

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

def display_list(items, formatter, empty_msg="No data yet."):
    if not items:
        print(empty_msg)
        return
    
    for i, item in enumerate(items, start=1):
        print(f"{i}. ", end=" ")
        formatter(item)
    print()

def format_list(line):
    task, status = line.strip().split("|")
    print(task)
    print(f"     Status: {status}")

def choose_item():
    trackers = load_data(FILE)
    display_list(trackers, format_list, "No data yet.")

    if not trackers:
        return None, None

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Invalid Input.")
        return None, None

    if choice < 1 or choice > len(trackers):
        return None, None

    return trackers, choice - 1    

def add_workout():
    task = input("Workout: ").strip()
    status = "Pending"
    trackers = load_data(FILE)
    trackers.append(f"{task}|{status}\n")
    save_update(FILE, trackers)
    print("Workout added successfully.")

def view_workouts():
    trackers = load_data(FILE)
    display_list(trackers, format_list, "No data yet.")

def mark_done():
    trackers, index = choose_item()
    if trackers is None:
        return    
    
    task_name = trackers[index].strip().split("|")[0]
    trackers[index] = f"{task_name}|Done\n" 
    save_update(FILE, trackers)
    print("Task has been updated to 'Done'.")

def delete_task():
    trackers, index = choose_item()
    if trackers is None:
        return       
    
    trackers.pop(index)
    save_update(FILE, trackers)
    print("Workout has been deleted.")

def load_menu():
    menu = {
        "1": ("Add Workout", add_workout),
        "2": ("View Workout", view_workouts),
        "3": ("Mark Done", mark_done),
        "4": ("Delete Workout", delete_task)
    }
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("5. Exit")

        choice = input("Choose Option: ")
        if choice == "5":
            print("Goodbye")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid Option.")

load_menu()