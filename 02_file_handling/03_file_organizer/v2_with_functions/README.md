# File Organizer V2 — With Functions

A complete rebuild of the file organizer using functions.
Now actually moves files into categorized folders automatically.

## What It Does
- Scans a folder and identifies files vs folders
- Looks inside subfolders and lists their contents
- Counts all files by type and displays a summary
- Automatically moves files into categorized folders:
  - Images (.jpg, .png)
  - Videos (.mp4)
  - Documents (.pdf)
  - Music (.mp3)
  - Others (anything else)
- Creates category folders automatically if they
  don't exist

## What I Learned
- Organizing code into clean reusable functions
- Using dictionaries to map categories to extensions
- Looping through dictionaries with `.items()`
- Using `shutil.move()` to physically move files
- Creating folders automatically with `os.makedirs()`
- Checking if a folder exists with `os.path.exists()`
- Using boolean flags to track action completion
- Using `break` to stop a loop once a match is found
- Building tools that don't just read but actually
  act on the file system

## Growth From V1
V1 only scanned and counted — read only.
V2 uses functions, dictionaries and actually moves
files into organized folders automatically.
Same idea, completely rebuilt with everything
learned since V1.

## Warning
This script moves files permanently.
Test on a folder with copies first.

## How To Run
1. Change `folder_path` to any folder on your computer
```python
folder_path = r"C:\Your\Folder\Path"
```
2. Run the script
```bash
python file_organizer_v2.py
```