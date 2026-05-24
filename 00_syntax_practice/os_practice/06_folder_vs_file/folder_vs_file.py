import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.splitext(file)[1] == "":
        print(f"{file} is folder")
    

    else:
        x = os.path.splitext(file)[0]
        print(f"{x} is file")