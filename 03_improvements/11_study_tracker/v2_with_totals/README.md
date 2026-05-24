# Study Tracker V2 — With Totals

An upgraded study tracker with total hours
calculation and better session management.

## What It Does
- Add study sessions with subject and hours
- Automatically records date and time
- View all sessions with subject, date and hours
- Clear all sessions and start fresh
- Calculate total hours studied across all sessions
- All sessions saved permanently to a txt file

## What I Learned
- Storing three fields in one line using `|` separator
- Unpacking three values — `topic, time, hours`
- Summing a specific field across all records
- Handling `FileNotFoundError` in multiple functions
- Using `pass` to clear a file cleanly
- Building tools for your own use — this tracks
  your own real learning journey!

## Growth From V1
V1 only added and viewed sessions.
V2 adds total hours calculation, clear function
and better error handling throughout.

## How To Run
```bash
python study_tracker_v2.py
```