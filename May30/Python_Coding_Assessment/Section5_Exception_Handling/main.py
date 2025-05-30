"""
Q12. Write a program that accepts a number from the user and prints the square. Handle
    the case when input is not a number.
"""

try:
    number = float(input("Enter a number: "))
    print(f"The square of a number {number}: {number * number}")

except ValueError as Error:
    print(f"Error Occurred: {Error}")

"""
Q13. Handle a potential ZeroDivisionError in a division function.
"""

try:
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))
    print(f"Division of two numbers: {number1 / number2}")

except ZeroDivisionError as Error:
    print("Number could not be divided by zero")

except ValueError as Error:
    print(f"Error Occurred: {Error}")
