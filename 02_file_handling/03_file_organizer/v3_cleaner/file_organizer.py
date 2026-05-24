import os
import shutil

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

categories = {
    "Images" : [".jpg", ".png"],
    "Documents" : [".pdf", ".txt"],
    "Videos" : [".mp4", ".mkv"],
    "Audio" : [".mp3"]
}

count = {
    "Images" : 0,
    "Documents" : 0,
    "Videos" : 0,
    "Audio" : 0,
    "Other" : 0
}

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    ext = os.path.splitext(file)[1].lower()

    moved = False
    
    for category, extensions in categories.items():
        if ext in extensions:
            dest_folder = os.path.join(folder_path, category)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            shutil.move(file_path, os.path.join(dest_folder, file))
            print(f"Moved {file} - {category}")
            count[category] += 1
            moved = True
            break

    if not moved:
        other_folder = os.path.join(folder_path, "Others")

        if not os.path.exists(other_folder):
            os.makedirs(other_folder)

        shutil.move(file_path, os.path.join(other_folder, file))
        count["Other"] += 1

for key, value in count.items():
    print(f"{key}: {value} files moved")