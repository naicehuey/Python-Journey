import json

print("Welcome To Inventory Management System (I.M.S)")
def lines():
    print("=" *40)

def save_inventory(inventory):
    with open("inventory.json", "w") as inventoryx:
        json.dump(inventory, inventoryx)
    
def load_inventory():
    try:
        with open("inventory.json", "r") as inventoryx:
            return json.load(inventoryx)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
    
inventory = load_inventory()

def search_inventory(inventory):
    lines()
    print("     I.M.S: SEARCH   ")
    lines()
    keyword = input("Search for product: ").strip()
    if keyword == "":
        print("Can't search nothing")
        return
    
    found = False

    for i, invent in enumerate(inventory, start=1):
        if keyword.lower() in invent["name"].lower():
            print("Search has been found")
            lines()
            print(f"{i}. {invent['name']}")
            print(f"        Price: MKW {invent['price']}")
            print(f"        Units: {invent['stock']}")
            print(f"        Category: {invent['category']}")
            lines()
            found = True

    if not found:
        print("Product was not found")
        ask = input("Would you like to add the products(Y/N): ").lower()
        if ask == "y":
            add_inventory(inventory)

def add_inventory(inventory):
    lines()
    print("  I.M.S: ADDING STOCK ")
    lines()
    input1 = input("What's the product: ").strip()
    input2 = int(input("What's the price: "))
    input3 = input("Stock unit: ").strip()
    input4 = input("Categorize It: ").strip()

    new = {
        "name": input1,
        "price": input2,
        "stock": input3,
        "category": input4
    }
    if input1 == "" or input3 =="" or input4 == "":
        print("We need all field to work")
        return

    inventory.append(new)
    print("Inventory was successfully Added")
    lines()

def view_inventory(inventory):
    if len(inventory) == 0:
        print("Sorry seems like your Inventory is Empty")
        lines()
        return
    
    for i, invent in enumerate(inventory, start=1):
        print(f"{i}. {invent['name']}")
        print(f"        Price: MKW {invent['price']}")
        print(f"        Units: {invent['stock']}")
        print(f"        Category: {invent['category']}")
    
    lines()

def edit_inventory(inventory):
    lines()
    print("   I.M.S: EDITING STOCK ")
    lines()
    if len(inventory) == 0:
        print("Inventory is Empty")
        return
    
    view_inventory(inventory)
    
    try:
        ask = int(input("Which Product do you wanna edit: "))
        if ask < 1 or ask > len(inventory):
            print("Wrong Choice")
            return

        index = ask - 1

        print("Which section do you wish to edit.\n"
              "1. Product Name. \n2. Product Prices.\n"
              "3. Product Stock Unit.\n"
              "4. Product Category")
        input1 = int(input("Choose Option: "))
        if input1 not in (1, 2, 3, 4):
            print("Wrong Input")
            return
        
        if input1 == 1:
            xput = input("Change name: ").strip()
            inventory[index].update({"name": xput})

        elif input1 == 2:
            xput = input("Change Price: ").strip()
            inventory[index].update({"price": xput})

        elif input1 == 3:
            xput = int(input("Change Stock Unit: "))
            inventory[index].update({"stock": xput})

        else:
            xput = input("Change Category: ").strip()
            inventory[index].update({"category": xput})

        print("Updated Successfully")

    except ValueError:
        print("Invalid Input")

def restock_product(inventory):
    lines()
    print("   I.M.S: RESTOCK PRODUCT  ")
    lines()

    found = False

    for i, invent in enumerate(inventory, start=1):
        if int(invent["stock"]) < 5:
            print("These Products Need a Restock")
            print(f"{i}. {invent['name']}")
            print(f"      Stock Remaining: {invent['stock']}")
            found = True
        
    xxput = int(input("Which one would you like to restock: "))
    index = xxput - 1
    if xxput < 1 or xxput > len(inventory):
        print("not in question")
        return
    
    units = int(input("How many units do you wanna restock with: "))
    added = int(inventory[index]["stock"]) + units
    inventory[index]["stock"] = added
    print(f"Restock was successful.\nRestock Unit: {inventory[index]['stock']}")

def sell_stock(inventory):
    lines()
    print("   I.M.S: SELLING PRODUCTS  ")
    lines()

    xput = input("What product do you wanna sell: ").strip()
    if xput == "":
        print("It can not be empty")
        return
    
    for i, invent in enumerate(inventory, start=1):
        if xput.lower() in invent["name"].lower():
            print("Product is available")
            xput1 = int(input("How many stocks do you wanna sell: "))
            if xput1 <= int(invent["stock"]):
                sold = int(invent["stock"]) - xput1
                invent["stock"] = sold
                total = int(invent["price"]) * xput1
                print(f"{i}. {invent['name']}")
                print(f"        Total Sold Stocks: {xput1}")
                print(f"        Remaining Stocks:  {sold}")
                print(f"        Total Cost in MKW:  {total}")
                return
            
            low_stock_alert(inventory)

def low_stock_alert(inventory):
    found = False

    for i, invent in enumerate(inventory, start=1):
        if int(invent["stock"]) <= 5:
            print("These Products Need a Restock")
            print(f"{i}. {invent['name']}")
            print(f"      Stock Remaining: {invent['stock']}")
            found = True
        
    if not found:
        print("All stocks are okay")

def delete_product(inventory):
    lines()
    print(" I.M.S: DELETE STOCK ")
    lines()
    if len(inventory) == 0:
        print("The Inventory seems Empty")
        return
    
    view_inventory(inventory)

    try:
        choice = int(input("Which inventory do you wanna delete:"))
        index = choice - 1

        if choice < 1 or choice > len(inventory):
            print("Sorry! Invalid Input")
            return
        
        inventory.pop(index)

    except ValueError:
        print("Invalid Input")

def menu():
    lines()
    print("       MAIN MENU      ")
    lines()
    while True:
        try:
            menu = [
                "0. Search Product",
                "1. Add New Inventory",
                "2. View Inventory",
                "3. Delete Inventory",
                "4. Edit Product",
                "5. Restock",
                "6. Sell",
                "7. Reports",
                "8. Exit"
            ]

            for item in menu:
                print(item)
            lines()
            choice = int(input("Choose Option: "))
            
            if choice == 0:
                search_inventory(inventory)
            elif choice == 1:
                add_inventory(inventory)
                save_inventory(inventory)
            elif choice == 2:
                view_inventory(inventory)
            elif choice == 3:
                delete_product(inventory)
                save_inventory(inventory)
            elif choice == 4:
                edit_inventory(inventory)
                save_inventory(inventory)
            elif choice == 5:
                restock_product(inventory)
                save_inventory(inventory)
            elif choice == 6:
                sell_stock(inventory)
                save_inventory(inventory)
            elif choice == 7:
                low_stock_alert(inventory)
            elif choice == 8:
                print("Thanks for Using I.M.S")
                break
            else:
                print("Wrong Input")

        except ValueError:
            print("Wrong Input")

menu()
