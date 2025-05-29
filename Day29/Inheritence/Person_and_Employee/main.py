"""
8. Person → Employee
   Class Person: name, age
   Class Employee inherits Person, adds emp_id, salary
   Method display_info() shows all detail
"""
from Inheritence.Person_and_Employee.Employee import Employee


name = input("Enter your name: ")
age = int(input("Enter your age: "))
emp_id = int(input("Enter your enployee id: "))
salary = float(input("Enter your salary: "))
person_obj = Employee(name, age, emp_id, salary)
person_obj.display_info()