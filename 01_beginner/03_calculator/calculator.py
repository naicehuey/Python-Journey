x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = input("Enter a mathematical operator: ")
if z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "*":
    print(x * y)
elif z == "/":
    print(x / y)
else:
    print("Operator not supported")