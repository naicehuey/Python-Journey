-- ================================================
-- File: where_clauses.sql
-- Database: PracticeDB
-- Topics: CREATE, INSERT, SELECT, WHERE, AND, OR, UPDATE,
-- CONDITION: NOT_EQUAL_TO, GREATER_THAN, LESS_THAN, GREATER_THAN/LESS_THAN_OR_EQUAL_TO
-- ================================================

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price NUMERIC(10,2),
    stock INTEGER
);

-- Inserting 6 random products
INSERT INTO Products
VALUES
(1, 'Novel', 'Books', 70, 6),
(2, 'Banana', 'Food', 100, 20),
(3, 'Dell Laptop', 'Laptops', 750, 5),
(4, 'Samsung Laptop', 'Laptops', 800, 8),
(5, 'Samsung TV', 'Electronics', 9000, 7),
(6, 'Samsung S26', 'Phones', 1800, 16),
(7, 'Miecrowave', 'Electronics', 300, 10);

-- Now writing queries:

-- 1. Products where price is greater than 100
SELECT * FROM Products WHERE price > 100;

-- 2. Products where stock is less than 10
SELECT * FROM Products WHERE stock < 10;

-- 3. Products where category is 'Electronics'
--    AND price is greater than 500
SELECT * FROM Products WHERE price > 500 AND category = 'Electronics';

-- 4. Products where category is 'Phones'
--    OR category is 'Laptops'
SELECT * FROM Products WHERE category = 'Phones' or category = 'Laptops';

-- 5. Inserting one more product
INSERT INTO Products
VALUES
(8, 'Sony x9', 'Phone', 1100, 6) RETURNING *;

-- 6. Products where brand is NOT 'Eletronics'
SELECT * FROM Products WHERE category != 'Electronics';

-- 7. Products where price is between 100 and 500
-- Hint: price >= 100 AND price <= 500
SELECT * FROM Products WHERE price >= 100 AND price <= 800;

-- 8. Update one product price
UPDATE Products SET price = 2000 WHERE product_id = 6 RETURNING *;

-- 9. Delete one product
DELETE FROM Products WHERE product_name = 'Novel' RETURNING *;

-- 10. Drop product table
DROP TABLE Products;

-- Note: I Usually use RETURNING to show effects taken without using creating a SELECT_query separately 