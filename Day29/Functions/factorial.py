"""
 3. Recursive Factorial Function: Create a function factorial(n) using recursion to return the factorial of a number.
"""

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

number = int(input("Enter a positive number: "))
print(f"Factorial of the given number {number} is: {factorial(number)}")