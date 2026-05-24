# Pretty Chatbot — Improvements

A command-line chatbot with conversation history
built with Python. Named Pretty.

## What It Does
- Chats with the user through a scripted conversation
- Saves full chat history to a txt file
- View all previous conversations anytime
- Clear chat history and start fresh
- Menu driven with input validation and error handling

## What I Learned
- Building multiple functions that each do one job
- Using `"a"` mode to append chat history to a file
- Using `"w"` mode with `pass` to clear a file cleanly
- Storing menu options in a list and looping to display them
- Using `try/except ValueError` for invalid menu input
- Validating input against a list using `if x not in [...]`
- Formatting and saving a full conversation to a file
- Building a complete program with a persistent loop

## Known Limitations
- Conversation is scripted — Pretty always says the same things
- `if contents == ""` check does not work correctly
  since `readlines()` returns a list not a string
  — should be `if not contents`

## How To Run
```bash
python pretty_chatbot.py
```