with open("notes.txt", "w") as file:
    file.write("Hello World")

yes = input("What should we print: ")

with open("notes.txt", "a") as file:
    file.write("\nLearning File Handling")
    file.write(f"\n{yes}")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)