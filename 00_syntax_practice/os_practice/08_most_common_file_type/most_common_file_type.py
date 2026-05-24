import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

image_count = 0
video_count = 0
document_count = 0
others_count = 0
music_count = 0

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

    else:
            others_count += 1


common = max(image_count, video_count, document_count, others_count, music_count)
if common == image_count:
    print("Images are the most found")

elif common == video_count:
    print("Videos are the most found")

elif common == music_count:
    print("Music is the most found")

elif common == document_count:
    print("Documents are the most found")

else:
    print("Others are the most found")

print("Total: ", common)