# Workout Tracker — Reusable Functions

A simple command-line workout tracker built
with Python and text file storage.
Built to practice reusable functions,
file handling, and menu-driven applications.

## What It Does
- Add new workouts with a default Pending status
- View all saved workouts in a formatted list
- Mark workouts as Done
- Delete completed or unwanted workouts
- Save workout progress permanently using a text file

## What I Learned
- Building reusable helper functions like
  `load_data()`, `save_update()`,
  `display_list()`, and `choose_item()`
  to keep the program organized
- Reusing a single selection function
  across multiple features to eliminate
  duplicate code
- Working with lists and text files
  to update persistent data
- Separating formatting logic from
  program logic for cleaner code
- Creating a dictionary-based menu
  that maps user choices to functions
- Validating user input before
  processing program actions

## Note
This project was built to reinforce
the reusable function pattern while
creating a simple workout tracker.
The focus was writing cleaner,
more maintainable code by organizing
repeated logic into helper functions.

## How To Run
```bash
python "workout tracker last stand.py"
```