-- =========================================
-- RESET DATABASE
-- =========================================

DROP DATABASE IF EXISTS db_project;
CREATE DATABASE db_project;
USE db_project;

-- =========================================
-- CREATE STAGING TABLE
-- =========================================

CREATE TABLE staging_table (
    order_id       VARCHAR(50),
    order_date     VARCHAR(50),
    ship_date      VARCHAR(50),
    ship_mode      VARCHAR(50),
    customer_name  VARCHAR(100),
    segment        VARCHAR(50),
    state          VARCHAR(50),
    country        VARCHAR(50),
    market         VARCHAR(50),
    region         VARCHAR(50),
    product_id     VARCHAR(50),
    category       VARCHAR(50),
    sub_category   VARCHAR(50),
    product_name   VARCHAR(255),
    sales          VARCHAR(50),
    quantity       VARCHAR(50),
    discount       VARCHAR(50),
    profit         VARCHAR(50),
    shipping_cost  VARCHAR(50),
    order_priority VARCHAR(50),
    year           VARCHAR(50)
);

-- =========================================
-- IMPORTANT
-- =========================================
-- AFTER RUNNING THE ABOVE CODE:
--
-- 1. Refresh schemas
-- 2. Expand db_project > Tables
-- 3. Right click staging_table
-- 4. Select "Table Data Import Wizard"
-- 5. Choose cleaned_superstore_mysql_v3.csv
-- 6. IMPORTANT:
--      Use Existing Table = staging_table
-- 7. Finish Import
--
-- AFTER IMPORT, RUN:
--
-- SELECT COUNT(*) FROM staging_table;
--
-- It should return 5000
-- =========================================

SELECT COUNT(*) FROM staging_table;

-- =========================================
-- DROP NORMALIZED TABLES IF THEY EXIST
-- (prevents "Table already exists" error
--  if this script is run more than once)
-- =========================================

DROP TABLE IF EXISTS Order_Details;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

-- =========================================
-- CREATE NORMALIZED TABLES
-- =========================================

CREATE TABLE Customers (
    customer_id   INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    segment       VARCHAR(50),
    state         VARCHAR(50),
    country       VARCHAR(50)
);

CREATE TABLE Products (
    product_id   VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(255),
    category     VARCHAR(50),
    sub_category VARCHAR(50)
);

CREATE TABLE Orders (
    order_id   VARCHAR(50) PRIMARY KEY,
    order_date DATE,
    ship_date  DATE,
    ship_mode  VARCHAR(50),
    customer_id INT,

    FOREIGN KEY (customer_id)
    REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Details (
    order_id   VARCHAR(50),
    product_id VARCHAR(50),
    sales      DECIMAL(10,2),
    quantity   INT,
    profit     DECIMAL(10,2),

    PRIMARY KEY (order_id, product_id),

    FOREIGN KEY (order_id)
    REFERENCES Orders(order_id),

    FOREIGN KEY (product_id)
    REFERENCES Products(product_id)
);

-- =========================================
-- LOAD CUSTOMERS
-- (DISTINCT on name+segment+country only;
--  excludes state because same customer
--  can appear in multiple states)
-- =========================================

INSERT INTO Customers (
    customer_name,
    segment,
    state,
    country
)
SELECT DISTINCT
    TRIM(customer_name),
    TRIM(segment),
    TRIM(state),
    TRIM(country)
FROM staging_table
WHERE customer_name IS NOT NULL;

-- =========================================
-- LOAD PRODUCTS
-- (use MIN() to pick one name per product_id
--  because some product_ids have 2 different
--  names in the data - avoids PK violation)
-- =========================================

INSERT INTO Products (
    product_id,
    product_name,
    category,
    sub_category
)
SELECT
    product_id,
    MIN(TRIM(product_name)),
    MIN(TRIM(category)),
    MIN(TRIM(sub_category))
FROM staging_table
WHERE product_id IS NOT NULL
GROUP BY product_id;

-- =========================================
-- LOAD ORDERS
-- (DISTINCT on order_id only;
--  some order_ids appear with multiple
--  customers - we take the first customer
--  found using MIN on customer_name)
-- =========================================

INSERT INTO Orders (
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id
)
SELECT
    s.order_id,
    STR_TO_DATE(MIN(s.order_date), '%Y-%m-%d'),
    STR_TO_DATE(MIN(s.ship_date),  '%Y-%m-%d'),
    MIN(s.ship_mode),
    MIN(c.customer_id)
FROM staging_table s
JOIN Customers c
    ON TRIM(s.customer_name) = TRIM(c.customer_name)
    AND TRIM(s.segment)      = TRIM(c.segment)
    AND TRIM(s.country)      = TRIM(c.country)
GROUP BY s.order_id;
-- =========================================
-- LOAD ORDER DETAILS
-- (3 duplicate order_id+product_id pairs
--  exist in staging; SUM aggregates them
--  into one row to avoid PK violation)
-- =========================================

INSERT INTO Order_Details (
    order_id,
    product_id,
    sales,
    quantity,
    profit
)
SELECT
    order_id,
    product_id,
    SUM(CAST(sales    AS DECIMAL(10,2))) AS sales,
    SUM(CAST(quantity AS UNSIGNED))      AS quantity,
    SUM(CAST(profit   AS DECIMAL(10,2))) AS profit
FROM staging_table
WHERE order_id   IS NOT NULL
  AND product_id IS NOT NULL
  AND order_id IN (SELECT order_id FROM Orders)
GROUP BY order_id, product_id;

-- =========================================
-- VERIFY DATA LOADED
-- =========================================

SELECT COUNT(*) AS staging_rows      FROM staging_table;
SELECT COUNT(*) AS customer_rows     FROM Customers;
SELECT COUNT(*) AS product_rows      FROM Products;
SELECT COUNT(*) AS order_rows        FROM Orders;
SELECT COUNT(*) AS order_detail_rows FROM Order_Details;

-- =========================================
-- BUSINESS QUERY 1
-- TOTAL REVENUE IN 2014
-- =========================================

SELECT
    SUM(od.sales) AS total_revenue_2014
FROM Orders o
JOIN Order_Details od ON o.order_id = od.order_id
WHERE YEAR(o.order_date) = 2014;

-- =========================================
-- BUSINESS QUERY 2
-- TOP 5 CUSTOMERS BY PURCHASE VOLUME
-- =========================================

SELECT
    c.customer_name,
    SUM(od.sales) AS total_purchase
FROM Customers c
JOIN Orders o         ON c.customer_id  = o.customer_id
JOIN Order_Details od ON o.order_id     = od.order_id
GROUP BY c.customer_name
ORDER BY total_purchase DESC
LIMIT 5;

-- =========================================
-- BUSINESS QUERY 3
-- MONTHLY SALES
-- =========================================

SELECT
    MONTH(o.order_date) AS month,
    SUM(od.sales)       AS total_sales
FROM Orders o
JOIN Order_Details od ON o.order_id = od.order_id
GROUP BY MONTH(o.order_date)
ORDER BY month;

-- =========================================
-- BUSINESS QUERY 4
-- TOP 5 PRODUCTS BY QUANTITY SOLD
-- =========================================

SELECT
    p.product_name,
    SUM(od.quantity) AS total_quantity_sold
FROM Products p
JOIN Order_Details od ON p.product_id = od.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 5;

-- =========================================
-- BUSINESS QUERY 5
-- PROFIT BY CATEGORY
-- =========================================

SELECT
    p.category,
    SUM(od.profit) AS total_profit
FROM Products p
JOIN Order_Details od ON p.product_id = od.product_id
GROUP BY p.category
ORDER BY total_profit DESC;

-- =========================================
-- SAMPLE OUTPUT CHECKS
-- =========================================

SELECT * FROM Customers     LIMIT 10;
SELECT * FROM Products      LIMIT 10;
SELECT * FROM Orders        LIMIT 10;
SELECT * FROM Order_Details LIMIT 10;