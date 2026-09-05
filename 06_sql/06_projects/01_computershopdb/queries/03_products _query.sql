-- ================================================
-- Table: Products
-- Database: ComputerShopDB
-- Topics: CREATE, INSERT, UPDATE, DELETE,
--         WHERE conditions, ORDER BY,
--         GROUP BY, HAVING
-- ================================================

-- Create Products table
CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    brand TEXT,
    price NUMERIC(10,2),
    stock INTEGER
);

-- Insert products
INSERT INTO Products
VALUES
(1, 'PS5', 'Sony', 950000, 5),
(4, 'Samsung 980 SSD', 'Samsung', 95000, 30);

-- View all products
SELECT * FROM Products;

-- Select specific columns
SELECT product_name, price
FROM Products;

-- Filter by stock
SELECT *
FROM Products
WHERE stock > 10;

-- Update stock by product ID
UPDATE Products
SET stock = 4
WHERE product_id = 1;

-- View product name and stock
SELECT product_name, stock FROM Products;

-- View specific product
SELECT * FROM Products WHERE product_id = 1;

-- Insert new product
INSERT INTO Products
(product_id, product_name, brand, price, stock)
VALUES
(5, 'Xbox 720', 'Microsoft', 500000.00, 10);

-- View all products
SELECT * FROM Products;

-- Delete a product
DELETE FROM Products
WHERE product_id = 4;

-- Filter by price conditions
SELECT * FROM Products WHERE price > 100000;
SELECT * FROM Products WHERE price >= 0;
SELECT * FROM Products WHERE price <= 120000;

-- Filter by brand conditions
SELECT * FROM Products WHERE brand <> 'Sony';
SELECT * FROM Products WHERE brand = 'Sony' AND price > 500000;
SELECT * FROM Products WHERE brand = 'Sony' OR brand = 'Corsair';
SELECT * FROM Products WHERE NOT brand = 'Sony';

-- Order by price
SELECT * FROM Products ORDER BY price ASC;
SELECT * FROM Products ORDER BY price DESC;

-- Total stock per brand for brands with more than 20 units
SELECT
    brand,
    SUM(stock) AS total_stock
FROM Products
GROUP BY brand
HAVING SUM(stock) > 20;