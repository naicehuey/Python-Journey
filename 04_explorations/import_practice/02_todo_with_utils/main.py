from datetime import datetime
from utilis import load_data, save_data, display_list, choose, FILE

def format_list(line):
    task, status, date = line.strip().split("|")
    print(f"Task: {task}")
    print(f"    Task Status: {status}")
    print(f"    Date Added: {date}")
    
def add_task():
    tasks = load_data(FILE)
    task = input("Task: ").strip()
    status = "Pending"
    date = datetime.now()
    tasks.append(f"{task}|{status}|{date}\n")
    save_data(FILE, tasks)
    print("Task added successfully.")

def view_task():
    tasks = load_data(FILE)
    display_list(tasks, format_list, "No Tasks Yet!!")

def mark_done():
    view_task()
    index = choose()
    if index is None:
        return

    tasks = load_data(FILE)
    task, status, date = tasks[index].strip().split("|")
    tasks[index] = f"{task}|Done|{date}\n"
    save_data(FILE, tasks)
    print("Task marked as done.")
    
def search():
    tasks = load_data(FILE)
    results = []
    keyword = input("Search Task: ").strip().lower()

    for item in tasks:
        task, _, _ = item.strip().split("|") 
        if keyword in task.lower():
            results.append(item)
    
    display_list(results, format_list, "No Such Tasks.")

def delete_task():
    view_task()
    index = choose()
    if index is None:     
        return

    tasks = load_data(FILE)
    tasks.pop(index)
    save_data(FILE, tasks)
    print("Task has been deleted.")

def report():
    tasks = load_data(FILE)
    total = 0
    pending = 0
    done = 0

    for item in tasks:         
        total += 1
        _, status, _ = item.strip().split("|")
        if status == "Pending":
            pending += 1
        elif status == "Done":
            done += 1

    print("Tasks Report")
    print(f"Total Tasks: {total}")
    print(f"Done Tasks: {done}")
    print(f"Pending Tasks: {pending}")

def menu():
    options = {
        "1": ("Add Task", add_task),
        "2": ("View Tasks", view_task),
        "3": ("Search Tasks", search),
        "4": ("Mark Done", mark_done),
        "5": ("Report", report),
        "6": ("Delete Task", delete_task)
    }
    while True:
        for key, (label, _) in options.items():
            print(f"{key}. {label}")
        print("7. Exit")

        choice = input("Choose: ").strip()
        if choice == "7":
            print("Goodbye.")
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid Input")

menu()