# Notes Writer V3 — With Timestamps

An upgraded notes app that records when each
note was added. Built with Python and txt storage.

## What It Does
- Add a new note with automatic timestamp
- View all notes with their creation time
- Remove a specific note by number
- Clear all notes at once
- All notes saved permanently to a txt file

## What I Learned
- Adding timestamps automatically using `datetime.now()`
- Storing multiple fields using `|` separator —
  note content and timestamp in one line
- Splitting stored data to display fields separately
- Using `_` to ignore timestamp when only
  note names are needed
- Building delete by number — read, pop, write back
- That adding timestamps makes notes more useful
  in real world apps

## Growth From V2
V2 had a menu but no timestamps and no delete.
V3 adds automatic timestamping and delete —
making it feel like a real note taking app.

## How To Run
```bash
python notes_writer_v3.py
```