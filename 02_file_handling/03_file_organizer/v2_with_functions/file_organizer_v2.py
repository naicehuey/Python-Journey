import os
import shutil

folder_path = r"E:\Python Road Map\1.Trials Understanding Syntax\test_folder"

categories = {
    "images" : [".jpg", ".png"],
    "Videos" : [".mp4"],
    "Documents" : [".pdf"],
    "Music" : [".mp3"]
}

def scanner():
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        ext = os.path.splitext(file)[1]
        if os.path.isdir(file_path) :
            print(f"{file} is a Folder")
            continue
        else:
            print(f"{file} is a File")

def inside_scanner():
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isdir(file_path):
            print(file)
            inside_files = os.listdir(file_path)
            for inside_file in inside_files:
                    print("     ", inside_file)

def count_files():
    image_count = 0
    video_count = 0
    document_count = 0
    music_count = 0
    others = 0
    folder_count = 0

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        ext = os.path.splitext(file)[1]
        
        if ext in [".jpg", ".png"]:
            image_count += 1
        elif ext == ".mp4":
            video_count += 1
        elif ext == ".pdf":
            document_count += 1
        elif ext == ".mp3":
            music_count += 1
        elif ext == "":
            folder_count += 1
        else:
            others += 1
            
    print(f"Number of Folders : {folder_count}")
    print(f"Number of Files: {image_count + music_count + document_count + video_count + others}")

def move_files():
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isdir(file_path):
            continue
        ext = os.path.splitext(file)[1]
        move = False
        for category, extensions in categories.items():
            if ext in extensions:
                dest_folder = os.path.join(folder_path, category)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(file_path, os.path.join(dest_folder, file))
                print(f"Moved {file} to {category}")
                move = True
                break
        if not move:
            other_folder = os.path.join(folder_path, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, "Others"))
            print(f"Moved {file} to {other_folder}")

scanner()
move_files()
inside_scanner()
count_files()