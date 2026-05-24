# Slot Machine Game — Improvements

A fully working command-line slot machine game
built with Python. The most complex project so far.

## What It Does
- Lets the user deposit a starting balance
- Choose how many lines to bet on (1-3)
- Choose how much to bet per line
- Spins a 3x3 slot machine with 4 symbols
- Calculates winnings based on matching lines
- Tracks balance across multiple spins
- Quits and shows final balance when done

## What I Learned
- Using constants for configuration (`MAX_BET`, `MIN_BET`)
- Building multiple functions that work together
- Using two dictionaries together (`symbol_count`, `symbol_value`)
- Using `for/else` loop — else runs only if loop
  completes without hitting `break`
- Using `isdigit()` for clean input validation
- Copying a list with `[:]` to avoid modifying the original
- Using `random.choice()` with `.remove()` to prevent
  duplicate symbols in the same column
- Unpacking a list in print using `*winning_lines`
- Tracking a running balance across multiple game rounds
- Building a complete game loop with deposit, spin and quit

## How To Run
```bash
python slot_machine.py
```