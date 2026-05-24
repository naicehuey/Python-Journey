import json

def save_user(users):
    with open("users.json", "w") as userx:
        json.dump(users, userx)

def load_user():
    try:
        with open("users.json", "r") as userx:
            return json.load(userx)
    except (json.JSONDecodeError, FileNotFoundError):
        return[]
    
users = load_user()

def lines():
    print("=" *40)

def create_user():
    lines()
    print("     Create User")
    lines()
    user_name = input("Create a Username: ").strip()
    if user_name == "":
        print("Username can not be an empty space")
        return
    
    password = input("Please create a password: ").strip()
    if password == "" or len(password) < 8:
        print("Password needs to have 8 or more characters")
        return
    
    new_user ={
        "name" : user_name,
        "passcode" : password
    }

    users.append(new_user)
    print("User Registered!")

def login():
    lines()
    print("     Login")
    lines()

    attempt = 3

    while attempt > 0:
        username = input("Username: ").strip()
        if username == "":
            print("Username can not be an empty space")
            continue
        
        user_password = input("Password: ").strip()
        if user_password == "" or len(user_password) < 8:
            print("Password needs @least 8 characters")
            continue
        
        found_user = False
        correct_password = False
        
        for u in users:
            if u["name"] == username:
                found_user = True
                if u["passcode"] == user_password:
                    correct_password = True
                break
            
        if not found_user:
            attempt -= 1
            print(f"User not found. Attempts left: {attempt}")
            
        elif not correct_password:
            attempt -= 1
            print(f"Incorrect Password. Attempts left: {attempt}")
            
        else:
            print("Login Successful")
            return

    print("Account locked. Too many failed attempts.")
        
def menu():
    lines()
    print("     Main Menu")
    lines()
    while True:
        try:
            menu = [
                "1. Create User",
                "2. Login",
                "3. Exit"
            ]
            for item in menu:
                print(item)

            lines()
            chose = int(input("Chose Option:  "))
            lines()

            if chose == 1:
                create_user()
                save_user(users)

            elif chose == 2:
                login()

            elif chose == 3:
                print("Till next time, Thank you!!")
                break

            else:
                print("Wrong choice, try again")

        except ValueError:
            print("Invalid Input")

menu()