FILE = "sessions0.txt"
 
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
 
def display_list(items, formatter, empty_msg="No studies here yet"):
    if not items:
        print(empty_msg)
        return
    
    for i, item in enumerate(items, start=1):
        print(f"{i}.", end=" ")
        formatter(item)
    print()
 
def format_session(line):
    parts = line.strip().split("|")
    if len(parts) == 2:
        subject, status = parts
        print(subject)
        print(f"  Status: {status}")
 
def add_task():
    subject = input("Subject Name: ").strip()
    status = "Pending"
    save_data(FILE, f"{subject}|{status}\n")
    print("Task added successfully.")
 
def view_tasks():
    tasks = load_data(FILE)
    display_list(tasks, format_session, "Nothing Here Yet!!")
 
def search_task():
    tasks = load_data(FILE)
    results = []
    keyword = input("Search Task: ").strip()

    for task in tasks:
        if keyword.lower() in task.lower():
            results.append(task)

    display_list(results, format_session, "No task found.")
 
def mark_task():
    tasks = load_data(FILE)
    display_list(tasks, format_session, "Nothing here yet")
    if not tasks:
        return

    try:
        choice = int(input("Which task do you wanna mark done: "))
    except ValueError:
        print("Invalid Input")
        return

    if choice < 1 or choice > len(tasks):
        print("Invalid option.")
        return
 
    subject = tasks[choice - 1].strip().split("|")[0]
    tasks[choice - 1] = f"{subject}|Done\n"
    save_update(FILE, tasks)
    print("Task has been completed.")
 
def delete_task():
    tasks = load_data(FILE)
    display_list(tasks, format_session, "Nothing here yet")
    if not tasks:
        return

    try:
        choice = int(input("Which task do you wanna delete: "))
    except ValueError:
        print("Invalid Input")
        return

    if choice < 1 or choice > len(tasks):
        print("Invalid option.")
        return
 
    tasks.pop(choice - 1)
    save_update(FILE, tasks)
    print("Task has been deleted.")
 
def report():
    tasks = load_data(FILE)
    result_pending = []
    result_done = []
 
    for task in tasks:
        parts = task.strip().split("|")
        if len(parts) != 2:
            continue
        _, status = parts
        if status == "Pending":
            result_pending.append(task)
        elif status == "Done":
            result_done.append(task)
 
    print("Pending Tasks:")
    display_list(result_pending, format_session, "No pending tasks")
    print()
    print("Completed Tasks:")
    display_list(result_done, format_session, "No completed tasks")
    print()
 
def load_menu():
    menu = {
        "1": ("Add Task", add_task),
        "2": ("View Tasks", view_tasks),
        "3": ("Search Tasks", search_task),
        "4": ("Complete Task", mark_task),
        "5": ("Delete Task", delete_task),
        "6": ("Report", report)
    }
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("7. Exit")
 
        choice = input("Choose: ").strip()
        if choice == "7":
            print("Goodbye!!")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid Option.")
 
load_menu()