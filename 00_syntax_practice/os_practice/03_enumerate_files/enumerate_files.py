import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

for i, file in enumerate(os.listdir(folder_path), start=1):
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    print(f"{i}. {file}")