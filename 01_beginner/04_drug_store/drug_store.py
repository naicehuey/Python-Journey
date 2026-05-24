list1= ["panado", "aspirin", "paracetamol", "fragile"]
options = int(input("1. Enter a medicine name\n2.Enter a new medicine name\n3.Drugs we are out of stock\nEnter your option: "))
ask = input("Enter a medicine name: ").lower()
New_drug = input("Enter a new medicine name: ").lower()
if options == 1:
    if ask in list1:
        print("Medicine is available")
    else:
        print("Medicine is not available")
elif options == 2:
    list1.append(New_drug)
    print(list1)
elif options == 3:
    list1.remove(ask)
    print(list1)