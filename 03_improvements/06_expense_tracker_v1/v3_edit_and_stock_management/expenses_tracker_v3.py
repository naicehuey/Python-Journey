def save_expenses(expense):
    with open("expense.txt", "a") as file:
        file.write(f"{expense}\n")

def load_expenses():
    with open("expense.txt", "r") as file:
        contents = file.readlines()

    for i, content in enumerate(contents, start=1):
        exp_name, exp_price, exp_stock, exp_total = content.strip().split("|")
        print(f"{i}. {exp_name}")
        print(f"           Price: MWK {exp_price}")
        print(f"           Stock: {exp_stock}")
        print(f"           Total: MWK {exp_total}")

def add_expense():
    product = input("Product Name: ").strip()
    price = int(input("Product Price: "))
    stock = int(input("Stock Quantity: "))
    total = price * stock

    expense = f"{product}|{price}|{stock}|{total}"
    save_expenses(expense)

def sum_stock():
    try:
        with open("expense.txt", "r") as file:
            contents = file.readlines()

        for i, content in enumerate(contents, start=1):
            name, price, stock, total = content.strip().split("|")
            print(f"{i}. Product: {name}")
            print(f"        Price: {price}")
            print(f"        Stock: {stock}")
            print(f"        Total: {total}")

        choice = int(input("Choose Expense: "))
        index = choice - 1

       
        name, price, old_stock, old_total = contents[index].strip().split("|")

        option = int(input(
            "1. Add Stock\n"
            "2. Subtract Stock\n"
            "Enter option: "
        ))
        
        if option == 1:
            add = int(input("How many stocks do you wanna add: "))
            old_stock = int(old_stock)
            price = int(price)
            new_stock = add + old_stock
            new_total = price * new_stock
            stock_time = f"{name}|{price}|{new_stock}|{new_total}\n"
            contents[index] = stock_time

        elif option == 2:
            sub = int(input("How many stocks do you wanna remove: "))
            old_stock = int(old_stock)
            price = int(price)
            if sub > old_stock:
                print("We don't have enough to remove that amount.")
                return
            else:
                new_stock = old_stock - sub
                new_total = price * new_stock
                stock_time = f"{name}|{price}|{new_stock}|{new_total}\n"
                contents[index] = stock_time
        
        else:
            print("Wrong option")
            return

        with open("expense.txt", "w") as file:
            for content in contents:
                file.write(content)

        print("Stock Updated Successfully")

    except FileNotFoundError:
        print("File Not Found")

def edit_expense():
    try:
        with open("expense.txt", "r") as file:
            contents = file.readlines()
            if len(contents) == 0:
                print("No Expenses Yet.")
                return

        for i, content in enumerate(contents, start=1):
            name, price, stock, total = content.strip().split("|")
            print(f"{i}. Product: {name}")
            print(f"        Price: {price}")
            print(f"        Stock: {stock}")
            print(f"        Total: {total}")

        choose = int(input("Which product you wanna edit: "))
        index = choose - 1

        name, price, stock, total = contents[index].strip().split("|")

        choice = int(input(
            "1. Edit product name, price and stock\n"
            "2. Edit just the product price\n"
            "3. Edit just the stock quantity\n"
            "Enter option: "
        ))

        if choice == 1:
            product = input("New Product: ").strip()
            new_price = int(input("New Price: "))
            new_stock = int(input("New Stock: "))
            total = new_price * new_stock
            new_product = f"{product}|{new_price}|{new_stock}|{total}\n"

        elif choice == 2:
            new_price = int(input("New Price: "))
            new_total = new_price * int(stock)
            new_product = f"{name}|{new_price}|{stock}|{new_total}\n"

        elif choice == 3:
            new_stock = int(input("New Stock Quantity: "))
            new_total = int(price) * new_stock
            new_product = f"{name}|{price}|{new_stock}|{new_total}\n"

        else:
            print("Wrong Option")
            return

        contents[index] = new_product

        with open("expense.txt", "w") as file:
            for content in contents:
                file.write(content)

        print("Updated Successfully")

    except FileNotFoundError:
        print("File Not Found")

def clear_expenses():
    with open("expense.txt", "w") as file:
        pass
    print("Expenses Have Been Cleared")

def remove_expense():
    with open("expense.txt", "r") as file:
        contents = file.readlines()

    for i, content in enumerate(contents, start=1):
        product, _, _, _ = content.strip().split("|")
        print(f"{i}. {product}")

    chose = int(input("Which expense you wanna remove: "))
    index = chose - 1

    contents.pop(index)
    with open("expense.txt", "w") as file:
        for content in contents:
            file.write(content)

    print("Expense removed successfully")

def total_expense():
    try:
        with open("expense.txt", "r") as file:
            contents = file.readlines()

        total = 0
        for content in contents:
            _, exp_price, _, _ = content.strip().split("|") 
            total += int(exp_price)

        print(f"Expenses Total Cost: MWK {total}")

    except FileNotFoundError:
        print("File Not Found")

def load_menu():
    while True:
        try:
            menu = [
                "1. Add Expense",
                "2. View Expenses",
                "3. Edit Expense",  
                "4. Clear Expenses",
                "5. Total Expenses Spent",
                "6. Update Stock",
                "7. Exit"
            ]
            for item in menu:
                print(item)

            chose = int(input("Choose Option: "))

            if chose not in [1, 2, 3, 4, 5, 6, 7]:
                print("Wrong option")

            elif chose == 1:
                add_expense()

            elif chose == 2:
                load_expenses()

            elif chose == 3:
                edit_expense()

            elif chose == 4:
                clear_expenses()

            elif chose == 5:
                total_expense()

            elif chose == 6:
                sum_stock()

            else:
                print("Thank you for using this app.")
                break

        except ValueError:
            print("Invalid Option")

load_menu()
