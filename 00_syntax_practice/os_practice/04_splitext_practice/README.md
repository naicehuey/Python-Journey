# Splitext Practice — OS Practice

Testing how to split filenames and extensions
using `os.path.splitext()`.

## What It Does
- Scans a folder and splits each filename
- Displays the name and extension separately
- Skips folders by checking for empty extension

## What I Learned
- Using `os.path.splitext()` to separate filename from extension
- `splitext()[0]` returns the filename without extension
- `splitext()[1]` returns just the extension (e.g. `.jpg`)
- Folders return an empty string `""` from `splitext()`
  which is a useful way to detect and skip them

## Bug Found
An earlier version used `os.path.splittext()` — a typo!
The correct method is `os.path.splitext()`
This crash taught me to always double check
method names carefully.

## What This Led To
`splitext()` became a core tool used in every
version of the File Organizer project.