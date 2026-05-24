# Count Files By Type V2 — OS Practice

A refined version of the file counter with
cleaner output and bug fixes.

## What It Does
- Scans a folder and skips subfolders
- Counts files by type — Images, Videos, Documents, Music, Others
- Displays a clean formatted summary of results

## What I Learned
- Output formatting makes results easier to read
- Small refinements to existing code matter
- Always verify counter logic — `+= 1` not `+= 0`
- Thinking about how results look to the user
  is just as important as the logic itself

## What Changed From V1
- Fixed `video_count += 0` bug — now correctly `+= 1`
- Added `===== SUMMARY =====` header for cleaner presentation
- Shows that revisiting old code and improving it
  is a normal and important part of development

## What This Led To
The clean summary output style was carried forward
into the File Organizer project.