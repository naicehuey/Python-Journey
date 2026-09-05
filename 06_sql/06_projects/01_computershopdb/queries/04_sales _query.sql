-- ================================================
-- Table: Sales — Early Version
-- Database: ComputerShopDB
-- Topics: FOREIGN KEYS, Basic JOIN
-- Note: This is the first version of the Sales
--       table before Join Query was built
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

-- Join Customer and Sales
SELECT * FROM Customer
JOIN Sales
ON Customer.customer_id = Sales.customer_id;

-- View all products
SELECT * FROM Sales