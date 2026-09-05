-- ================================================
-- Table: Employee
-- Database: ComputerShopDB
-- Topics: CREATE, INSERT, UPDATE, DELETE,
--         WHERE, ORDER BY, COUNT, MAX, AVG,
--         GROUP BY, HAVING
-- ================================================

-- Create Employee table
CREATE TABLE Employee (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    employee_position TEXT NOT NULL,
    salary NUMERIC NOT NULL,
    phone_number NUMERIC
);

-- Insert sample employees
INSERT INTO Employee
VALUES
(1, 'James', 'Manager', 400000, 0998737524),
(2, 'Maria', 'Salesperson', 250000, 0997646824),
(3, 'John', 'Technician', 350000, 088493736),
(4, 'Naomie', 'Cashier', 300000, 089367254),
(5, 'Ruth', 'Store Assistant', 200000, 0968468247);

-- View all employees
SELECT * FROM Employee;

-- Update employee position and salary
UPDATE Employee
SET 
    employee_position = 'Assistant Manager',
    salary = 380000
WHERE employee_id = 2;

-- Delete an employee
DELETE FROM Employee
WHERE employee_id = 1;

-- Filter by salary
SELECT * FROM Employee
WHERE salary > 300000;

-- Filter by position
SELECT * FROM Employee
WHERE employee_position = 'Technician';

-- Exclude a position
SELECT * FROM Employee
WHERE employee_position <> 'Manager';

-- Order by salary highest to lowest
SELECT salary, employee_name FROM Employee
ORDER BY salary DESC;

-- Order by salary lowest to highest
SELECT salary, employee_name FROM Employee
ORDER BY salary ASC;

-- Count total employees
SELECT COUNT(employee_name) AS total_employees
FROM Employee;

-- Find highest salary
SELECT MAX(salary) AS biggest_salary
FROM Employee;

-- Find average salary
SELECT AVG(salary) AS average_salary
FROM Employee;

-- Count employees per salary group
SELECT COUNT(salary) AS number_in_salary 
FROM Employee
GROUP BY salary;

-- Positions with less than 2 employees
SELECT employee_position, COUNT(*) AS total_employees
FROM Employee
GROUP BY employee_position
HAVING COUNT(*) < 2;