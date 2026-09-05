# ComputerShopDB — SQL Practice

PostgreSQL practice scripts built around a
fictional computer shop database. First SQL
database project documenting the learning
journey from basic queries to joins.

## Database Tables

### Customer
Stores customer information — name, country
and phone number.

### Employee
Stores employee details — name, position,
salary and phone number.

### Products
Stores product inventory — name, brand,
price and stock quantity.

### Sales
Junction table linking customers and employees
to sales transactions using foreign keys.

## What I Learned

### DDL — Data Definition Language
- `CREATE TABLE` — defining table structure
- Data types — INTEGER, TEXT, NUMERIC, DATE
- Constraints — PRIMARY KEY, NOT NULL
- `FOREIGN KEY` — linking tables together
- `DROP TABLE` — removing a table

### DML — Data Manipulation Language
- `INSERT INTO` — adding records
- `UPDATE SET WHERE` — modifying records
- `DELETE WHERE` — removing records

### DQL — Data Query Language
- `SELECT` — basic and specific column queries
- `WHERE` — filtering with conditions
- `AND`, `OR`, `NOT` — combining conditions
- `<>` — not equal operator
- `ORDER BY ASC/DESC` — sorting results

### Aggregate Functions
- `COUNT()` — counting rows
- `SUM()` — totalling values
- `AVG()` — calculating averages
- `MAX()` — finding highest value
- `MIN()` — finding lowest value

### Grouping
- `GROUP BY` — grouping results by column
- `HAVING` — filtering after GROUP BY
- Difference between WHERE and HAVING —
  WHERE filters before grouping,
  HAVING filters after grouping

### Joins
- `JOIN ... ON` — combining two tables
- Multi-table JOIN — joining three tables
- Understanding foreign keys and
  how tables relate to each other

## How To Run
1. Open PostgreSQL or pgAdmin
2. Create a database called `computershopdb`
3. Run scripts in this order:
   - `customer_query.sql`
   - `employee_query.sql`
   - `products_query.sql`
   - `sales_query.sql`
   - `join_query.sql`
   - `practice_scripts.sql`

## Database: ComputerShopDB