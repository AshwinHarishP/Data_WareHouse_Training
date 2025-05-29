from oops.Person import Person


class Student(Person):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        super().show()
        print("Grade: ", self.grade)

s = Student("Ashwin", "O")
s.show()