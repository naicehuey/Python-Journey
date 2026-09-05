-- ================================================
-- Table: Customer
-- Database: ComputerShopDB
-- Topics: CREATE, INSERT, SELECT, UPDATE
-- ================================================

-- Create Customer table
CREATE TABLE Customer (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    country TEXT,
    phone NUMERIC
);

-- Insert sample customers
INSERT INTO Customer
VALUES
(1, 'John Phiri', 'Malawi', 099304824),
(2, 'Mary Namadingo', 'Zambia', 023657839),
(3, 'Nmania Nenezo', 'Mozambique', 0440864824);

-- View all customers
SELECT * FROM Customer;

-- Update a customer name
UPDATE Customer
SET customer_name = 'John Namka'
WHERE customer_name = 'John Phiri';

-- Verify update
SELECT * FROM Customer;
