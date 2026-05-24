from datetime import datetime

def lines():
    print("=" *30)

def save_session(study):
    with open("study.txt", "a") as file:
        file.write(f"{study}\n")

def load_session():
    lines()
    print("       View History")
    lines()
    try:
        with open("study.txt", "r") as file:
            contents = file.readlines()

        if len(contents) == 0:
            print("File Not Found.")
            return

        for i, content in enumerate(contents, start=1):
            topic, time, hours = content.strip().split("|")
            print(f"{i}. Subject: {topic}")
            print(f".      Date/Time: {time}")
            print(f".      Time Spent: {hours} Hours")

    except FileNotFoundError:
        print("File does not exist.")

def add_topic():
    lines()
    print("       Add Study Session")
    lines()
    topic = input("Add Subject: ").strip()
    hours = int(input("Hours To Read: "))

    time = datetime.now()

    study = f"{topic}|{time}|{hours}"

    save_session(study)

def clear_session():
    lines()
    print("       Clear History")
    lines()
    with open("study.txt", "w") as file:
        pass

    print("Study Sessions Have been cleared")

def total_hours():
    lines()
    print("       Total Session Hours")
    lines()
    try:
        with open("study.txt", "r") as file:
            contents = file.readlines()

        total = 0
        for content in contents:
            y, x, hours = content.strip().split("|")
            plus = int(hours)
            total += plus

        print(f"Total hours spent Studying: {total}")

    except FileNotFoundError:
        print("File Not Found")

def load_menu():
    lines()
    print("       Main Menu")
    lines()
    while True:
        try:
            menu = [
            "1. Add Session",
            "2. View Sessions",
            "3. Clear Sessions",
            "4. Total Study Hours",
            "5. Exit"
            ]
            for item in menu:
                print(item)

            chose = int(input("Choose Option: "))

            if chose not in [1, 2, 3, 4, 5]:
                print("Wrong Input")

            elif chose == 1:
                add_topic()

            elif chose == 2:
                load_session()

            elif chose == 3:
                clear_session()

            elif chose == 4:
                total_hours()

            else:
                print("Thank you for using this app. Bye")
                break

        except ValueError:
            print("Invalid Option")

load_menu()