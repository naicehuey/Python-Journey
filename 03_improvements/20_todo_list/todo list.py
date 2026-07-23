FILE = "tracker.txt"
 
def save_data(filename, data):
    with open(filename, "a") as file:
        file.write(data)
 
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
 
def display_list(items, formatter, empty_msg="No tasks yet."):
    if not items:
        print(empty_msg)
        return
    for i, item in enumerate(items, start=1):
        print(f"{i}.", end=" ")
        formatter(item)
    print()
 
def format_list(line):
    task, status = line.strip().split("|")
    print(task)
    print(f"    Status: {status}")

def choose_task():
    tasks = load_data(FILE)
    display_list(tasks, format_list, "No tasks yet.")

    if not tasks:
        return None, None
    
    try:
        choice = int(input("Choose task: "))
    except ValueError:
        print("Invalid Input")
        return None, None

    if choice < 1 or choice > len(tasks):
        return None, None
    
    return tasks, choice - 1
 
def add_task():
    task = input("Task Name: ").strip()
    status = "Pending"
    save_data(FILE, f"{task}|{status}\n")
    print("Task added successfully.")
 
def view_tasks():
    tasks = load_data(FILE)
    display_list(tasks, format_list, "Nothing to display yet.")
 
def search_tasks():
    tasks = load_data(FILE)
    results = []
    keyword = input("Search task: ").lower().strip()
 
    for item in tasks:
        task, status = item.strip().split("|")
        if keyword in task.lower():
            results.append(item)
 
    display_list(results, format_list, "Task not found.")
 
def mark_complete_task():
    tasks, index = choose_task()
    if tasks is None:
        return
    
    task_name = tasks[index].strip().split("|")[0]
    tasks[index] = f"{task_name}|Complete\n"
    save_update(FILE, tasks)
    print("Task has been completed.")
 
def delete_task():
    tasks, index = choose_task()
    if tasks is None:
        return
    
    tasks.pop(index)
    save_update(FILE, tasks)
    print("Task has been deleted.")
 
def report():
    tasks = load_data(FILE)
    pending = 0
    complete = 0
    total = 0
 
    for item in tasks:
        task, status = item.strip().split("|")
        total += 1
        if status == "Complete":
            complete += 1
        else:
            pending += 1
 
    print(f"Pending Tasks:  {pending}")
    print(f"Complete Tasks: {complete}")
    print(f"Total Tasks:    {total}")
 
def load_menu():
    menu = {
        "1": ("Add Task", add_task),
        "2": ("View Tasks", view_tasks),
        "3": ("Search Task", search_tasks),
        "4": ("Complete Task", mark_complete_task),
        "5": ("Delete Task", delete_task),
        "6": ("Report", report)
    }
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("7. Exit")
 
        choice = input("Choose: ").strip()
        if choice == "7":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid Option.")
 
load_menu()