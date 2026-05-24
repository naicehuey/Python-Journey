import os

folder_path = r"E:\Python Road Map\2. Understanding Projects\test_folder"

count = 0

items = os.listdir(folder_path)
if not items :
    print("Folder is empty")

else:
    print("Folder contains files")

    for item in items:
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):
            print(f"\nInside folder: {item}")
            sub_items = os.listdir(item_path)
            if not sub_items:
                print("     (Empty)")
            else:
                for sub in sub_items:
                    print("     ", sub)

        else:
            print("File: ", item)