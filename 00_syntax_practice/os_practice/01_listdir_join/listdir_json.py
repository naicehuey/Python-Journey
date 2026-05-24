import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

files = os.listdir(folder_path)

for file in files:
    print(file)

file_path = os.path.join(folder_path, file)

print(file_path)

ext = os.path.splitext(file_path)[1]
print(ext)