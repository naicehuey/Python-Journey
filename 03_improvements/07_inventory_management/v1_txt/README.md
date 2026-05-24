# Inventory Management V1 — TXT Storage

A simple command-line inventory management app
built with Python using txt file storage.

## What It Does
- Add new products with name and quantity
- View full inventory in a numbered list
- Search for a product by name
- Update quantity of an existing product
- Remove a product from inventory
- All data saved permanently to a txt file

## What I Learned
- Using `:` as a separator to store name
  and quantity together in one line
- Reading, modifying and writing back to a file
- Adding to existing quantity —
  `int(inv_quantity) + quantity`
- Using `_` to ignore unwanted unpacked values
- Handling `FileNotFoundError` for missing files
- That txt storage works but has limits —
  updating specific fields is tricky vs JSON

## Known Bug
- `update_quantity()` writes back the original
  list without saving the updated line —
  quantity changes are never actually saved

## How To Run
```bash
python inventory_management_v1.py
```