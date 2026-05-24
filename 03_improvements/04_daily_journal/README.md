# Daily Journal — Improvements

A simple command-line daily journal app
built with Python.

## What It Does
- Start a brand new journal entry
- Add new thoughts to existing journal
- View all journal entries in a numbered list
- Menu driven with full input validation

## What I Learned
- Building clean focused functions that do one job
- Using all three file modes together:
  - `"w"` — start a fresh journal
  - `"a"` — add to existing journal
  - `"r"` — read and display journal
- Using `enumerate()` for clean numbered output
- Using `.strip()` to clean up lines when displaying
- Storing menu options in a list and looping to print
- Using `try/except ValueError` for menu validation
- That sometimes simple and clean is better
  than complex — not every app needs many features

## How To Run
```bash
python daily_journal.py
```