import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

for i, file in enumerate(os.listdir(folder_path), start=1):
    file_path = os.path.join(folder_path, file)

    ext = os.path.splitext(file_path)[1]
    if ext in [".png", ".jpg"]:
        print(f"Here is your search:\n{file}")