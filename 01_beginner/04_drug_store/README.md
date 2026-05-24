# Drug Store — Beginner

A simple command-line drug store inventory
system built with Python.

## What It Does
- Check if a medicine is available in the store
- Add a new medicine to the inventory
- Remove a medicine that is out of stock
- Case-insensitive search so capitalization doesn't matter

## What I Learned
- Storing multiple items using Python lists
- List methods — `.append()`, `.remove()`, `.lower()`
- Using `.lower()` to handle case sensitivity
- Building a menu-driven program with `if/elif`
- Nested `if/else` inside a menu option
- Thinking about user experience — making sure
  capitalization doesn't break the search

## Known Limitations
- All inputs are collected before the option is chosen
- Data resets every time the program restarts
  (no saving yet)

## How To Run
```bash
python drug_store.py
```

## Example
```
1. Enter a medicine name
2. Enter a new medicine name
3. Drugs we are out of stock
Enter your option: 1
Enter a medicine name: panado
Medicine is available
```