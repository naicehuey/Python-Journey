# Contact Book V2 — TXT Upgraded

An upgraded command-line contact book built
with Python and txt storage.
Adds contact editing to the original version.

## What It Does
- Add a new contact with name and number
- View all saved contacts in a numbered list
- Delete a specific contact by number
- Search for a contact by name
- Edit an existing contact's name and number
- All contacts saved permanently to a txt file

## What I Learned
- Editing a specific line in a txt file by index —
  `contents[index] = f"{name}|{number}\n"`
- Reading file into memory, modifying a specific
  item by index, then writing everything back
- That editing txt files means replacing the whole
  file — you can't just change one line directly
- Building on existing projects by adding one
  feature at a time — edit was missing from v1
- Confirming actions with success messages —
  "Contact deleted successfully"

## Growth From V1
V1 had add, view, delete and search.
V2 adds edit — giving full control over contacts.
Same txt storage, same patterns, one new feature
that makes the app feel complete.

## Known Limitation
- Edit doesn't validate empty name or number —
  you could accidentally save a blank contact

## How To Run
```bash
python contact_book_v2_txt.py
```

## Example
```
1. Add Contacts
2. View Contacts
3. Delete Contact
4. Search
5. Edit Contact
6. Exit
Choose Option: 5
1. Name: Huey
        Mobile No: 0991234567
Which Contact You Wanna Edit: 1
Name: Huey Kid
Number: 0997654321
Edited Successfully
```