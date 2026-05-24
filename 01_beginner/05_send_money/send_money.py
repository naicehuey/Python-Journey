import datetime

print("Hello Mate, Welcome to Send Your Money Safe")
cards = ["lelrofnsk@outlook.com", "Hujkahdo@gmail.com", "Malume@gmail.com", "Cwm@outlook.com"]
x = datetime.datetime.now()
print(x)

y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")