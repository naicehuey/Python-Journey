# Import Practice — Book Details and Games

Two connected Python files exploring how to
import functions from one file into another.
Built as a test run of Python's import system.

## What It Does

### book_details.py
- Add books with name, author and release year
- View all books in a formatted list
- Search books by name
- Delete a specific book
- Saves all data to JSON

### games_inheritance.py
- Imports reusable functions from book_details.py
- Add games with name and category
- View all games
- Search games by name
- Rate games on a scale of 1-10
- Generate a report — low, mid and high rated games
- Saves all data to a separate JSON file

## What I Learned
- Importing functions from your own Python files —
  `from book_details import save_data, load_data`
- Writing reusable functions that work across
  multiple files — `display_list()` and `choose_item()`
  work for both books and games
- Passing functions as parameters —
  `display_list(items, formatter)` where formatter
  is itself a function
- Using `if __name__ == "__main__"` — runs only
  when the file is the main file not when imported
- Using a dictionary as a menu —
  `{"1": ("Add Book", add_book)}` storing label
  and function together
- Passing filename as a parameter to `load_data()`
  and `save_data()` making them work with any file
- That Python lets you split code across files
  and connect them — the foundation of
  building larger programs

## Important Note
Both files must be in the same folder to work —
`games_inheritance.py` imports directly from
`book_details.py`

## How To Run
Run book details standalone:
```bash
python book_details.py
```

Run games which imports from book details:
```bash
python games_inheritance.py
```