# Cars With Main — Import Practice

A two file car management app where shared
utility functions live in main.py and are
imported into main_game.py.

## Files
- `main.py` — shared utility functions
- `main_game.py` — car management program
  that imports from main.py

## What It Does
- Add cars with name, model, performance
  rating and release year
- View all cars in formatted list
- Delete a specific car
- Generate performance report —
  high, mid and low performance cars
- All data saved permanently using JSON

## What I Learned
- Writing a utility file from scratch —
  `main.py` contains only reusable functions
- Importing specific functions from own file —
  `from main import save_data, load_data`
- Validating multiple fields together —
  rate range AND release year length
- Using `elif` in report ranges to prevent
  overlap between categories
- Using specific `except ValueError` instead
  of bare `except` for cleaner error handling
- That naming utility files clearly matters —
  `main.py` for shared tools, `main_game.py`
  for the actual program

## Important Note
Both files must be in the same folder to work.

## How To Run
```bash
python main_game.py
```