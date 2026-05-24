# Inventory Management V2 — JSON Storage

A fully featured command-line inventory management
system built with Python and JSON storage.

## What It Does
- Add products with name, price, stock and category
- View full inventory in detailed format
- Search products with suggestion to add if not found
- Edit specific fields of a product
- Delete products from inventory
- Restock products running low
- Sell products and deduct from stock
- Low stock alert for products with 5 or fewer units
- All data saved permanently using JSON

## What I Learned
- Building the largest function based app so far
- Selective field editing using numbered options
- Reusing functions — `low_stock_alert()` called
  from both `sell_stock()` and the menu
- Calculating total sale cost — price times quantity
- Checking stock levels and alerting when low
- Building consistent UX patterns across projects

## How To Run
```bash
python inventory_management_v2.py
```