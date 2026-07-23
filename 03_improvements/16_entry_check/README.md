# Entry Check — Improvements

A command-line entry tracker built with
Python and txt storage.

## What It Does
- Add entries with task name, task and timestamp
- View all entries in formatted list
- Search entries by task name
- Delete a specific entry
- View the latest entry added
- All entries saved permanently to txt file

## What I Learned
- Using two separate save functions —
  `save_data()` for appending new entries
  `save_update()` for writing back modified list
- Passing a string directly to save function
  instead of a list
- Using `entries[-1]` to get the last item
  in a list — latest entry
- That menu dictionary must map to the correct
  function — wrong mapping causes silent bugs
- Removing unnecessary parameters from functions
  that don't need them

## How To Run
```bash
python entry_check.py
```