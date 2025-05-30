"""
Q7. Write a c ass Employee With __init__, display() and is_high_earner() methods
    An employee is a high earner if salary > 60000.
"""
class Employee:
    def __init__(self, employee_id, name, department, salary, joining_date):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.joining_date = joining_date

    def display(self):
        print(f"ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(f"Joining Date: {self.joining_date}")

    def is_high_earner(self):
        return self.salary > 60000

"""
Q8. Create a class Project that inherits from Employee and adds project_name and
    hours_allocated .
"""
class Project(Employee):
    def __init__(self, employee_id, name, department, salary, joining_date, project_name, hours_allocated):
        super().__init__(employee_id, name, department, salary, joining_date)
        self.project_name = project_name
        self.hours_allocated = hours_allocated

    def display(self):
        super().display()
        print(f"Project Name: {self.project_name}")
        print(f"Hours Allocated: {self.hours_allocated}")


"""
# Q9: Instantiate 3 employees and check high earner status
"""
employees = []
n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"Enter details for employee {i+1}:")
    emp_id = int(input("Id: "))
    name = input("Name: ")
    department = input("Department: ")
    salary = int(input("Salary: "))
    join_date = input("Join Date: ")

    emp = Employee(emp_id, name, department, salary, join_date)
    employees.append(emp)

print("\nEmployee Details:")
for employee in employees:
    employee.display()
    if employee.is_high_earner():
        print("High earner:")
    else:
        print("Not a high earner")

    print("\n")
