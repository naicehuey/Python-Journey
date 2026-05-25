# Expense Tracker V2 — TXT Storage with Edit & Stock Management

A command-line expense tracker built
with Python using txt file storage.
This version adds editing and stock management features.

## What It Does
-Add expenses with product name, price, stock, and total
-View all saved expenses in a numbered list
-Edit existing expenses:
-Change product name and price
-Update only the price
-Update only the stock quantity
-Manage stock:
-Add stock to existing products
-Subtract stock with validation (no negative stock)
-Remove a specific expense by number
-Clear all expenses at once
-Calculate and display total amount spent
-All data saved permanently to a txt file

## What I Learned
-Extending the txt storage format to handle multiple fields (product|price|stock|total)
-Using .split("|") to unpack multiple values cleanly
-Validating user input with try/except for FileNotFoundError and ValueError
-Updating specific list items by index (contents[index] = new_product)
-Writing back updated lists to file after edits — ensuring persistence
-Defensive programming when subtracting stock (preventing negative values)
-Designing a flexible edit menu with multiple options
-Using while True loops to keep the menu running until exit
-Building modular functions for add, edit, remove, clear, and total — clean structure

## How It Works — Menu Flow
Main Menu
↓
Add Expense → saves product, price, stock, total
↓
View Expenses → shows numbered list with details
↓
Edit Expense → choose product → edit fields
↓
Stock Management → add or subtract stock with validation
↓
Remove / Clear / Total → manage data
↓
Exit → program ends

## How To Run
```bash
python expense_tracker_v2.py
```

## Example
==============================
Main Menu
Add Expense
View Expenses
Edit Expense
Clear Expenses
Total Expenses Spent
Exit
Choose Option: 1
==============================
Add Expense
==============================
Product Name: sugar
Product Price: 500
Stock Quantity: 3
==============================
Expense Added: sugar | 500 | 3 | 1500