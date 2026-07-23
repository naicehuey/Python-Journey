# Todo App With Utils — Import Practice

A two file todo app where utility functions
live in a separate file and are imported
into the main program.

## Files
- `utilis.py` — reusable helper functions
- `main.py` — main program that imports from utilis

## What It Does
- Add tasks with automatic timestamp
- View all tasks with status and date
- Search tasks by name
- Mark tasks as done
- Delete tasks
- Generate a report — total, done and pending
- All tasks saved permanently to a txt file

## What I Learned
- Splitting code into two files —
  utility functions separate from main logic
- Importing a variable from another file —
  `from utilis import FILE`
- Reusing `display_list()` and `choose()`
  across different programs
- That `utilis.py` is a common pattern in
  real projects — utility files hold shared
  helper functions used everywhere
- Storing tasks as formatted strings in txt —
  `task|status|date` pattern
- Updating a specific line by index in a list
  then saving back to file

## Important Note
Both files must be in the same folder to work.

## How To Run
```bash
python main.py
```