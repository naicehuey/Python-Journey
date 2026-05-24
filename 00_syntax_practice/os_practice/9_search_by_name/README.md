# Search By Name — OS Practice

Testing how to search for a specific file
by name inside a folder.

## What It Does
- Takes a filename as input from the user
- Searches a folder for a matching file
- Displays the file if found
- Notifies the user if nothing was found

## What I Learned
- Searching files by name using `splitext()[0]`
- Combining `.strip()` and `.lower()` for clean input
- Extracting just the filename without extension
  to make searching easier for the user
- Building a simple but functional search tool

## Bug Found
The "not found" message is outside the loop so it
only checks against the last file scanned —
not all files. The fix is to use a `found` flag:
```python
found = False
for file in os.listdir(folder_path):
    if keyword == name:
        found = True
        print("Found: ", file)
if not found:
    print("We couldn't find it")
```

## Interesting Note
A `found` flag was used correctly in an earlier
practice file but not here — proof that learning
is not always linear. Skills need practice
to become habits.