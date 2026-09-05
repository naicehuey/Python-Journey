-- ================================================
-- File: order_by.sql
-- Database: PracticeDB
-- Topics: ORDER BY ASC, ORDER BY DESC, 
--         WHERE + ORDER BY, multi-column sort
-- ================================================

-- Create an Employees table
CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    department TEXT,
    salary NUMERIC,
    years_experience INTEGER
);

-- Insert 6 employees
INSERT INTO Employees
VALUES
(1, 'Hugh Manstack', 'I.T', 600000, 5),
(2, 'Damian Freeman', 'H.R', 800000, 4),
(3, 'Simon Rwanda', 'I.T', 400000, 4),
(4, 'Mary Naomia', 'Law', 500000, 3),
(5, 'Jane Sofania', 'Law', 300000, 1),
(6, 'Jimmy Osborn', 'Acconts', 700000, 6);

-- Now writing these queries:

-- 1. Order employees by salary highest to lowest
SELECT * FROM Employees ORDER BY salary DESC;

-- 2. Order employees by salary lowest to highest
SELECT * FROM Employees ORDER BY salary ASC;

-- 3. Order employees by name alphabetically A-Z by Default is ASCEND
SELECT * FROM Employees ORDER BY employee_name ASC;

-- 4. Order employees by name Z-A
SELECT * FROM Employees ORDER BY employee_name DESC;

-- 5. Order by years experience highest to lowest
--    but only show employees with salary above 500000
SELECT * FROM Employees WHERE Salary > 300000 ORDER BY years_experience DESC;

-- 6. Order by department name then by salary
--    within each department
-- Hint: ORDER BY department ASC, salary DESC
SELECT * FROM Employees ORDER BY department ASC, salary DESC;