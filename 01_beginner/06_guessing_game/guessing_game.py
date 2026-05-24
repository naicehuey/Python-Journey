import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fruits = ['apple', 'banana', 'mango', 'guava']

print("We are about to start a guessing a game between fruits and numbers")
choice = input("which one are you gonna go for?: ")
a = choice.lower()

if a == "fruits":
    print(fruits)
    choose = input("Guess my choice: ").lower()
    pc = random.choice(fruits)
    if choose == pc:
        print("You win")
    else:
        print("This is my choice " + pc)
        print("You Lose, Try again")

elif a == "numbers":
    print(numbers)
    choose = input("Guess my number: ")
    pc = random.choice(numbers)
    if choose == pc:
        print("You win")
    else:
        print("This is my choice " + str(pc))
        print("You Lose, Try again")

else:
    print("This wasn't part of the game")