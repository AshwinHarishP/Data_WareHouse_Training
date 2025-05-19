/* Creating a Database */
CREATE DATABASE ProductInventoryDB;
USE ProductInventoryDB;

/* Creating a Table */
CREATE TABLE ProductInventory(
	ProductID INT PRIMARY KEY,
	ProductName VARCHAR(50),
	Category VARCHAR(50),
	Quantity INT,
	UnitPrice FLOAT,
	Supplier VARCHAR(50),
	LastRestocked DATE
);

/* Inserting Values */
INSERT INTO ProductInventory(ProductID, ProductName, Category, Quantity, UnitPrice, Supplier, LastRestocked)
VALUES
(1, 'Laptop', 'Electronics', 20, 70000, 'TechMart', '2025-04-20'),
(2, 'Office Chair', 'Furniture', 50, 5000, 'HomeComfort', '2025-04-18'),
(3, 'Smartwatch', 'Electronics', 30, 15000, 'GadgetHub', '2025-04-22'),
(4, 'Desk Lamp', 'Lighting', 80, 1200, 'BrightLife', '2025-04-25'),
(5, 'Wireless Mouse', 'Electronics', 100, 1500, 'GadgetHub', '2025-04-30');


/* Tasks */

/* 1. Insert a product named "Gaming Keyboard", Category Electronics, Quantity 40, UnitPrice 3500, Supplier TechMart, LastRestocked 2025-05-01. */
INSERT INTO ProductInventory(ProductID, ProductName, Category, Quantity, UnitPrice, Supplier, LastRestocked)
VALUES
(6, 'Gaming Keyboard', 'Electronics', 40, 3500, 'TechMart', '2025-05-01');

/* 2. Increase the Quantity of Desk Lamp by 20. */
UPDATE ProductInventory
SET Quantity = Quantity + 20
WHERE ProductName = 'Desk Lamp';

/* 3. Remove the product with ProductID = 2 (Office Chair). */
DELETE FROM ProductInventory
WHERE ProductID = 2;

/* 4. Display all products sorted by ProductName in ascending order. */
SELECT * FROM ProductInventory
ORDER BY ProductName ASC;

/* 5. List products sorted by Quantity in descending order. */
SELECT * FROM ProductInventory
ORDER BY Quantity DESC;

/* 6. Display all Electronics products. */
SELECT * FROM ProductInventory
WHERE Category = 'Electronics';

/* 7. List all Electronics products with Quantity > 20. */ 
SELECT * FROM ProductInventory
WHERE Category = 'Electronics' AND Quantity > 20 ;

/* 8. Retrieve all products that belong to Electronics or have a UnitPrice below 2000. */
SELECT * FROM ProductInventory
WHERE Category = 'Electronics' OR UnitPrice < 2000 ;

/* 9. Calculate the total value of all products (Quantity * UnitPrice). */
SELECT SUM(Quantity * UnitPrice) AS TotalValue
FROM ProductInventory;

/* 10. Find the average price of products grouped by Category. */
SELECT Category, AVG(UnitPrice) AS AveragePrice
FROM ProductInventory
GROUP BY Category;

/* 11.Display the number of products supplied by GadgetHub. */ 
SELECT COUNT(*) AS TotalProducts
FROM ProductInventory
WHERE Supplier = 'GadgetHub';

/* 12. List all products whose ProductName starts with 'W'. */
SELECT *
FROM ProductInventory
WHERE ProductName LIKE 'W%';

/* 13. Display all products supplied by GadgetHub with a UnitPrice above 10000. */
SELECT *
FROM ProductInventory
WHERE Supplier = 'GadgetHub' AND UnitPrice > 10000;

/* 14. List all products with UnitPrice between 1000 and 20000. */
SELECT *
FROM ProductInventory
WHERE UnitPrice BETWEEN 1000 AND 20000;

/* 15. Display the top 3 products with the highest UnitPrice. */
SELECT TOP 3 ProductName
FROM ProductInventory
ORDER BY UnitPrice DESC;

/* 16. Find all products restocked in the last 10 days. */
SELECT *
FROM ProductInventory
WHERE LastRestocked >= DATEADD(DAY, -10, GETDATE());

/* 17. Calculate the total quantity of products from each Supplier. */
SELECT Supplier, SUM(Quantity) AS TotalQuantity
FROM ProductInventory
GROUP BY Supplier;

/* 18. List all products with Quantity less than 30. */
SELECT *
FROM ProductInventory
WHERE Quantity < 30;

/* 19. Find the supplier who provides the maximum number of products. */
SELECT TOP 1 Supplier, COUNT(*) AS ProductCount
FROM ProductInventory
GROUP BY Supplier
ORDER BY ProductCount DESC;

/*20. Find the product with the highest total stock value (Quantity * UnitPrice). */
SELECT TOP 1 ProductName, (Quantity * UnitPrice) AS StockValue
FROM ProductInventory
ORDER BY StockValue DESC;
