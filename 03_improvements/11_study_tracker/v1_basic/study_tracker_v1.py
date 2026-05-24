from datetime import datetime

def lines():
    print("=" *30)

def save_session(session):
        with open("sessions.txt", "a") as file:
            file.write(f"{session}\n")

def load_session():
    lines()
    print("       View History")
    lines()
    with open("sessions.txt", "r") as file:
        contents = file.readlines()
        print("Here is the record: ")
        for i, content in enumerate(contents, start=1):
            print(i, ".", content)

def add_session():
    lines()
    print("       Add Study Session")
    lines()
    topic = input("What subject are you gonna study: ").strip().lower()
    hours = int(input("How many hours are you gonna study: "))

    time = datetime.now()

    session = f"{topic} | {hours} Hours | {time}"

    save_session(session)
    print("Session Recorded Successfully")

def view_session():
    load_session()

def load_menu():
    lines()
    print("       MAIN MENU")
    lines()
    while True:
        try:
            menu = [
                "1. Add a Study Session",
                "2. View Your Session History",
                "3. Exit"
            ]

            for item in menu:
                print(item)

            choose = int(input("Choose Option: "))

            if choose not in [1, 2, 3]:
                print("Wrong Option")

            elif choose == 1:
                add_session()

            elif choose == 2:
                view_session()

            else:
                print("Thank You For Using Study Records.\nCome Back Again.")
                break
        except ValueError:
            print("Invalid Option")

load_menu()