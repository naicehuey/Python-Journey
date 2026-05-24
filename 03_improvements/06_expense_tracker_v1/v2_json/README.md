# Expense Tracker V2 — JSON Storage

A fully featured command-line expense tracking app
built with Python and JSON storage.

## What It Does
- Add expenses with title, amount, category and date
- View all expenses in a detailed formatted list
- Search expenses by title with suggestion to add
- Edit existing expenses
- Delete expenses
- Filter expenses by category
- Sort expenses by amount or date
- Show monthly spending summary
- Show total amount spent
- All data saved permanently using JSON

## What I Learned
- Using `datetime.strftime()` to format dates
- Using `.update()` to modify dictionary fields
- Using `sum()` with a generator expression
- Building dynamic category counts using a dictionary
- Sorting with `lambda` functions — 4 sort modes
- Grouping data by month for a summary view
- Suggesting to add when search returns nothing
- Building the most complete app so far

## How To Run
```bash
python expense_tracker_v2.py
```