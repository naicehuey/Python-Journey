# To-Do List V2 — TXT Upgraded

An upgraded command-line to-do list app
built with Python and txt storage.
Adds separate complete and delete functions.

## What It Does
- Add new tasks to your list
- View all current tasks in a numbered list
- Mark a task as complete with `[x]` indicator
- Delete a specific task permanently
- Clear all tasks at once
- All tasks saved permanently to a txt file

## What I Learned
- Separating complete and delete into two
  different functions — more realistic task management
- Complete shows `[x]` feedback without removing —
  acknowledging done work before deciding to delete
- Delete uses `.pop(index)` to remove permanently
- That real task managers treat completion and
  deletion as two different actions —
  complete means done, delete means remove

## Known Bugs
- `complete_task()` writes back original list
  without marking the task — completion indicator
  shows but task status never actually changes
- Missing comma between menu items 5 and 6 —
  they merge into one string

## Growth From V1
V1 had complete which removed the task immediately.
V2 separates complete and delete giving the user
more control over their tasks.

## How To Run
```bash
python todo_list_v2_txt.py
```

## Example
```
1. Add Tasks
2. View Tasks
3. Complete Task
4. Clear Tasks
5. Delete Task
6. Exit
Choose Option: 3
1. learn python
2. build projects
Which task are you done with: 1
[x] - learn python
Task has been completed
```