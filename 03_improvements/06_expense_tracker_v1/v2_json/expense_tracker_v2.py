import json
from datetime import datetime

print("This is a Expense Tracking App\nWelcome !!")

def save_expense(expenses):
    with open("expenses.json", "w") as expensex:
        json.dump(expenses, expensex)

def load_expense():
    try:
        with open("expenses.json", "r") as expensex:
            return json.load(expensex)
        
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
    
expenses = load_expense()

def lines():
    print("=" *30)

def add_expenses(expenses):
    lines()
    print("EXPENSE TRACKER: ADDING EXPENSES")
    lines()
    try:
        input1 = input("What you buying: ").strip()
        input2 = int(input("How much does it cost: "))
        input3 = input("Which category is this: ").strip()
        if input1 ==""  or input3 == "":
            print("All fields are required")
            return

        time = datetime.now().strftime("%Y - %B - %A %H:%M")

        expenses.append({
                "title" : input1,
                "amount" : input2,
                "category" : input3,
                "date" : time
            }
        )

        print("Expense has been added Successfully")

    except ValueError:
        print("Amount must be a number")

def search_expense(expenses):
    lines()
    print("           EXPENSE TRACKER: SEARCH         ")
    lines()
    keyword = input("Search: ").strip()
    if keyword =="":
        print("Please!!, The Search Bar Can Not Be Empty.. ")
        return
        
    found = False

    for i, expense in enumerate(expenses, start=1):
        if keyword.lower() in expense["title"].lower():
            print("Expense found")
            print(f"{i}. {expense['title']}")
            found = True

    if not found:
        print("No such expense yet!")
        ask = input("Would you like to add perhaps(Y/N): ").strip()
        if ask.lower() == "y":
            add_expenses(expenses)

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet")
        return
    
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['title']}")
        print(f"    Amount spend: {expense['amount']}")
        print(f"    Category : {expense['category']}")
        print(f"    Date Added: {expense['date']}")
        print()

def edit_expense(expenses):
    lines()
    print("      EXPENSE TRACKER: EDIT       ")
    view_expenses(expenses)

    if len(expenses) == 0:
        return
    
    try:
        choose = int(input("Which expense do you wanna change: "))
        if choose < 1 or choose > len(expenses):
            print("Invalid Input")
            return
        
        index = choose - 1

        input1 = input("What you buying: ").strip()
        input2 = int(input("How much does it cost: "))
        input3 = input("Which category is this: ").strip()

        expenses[index].update({
                "title" : input1,
                "amount" : input2,
                "category" : input3
            }
        )

        print("Expense has been Updated Successfully")

    except (ValueError, IndexError):
        print("Invalid Input")   

def filter_by_category(expenses):
    lines()
    print("           EXPENSE TRACKER: FILTER          ")
    lines()
    if len(expenses) == 0:
        print("No Expenses to be Filtered")
        return
    
    try:
        choice = int(input("1. For search by category.\n2. For all categories: "))

        if choice == 1:
            search = input("What Category do you wanna search on: ").strip()
            same = 0
            found = False

            for i, expense in enumerate(expenses, start=1):
                if expense['category'].lower() == search.lower():
                    same += 1
                    found = True

            if found:
                print(f"Here is your search: {search}: {same}")
            else:
                print("Couldn't find the category")

        if choice == 2:
            counts = {}
            for expense in expenses:
                category = expense["category"]
                if category in counts:
                    counts[category] += 1
                else:
                    counts[category] = 1

            for category, total in counts.items():
                print(f"{category} = {total}")

    except ValueError:
        print("Invalid Option")

def sort_expenses(expenses):
    lines()
    print("       EXPENSE TRACKER: SORT        ")
    lines()
    try:
        choice = int(input("1. Lowest Amount \n2. Highest Amount \n3. Newest Date. \n4. Old Date: "))
        if choice not in (1, 2, 3, 4):
            print("Invalid Choice")
            return
        
        if choice == 1:
            sorted_expenses = sorted(expenses, key=lambda expense: expense["amount"])
        elif choice == 2:
            sorted_expenses = sorted(expenses, key=lambda expense: expense["amount"], reverse=True)
        elif choice == 3:
            sorted_expenses = sorted(expenses, key=lambda expense: expense["date"])
        else:
            sorted_expenses = sorted(expenses, key=lambda expense: expense["date"], reverse=True)

        for i, expense in enumerate(sorted_expenses, start=1):
            print(f"{i}. {expense['title']} - {expense['amount']} - {expense['date']}")

    except ValueError:
        print("Wrong Choice")

def delete_expense(expenses):
    lines()
    print("  EXPENSE TRACKER: DELETE  ")
    if len(expenses) == 0:
        print("You haven't added anything yet")
        return
        
    view_expenses(expenses)

    try:
        choice = int(input("Which expense do you wanna delete: "))
        index = choice - 1

        if choice < 1 or choice > len(expenses):
            print("Wrong choice")
            return
        
        expenses.pop(index)
        print("Expense has been removed")

    except ValueError:
        print("invalid Option")

def show_total(expenses):
    lines()
    print("EXPENSE TRACKER: SUMMING UP")
    lines()
    if len(expenses) == 0:
        print("You haven't added anything yet")
        return
    
    view_expenses(expenses)
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Spent: {total}")

def month_summary(expenses):
    lines()
    print("EXPENSE TRACKER: MONTHLY SUMMARY")
    lines()
    if len(expenses) == 0:
        print("The Expenses are Empty")
        return
    
    summary = {}
    for expense in expenses:
        month = expense["date"][:10]
        amount = expense["amount"]

        if month in summary:
            summary[month] += amount
        else:
            summary[month] = amount

    for month, total in summary.items():
        print(f"{month} = {total}")

def menu():
    lines()
    print("       MAIN MENU      ")
    lines()
    while True:
        try:
            print("0. Search for expense. \n1. Add Expenses\n2. View Expenses.\n3. Delete Expenses.\n4. Category.\n5. Show Total Spent On Expenses.\n6. Edit Expenses. \n7. Monthly Summary. \n8. Sort Expenses. \n9. Exit App")
            lines()
            choice = int(input("Choose Option: "))

            if choice == 0:
                search_expense(expenses)
            elif choice == 1:
                add_expenses(expenses)
                save_expense(expenses)
            elif choice == 2:
                view_expenses(expenses)
            elif choice == 3:
                delete_expense(expenses)
                save_expense(expenses)
            elif choice == 4:
                filter_by_category(expenses)
            elif choice == 5:
                show_total(expenses)
            elif choice == 6:
                edit_expense(expenses)
                save_expense(expenses)
            elif choice == 7:
                month_summary(expenses)
            elif choice == 8:
                sort_expenses(expenses)
            elif choice == 9:
                print("Thank you for using Expenses Tracker.\nHave a Great Day!!")
                break
            else:
                print("Wrong option")

        except ValueError:
            print("Invalid Option")

menu()