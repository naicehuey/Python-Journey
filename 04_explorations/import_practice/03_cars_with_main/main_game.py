from main import (
    save_data,
    load_data,
    display_list,
    choose_item
)

FILE = "cars.json"

def get_cars():
    return load_data(FILE)

def add_cars():
    name = input("Car Name: ").strip()
    model = input("Car Model: ").strip()
    try:
        rate = int(input("Car Performance Rating (1-10): "))
        release_year = input("Release Year: ").strip()

        if len(release_year) != 4 or rate > 10 or rate < 1:
            print("Invalid rate or release year. Try again.")
            return
        
        cars = get_cars()
        cars.append({
            "carname": name,
            "carmodel": model,
            "carrate": rate,
            "release": release_year
        })

        save_data(FILE, cars)
        print("Car added successfully.")

    except ValueError:
        print("Invalid Input.")

def format_cars(item):
    print(item["carname"])
    print(f"    Model: {item['carmodel']}")
    print(f"    Performance Rate: {item['carrate']}")
    print(f"    Release Year: {item['release']}")

def view_cars():
    cars = get_cars()
    display_list(cars, format_cars, "No cars yet!")

def delete_car():
    cars = get_cars()
    index = choose_item(cars, format_cars)

    if index is None:
        return
    
    cars.pop(index)
    save_data(FILE, cars)
    print("Deleted successfully.")

def report():
    cars = get_cars()
    total_cars = 0
    high_performance = 0
    mid_performance = 0 
    low_performance = 0

    for car in cars:
        total_cars += 1
        if car['carrate'] <= 3:
            low_performance += 1
        elif car['carrate'] < 7:
            mid_performance += 1
        else:
            high_performance += 1

    print(f"Total Cars: {total_cars}")
    print(f"High Performance Cars: {high_performance}")
    print(f"Mid Performance Cars: {mid_performance}")
    print(f"Low Performance Cars: {low_performance}")

def load_menu():
    menu = {
        "1": ("Add Car", add_cars),
        "2": ("View Cars", view_cars),
        "3": ("Delete Car", delete_car),
        "4": ("Report", report)
    }
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("5. Exit")

        choice = input("Choose: ")
        if choice == "5":
            print("Goodbye.")
            break    
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid Input")

load_menu()