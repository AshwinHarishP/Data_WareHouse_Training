"""
 7. Student Grade System
Create a class Student with:
Attributes:
            name,
            marks (a list)
Method:
        average()
        grade() — returns A/B/C/F based on average
"""

class StudentGradeSystem:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return  sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return  "A"

        elif avg >= 70:
            return "B"

        elif avg >= 50:
            return  "C"

        return "F"


name = input("Enter name of the student: ")
marks = []
for i in range(3):
    print("Mark ", i+1)
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)
student = StudentGradeSystem(name, marks)

print(f"Average mark: {student.average():.2f}")
print(f"Student grade: {student.grade()}")
