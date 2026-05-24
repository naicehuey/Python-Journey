# Notes Writer V1 — File Handling

A simple command-line notes writer built with Python.

## What It Does
- Creates a notes file and writes a default message
- Takes user input and saves it permanently to the file
- Reads and displays the full content of the file

## What I Learned
- The difference between all three file modes:
  - `"w"` — creates or overwrites a file
  - `"a"` — appends without deleting existing content
  - `"r"` — reads the file content
- Using `file.read()` vs `file.readlines()`
- Writing multiple lines using `\n` inside a file
- Combining hardcoded text and user input in one file
- That `"w"` mode always starts fresh while
  `"a"` mode builds on what is already there

## Known Limitations
- File is overwritten every time the program runs
  due to `"w"` mode at the start

## How To Run
```bash
python notes_writer_v1.py
```