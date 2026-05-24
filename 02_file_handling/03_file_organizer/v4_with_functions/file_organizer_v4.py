import os
import shutil

folder_path = r"E:\Python Road Map\1.Trials Understanding Syntax\Test_2_"

categories = {
    "Image" : [".jpg", ".png"],
    "Document" : [".pdf", ".txt"],
    "Music" : [".mp3", ".flac"],
    "Videos" : [".mp4", ".mkv"]
}

counts = {
    "Image": 0,
    "Document": 0,
    "Music": 0,
    "Videos": 0,
    "Others": 0
}

def scan_folders():
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file)[1]

        moved = False

        for category, extensions in categories.items():
            if ext in extensions:
                move_file(file_path, file, category)
                count_file(category)
                moved = True
                break
        
        if not moved:
            move_file(file_path, file, "Others")
            count_file("Others")

def count_file(category):
    counts[category] += 1

def move_file(file_path, file, category):
    dest_folder = os.path.join(folder_path, category)

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    shutil.move(file_path, os.path.join(dest_folder, file))
    print(f"{file} has been moved to {dest_folder}")

def show_total():
    print("\nFile Total:")
    for category, total in counts.items():
        print(f"{category}: {total}")

scan_folders()
show_total()