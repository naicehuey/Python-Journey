# Drug Store V2 — With Functions

A rebuilt command-line drug store app using
functions and a dictionary lookup table.

## What It Does
- Add new drugs to the store inventory
- Sell a drug and update its units
- Check current stock lineup
- Remove unsupported drugs from inventory

## What I Learned
- Using tuples to store related data — `("Panado", 100)`
- Unpacking tuples in a loop — `for drug, units in drugslist`
- Using a dictionary as a function lookup table —
  mapping numbers directly to functions
- Using `dict.get(key, default)` to handle invalid options
  without a long `if/elif` chain
- Storing functions as dictionary values and calling them
  with `()` at the end — a very professional Python pattern
- Using `quit()` to stop the program at a specific point

## How To Run
```bash
python drug_store_v2.py
```