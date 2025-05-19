/* Creating a Database */
CREATE DATABASE BookDB;
USE BookDB;

/* Creating a Table */
CREATE TABLE Book(
	BookID INT PRIMARY KEY,
	Title VARCHAR(30),
	Author VARCHAR(30),
	Genre VARCHAR(30),
	Price FLOAT,
	PublishedYear INT,
	Stock INT
);

/* Inserting Values */
INSERT INTO Book(BookID, Title, Author, Genre, Price, PublishedYear, Stock) VALUES
	(1, 'The Alchemist', 'Paulo Coelho', 'Fiction', 300, 1988, 50),
	(2, 'Sapiens', 'Yuval Noah Harari','Non-Fiction', 500, 2011, 30),
	(3, 'Atomic Habits', 'James Clear','Self-Help', 400, 2018, 25),
	(4, 'Rich Dad Poor Dad', 'Robert Kiyosaki','Personal Finance', 350, 1997, 20),
	(5, 'The Lean Startup', 'Eric Ries','Business', 450, 2011, 15);


/* Tasks */

/*1. Insert a book titled "Deep Work" by Cal Newport, Genre Self-Help, Price 420, Published Year 2016, Stock 35. */
INSERT INTO Book(BookID, Title, Author, Genre, Price, PublishedYear, Stock) 
VALUES (6, 'Deep Work', 'Cal Newport','Self-Help', 420, 2016, 35 );

/*2. Increase the price of all Self-Help books by 50. */
UPDATE Book
SET Price = Price + 50
WHERE Genre = 'Self-Help';

/*3. Remove the book with BookID = 4 (Rich Dad Poor Dad) */
DELETE Book
where BookID = 4;

/*4. Display all books sorted by Title in ascending order. */
SELECT * FROM Book
ORDER BY Title ASC;

/*5. List books sorted by Price in descending order. */
SELECT * FROM Book
ORDER BY Price DESC;

/*6. Display all books belonging to the Fiction genre. */
SELECT * FROM Book
WHERE Genre = 'Fiction';

/*7. List all Self-Help books priced above 400. */
SELECT * FROM Book
WHERE Genre ='Self-Help' AND Price > 400;

/*8. Retrieve all books that are either Fiction or published after 2000. */
SELECT * FROM Book
WHERE Genre ='Fiction' OR PublishedYear > 2000;

/* 9. Calculate the total value of all books in stock (Price * Stock). */
SELECT SUM(Price * Stock) AS TotalValue 
FROM Book;

/* 10. Calculate the average price of books grouped by Genre */
SELECT Genre, AVG(price) AS AveragePrice
FROM Book
GROUP BY Genre;

/* 11. Count the number of books written by Paulo Coelho. */
SELECT COUNT(*) AS TotalBooks
FROM Book
WHERE Author = 'Paulo Coelho';

/* 12. List all books whose Title contains the word "The". */
SELECT * FROM Book
WHERE Title LIKE '%The%';

/* 13. Display all books by Yuval Noah Harari priced below 600. */
SELECT * FROM Book
WHERE Author = 'Yuval Noah Harari' AND Price < 600;

/* 14. List books priced between 300 and 500. */
SELECT * FROM Book
WHERE Price BETWEEN 300 AND 500;

/* 15. Display the top 3 books with the highest price. */
SELECT TOP 3 * 
FROM Book
ORDER BY Price DESC;

/* 16. Find all books published before the year 2000. */
SELECT * FROM Book
WHERE PublishedYear < 2000;

/* 17. Calculate the total number of books in each Genre. */
SELECT Genre, COUNT(*) AS TotalBooks
FROM Book
GROUP BY Genre;

/* 18. Identify any books having the same title. */
SELECT Title, COUNT(*) AS TotalCount
FROM Book
GROUP BY Title
HAVING COUNT(*) > 1;

/* 19. Find the author who has written the maximum number of books. */
SELECT TOP 1 Author, COUNT(*) AS MaximumBooks
FROM Book
GROUP BY Author
ORDER BY COUNT(*) DESC;

/* 20. Find the earliest published book in each genre. */
SELECT Genre, MIN(PublishedYear) AS EarliestYear
FROM Book
GROUP BY Genre;