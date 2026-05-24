# Guessing Game — Beginner

A fun command-line guessing game built with Python.

## What It Does
- Lets the user choose between guessing a fruit or a number
- Displays available options to guess from
- Randomly picks a choice using the computer
- Tells the user if they won or lost

## What I Learned
- Using the `random` module and `random.choice()`
- Building a multi-mode program in one script
- Applying `.lower()` consistently for better
  user experience
- Combining lists, user input and randomness together
- That randomness makes programs feel alive and fun

## Known Bugs
- Number guessing always returns a loss even on
  correct guess — input returns a string but list
  contains integers (type mismatch)
- This was a valuable lesson about data types

## How To Run
```bash
python guessing_game.py
```