/* Creating a Database */
CREATE DATABASE EmployeeAttendanceDB;
USE EmployeeAttendanceDB;

/* Creating Table */
CREATE TABLE EmployeeAttendance(
	AttendanceID INT PRIMARY KEY,
	EmployeeName VARCHAR(50),
	Department VARCHAR(50),
	Date DATE,
	Status VARCHAR(8),
	HoursWorked INT
);

/* Inserting Values */
INSERT INTO EmployeeAttendance(AttendanceID, EmployeeName, Department, Date, Status, HoursWorked)
VALUES
(1, 'John Doe', 'IT', '2025-05-01', 'Present', 8),
(2, 'Priya Singh', 'HR', '2025-05-01', 'Absent', 0),
(3, 'Ali Khan', 'IT', '2025-05-01', 'Present', 7),
(4, 'Riya Patel', 'Sales', '2025-05-01', 'Late', 6),
(5, 'David Brown', 'Marketing', '2025-05-01', 'Present', 8);


/* Tasks */

/* 1. Insert a record for Neha Sharma, from Finance, on 2025-05-01, marked as Present, with 8 hours worked. */
INSERT INTO EmployeeAttendance(AttendanceID, EmployeeName, Department, Date, Status, HoursWorked)
VALUES
(6, 'Neha Sharma', 'Finance', '2025-05-01', 'Present', 8)

/* 2. Change Riya Patel's status from Late to Present. */
UPDATE EmployeeAttendance
SET Status = 'Present'
WHERE AttendanceID = 4;

/* 3. Remove the attendance entry for Priya Singh on 2025-05-01. */
DELETE FROM EmployeeAttendance
WHERE AttendanceID = 2 AND Date = '2025-05-01';

/* 4. Display all attendance records sorted by EmployeeName in ascending order. */
SELECT * FROM EmployeeAttendance
ORDER BY EmployeeName ASC;

/* 5. List employees sorted by HoursWorked in descending order. */
SELECT * FROM EmployeeAttendance
ORDER BY HoursWorked DESC;

/* 6. Display all attendance records for the IT department. */
SELECT * FROM EmployeeAttendance
WHERE Department = 'IT';

/* 7. List all Present employees from the IT department. */
SELECT * FROM EmployeeAttendance
WHERE Department = 'IT' AND Status = 'Present';

/* 8. Retrieve all employees who are either Absent or Late. */
SELECT * FROM EmployeeAttendance
WHERE Status = 'Absent' OR Status = 'Late';

/* 9. Calculate the total hours worked grouped by Department. */
SELECT Department, SUM(HoursWorked) AS TotalHoursWorked 
FROM EmployeeAttendance
GROUP BY Department;

/* 10. Find the average hours worked per day across all departments. */
SELECT Department, AVG(HoursWorked) AS AvgHoursWorked 
FROM EmployeeAttendance
GROUP BY Department;

/* 11. Count how many employees were Present, Absent, or Late. */
SELECT Status, COUNT(*) AS TotalEmployees
FROM EmployeeAttendance
GROUP BY Status;

/* 12. List all employees whose EmployeeName starts with 'R'. */
SELECT EmployeeName
FROM EmployeeAttendance 
WHERE EmployeeName LIKE 'R%';

/*13. Display employees who worked more than 6 hours and are marked Present. */ 
SELECT * FROM EmployeeAttendance
WHERE Status = 'Present' AND HoursWorked > 6;

/*14. List employees who worked between 6 and 8 hours. */
SELECT * FROM EmployeeAttendance
WHERE HoursWorked BETWEEN 6 AND 8;

/* 15. Display the top 2 employees with the highest number of hours worked. */
SELECT TOP 2 EmployeeName, HoursWorked
FROM EmployeeAttendance
ORDER BY HoursWorked DESC;

/* 16. List all employees whose HoursWorked are below the average. */
SELECT EmployeeName 
FROM EmployeeAttendance
WHERE HoursWorked < (
	SELECT AVG(HoursWorked)
	FROM EmployeeAttendance
);

/* 17. Calculate the average hours worked for each attendance status (Present, Absent, Late). */
SELECT Status, AVG(HoursWorked) AS AverageHoursWorked 
FROM EmployeeAttendance
GROUP BY Status;

/* 18. Identify any employees who have multiple attendance records on the same date. */
SELECT EmployeeName, Date
FROM EmployeeAttendance
GROUP BY EmployeeName, Date
HAVING COUNT(*) > 1;


/* 19. Find the department with the highest number of Present employees. */ 
SELECT TOP 1 Department, COUNT(*) AS CountOfEmployees
FROM EmployeeAttendance
WHERE Status = 'Present'
GROUP BY Department
ORDER BY CountOfEmployees DESC;

/* 20. Find the employee with the most hours worked in each department. */
SELECT Department, EmployeeName, HoursWorked
FROM EmployeeAttendance e
WHERE HoursWorked = (
    SELECT MAX(HoursWorked)
    FROM EmployeeAttendance
    WHERE Department = e.Department
);
