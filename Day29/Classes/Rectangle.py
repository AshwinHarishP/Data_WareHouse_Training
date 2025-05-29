"""
4. Class: Rectangle

Attributes:
            length,
            width
Methods:
        area(),
        perimeter(),
        width,
        is_square() → returns True if length == width
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return  self.length * self.width

    def is_square(self):
        return self.length == self.width

    def perimeter(self):
        return  2 * (self.length + self.width)

length = float(input("Enter a length: "))
width = float(input("Enter a width: "))

obj = Rectangle(length, width)
print(f"It is a square: {obj.is_square()}")
print(f"Area: {obj.area()}")
print(f"Perimeter: {obj.perimeter()}")






