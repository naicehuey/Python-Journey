# Quiz App — Improvements

A fully featured command-line quiz app built
with Python and JSON storage.

## What It Does
- Choose between Math or Geography quiz
- Questions shuffled randomly every time
- Scores answers and shows percentage
- Pass or Fail result based on 50% threshold
- Replay option after every quiz
- View full quiz history with scores
- View stats — total, average and best score
- All history saved permanently using JSON

## What I Learned
- Building nested dictionaries with lists
- Using `random.shuffle()` to randomize questions
- Calculating percentage scores
- Using `:.0f` to format floats cleanly
- Using list comprehension for the first time —
  `[h["score"] for h in history]`
- Calculating stats from saved data
- Building a replay loop

## How To Run
```bash
python quiz_app.py
```