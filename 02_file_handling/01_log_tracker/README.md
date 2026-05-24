# Log Tracker — File Handling

A simple command-line log tracker built with Python.
The first project that saves data permanently.

## What It Does
- Records the exact date and time every time
  the program runs
- Saves logs permanently to a `log.txt` file
- Displays all previous logs on every run

## What I Learned
- File handling in Python using `open()`
- Difference between file modes:
  - `"a"` — append, keeps existing content
  - `"r"` — read, displays file content
- Using `with` statement for safe file handling
  (automatically closes the file)
- Using `readlines()` to read content as a list
- Cleaner datetime import —
  `from datetime import datetime` instead of
  `import datetime` then `datetime.datetime.now()`
- Making data persist between program runs
  for the first time

## Why This Project Matters
Every project before this forgot everything when closed.
This is the first project that remembers — a fundamental
shift in how programs work.

## How To Run
```bash
python log_tracker.py
```