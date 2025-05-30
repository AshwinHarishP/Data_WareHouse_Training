"""
1. Write a Python program to print all odd numbers between 10 and 50
"""
for i in range(10, 51):
    if i % 2:
        print(i)

"""
2. Create a function that returns whether a given year is a leap year.
"""
def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))

if leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

"""
Q3. Write a loop that counts how many times the letter a appears in a given string.
"""

word = input("Enter a word: ").lower()
count_a = 0
for char in word:
    if char == 'a':
        count_a += 1

print(f"Letter 'a' count: {count_a}")
