-- ================================================
-- File: aggregate_functions.sql
-- Database: PracticeDB
-- Topics: AGGREGATE FUNCTIONS, MULTIPLE CONDITIONS, HAVING, GROUP BY 
-- ================================================

-- Create a Sales table
CREATE TABLE Sales (
    sale_id INTEGER PRIMARY KEY,
    salesperson TEXT NOT NULL,
    product TEXT,
    amount NUMERIC(10,2),
    region TEXT,
    sale_date DATE
);

-- Insert 8 sales records of your choice
INSERT INTO Sales (sale_id, salesperson, product, amount, region, sale_date)
VALUES
(1, 'John Walker', 'AKA 47', 80000, 'Central', '2026-08-12'),
(2, 'Kratos Sparta', 'Battle Axe', 705000, 'North', '2025-03-01'),
(3, 'Tony Stark', 'Ironman Suit', 200000, 'South', '2022-05-20'),
(4, 'Bruce Wayne', 'Ultrity Belt', 150000, 'East', '2021-09-05'),
(5, 'John Walker', 'M16s Granade', 50000, 'Central', '2026-08-12'),
(6, 'Bruce Wayne', 'Bat-Mobile', 950000, 'East', '2023-04-30'),
(7, 'Tony Stalk', 'Hulk-Buster', 220000, 'South', '2022-10-02'),
(8, 'Kratos Sparta', 'Spartan Shield', 500000, 'Central', '2025-09-28'),
(9, 'Bruce Wayne', 'Battle Suit', 200000, 'East', '2024-11-18');


-- writing these queries:

-- 1. Count total number of sales
SELECT COUNT(sale_id) AS total_sales FROM Sales;

-- 2. Count sales in one specific region
SELECT COUNT(sale_id) AS total_region_sales FROM Sales
WHERE region = 'East';

-- 3. Sum of all sales amounts
SELECT SUM(amount) AS total_sales FROM Sales;

-- 4. Average sale amount
SELECT AVG(amount) AS average_sale_amount FROM Sales;

-- 5. Highest single sale amount
SELECT MAX(amount) AS highest_sale FROM Sales;

-- 6. Lowest single sale amount
SELECT MIN(amount) AS lowest_sale FROM Sales;

-- 7. Count, Sum and Average in one query
SELECT COUNT(sale_id) AS total_region_sales, SUM(amount) AS total_sales, AVG(amount) AS average_sale_amount
FROM Sales;

-- 8. Total sales per salesperson
SELECT salesperson, SUM(amount) FROM Sales GROUP BY salesperson;

-- 9. Average sale amount per region
SELECT region, AVG(amount) AS average_sale_amount FROM Sales GROUP BY region;

-- 10. Only show regions where total sales
--     amount is above a number you choose
SELECT region, SUM(amount) AS total_sales FROM Sales
GROUP BY region HAVING SUM(amount) > 200000;