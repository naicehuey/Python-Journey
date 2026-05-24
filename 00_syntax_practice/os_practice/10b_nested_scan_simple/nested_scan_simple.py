import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        print(file, "is a folder")

        inside_files = os.listdir(file_path)
        for inside_file in inside_files:
            print("     ", inside_file)
