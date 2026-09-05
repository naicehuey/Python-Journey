# SQL Basics — PracticeDB

Foundational SQL practice scripts built using
fresh tables in PostgreSQL. Three focused files
covering the core building blocks of SQL —
selecting, filtering and sorting data.

## Files

### 01_select_queries.sql
Basic SELECT practice using a Students table.

**Table:** Students
- student_id, student_name, age, grade, city

**What I Practiced:**
- `SELECT *` — get all columns
- `SELECT column, column` — get specific columns
- `WHERE` — filter by condition
- `AS` — rename a column with an alias
- `DISTINCT` — remove duplicate values
- `INSERT` — add new records
- `DELETE ... RETURNING *` — delete and see what was removed
- `DROP TABLE` — remove the entire table

**Key Discovery:**
`RETURNING *` shows the affected rows immediately
after an INSERT, UPDATE or DELETE — no need to
write a separate SELECT to verify the change.

---

### 02_where_clauses.sql
WHERE condition practice using a Products table.

**Table:** Products
- product_id, product_name, category, price, stock

**What I Practiced:**
- `WHERE price > value` — greater than
- `WHERE stock < value` — less than
- `WHERE price >= value AND price <= value` — range
- `AND` — both conditions must be true
- `OR` — either condition can be true
- `!=` — not equal to operator
- `UPDATE SET WHERE` — update specific records
- `DELETE WHERE` — delete specific records
- `INSERT ... RETURNING *` — insert and verify
- `DROP TABLE` — clean up after practice

---

### 03_order_by.sql
Sorting practice using an Employees table.

**Table:** Employees
- employee_id, employee_name, department,
  salary, years_experience

**What I Practiced:**
- `ORDER BY salary DESC` — highest to lowest
- `ORDER BY salary ASC` — lowest to highest
- `ORDER BY employee_name` — alphabetical A-Z
- `ORDER BY employee_name DESC` — Z-A
- `WHERE + ORDER BY` — filter then sort
- `ORDER BY department ASC, salary DESC` —
  sort by two columns at once

---

## Key Lessons From This Section

### RETURNING *
```sql
DELETE FROM Students 
WHERE student_id = 2 RETURNING *;
```
PostgreSQL specific feature — shows exactly
what was inserted, updated or deleted without
needing a separate SELECT query. Very useful
for verifying changes immediately.

### != vs <>
Both mean NOT EQUAL TO in PostgreSQL:
```sql
WHERE category != 'Electronics'
WHERE category <> 'Electronics'
```
Both work — `!=` is more common in Python
and programming, `<>` is the SQL standard.

### Multi-column ORDER BY
```sql
ORDER BY department ASC, salary DESC
```
First sorts by department alphabetically,
then within each department sorts by salary
highest to lowest — powerful for grouped
sorting without GROUP BY.

### DISTINCT
```sql
SELECT DISTINCT city FROM Students;
```
Removes duplicate values — if 3 students
are from Lilongwe it only shows Lilongwe once.

## Database: PracticeDB
## Tool: PostgreSQL / pgAdmin