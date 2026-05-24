def lines():
    print("=" *40)

def save_user(users):
    with open("users.txt", "a") as file:
        file.write(users)

def load_users():
    lines()
    print("     View Users")
    lines()
    with open("users.txt", "r") as file:
        users = file.readlines()

        print("\nRegistered Users:")
        for i, user in enumerate(users, start=1):
            username, _ = user.strip().split(":")
            print(f"{i}. {username}")

def register():
    lines()
    print("     Register Account")
    lines()
    print("Register Account")
    name = input("Username: ").strip()
    password = input("Password: ").strip()

    users = f"{name}:{password}"

    save_user(users)

def login():
    lines()
    print("     Login")
    lines()
    name_log = input("Username: ").strip()
    pass_log = input("Password: ").strip()

    with open("users.txt", "r") as file:
        users = file.readlines()

        for user in users:
            username, password = user.strip().split(":")
            if username == name_log and password == pass_log:
                print("Login In Successfull")
                return

        print("Login Failed. Try Again")

def load_menu():
    lines()
    print("     Main Menu")
    lines()
    while True:
        try:
            menu = [
                "1. Register",
                "2. Login",
                "3. View Users",
                "4. Exit"
            ]

            for item in menu:
                print(item)

            print()
            chose = int(input("Choose Option: "))

            if chose not in  [1, 2, 3, 4]:
                print("Wrong Choice")

            elif chose == 1:
                register()

            elif chose == 2:
                login()

            elif chose == 3:
                load_users()

            else:
                print("Thank you for your time")
                break
        
        except ValueError:
            print("Invalid Input")

load_menu()