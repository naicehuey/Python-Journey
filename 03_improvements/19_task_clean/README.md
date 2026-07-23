# Study Task Manager — Reusable Functions

A simple command-line study task manager built
with Python and text file storage.
Built to practice reusable functions, file handling,
and menu-driven programming.

## What It Does
- Add new study tasks with a default Pending status
- View all saved tasks in a formatted list
- Search tasks by keyword
- Mark tasks as completed
- Delete tasks from the list
- Generate a report showing Pending and Completed tasks
- Save all tasks permanently using a text file

## What I Learned
- Reusing helper functions like
  `save_data()`, `load_data()`,
  `save_update()` and `display_list()`
  to reduce duplicate code
- Separating formatting logic into its own
  function for cleaner and reusable output
- Using dictionaries to build a simple
  menu system that maps options to functions
- Reading from and writing to text files
  while preserving existing data
- Validating user input with `try` and `except`
  and returning immediately after invalid input
- Updating and deleting specific records
  by modifying lists before saving them back

## Note
This project was built to strengthen my
understanding of reusable functions,
file handling, and writing cleaner code by
breaking large problems into smaller functions.

## How To Run
```bash
python "Task Clean.py"
```