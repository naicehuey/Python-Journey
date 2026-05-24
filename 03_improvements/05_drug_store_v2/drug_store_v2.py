print("Welcome To The Drug Store")

drugslist = [("Panado", 100), ("Ra", 100), ("Parapain", 100), ("Aspirin", 100), ("Headaxe", 100), ("ARVs", 100)]

def add_drug():
    add_drug = input(f"Here is the {drugslist}.\nwhat drugs do you wanna add? :")
    drug_units = int(input("How many units?: "))
    drugslist.append((add_drug, drug_units))
    print(f"{add_drug} is the new drug added.\nHere is the new list {drugslist}")

def sell_drug():
    meds = input("what you wanna buy?: ").lower()
    for drug, units in drugslist:
        if meds == drug.lower():
            number = int(input("How many you wanna buy?: "))
            drugs = [(meds, units - number)] 
            print(drugs)
            quit() 

def check_stock():
    print("Here is our current stock lineup:")
    for i, drugslist in enumerate(drugslist, start=1):
        print(f"{i}. {drugslist}")

def remove_drug():
    buy_drugs = input(f"Here is the drugs list: {drugslist}.\n Which drugs do you wanna buy? ")
    drugslist.remove(buy_drugs)
    print(f"Here is what we have now :{drugslist} \nAnd we are out of {buy_drugs} now, That was the last one.")
    
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