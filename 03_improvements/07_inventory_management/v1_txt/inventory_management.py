def save_inventory(inventories):
    with open("inventory.txt", "a") as file:
        file.write(f"{inventories}\n")

def load_inventory():
    with open("inventory.txt", "r") as file:
        contents = file.readlines()

        if len(contents) == 0:
            print("Inventory Is Empty.")
            return

        for i, content in enumerate(contents, start=1):
            print(f"{i}. {content.strip()}")

def lines():
    print("=" *30)

def add_item():
    lines()
    print("     Add Inventory")
    lines()
    inv_name = input("Product Name: ").strip()
    inv_quantity = int(input("Product Quantity: "))

    inventories = f"{inv_name}:{inv_quantity}"
    print("This product was successfully added.")

    save_inventory(inventories)

def search_item():
    lines()
    print("     Search Inventory")
    lines()
    with open("inventory.txt","r") as file:
        contents = file.readlines()

        keyword = input("Search: ").strip()

        for content in contents:
            inv_name, _ = content.strip().split(":")
            if keyword.lower() == inv_name:
                print(content.strip())
                return
            
        print("This item is not available")

def update_quantity():
    lines()
    print("     Update Inventory Quantity")
    lines()
    with open("inventory.txt", "r") as file:
        contents = file.readlines()

        for i, content in enumerate(contents, start=1):
            print(f"{i}. {content.strip()}")

        choose = int(input("Which product quantity you wanna update: "))
        quantity = int(input("How many you wanna add: "))

        index = choose - 1

        choice = contents[index]

        inv_name , inv_quantity = choice.strip().split(":")

        new = int(inv_quantity) + quantity

        choice = f"{inv_name}:{new}\n"

        with open("inventory.txt", "w") as file:
                for content in contents:
                    file.write(content)

                print("Updated Successfully")

def remove_item():
    lines()
    print("     Remove Inventory")
    lines()
    try:
        with open("inventory.txt", "r") as file:
            contents = file.readlines()

            if len(contents) == 0:
                print("No Content Yet!!!")
                return
            
            for i, content in enumerate(contents, start=1):
                print(f"{i}. {content.strip()}")

            choose = int(input("Which product do you wanna delete: "))
            index = choose - 1

            contents.pop(index)
            with open("inventory.txt", "w") as file:
                for content in contents:
                    file.write(content)

                print("Product has been removed Successfully.")

    except FileNotFoundError:
        print("File is Missing.")

def load_menu():
    lines()
    print("     Main Menu")
    lines()
    while True:
        try:
            menu = [
                "1. Add Item",
                "2. View Inventory",
                "3. Search Item",
                "4. Update Quantity",
                "5. Remove Item",
                "6. Exit"
            ]

            for item in menu:
                print(item)

            chose = int(input("Choose Option: "))

            if chose not in [1, 2, 3, 4, 5, 6]:
                print("Wrong Input")

            elif chose == 1:
                add_item()

            elif chose == 2:
                load_inventory()

            elif chose == 3:
                search_item()

            elif chose == 4:
                update_quantity()

            elif chose == 5:
                remove_item()

            else:
                print("Thanks for using this app.\nBye")
                break

        except ValueError:
            print("Invalid Input")

load_menu()