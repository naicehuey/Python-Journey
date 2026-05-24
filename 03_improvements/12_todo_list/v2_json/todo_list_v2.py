import json
from datetime import datetime
import os

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
tasks = load_tasks()

def lines():
    print("=" * 30)

def add_task(tasks):
    lines()
    print("    Add Task")
    lines()
    task = input("Add your task: ")
    if task.strip() == "":
        print("Task can not be empty")
        return
    
    time = datetime.now().strftime("%Y - %B - %A  %H:%M")

    tasks.append({
         "title": task,
         "done": False,
         "time": time,
         "urgent": False
    })

def view_tasks(tasks, filter=None):
    lines()
    print("      View Tasks")
    lines()
    if len(tasks) == 0:
        print("There is no task to show")
        return
    
    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        label = "DONE" if task["done"] else "URGENT" if task.get("urgent", False) else "PENDING"
        if filter == "done" and not task["done"]:
            continue
        if filter == "pending" and task["done"]:
            continue
        if filter == "urgent" and not task.get("urgent", False):
            continue
        
        print(f"[{status}] {i}. {task['title']} ({label})")
        print(f"       Added: {task['time']}")
        print()

def search_tasks(tasks):
    lines()
    print("    Search Task")
    lines()
    keyword = input("Search for task: ").strip()
    if keyword == "":
        print("Search cannot be empty")
        return
    
    found = False

    for i, task in enumerate(tasks, start=1):
        if keyword.lower() in task["title"].lower():
            print(f"{i}. {task['title']}")
            found = True

    if not found:
        print("No matching tasks found")

def mark_done(tasks):
    lines()
    print("    Mark Done")
    lines()
    view_tasks(tasks)

    try:
        index = int(input("Which task should be marked as done: "))
        tasks[index - 1]["done"] = True
        print("Task has been marked as done")

    except (IndexError, ValueError):
        print("Invalid Input")

def mark_urgent(tasks):
    lines()
    print("    Mark Urgent")
    lines()
    view_tasks(tasks)

    try:
        index = int(input("Which task should be marked as urgent: "))
        tasks[index - 1]["urgent"] = True
        print("Task has been marked as urgent")

    except (IndexError, ValueError):
        print("Invalid option")

def edit_task(tasks):
    lines()
    print("    Edit Task")
    lines()
    try:
        if len(tasks) == 0:
            print("Nothing to edit yet")
        else:
            view_tasks(tasks)
            index = int(input("Which task you wanna edit: "))
            if index < 1 or index > len(tasks):
                print("Invalid option")
            else:
                new_title = input("Please add the new task: ")
                if new_title.strip() == "":
                    print("This task is empty")
                else:
                    tasks[index - 1]["title"] = new_title
                    print("Task has been updated.")

    except (ValueError, IndexError):
        print("Wrong Input")

def delete_tasks(tasks):
    lines()
    print("    Delete Task")
    lines()
    if len(tasks) == 0:
        print("There are no tasks yet")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']}")

        try:
            deletel = int(input("Enter the number of the task you wanna delete: "))
            
            if deletel < 1 or deletel > len(tasks):
                print("Invalid task number")
            else:
                removed = tasks.pop(deletel - 1)
                print(f"Deleted task: {removed['title']}")

        except ValueError:
            print("Please enter a valid number")

def show_stats(tasks):
    lines()
    print("    Show Task Stats")
    lines()
    total_tasks = len(tasks)
    done_tasks = 0
    urgent_tasks = 0

    for task in tasks:
        if task["done"]:
            done_tasks += 1
        if task.get("urgent", False):
            urgent_tasks += 1

    pending_tasks = total_tasks - done_tasks
    
    print(f"Total Tasks: {total_tasks}")
    print(f"Done Tasks: {done_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Urgent Tasks: {urgent_tasks}")

while True:
    lines()
    print("    Main Menu")
    lines()
    try:
        choices = int(input(
            "1. Search Task\n"
            "2. Add Task\n"
            "3. View Task\n"
            "4. Delete Task\n"
            "5. Mark As Done\n"
            "6. Mark As Urgent\n"
            "7. Edit Task\n"
            "8. Show Tasks Status\n"
            "9. Exit Program\n"
            "What We Going For: "
        ))

        if choices == 1:
            search_tasks(tasks)
        elif choices == 2:
            add_task(tasks)
            save_tasks(tasks)
        elif choices == 3:
            try:
                x = int(input(
                    "1. Done Tasks\n"
                    "2. Pending Tasks\n"
                    "3. Urgent Tasks\n"
                    "4. All Tasks\n"
                    "How do you wanna view tasks: "
                ))
                if x == 1:
                    view_tasks(tasks, "done")
                elif x == 2:
                    view_tasks(tasks, "pending")
                elif x == 3:
                    view_tasks(tasks, "urgent")
                elif x == 4:
                    view_tasks(tasks)
                else:
                    print("Invalid option")
            except ValueError:
                print("Please enter a number")
        elif choices == 4:
            delete_tasks(tasks)
            save_tasks(tasks)
        elif choices == 5:
            mark_done(tasks)
            save_tasks(tasks)
        elif choices == 6:
            mark_urgent(tasks)
            save_tasks(tasks)
        elif choices == 7:
            edit_task(tasks)
            save_tasks(tasks)
        elif choices == 8:
            show_stats(tasks)
        elif choices == 9:
            print("Thank you for using this to do list")
            break
        else:
            print("Wrong input")
    
    except ValueError:
        print("Please enter a number")
        continue