# Todo List Manager — Reusable Functions

A simple command-line todo list manager built
with Python and text file storage.
Built to practice reusable functions,
code organization, and CRUD operations.

## What It Does
- Add new tasks with a default Pending status
- View all saved tasks in a formatted list
- Search tasks by name
- Mark tasks as Complete
- Delete tasks from the list
- Display a report showing total, pending,
  and completed tasks
- Save all tasks permanently using a text file

## What I Learned
- Creating reusable helper functions like
  `save_data()`, `load_data()`,
  `save_update()`, and `display_list()`
  to avoid repeating code
- Building a reusable `choose_task()`
  function that handles task selection
  for multiple features
- Separating formatting logic into its own
  function to keep the code clean
- Working with text files to store
  and update persistent data
- Using dictionaries to build a
  menu-driven application
- Validating user input with
  `try` and `except` before processing
- Improving code readability by breaking
  large problems into smaller functions

## Note
This project was built to reinforce
reusable programming patterns while creating
a complete command-line CRUD application.
The focus was writing cleaner, more
maintainable code through helper functions.

## How To Run
```bash
python "todo list.py"
```