import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

keyword = input("Enter extension you wanna find? ").strip().lower()
ext = "." + keyword
ext_count = 0

found = False

for file in os.listdir(folder_path):
    if ext in file:
        ext_count += 1
        print(file)
        found = True

print("Found ", ext_count, " Of This Extensions")

if not found:
    print("Extension not found")