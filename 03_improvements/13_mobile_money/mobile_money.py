import json

def save_account(accounts):
    with open("account.json", "w") as file:
        json.dump(accounts, file)

def load_account():
    try:
        with open("account.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

accounts = load_account()
logged_in = None

def lines():
    print("=" *30)

def register_acc():
    lines()
    print("      New Account")
    lines()
    name = input("Username: ").strip()
    pin = int(input("Pin: "))

    new = {
        "username" : name,
        "pin" : pin,
        "balance" : 0
    }

    accounts.append(new)
    save_account(accounts)
    lines()
    print("Account Created Successfully")

def delete_acc():
    global logged_in
    if logged_in:
        accounts.remove(logged_in)
        save_account(accounts)
        logged_in = None
        lines()
        print("Account deleted successfully.")
        # No need to call logged_out() — already handled above
    else:
        print("No account logged in")

def login():
    lines()
    print("      Login Account")
    lines()
    global logged_in
    name = input("Username: ").strip()
    pin = int(input("What is your pin: "))
    for account in accounts:
        if pin == account["pin"] and name == account["username"]:
            logged_in = account
            lines()
            print("Login Successful")
            return True

    lines()
    print("Login Failed")
    return False

def withdraw():
    lines()
    print("      Withdraw")
    lines()
    global logged_in
    if logged_in:
        if logged_in["balance"] == 0:
            print("Your balance is empty. Please deposit first.")
        else:
            print(f"Balance: {logged_in['balance']}")
            take = int(input("Amount to withdraw: "))
            if logged_in["balance"] - take >= 0:
                logged_in["balance"] -= take
                lines()
                print(f"Withdrawn: {take}")
                print(f"New Balance: {logged_in['balance']}")
                save_account(accounts)
            else:
                print("Insufficient funds!")  # ← Fixed!
    else:
        print("No account logged in")

def deposit():
    lines()
    print("      Deposit")
    lines()
    global logged_in
    if logged_in:
        put = int(input("How much you wanna deposit: "))
        if put > 0:
            logged_in["balance"] += put
            lines()
            print(f"New Balance: {logged_in['balance']}")
            save_account(accounts)
        else:
            print("Deposit must be positive")
    else:
        print("No account logged in")

def logged_out():
    global logged_in
    logged_in = None
    lines()
    print("Logged out successfully")

def invalid_option():
    print("Error 101: This option does not exist.")

def load_menu():
    lines()
    print("      Main Menu")
    lines()
    while True:
        try:
            menu = [
                "1. New Account",
                "2. Login",
                "3. Exit"   # ← Fixed typo!
            ]

            for item in menu:
                print(item)

            options = int(input("Choose Option: "))

            if options not in [1, 2, 3]:
                print("Wrong Input")

            elif options == 1:
                register_acc()
                lines()

            elif options == 2:
                success = login()
                lines()

                if success:
                    while True:
                        lines()
                        action = {
                            1: withdraw,
                            2: deposit,
                            3: delete_acc,
                            4: logged_out
                        }

                        option = int(input(
                            "1. Withdraw\n"
                            "2. Deposit\n"
                            "3. Delete Account\n"
                            "4. Logout\n"
                            "Enter your Option: "
                        ))

                        action.get(option, invalid_option)()

                        if option == 3 or option == 4:
                            break   # ← Combined into one clean check!

            else:
                lines()
                print("Thank you for using this app.")
                break

        except ValueError:
            print("Invalid Input")

load_menu()