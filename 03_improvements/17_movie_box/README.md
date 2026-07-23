# Movie Box — Improvements

A command-line movie management app built
with Python and JSON storage.

## What It Does
- Add movies with name and category
- View all movies with ratings
- Search movies by name
- Delete a movie
- Rate a movie out of 10
- Generate a report — total, low and high rated
- All data saved permanently using JSON

## What I Learned
- Returning two values from a function —
  `return movies, index` and unpacking with
  `movies, index = choose_movie()`
- Checking both return values for None —
  `if movies is None: return`
- Displaying a single item as a list —
  `display_list([movies[index]], format_list)`
- Validating rate range — between 1 and 10
- Building a reusable `choose_movie()` function
  used by both delete and rate

## How To Run
```bash
python movie_box.py
```