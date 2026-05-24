from datetime import datetime

time = datetime.now()

with open("log.txt", "a") as file:
    file.write(f"{time}\n")

with open("log.txt", "r") as file:
    content = file.readlines()
    print(content)