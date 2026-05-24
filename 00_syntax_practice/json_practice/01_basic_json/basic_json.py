import json

tasks = ["Task 1", "Task 2"]

with open("tasks.json", "w") as file:
    json.dump(tasks, file)

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

except json.JSONDecodeError:
    print("File is Corrupted, resetting...")
    tasks= []

print(tasks)