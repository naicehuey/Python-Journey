print("Welcome To The Drug Store")

drugslist = [("Panado", 100), ("Ra", 100), ("Parapain", 100), ("Aspirin", 100), ("Headaxe", 100), ("ARVs", 100)]

def add_drug():
    add_drug = input(f"Here is the {drugslist}.\nwhat drugs do you wanna add? :")
    drug_units = int(input("How many units?: "))
    drugslist.append((add_drug, drug_units))
    print(f"{add_drug} is the new drug added.\nHere is the new list {drugslist}")

def sell_drug():
    meds = input("What you wanna buy?: ").lower()
    for i, (drug, units) in enumerate(drugslist):
        if meds == drug.lower():
            number = int(input("How many you wanna buy?: "))
            if number > units:
                print("Not enough stock!")
                return
            new_units = units - number
            drugslist[i] = (drug, new_units)
            print(f"Sold {number} of {drug}")
            print(f"Remaining stock: {new_units}")
            return
    print("Medicine not found")

def check_stock():
    print("Here is our current stock lineup:")
    for i, drug in enumerate(drugslist, start=1):
        print(f"{i}. {drug}")

def remove_drug():
    print("Here is the drugs list:")
    for i, (drug, units) in enumerate(drugslist, start=1):
        print(f"{i}. {drug} - {units} units")
    
    choose = int(input("Which drug number do you wanna remove: "))
    index = choose - 1
    
    if index < 0 or index >= len(drugslist):
        print("Invalid choice")
        return
    
    removed = drugslist.pop(index)
    print(f"{removed[0]} has been removed.")
    
def invalid_option():
    print("Error 101: This option does not exist.")

actions = {
    1: add_drug,
    2: sell_drug,
    3: check_stock,
    4: remove_drug
}

option = int(input(
    "What would you like to do?\n"
    "1. Add a New Drug\n"
    "2. Sell a Drug\n"
    "3. Check Stock\n"
    "4. Remove Unsupported Drug\n"
    "Enter option: "
))

actions.get(option, invalid_option)()
