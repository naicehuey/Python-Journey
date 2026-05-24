# Nested Folder Scan — OS Practice

Testing how to scan folders and their subfolders
while handling empty folders at both levels.

## What It Does
- Checks if the main folder is empty before scanning
- Identifies files and folders separately
- Scans inside subfolders and lists their contents
- Handles empty subfolders gracefully

## What I Learned
- Using `if not list` to check if a folder is empty
- Building nested loops — a loop inside a loop
- Scanning two levels deep — main folder and subfolders
- Handling edge cases at multiple levels consistently
- Using `if not sub_items` to catch empty subfolders
- Indenting output `"     "` to show folder hierarchy visually

## Why This One Stands Out
This is the most complex practice file so far —
two levels of scanning, empty checks at both levels,
and visual hierarchy in the output. A big jump
in logical thinking.

## What This Led To
This became the `inside_scanner()` function in
`02_file_handling/file_organizer/v2_with_functions/`
— you can see the exact same logic there!