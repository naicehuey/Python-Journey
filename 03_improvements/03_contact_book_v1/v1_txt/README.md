# Contact Book V1 — TXT Storage

A fully working command-line contact book
built with Python using txt file storage.

## What It Does
- Add a new contact with name and number
- View all saved contacts in a numbered list
- Delete a specific contact by number
- Search for a contact by name
- All contacts saved permanently to a txt file
- Menu driven with full input validation

## What I Learned
- Creating a custom data format using `|` as separator
- Splitting stored data back into parts using `.split("|")`
- Using `list.pop(index)` to remove a specific item
- Reading a file into memory, modifying it, then
  saving it back — a professional data handling pattern
- Handling `FileNotFoundError` for missing files
- Case insensitive search using `.lower()` on both sides
- Checking `len(contents) == 0` for empty files

## How To Run
```bash
python contact_book_v1.py
```