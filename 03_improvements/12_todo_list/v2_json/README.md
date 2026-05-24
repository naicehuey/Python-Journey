# To-Do List V2 — JSON Storage

A fully featured command-line to-do list app
built with Python and JSON storage.

## What It Does
- Add tasks with automatic timestamp
- View tasks filtered by status —
  Done, Pending, Urgent or All
- Search tasks by keyword
- Mark tasks as Done or Urgent
- Edit existing task titles
- Delete specific tasks
- Show full stats — total, done, pending, urgent
- Visual status icons ✔ and ✘ for each task
- All tasks saved permanently using JSON

## What I Learned
- Building a 4 field task model —
  title, done status, timestamp and urgency
- Building a filter system using function parameters
- Using three task states — DONE, URGENT, PENDING
- Using visual icons ✔ and ✘ for status display
- Using `task.get("urgent", False)` for safe
  dictionary access with a default value
- Catching multiple exceptions together —
  `except (IndexError, ValueError)`
- Building complete task stats from data
- That the same simple idea rebuilt with more
  features becomes a real application

## Growth From V1
V1 was a simple add, view, complete, clear app.
V2 adds JSON storage, filtering, urgency marking,
search, stats and visual icons — a real application.

## How To Run
```bash
python todo_list_v2.py
```