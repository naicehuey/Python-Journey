# Library Management App

A command-line library management app built
with Python and txt storage.

## What It Does
- Add books with name and author
- View all books with status and borrow time
- Search books by name or author
- Borrow a book — updates status to Borrowed
  with timestamp
- Return a book — updates status back to Active
- Remove a specific book from the library
- Clear entire library
- All data saved permanently to a txt file

## What I Learned
- Storing 4 fields in one txt line —
  book, author, status and timestamp
- Using status flags — "Active" and "Borrowed"
  to track book availability
- Updating a specific field in a txt line —
  changing status and timestamp on borrow/return
- Checking status before borrowing —
  preventing double borrowing
- Checking status before returning —
  preventing returning a book that wasn't borrowed
- Using `result_count` as a separate counter
  for search results independent of list index
- Searching by two different fields —
  book name or author name
- Recording timestamps on borrow and return
  for a complete borrowing history
- Defensive programming — validating index
  range before accessing list items

## How To Run
```bash
python library_app.py
```

## Example
```
1. Add Book
2. Search Book
3. View Books
4. Borrow Book
5. Return Book
6. Remove Book
7. Clear Library
8. Exit
Choose Option: 1
Book Name: Rich Dad Poor Dad
Author Name: Robert Kiyosaki
Book Successfully Added!
Choose Option: 4
1. Book: Rich Dad Poor Dad — Active
Which book do you wanna borrow: 1
Book has been borrowed
Rich Dad Poor Dad @ Time: 2025-05-01 10:23:45
```