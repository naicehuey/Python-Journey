def save_history(history):
    with open("history.txt", "a") as file:
        file.write(history)

def send_message():
      txt = "Hello, I am Pretty, Whats Your name: "
      print(txt)
      Huey = input("Waiting for your reply: ")
      txt1 = f"Nice to meet you, {Huey}.\nWhat you wanna talk about? "
      print(txt1)
      huey = input("Waiting for reply: ")
      txt2 = f"So you wanna talk about {huey}.\nI am taking my time off.\nWe will talk about it soon.\nBye.\n"
      print(txt2)

      history = f"Pretty: {txt}\n{Huey}: {Huey}\nPretty: {txt1}\n{Huey}: {huey}\nPretty: {txt2}\n"
      
      save_history(history)

def view_history():
        with open("history.txt", "r") as file:
            contents = file.readlines()
            if not contents:
                print("History Is Empty")
            else:
                print("Here is all your chat history:")
                for content in contents:
                    print(f"{content.strip()}")

def clear_history():
        with open("history.txt", "w") as file:
            pass

        print("History has been cleared.\nLets start a new.")
        print()

def menu():
    while True:
        try:
            menu = [
                "1. Send Message ",
                "2. View Chat History",
                "3. Clear Chat",
                "4. Exit"
            ]  

            for item in menu:
                print(item)

            choose = int(input("Make a choice: "))
            print()

            if choose not in [1, 2, 3, 4]:
                print("Wrong Option")

            elif choose == 1:
                send_message()

            elif choose == 2:
                view_history()

            elif choose == 3:
                clear_history()

            else:
                print("Thank you for using our chatbox")
                break

        except ValueError:
            print("Invalid Option")

menu()
