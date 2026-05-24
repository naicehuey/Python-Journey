# Rock Paper Scissors — Beginner

A classic command-line Rock Paper Scissors game
built with Python.

## What It Does
- Takes player choice — rock, paper or scissors
- Randomly generates computer choice
- Compares choices and declares winner
- Displays a descriptive result message

## What I Learned
- Returning a dictionary from a function to
  carry multiple related values together
- Accessing returned dictionary values —
  `choices["player"]` and `choices["computer"]`
- Separating logic from output — `check_win()`
  returns a string instead of printing directly
- Covering all game conditions with nested `if/else`
- Chaining two functions together —
  output of one becomes input of another

## Known Issues
- `options` list has `"scissor"` but prompt says
  `"scissors"` — type mismatch means scissors
  never wins
- No replay loop — game plays once and exits

## How To Run
```bash
python rock_paper_scissors.py
```