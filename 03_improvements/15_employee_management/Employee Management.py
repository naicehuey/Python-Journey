import json

FILE = "employees.json"

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def display_list(items, formatter, empty_msg="Nothing Here Yet"):
    if not items:
        print(empty_msg)
        return
    
    for i, item in enumerate(items, start=1):
        print(f"{i}.", end=" ")
        formatter(item)
    print()

def format_employee(item):
    print(item['name'])
    print(f"        Position: {item['position']}")
    print(f"        Salary: {item['salary']}")
    print(f"        Status: {item['status']}")

def add_employee():
    employees = load_data(FILE)

    name = input("Employee name: ").strip()
    position = input("Employee position: ").strip()

    try:
        salary = int(input("Employee salary: "))
    except ValueError:
        print("Salary must be a number")
        return

    status = "Active"

    employees.append({
        "name": name,
        "position": position,
        "salary": salary,
        "status": status
    })

    save_data(FILE, employees)
    print("New Employee Added.")

def view_employee():
    employees = load_data(FILE)
    display_list(employees, format_employee, "Nothing here yet.")

def search_employee():
    employees = load_data(FILE)
    results = []

    keyword = input("Search employee: ").strip()

    for employee in employees:
        if keyword.lower() in employee['name'].lower():
            results.append(employee)

    display_list(results, format_employee, "No employee found.")

def delete_employee():
    employees = load_data(FILE)
    display_list(employees, format_employee, "Nothing here yet.")

    if not employees:
        return

    try:
        choice = int(input("Which employee to delete: "))
    except ValueError:
        print("Invalid Input")
        return

    if choice < 1 or choice > len(employees):
        print("Invalid Option.")
        return
    
    name = employees[choice - 1]['name']
    employees.pop(choice - 1)
    save_data(FILE, employees)
    print(f"{name} has been removed from the database.")

def promote_employee():
    employees = load_data(FILE)
    display_list(employees, format_employee, "Nothing here yet.")

    if not employees:
        return

    try:
        choice = int(input("Which employee to promote: "))
    except ValueError:
        print("Invalid Input")
        return

    if choice < 1 or choice > len(employees):
        print("Invalid Option.")
        return
    
    new_position = input("New position: ").strip()

    try:
        new_salary = int(input("New salary: "))
    except ValueError:
        print("Salary must be a number")
        return

    employees[choice - 1]['position'] = new_position
    employees[choice - 1]['salary'] = new_salary

    save_data(FILE, employees)
    print(f"{employees[choice - 1]['name']} has been promoted!")
    print(f"    New Position: {new_position}")
    print(f"    New Salary: {new_salary}")

def deactivate_employee():
    employees = load_data(FILE)
    display_list(employees, format_employee, "Nothing here yet.")

    if not employees:
        return

    try:
        choice = int(input("Which employee to deactivate: "))
    except ValueError:
        print("Invalid Input")
        return

    if choice < 1 or choice > len(employees):
        print("Invalid Option.")
        return

    confirm = input("Are you sure you want to deactivate this employee (Y/N): ").strip().lower()

    if confirm not in ["y", "n"]:
        print("Invalid Answer.")
    
    elif confirm == "y":
        employees[choice - 1]['status'] = "Deactivated"
        save_data(FILE, employees)
        print(f"{employees[choice - 1]['name']} has been deactivated.") 

    else:
        print(f"Alright, {employees[choice - 1]['name']} stays active.")

def report():
    employees = load_data(FILE)

    if not employees:
        print("No employees yet.")
        return

    print("Here is the list of employees: ")
    for i, employee in enumerate(employees, start=1):
        print(f"{i}. {employee['name']} — {employee['status']}")

    print()
    total = sum(employee['salary'] for employee in employees) 
    highest = max(employee['salary'] for employee in employees) 
    active = sum(1 for employee in employees if employee['status'] == "Active")
    deactivated = sum(1 for employee in employees if employee['status'] == "Deactivated")

    print(f"Total Employees: {len(employees)}")
    print(f"Active Employees: {active}")
    print(f"Deactivated Employees: {deactivated}")
    print(f"Total Salary Expenditure: {total}")
    print(f"Highest Salary: {highest}")

def load_menu():
    menu = {
        "1": ("Add Employee", add_employee),
        "2": ("View Employees", view_employee),
        "3": ("Search Employee", search_employee),
        "4": ("Delete Employee", delete_employee),
        "5": ("Promote Employee", promote_employee),
        "6": ("Deactivate Employee", deactivate_employee),
        "7": ("Report", report)
    }
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("8. Exit")

        choice = input("Choose: ").strip()
        if choice == "8":
            print("Thank you for using Employee Management.")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid Option.")

load_menu()