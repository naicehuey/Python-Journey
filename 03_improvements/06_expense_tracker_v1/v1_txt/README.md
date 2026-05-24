# Expense Tracker V1 — TXT Storage

A simple command-line expense tracker built
with Python using txt file storage.

## What It Does
- Add expenses with product name and price
- View all saved expenses in a numbered list
- Remove a specific expense by number
- Clear all expenses at once
- Calculate and display total amount spent
- All data saved permanently to a txt file

## What I Learned
- Using `|` as a separator to store multiple
  fields in a single txt line
- Unpacking stored data with `.split("|")`
- Using `_` to ignore unwanted unpacked values
- Using `pass` to open and clear a file cleanly
- Calculating a running total by reading from file
- Handling `FileNotFoundError` for missing files
- Reading file into memory, modifying with `.pop()`
  then writing back — clean data handling pattern

## How To Run
```bash
python expense_tracker_v1.py
```
