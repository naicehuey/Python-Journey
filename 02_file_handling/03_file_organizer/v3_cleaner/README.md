# File Organizer V3 — Cleaner Version

A cleaner rebuild of the file organizer using
two dictionaries working together.

## What It Does
- Scans a folder and skips subfolders
- Moves files into categorized folders:
  - Images (.jpg, .png)
  - Documents (.pdf, .txt)
  - Videos (.mp4, .mkv)
  - Audio (.mp3)
  - Others (anything else)
- Creates category folders automatically
- Tracks and displays how many files moved

## What I Learned
- Using two dictionaries together —
  one for categories, one for counting
- Making extension matching case insensitive
  using `.lower()` on extensions
- Tracking move counts with `count[category] += 1`
- That the same problem rebuilt multiple times
  gets cleaner and more thoughtful each time

## Warning
This script moves files permanently.
Test on a folder with copies first.

## How To Run
```python
folder_path = r"C:\Your\Folder\Path"
```
```bash
python file_organizer_v3.py
```
