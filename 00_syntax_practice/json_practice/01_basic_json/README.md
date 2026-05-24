# Basic JSON Read Write — JSON Practice

First test of reading and writing JSON files in Python.
This is where data storage moved from txt to JSON.

## What It Does
- Writes a list of tasks to a JSON file
- Reads the JSON file back into Python
- Handles corrupted JSON files gracefully
- Resets data to empty list if file is corrupted

## What I Learned
- Importing and using the `json` module
- Writing Python data to JSON using `json.dump()`
- Reading JSON back into Python using `json.load()`
- The difference between `json.dump()` and `json.load()`
- Handling corrupted files with `json.JSONDecodeError`
- That JSON is cleaner and more structured than txt
  for storing complex data like lists and dictionaries
- Resetting data gracefully instead of crashing

## Why This One Matters
Every project before this either had no data saving
or used plain txt files. JSON opened the door to
storing structured data properly — a major step up.

## What This Led To
This was the foundation for all projects that
use JSON for data storage going forward.