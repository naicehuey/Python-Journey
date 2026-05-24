# File Organizer V1 — No Functions

A command-line file analysis tool built with Python.
Scans a folder and categorizes all files by type.

## What It Does
- Scans a specified folder on your computer
- Skips subfolders and only processes files
- Categorizes files into Images, Videos, Documents,
  Music and Others
- Displays each file's name, extension and full path
- Shows a final count summary of all file types

## What I Learned
- Using the `os` module to interact with the file system
- Listing folder contents with `os.listdir()`
- Building safe file paths with `os.path.join()`
- Checking if a path is a folder with `os.path.isdir()`
- Splitting filenames and extensions with `os.path.splitext()`
- Using `continue` to skip unwanted items in a loop
- Using raw strings `r"..."` for Windows file paths
- Tracking multiple counters simultaneously
- Combining everything learned in `00_syntax_practice`
  into one real working tool

## How To Run
1. Change `folder_path` to any folder on your computer
```python
folder_path = r"C:\Your\Folder\Path"
```
2. Run the script
```bash
python file_organizer_v1.py
```