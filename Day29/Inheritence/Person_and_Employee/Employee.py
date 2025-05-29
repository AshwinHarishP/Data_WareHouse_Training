from Inheritence.Person_and_Employee.Person import Person


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee Id: {self.emp_id}")
        print(f"Employee Salary: {self.salary}")
