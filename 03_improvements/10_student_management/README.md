# Student Management System — Improvements

A fully featured command-line student management
system built with Python and JSON storage.

## What It Does
- Add students with name, age, course and status
- View all students with details and grades
- Search students by name
- Add grades for 5 subjects per student
- Calculate and display average marks
- Show pass or fail based on 50% threshold
- Sort students by average grade
- Find the top performing student
- Show class summary — total, passed and failed
- Delete students from the system
- All data saved permanently using JSON

## What I Learned
- Building the most complex data model so far —
  a dictionary containing a list of dictionaries
- Calculating average from dictionary values —
  `sum(grade.values()) / len(grade)`
- Using `max()` with a custom key function
- Using `sorted()` with a custom key function
- Counting passed and failed from calculated averages
- Checking if grades exist before adding
- Using `:.2f` for precise decimal formatting

## How To Run
```bash
python student_management.py
```