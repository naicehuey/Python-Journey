# Folder vs File Detection — OS Practice

Testing how to tell folders apart from files
using `os.path.splitext()`.

## What It Does
- Scans a folder and checks each item
- Identifies and labels each item as a file or folder
- Extracts and displays the filename without extension

## What I Learned
- Folders return an empty string `""` from `splitext()`
  making it a useful way to detect them
- `splitext()[0]` extracts the filename without extension
- `splitext()[1]` extracts just the extension
- Exploring an alternative approach to `os.path.isdir()`
- Understanding why the same problem can have
  multiple solutions in Python

## Interesting Discovery
You don't always need `os.path.isdir()` to detect folders —
`splitext()` returning `""` tells you the same thing.
Knowing both approaches makes you a more flexible developer.

## What This Led To
This understanding made the File Organizer code
more confident and deliberate when handling
folders and files differently.