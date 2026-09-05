-- ================================================
-- Practice Scripts
-- Database: ComputerShopDB
-- Topics: SELECT, WHERE, AND/OR, ORDER BY,
--         Aggregates, GROUP BY, HAVING
-- ================================================

-- Basic SELECT all
SELECT *
FROM Employee;

-- Filter by salary
SELECT *
FROM Employee
WHERE salary > 300000;

-- Select specific columns with filter
SELECT employee_position, employee_name
FROM Employee
WHERE salary <= 300000;

-- AND condition — both must be true
SELECT employee_name, salary
FROM Employee
WHERE salary >= 300000 
AND employee_position = 'Technician';

-- OR condition — either can be true
SELECT employee_name, employee_position
FROM Employee
WHERE employee_position = 'Cashier' 
OR employee_position = 'Technician';

-- Order by salary high to low
SELECT employee_name, salary
FROM Employee
ORDER BY salary DESC;

-- Order by salary low to high
SELECT employee_name, salary
FROM Employee
ORDER BY salary ASC;

-- Aggregate functions
SELECT COUNT(*) AS total_employees FROM Employee;
SELECT SUM(salary) AS total_salary FROM Employee;
SELECT AVG(salary) AS average_salary FROM Employee;
SELECT MAX(salary) AS max_salary FROM Employee;
SELECT MIN(salary) AS min_salary FROM Employee;

-- Count employees per position
SELECT COUNT(*) AS total_employees, employee_position
FROM Employee
GROUP BY employee_position;

-- Insert new employees
INSERT INTO Employee
VALUES
(1, 'James', 'Technician', 400000, 947625372),
(6, 'Naomi', 'Manager', 500000, 934847242);

-- HAVING — filter after GROUP BY
-- Positions with more than 1 employee
SELECT employee_position, COUNT(*) AS total_employees
FROM Employee
GROUP BY employee_position
HAVING COUNT(*) > 1;

-- Complex query — WHERE + GROUP BY + HAVING
SELECT employee_position, salary, COUNT(*) AS total_employees
FROM Employee
WHERE salary > 300000
GROUP BY employee_position, salary
HAVING COUNT(*) = 1;

-- MAX salary per position for high earners
SELECT employee_position,
    MAX(salary) AS highest_salary,
    COUNT(*) AS total_employees
FROM Employee
WHERE salary > 300000
GROUP BY employee_position
HAVING COUNT(*) >= 1;

-- High earners ordered by salary
SELECT employee_name, salary
FROM Employee
WHERE salary > 300000
ORDER BY salary DESC;

-- Average salary check
SELECT AVG(salary) AS average_salary
FROM Employee;

-- Positions with more than 1 employee
SELECT employee_position, COUNT(*) AS total_employees
FROM Employee
GROUP BY employee_position
HAVING COUNT(*) > 1;