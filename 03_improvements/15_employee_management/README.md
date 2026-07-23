# Employee Management System

A command-line employee management system
built with Python and JSON storage.
Uses reusable utility functions within
a single file.

## What It Does
- Add new employees with name, position,
  salary and active status
- View all employees in formatted list
- Search employees by name
- Delete an employee from the database
- Promote an employee — update position
  and salary
- Deactivate an employee — change status
  without deleting
- Generate a report — total employees,
  active vs deactivated, total and highest
  salary expenditure
- All data saved permanently using JSON

## What I Learned
- Writing reusable functions within one file —
  `save_data()`, `load_data()`, `display_list()`
  work with any data not just employees
- Passing `formatter` as a function parameter —
  `display_list(items, format_employee)`
- Saving a value BEFORE modifying the list —
  save name before `pop()` so it's not lost
- Never name a variable the same as its
  function — causes shadowing bugs
- Using generator expressions with `sum()` —
  `sum(e['salary'] for e in employees)`
- Using `max()` with generator expression —
  `max(e['salary'] for e in employees)`
- Difference between delete and deactivate —
  delete removes permanently, deactivate
  keeps the record but marks as inactive
- Confirming destructive actions with Y/N
  before executing them

## How To Run
```bash
python employee_management.py
```

## Example
```
1. Add Employee
2. View Employees
3. Search Employee
4. Delete Employee
5. Promote Employee
6. Deactivate Employee
7. Report
8. Exit
Choose: 1
Employee name: John
Employee position: Developer
Employee salary: 50000
New Employee Added.
```