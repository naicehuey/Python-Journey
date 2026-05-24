print("Welcome To KiMeFra Restraunt.\n Here is the menu:\n Rice and Chicken: 5000\n Spaghetti: 2000")
list1 = ['rice and chicken', 'spaghetti']
choice = input("what do you choose: ").lower()
if choice == list1[0]:
    print("Here is the price: 5000")
    tip = int(input("We receive tip from 10 percent to 20 : "))
    x =  5000/100*tip
    print("Tip is 20 percent of the main price which is: " + str(x))
    y = x + 5000
    Total_price = ("Here is the total price" +str(y))
    print(Total_price)

elif choice == list1[1]:
    print("Here is the price: 2000")
    tip = int(input("We receive tip from 10 percent to 20 : "))
    x =  2000/100*tip
    print("with the Tip price which is" + str(x))
    y = x + 2000
    Total_price = ("Here is the total price" + str(y))
    print(Total_price)

else:
    print("It's not on the Menu")

choose1 = input("Would you like Tomato Spray or cheese spray?: ").lower()
if choose1 == "tomato spray":
    print("That will be 15")
    z = y + 15
    print("Here is the total: " + str(z))

elif choose1 == "cheese spray":
    print("That will be 40")
    z = y + 40
    print("Here is the total: " + str(z))

else:
    print("I guess there is nothing else, please enjoy your meal.")