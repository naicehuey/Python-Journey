-- ================================================
-- Table: Sales (Junction Table)
-- Database: ComputerShopDB
-- Topics: FOREIGN KEYS, JOIN, Multi-table JOIN
-- ================================================

-- Create Sales table with foreign keys
CREATE TABLE Sales (
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    employee_id INTEGER,
    sale_date DATE,

    FOREIGN KEY (customer_id)
        REFERENCES Customer(customer_id),

    FOREIGN KEY (employee_id)
        REFERENCES Employee(employee_id)
);

-- Insert a sale record
INSERT INTO Sales
VALUES
(1, 2, 2, '2026-09-05');

-- Join Customer and Sales — get customer name and sale date
SELECT customer_name, sale_date
FROM Customer
JOIN Sales
ON Customer.customer_id = Sales.customer_id;

-- Join Customer, Sales and Employee — get all three
SELECT customer_name, employee_name, sale_date
FROM Customer
JOIN Sales
ON Customer.customer_id = Sales.customer_id
JOIN Employee
ON Sales.employee_id = Employee.employee_id;

-- Join Employee and Sales — get employee name and sale date
SELECT employee_name, sale_date
FROM Employee
JOIN Sales
ON Employee.employee_id = Sales.employee_id;

-- Full join — customer name, employee name and sale date
SELECT customer_name, employee_name, sale_date
FROM Customer
JOIN Sales
ON Sales.customer_id = Customer.customer_id
JOIN Employee
ON Sales.employee_id = Employee.employee_id;