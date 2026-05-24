# Study Tracker V1 — Basic Version

The first version of the study session tracker
built with Python and txt storage.

## What It Does
- Add a study session with subject and hours
- Automatically records date and time
- View all recorded sessions
- All sessions saved permanently to a txt file

## What I Learned
- Recording sessions with automatic timestamp
- Storing multiple fields in a readable format
  using ` | ` as separator with labels
- Using a thin wrapper function —
  `view_session()` calling `load_session()`
- Using `.lower()` on input for consistency
- That starting simple and adding features
  later is a natural way to build

## How To Run
```bash
python study_tracker_v1.py
```