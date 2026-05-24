# Enumerate Files — OS Practice

Testing how to number files while scanning a folder.

## What It Does
- Scans a folder and lists all files with numbers
- Skips folders and only shows files

## What I Learned
- Using `enumerate()` to add a counter to a loop
- Using `start=1` to start counting from 1 instead of 0
- Combining `enumerate()` with `os.listdir()`
- Skipping folders using `os.path.isdir()` and `continue`
- Using `continue` to skip unwanted items mid-loop
- Clean numbered output using f-strings

## What This Led To
This exact numbered listing pattern was used
in the File Organizer project to display
files in a clean organized way.