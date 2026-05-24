# Extension Finder — OS Practice

Searching a folder for files matching a specific extension.

## What It Does
- Takes an extension as input from the user
- Searches a folder for all matching files
- Displays matching files and the total count
- Notifies the user if no matches are found

## What I Learned
- Using `.strip()` to remove accidental spaces from input
- Using `.lower()` to handle case sensitivity
- Building strings dynamically using `"." + keyword`
- Using a boolean flag (`found = True/False`) to track results
- Using `if not found` as a clean way to show error messages
- Counting matches with a counter variable

## What I Would Improve
- Use `file.endswith(ext)` instead of `ext in file`
  for more accurate extension matching

## What This Led To
These patterns were used directly in the
File Organizer project.