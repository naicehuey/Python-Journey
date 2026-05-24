def lines():
    print("=" *30)
    
def save_expenses(expense):
    with open("expense.txt", "a") as file:
        file.write(f"{expense}\n")

def load_expenses():
    lines()
    print("     View Expenses")
    lines()
    with open("expense.txt", "r") as file:
        contents = file.readlines()

    for i, content in enumerate(contents, start=1):
        exp_name, exp_price = content.strip().split("|")
        print(f"{i}. {exp_name}")
        print(f"           Prize: MWK {exp_price}")

def add_expense():
    lines()
    print("     Add Expense")
    lines()
    product = input("Product Name: ").strip()
    price = int(input("Product Price: "))

    expense = f"{product}|{price}"

    save_expenses(expense)

def clear_expenses():
    lines()
    print("     Clear Expenses")
    lines()
    with open("expense.txt", "w") as file:
        pass

    print("Expenses Have Been Cleared")

def remove_expense():
    lines()
    print("     Remove Expense")
    lines()
    with open("expense.txt", "r") as file:
        contents= file.readlines()

    for i, content in enumerate(contents, start=1):
        product, _ = content.strip().split("|")
        print(f"{i}. {product}")

    chose = int(input("Which expense you wanna remove: "))
    index = chose - 1

    contents.pop(index)
    with open("expense.txt", "w") as file:
        for content in contents:
            file.write(content)

def total_expense():
    lines()
    print("     Total On Expenses")
    lines()
    try:
        with open("expense.txt", "r") as file:
            contents = file.readlines()

        total = 0
        for content in contents:
            _ , exp_prize = content.strip().split("|")
            plus = int(exp_prize)
            total += plus

        print(f"Expenses Total Cost: MWK {total}")

    except FileNotFoundError:
        print("File Not Found")

def load_menu():
    lines()
    print("     Main Menu")
    lines()
    while True:
        try:
            menu = [
            "1. Add Expense",
            "2. View Expenses",
            "3. Clear Expenses",
            "4. Total Expenses Spent",
            "5. Exit"
            ]
            for item in menu:
                print(item)

            chose = int(input("Choose Option: "))

            if chose not in [1, 2, 3, 4, 5]:
                print("wrong option")

            elif chose == 1:
                add_expense()

            elif chose == 2:
                load_expenses()

            elif chose == 3:
                clear_expenses()

            elif chose == 4:
                total_expense()

            else:
                print("Thank you for using this app.")
                break

        except ValueError:
            print("Invalid Option")

load_menu()