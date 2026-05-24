# Count Files By Type — OS Practice

Testing how to count files by their extension type
before implementing it in the File Organizer project.

## What It Does
- Scans a folder and skips subfolders
- Counts files by type — Images, Videos, Documents, Music, Others
- Displays a final count for each category

## What I Learned
- Using multiple counters simultaneously to track different categories
- Using `+=` to increment a counter
- Combining `os.path.isdir()`, `continue` and `splitext()` together
- Checking extensions against a list using `in`
- Building up logic piece by piece before putting it in a real project

## Bug Found
`video_count += 0` should be `video_count += 1`
Videos were never being counted because of this typo —
caught and fixed in the next version and in the
real File Organizer project.

## What This Led To
This counting logic was directly used in
`02_file_handling/file_organizer/v1_no_functions/`