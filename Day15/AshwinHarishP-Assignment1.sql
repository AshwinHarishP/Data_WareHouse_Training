CREATE DATABASE ProductDB;
USE ProductDB;

/* Creating a Table */ 

CREATE TABLE Product(
	ProductID INT PRIMARY KEY,
	ProductName VARCHAR(50),
	Category VARCHAR(50),
	Price FLOAT,
	StockQuantity INT,
	Supplier VARCHAR(50)
);

/* Inserting Values */
INSERT INTO Product (ProductID, ProductName, Category, Price, StockQuantity, Supplier)
VALUES
(1, 'Laptop', 'Electronics', 70000, 50, 'TechMark'),
(2, 'Office Chair', 'Furniture', 5000, 100, 'HomeComfort'),
(3, 'Smartwatch', 'Electronics', 15000, 200, 'GadgetHub'),
(4, 'Desk Lamp', 'Lighting', 1200, 300, 'BrightLife'),
(5, 'Wireless Mouse', 'Electronics', 1500, 250, 'GadgetHub');

/* Tasks */

/* 1. Adding a new product */ 
INSERT INTO Product(ProductID, ProductName, Category, Price, StockQuantity, Supplier)
VALUES(6, 'Gaming Keyboard', 'Electronics', 3500, 150, 'TechMart');

/* 2. Updating a Product Price */
UPDATE Product
SET Price = Price * 1.10
WHERE Category = 'Electronics';

/* 3. Deleting a Product */
DELETE FROM Product 
WHERE ProductID = 4;

/* 4. Read all Products */
SELECT * FROM Product;

/* 5. Sort products by stock quantity */
SELECT * FROM Product
ORDER BY StockQuantity ASC;

/* 6. Filter products by category */ 
SELECT * FROM Product
WHERE Category = 'Electronics';

/* 7. Retrieve all Electronics products priced above 5000. */
SELECT * FROM Product
WHERE Category = 'Electronics' AND Price > 5000;

/* 8. List all products that are either Electronics or priced below 2000. */ 
SELECT * FROM Product
WHERE Category = 'Electronics' OR Price < 2000;

/* 9. Find the total stock value (Price * StockQuantity) for all products. */ 
SELECT SUM(Price * StockQuantity) AS TotalStockValue 
FROM Product;

/* 10. Calculate the average price of products grouped by Category. */
SELECT Category, AVG(Price) AS AveragePrice
FROM Product
GROUP BY Category;

/*11. Count the total number of products supplied by GadgetHub. */
SELECT COUNT(ProductID) AS TotalProducts 
FROM Product
WHERE Supplier = 'GadgetHub';


/* 12. Display all products whose ProductName contains the word "Wireless". */ 
SELECT * FROM Product
WHERE ProductName LIKE '%Wireless%';

/* 13. Retrieve all products supplied by either TechMart or GadgetHub. */ 
SELECT * FROM Product
WHERE Supplier IN('TechMart', 'GadgetHub');

/* 14. List all products with a price between 1000 and 20000. */
SELECT * FROM Product
WHERE Price BETWEEN 1000 AND 20000;

/* 15. Find products where StockQuantity is greater than the average stock quantity. */ 
SELECT * FROM Product
WHERE StockQuantity > (
	SELECT AVG(StockQuantity) 
	FROM Product
);

/* 16. Display the top 3 most expensive products in the table. */
SELECT TOP 3 *
FROM Product
ORDER BY Price DESC;

/* 17. Identify any duplicate supplier names in the table. */ 
SELECT Supplier, COUNT(*) AS SupplierCount
FROM Product
GROUP BY Supplier
HAVING COUNT(*) > 1

/*18. Generate a summary that shows each Category with the number of products and the total stock value. */
SELECT Category, COUNT(*) AS NumberOfProducts, SUM(Price * StockQuantity) AS TotalStockValue
FROM Product
GROUP BY Category;

/*19. Find the supplier who provides the maximum number of products. */

SELECT TOP 1 Supplier, COUNT(*) AS ProductCount
FROM Product
GROUP BY Supplier
ORDER BY ProductCount DESC;

/*20. List the most expensive product in each category. */

SELECT *
FROM Product p
WHERE Price = (
    SELECT MAX(Price)
    FROM Product
    WHERE Category = p.Category
);


select * from Product