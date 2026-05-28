def save_task(task):
    with open("task.txt", "a") as file:
        file.write(f"{task}\n")

def add_task():
    task = input("What task  do you wanna add: ").strip().lower()

    save_task(task)

def complete_task():
    with open("task.txt", "r") as file:
        tasks = file.readlines()
        
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        number =  int(input("Which task are you done with: "))
        index = number - 1
        chose = tasks[index].strip()
        tasks[index] = f"[x] {chose}\n"
        print(f"Task has been completed: \n[x] - {chose}")
        with open("task.txt", "w") as file:
            for task in tasks:
                file.write(task)

def delete_task():
    with open("task.txt", "r") as file:
        tasks = file.readlines()
        
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        number =  int(input("Which task are you done with: "))
        index = number - 1
         
        removed = tasks.pop(index)
        print(f"Task: {removed}\nHas been removed")
        with open("task.txt", "w") as file:
            for task in tasks:
                file.write(task)

def read_tasks():
    with open("task.txt", "r") as file:
        tasks = file.readlines()
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

def clear_tasks():
    with open("task.txt", "w") as file:
        pass

    print("Tasks have been clear")

def load_menu():
    while True:
        try:
            menu = [
                "1.Add Tasks",
                "2.View Tasks",
                "3.Complete Task",
                "4.Clear Tasks",
                "5.Delete Task",
                "6.Exit"
            ]
            for item in menu:
                print(item)

            choose = int(input("Choose Option"))

            if choose not in [1, 2, 3, 4, 5, 6]:
                print("Invalid Input")

            elif choose == 1:
                add_task()

            elif choose == 2:
                read_tasks()

            elif choose == 3:
                complete_task()

            elif choose == 4:
                clear_tasks()

            elif choose == 5:
                delete_task()

            else:
                print("Thank you for using task manager")
                break

        except ValueError:
            print("invalid Input")

load_menu()
