# File Organizer V4 — Cleanest Version

The most professional rebuild of the file organizer.
Each responsibility split into its own function.

## What It Does
- Validates folder exists before scanning
- Scans folder and skips subfolders
- Moves files into categorized folders
- Counts files moved per category
- Displays full summary after organizing

## What I Learned
- Splitting responsibilities into focused functions —
  `scan_folders()`, `move_file()`, `count_file()`
- Defensive programming — checking if folder exists
  before doing anything
- Orchestrator pattern — `scan_folders()` delegates
  work to other functions
- That small focused functions are easier to
  read, test and fix than large ones

## Growth From Previous Versions
- V1 — no functions, just a script
- V2 — functions but bugs in Others folder
- V3 — cleaner but no folder validation
- V4 — folder validation, split functions,
  most professional version yet

## Warning
This script moves files permanently.
Test on a folder with copies first.

## How To Run
```python
folder_path = r"C:\Your\Folder\Path"
```
```bash
python file_organizer_v4.py
```