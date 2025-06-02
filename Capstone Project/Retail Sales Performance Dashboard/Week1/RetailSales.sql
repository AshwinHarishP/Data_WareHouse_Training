CREATE DATABASE RetailSales;
USE RetailSales;

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Stores table
CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(50),
    region VARCHAR(50)
);

-- Employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(30),
    store_id INT,
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

-- Sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    store_id INT,
    employee_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Inserting Values

-- Inserting Values for Products
INSERT INTO products (product_id, product_name, price) VALUES
(1, 'Laptop', 750.00), (2, 'Phone', 400.00), (3, 'Tablet', 300.00),
(4, 'Monitor', 200.00), (5, 'Keyboard', 50.00), (6, 'Mouse', 30.00),
(7, 'Printer', 120.00), (8, 'Scanner', 150.00), (9, 'Headphones', 80.00),
(10, 'Webcam', 90.00), (11, 'Smartwatch', 250.00), (12, 'Router', 70.00),
(13, 'SSD 1TB', 150.00), (14, 'HDD 2TB', 100.00), (15, 'Graphics Card', 300.00),
(16, 'RAM 16GB', 90.00), (17, 'Power Bank', 40.00), (18, 'VR Headset', 500.00),
(19, 'Game Controller', 60.00), (20, 'Microphone', 110.00);

-- Inserting Values for Stores
INSERT INTO stores (store_id, store_name, region) VALUES
(1, 'Downtown Store', 'North'), (2, 'Mall Outlet', 'South'),
(3, 'Tech Plaza', 'East'), (4, 'Gadget Hub', 'West'),
(5, 'Central Store', 'North'), (6, 'Market Street', 'South'),
(7, 'City Mall', 'East'), (8, 'Digital World', 'West'),
(9, 'ShopSmart', 'North'), (10, 'FastBuy', 'South'),
(11, 'ElectroCity', 'East'), (12, 'GadgetLand', 'West'),
(13, 'Urban Tech', 'North'), (14, 'BuyZone', 'South'),
(15, 'Techie Town', 'East'), (16, 'ByteMart', 'West'),
(17, 'Circuit Central', 'North'), (18, 'Gizmo Garage', 'South'),
(19, 'Device Depot', 'East'), (20, 'Plug & Play', 'West');

-- Inserting Values for Employees
INSERT INTO employees (employee_id, employee_name, store_id) VALUES
(1, 'Alice', 1), (2, 'Bob', 2), (3, 'Charlie', 3), (4, 'David', 4),
(5, 'Eva', 5), (6, 'Frank', 6), (7, 'Grace', 7), (8, 'Hannah', 8),
(9, 'Ian', 9), (10, 'Jack', 10), (11, 'Karen', 11), (12, 'Leo', 12),
(13, 'Mona', 13), (14, 'Nate', 14), (15, 'Olivia', 15), (16, 'Paul', 16),
(17, 'Quincy', 17), (18, 'Rachel', 18), (19, 'Sam', 19), (20, 'Tina', 20);

-- Inserting Values for Sales
INSERT INTO sales (sale_id, product_id, store_id, employee_id, quantity, sale_date) VALUES
(1, 1, 1, 1, 2, '2025-06-01'), (2, 2, 2, 2, 5, '2025-06-01'),
(3, 3, 3, 3, 1, '2025-06-02'), (4, 4, 4, 4, 4, '2025-06-02'),
(5, 5, 5, 5, 3, '2025-06-03'), (6, 6, 6, 6, 6, '2025-06-03'),
(7, 7, 7, 7, 1, '2025-06-04'), (8, 8, 8, 8, 2, '2025-06-04'),
(9, 9, 9, 9, 2, '2025-06-05'), (10, 10, 10, 10, 3, '2025-06-05'),
(11, 11, 11, 11, 1, '2025-06-06'), (12, 12, 12, 12, 4, '2025-06-06'),
(13, 13, 13, 13, 2, '2025-06-07'), (14, 14, 14, 14, 2, '2025-06-07'),
(15, 15, 15, 15, 5, '2025-06-08'), (16, 16, 16, 16, 1, '2025-06-08'),
(17, 17, 17, 17, 2, '2025-06-09'), (18, 18, 18, 18, 3, '2025-06-09'),
(19, 19, 19, 19, 4, '2025-06-10'), (20, 20, 20, 20, 1, '2025-06-10');


-- Stored Procedure for  Daily Sales of Store
CREATE PROCEDURE DailySales 
    @storeId INT,
    @saleDate DATE
AS
BEGIN
    SELECT 
        s.store_id,
        st.store_name,
        SUM(p.price * s.quantity) AS TotalSales
    FROM sales s
    JOIN stores st ON s.store_id = st.store_id
    JOIN products p ON s.product_id = p.product_id
    WHERE s.store_id = @storeId AND s.sale_date = @saleDate
    GROUP BY s.store_id, st.store_name;
END;
GO

--EXEC DailySales @storeId = 1, @saleDate = '2025-06-01';

-- Index for product and region
CREATE INDEX idx_product_id ON sales(product_id);
CREATE INDEX idx_region ON stores(region);

