print("Welcome To Daily Journal")
def new_thought():
    lines()
    print("     New Journal")
    lines()
    thoughts = input("New Thought: ")

    with open("thoughts.txt", "w") as file:
        file.write(thoughts)
        print("Added Successfully")
        print()

def append_thoughts():
    lines()
    print("     Add a Thought")
    lines()
    thoughts = input("Add a Thought: ")

    with open("thoughts.txt", "a") as file:
        file.write(f"\n{thoughts}")
        print("Added Successfully")
        print()

def read_lines():
    lines()
    print("     View Journal")
    lines()
    with open("thoughts.txt", "r") as file:
        contents = file.readlines()
        for i, content in enumerate(contents, start=1):
            print(i, ".", content.strip())
        print()

def lines():
    print("=" *30)

def menu():
    lines()
    print("     Main Menu")
    lines()
    while True:
        try:
            optional = [
                "1. Start a New Journal",
                "2. Add a New Thought",
                "3. View Journal",
                "4. Exit"
            ]
            for x in optional:
                print(x)

            choose = int(input("Choose Option: "))
            print()

            if choose not in [1, 2, 3, 4]:
                print("Invalid Input")

            elif choose == 1:
                new_thought()

            elif choose == 2:
                append_thoughts()

            elif choose == 3:
                read_lines()

            else:
                print("Thank You, Goodbye")
                print()
                break

        except ValueError:
            print("Wrong Input")

menu()