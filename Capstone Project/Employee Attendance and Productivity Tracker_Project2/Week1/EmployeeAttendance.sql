CREATE DATABASE EmployeeAttendance;
USE EmployeeAttendance;

-- Creating Tables

-- Employee table
CREATE TABLE employees (
    employee_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_name NVARCHAR(100),
    department NVARCHAR(100)
);

-- Attendance Table
CREATE TABLE attendance (
    attendance_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT FOREIGN KEY REFERENCES employees(employee_id),
    clock_in DATETIME,
    clock_out DATETIME
);

-- Task Table
CREATE TABLE tasks (
    task_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT FOREIGN KEY REFERENCES employees(employee_id),
    task_description NVARCHAR(MAX),
    task_date DATE
);

-- Inserting Records

-- Inserting record for Employee Table
INSERT INTO employees (employee_name, department) VALUES
('Ashwin', 'IT'),
('Aravind', 'HR'),
('Akhilesh', 'Finance'),
('Neha', 'IT'),
('Rahul', 'HR'),
('Pooja', 'Finance'),
('Suresh', 'IT'),
('Anita', 'HR'),
('Vikram', 'Finance'),
('Rohit', 'IT'),
('Sneha', 'HR'),
('Karan', 'Finance'),
('Deepa', 'IT'),
('Ramesh', 'HR'),
('Priya', 'Finance'),
('Manoj', 'IT'),
('Kavita', 'HR'),
('Ajay', 'Finance'),
('Sunita', 'IT'),
('Vikas', 'HR');


-- Inserting record for Attendance Table
INSERT INTO attendance (employee_id, clock_in, clock_out) VALUES
(1, '2025-06-01 09:00:00', '2025-06-01 17:00:00'),
(2, '2025-06-01 09:15:00', '2025-06-01 17:15:00'),
(3, '2025-06-01 08:45:00', '2025-06-01 16:45:00'),
(4, '2025-06-01 09:00:00', '2025-06-01 17:00:00'),
(5, '2025-06-01 09:05:00', '2025-06-01 17:05:00'),
(6, '2025-06-01 09:10:00', '2025-06-01 17:10:00'),
(7, '2025-06-01 09:00:00', '2025-06-01 17:00:00'),
(8, '2025-06-01 09:20:00', '2025-06-01 17:20:00'),
(9, '2025-06-01 08:55:00', '2025-06-01 16:55:00'),
(10, '2025-06-01 09:05:00', '2025-06-01 17:05:00'),
(11, '2025-06-01 09:00:00', '2025-06-01 17:00:00'),
(12, '2025-06-01 09:10:00', '2025-06-01 17:10:00'),
(13, '2025-06-01 08:50:00', '2025-06-01 16:50:00'),
(14, '2025-06-01 09:00:00', '2025-06-01 17:00:00'),
(15, '2025-06-01 09:15:00', '2025-06-01 17:15:00'),
(16, '2025-06-01 09:00:00', '2025-06-01 17:00:00'),
(17, '2025-06-01 09:05:00', '2025-06-01 17:05:00'),
(18, '2025-06-01 08:55:00', '2025-06-01 16:55:00'),
(19, '2025-06-01 09:00:00', '2025-06-01 17:00:00'),
(20, '2025-06-01 09:10:00', '2025-06-01 17:10:00');


-- Inserting record for tasks Table
INSERT INTO tasks (employee_id, task_description, task_date) VALUES
(1, 'Prepare project report', '2025-06-01'),
(2, 'Conduct interviews', '2025-06-01'),
(3, 'Review financial statements', '2025-06-01'),
(4, 'Develop feature X', '2025-06-01'),
(5, 'Organize team meeting', '2025-06-01'),
(6, 'Update documentation', '2025-06-01'),
(7, 'Fix bugs in module Y', '2025-06-01'),
(8, 'Plan training session', '2025-06-01'),
(9, 'Audit accounts', '2025-06-01'),
(10, 'Deploy new release', '2025-06-01'),
(11, 'Coordinate client calls', '2025-06-01'),
(12, 'Design UI mockups', '2025-06-01'),
(13, 'Prepare invoices', '2025-06-01'),
(14, 'Conduct performance reviews', '2025-06-01'),
(15, 'Update CRM', '2025-06-01'),
(16, 'Research new tools', '2025-06-01'),
(17, 'Organize workshops', '2025-06-01'),
(18, 'Test software', '2025-06-01'),
(19, 'Prepare presentations', '2025-06-01'),
(20, 'Maintain server uptime', '2025-06-01');

-- Crud Operations
SELECT * FROM attendance WHERE employee_id = 1;
UPDATE attendance SET clock_out = '2025-06-01 18:30:00' WHERE attendance_id = 2;
DELETE FROM tasks WHERE task_id = 3;

-- Stored Procedure
CREATE PROCEDURE CalculateTotalHours
    @EmployeeID INT
AS
BEGIN
    SELECT 
        e.employee_id,
        e.employee_name,
        SUM(DATEDIFF(MINUTE, a.clock_in, a.clock_out))/60.0 AS TotalWorkingHours
    FROM employees e
    LEFT JOIN attendance a 
	ON e.employee_id = a.employee_id
    WHERE e.employee_id = @EmployeeID
    GROUP BY e.employee_id, e.employee_name;
END;

EXEC CalculateTotalHours @EmployeeID = 1;

-- Creating index for employeeID and Department
CREATE INDEX employee_id_index ON attendance(employee_id);
CREATE INDEX department_index ON employees(department);