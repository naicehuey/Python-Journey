-- ================================================
-- File: group_by.sql
-- Database: PracticeDB
-- Topics: AGGREGATE, HAVING, GROUP BY
-- ================================================

-- Create an Orders table
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    product_category TEXT,
    quantity INTEGER,
    price NUMERIC(10,2),
    order_date DATE,
    status TEXT
);

-- Insert 8 orders
-- Mix up categories, statuses and quantities
INSERT INTO Orders
VALUES
(1, 'Jessica Jones', 'Groceries', 8, 20000, '2023-04-12', 'Completed'),
(2, 'Luke Cage', 'Clothes', 6, 35000, '2025-05-01', 'Cancelled'),
(3, 'Dare Devil', 'Glasses', 1, 2000, '2026-09-05', 'Scheduled'),
(4, 'Iron Fist', 'Gloves', 4, 5000, '2025-02-16', 'Completed'),
(5, 'Peter Parker', 'Gloves', 2, 2000, '2023-06-03', 'Pending'),
(6, 'Jessica Jones', 'Daipers', 42, 12000, '2024-03-09', 'Scheduled'),
(7, 'Peter Parker', 'Groceries', 10, 22000, '2024-09-19', 'Cancelled'),
(8, 'Iron Fist', 'Glasses', 1, 1200, '2026-01-25', 'Pending');

-- writing these queries:

-- 1. Total quantity ordered per category
SELECT product_category, SUM(quantity) AS total_quantity 
FROM Orders
GROUP BY product_category
ORDER BY total_quantity DESC;

-- 2. Total revenue per category
-- Hint: SUM(quantity * price)
SELECT product_category, SUM(quantity * price) AS total_revenue 
FROM Orders
GROUP BY product_category;

-- 3. Count orders per status
-- (Completed, Pending, Cancelled etc)
SELECT status, COUNT(status) AS total_per_status FROM Orders
GROUP BY status;

-- 4. Average price per category
SELECT product_category, AVG(price) as average_price FROM Orders
GROUP BY product_category;

-- 5. Categories where total quantity
--    ordered is more than 10
-- Hint: HAVING
SELECT product_category, SUM(quantity) AS total_quantity FROM Orders
GROUP BY product_category HAVING SUM(quantity) > 10;

-- 6. Categories where average price
--    is above 5000
-- Hint: HAVING AVG
SELECT product_category, AVG(price) AS average_quantity FROM Orders
GROUP BY product_category HAVING AVG(price) > 5000;

-- 7. Most expensive product per category
-- Hint: MAX + GROUP BY
SELECT product_category, MAX(price) AS highest_price 
FROM Orders
GROUP BY product_category;

-- 8. Count of completed orders per customer
-- Hint: WHERE + GROUP BY
SELECT customer_name, COUNT(status) AS total_per_status FROM Orders
WHERE status = 'Completed' GROUP BY customer_name;

-- 9. Total revenue only from completed orders
-- Hint: WHERE status = then GROUP BY
SELECT customer_name, SUM(quantity * price) AS total_revenue FROM Orders
WHERE status = 'Completed' GROUP BY customer_name;

-- 10. Show category, total orders and
--     total revenue together in one query
SELECT product_category, 
    SUM(quantity) AS total_orders, 
    SUM(quantity * price) AS total_revenue 
FROM Orders
GROUP BY product_category;
