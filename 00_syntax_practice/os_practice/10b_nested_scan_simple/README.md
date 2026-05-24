# Nested Scan Simple — OS Practice

A simpler version of nested folder scanning
without empty folder handling.

## What It Does
- Scans a folder and identifies subfolders
- Lists the contents of each subfolder found
- Indents subfolder contents for visual clarity

## What I Learned
- Basic nested folder scanning using two loops
- Using `os.path.isdir()` to find subfolders
- Looping through subfolder contents with a second loop
- Using indentation in output to show hierarchy
- That the same problem can be solved with
  different levels of complexity

## Difference From 11_nested_folder_scan
- No empty folder check
- Only shows folders and their contents
- Does not handle individual files separately
- Simpler and more focused version

## Note
This was likely built before `11_nested_folder_scan`
as a first attempt at nested scanning — then improved
by adding empty checks and file handling in the next version.