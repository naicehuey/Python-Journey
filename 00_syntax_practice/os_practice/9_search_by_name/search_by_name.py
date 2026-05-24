import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

keyword = input("Search: ").strip().lower()

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    name = os.path.splitext(file)[0]

    if keyword == name:
        print("Found: ", file)

if keyword not in name:
    print("We couldn't find it")