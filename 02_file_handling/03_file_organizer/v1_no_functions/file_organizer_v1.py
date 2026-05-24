import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

image_count = 0
video_count = 0
document_count = 0
music_count = 0
other_count = 0

for i, file in enumerate(os.listdir(folder_path), start=1):
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    name = os.path.splitext(file)[0]
    ext = os.path.splitext(file)[1]

    if ext in [".jpg", ".png"]:
        image_count += 1
    
    elif ext == ".mp4":
        video_count += 1

    elif ext == ".pdf":
        document_count += 1

    elif ext == ".mp3":
        music_count += 1

    else:
        other_count += 1

    print(i, ". Name: ", name)
    print("         Extension: ", ext)
    print("         Path: ", file_path)

print("Final Count Summary:")
print("Images: ", image_count)
print("Video: ", video_count)
print("Documents: ",document_count)
print("Music: ", music_count)
print("Others: ", other_count)