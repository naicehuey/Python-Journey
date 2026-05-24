print("Do you want to add a new note or continue with the existing notes")
decide = int(input("1. to start a new or 2 to continue or 3. to view Notes: "))

if decide == 1:
    new_line = input("Add a thought: ")
    with open("notex.txt", "w") as file:
        file.write(new_line)

elif decide == 2:
    new_line = input("Add a new line: ")
    with open("notex.txt", "a") as file:
        file.write(f"\n{new_line}")
elif decide == 3:
    with open("notex.txt", "r") as file:
        news = file.readlines()
        for i, new in enumerate(news, start=1):
            print(i, ".", new.strip())
    exit()

else:
    print("Wrong Input")

with open("notex.txt", "r") as file:
    contents = file.readlines()
    for i, content in enumerate(contents, start=1):
        print(i, ".", content.strip())