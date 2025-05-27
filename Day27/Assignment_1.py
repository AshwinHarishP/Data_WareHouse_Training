import random
# Variables, Data Types, Operators

"""
1. Digit Sum Calculator Ask the user for a number and calculate the sum of its
digits. Example: 753 → 7 + 5 + 3 = 15
"""

number = input("Enter a number: ")
Sum = 0
for i in number:
    Sum += int(i)
print(Sum)

"""
2. Reverse a 3-digit Number Input a 3-digit number and print it reversed. Input:
 123 → Output: 321
"""

# Method: 1
number = input("Enter a number: ")
print(int(number[::-1]))

#Method: 2
number = int(input("Enter a number: "))
rev = 0

while number > 0:
    last_number = number % 10
    rev = rev * 10 + last_number
    number //= 10
print(rev)

"""
 3. Unit Converter: Build a converter that takes meters and converts to:
            1. centimeters
            2. feet
            3. inches
"""

meter = float(input("Enter length in meter: "))
centimeter = meter * 100
feet = meter * 3.28084
inches = meter * 39.3701

print(f"The given length: {meter}")
print(f"meter to centimeter: {centimeter}")
print(f"meter to feet: {feet}")
print(f"meter to inches: {inches}")

"""
4. Percentage Calculator Input marks of 5 subjects and calculate total, average,
 and percentage. Display grade based on the percentage
"""

total = 0
for i in range(5):
    print("Subject: ", i+1)
    mark = float(input("Enter student mark: "))
    total += mark
avg = total / 5
percentage = (total / 500) * 100
print(f"Total Marks: {total}")
print(f"Percentage: {percentage}")

if percentage > 90:
    print("Grade: A")
elif percentage > 80:
    print("Grade B")
elif percentage > 50:
    print("Grade C")
else:
    print("Grade D")

# Conditions

"""
5. Leap Year Checker: A year is a leap year if it’s divisible by 4 and (not
   divisible by 100 or divisible by 400).
"""

year = int(input("Enter year: "))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 = 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

"""
6. Simple Calculator: Input two numbers and an operator (+ - * /) and perform the
 operation using if...elif...else .
"""

number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
operator = input("Enter operator: ")

if operator == "+":
    print(f"Addition of {number1} and {number2}: ", number1 + number2)
elif operator == "-":
    print(f"Subtraction of {number1} and {number2}: ", number1 - number2)
elif operator == "*":
    print(f"Multiplication of {number1} and {number2}: ", number1 * number2)
elif operator == "/":
    if number2 != 0:
        print(f"Division of {number1} and {number2}: ", number1 / number2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Choice")

"""
7. Triangle Validator: Given 3 side lengths, check whether they can form a valid triangle.
"""

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid triangle")
else:
    print("Invalid triangle")

"""
8. Bill Splitter with Tip:  Ask total bill amount, number of people, and tip percentage. Show final amount per person.
"""

total_bill_amount = float(input("Enter total bill amount: "))
no_of_people = int(input("Enter number of people: "))
tip_percentage = int(input("Enter tip percentage: "))

tip_amount = (tip_percentage / 100) * total_bill_amount
final_amount = total_bill_amount + tip_amount

amount_per_person = final_amount / no_of_people

print(f"Tip amount: {tip_amount:.2f}")
print(f"Total bill including tip: {final_amount:.2f}")
print(f"Each person should pay: {amount_per_person:.2f}")

# Loops

"""
9. Find All Prime Numbers Between 1 and 100 Use a nested loop to check divisibility
"""

prime_numbers = []
for i in range(2, 101):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break

    if flag:
        prime_numbers.append(i)
print(prime_numbers)

"""
10. Palindrome Checker: Ask for a string and check whether it reads the same backward
"""

string = input("Enter a string: ")
# Method 1
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string not a palindrome")

#Method 2
i = 0
j = len(string)-1
flag = True
while i <= j:
    if string[i] == string[j]:
        i += 1
        j -= 1
    else:
        flag = False
        break
if flag:
    print("The string is palindrome")
else:
    print("The string is not a palindrome")

"""
11.  Fibonacci Series (First N Terms): Input n , and print first Fibonacci sequence.
"""

n = int(input("Enter a number: "))
temp1, temp2 = 0, 1
fibo_list = []

for i in range(n):
    fibo_list.append(temp1)
    temp1, temp2 = temp2, temp1 + temp2

print(fibo_list)

"""
12. Multiplication Table (User Input): Take a number and print its table up to 10:
"""

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} =  {number * i}")

"""
13. Number Guessing Game: 
        Generate a random number between 1 to 100
        Ask the user to guess
        Give hints: "Too High", "Too Low"
        Loop until the correct guess
"""

rand_number = random.randint(1, 100)
while True:
    input_number = int(input("Enter a number: "))
    if input_number > rand_number:
        print("Too High")
    elif input_number < rand_number:
        print("Too Less")
    else:
        print("You guses the correct answer!!!")
        break

# ATM Machine Simulation

"""
14.ATM Machine Simulation
     Balance starts at 10,000
     Menu: Deposit / Withdraw / Check Balance / Exit
     Use a loop to keep asking
     Use conditionals to handle choices
"""

amount = 10000
def menu():
    print("\n Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

acc_no = input("Enter account number: ")
password = input("Enter password: ")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nDeposit")
        deposit_amount = float(input("Enter the amount to be deposited: "))
        amount += deposit_amount
        print(f"Amount: {deposit_amount} deposited successful")

    elif choice == "2":
        print("\nWithdraw")
        withdraw_amount = float(input("Enter the amount to be withdraw: "))
        if withdraw_amount <= amount:
            amount -= withdraw_amount
            print(f"Amount: {withdraw_amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    elif choice == "3":
        print("\nCheck Balance")
        print(f"Account Number: {acc_no}")
        print(f"Balance: {amount}")

    elif choice == "4":
        print("\nExiting...")
        break

    else:
        print("Enter a valid choice !!!")


15. Password Strength Checker

"""
15. Password Strength Checker
        Ask the user to enter a password
        Check if it's at least 8 characters
        Contains a number, a capital letter, and a symbol
"""

password = input("Enter password: ")

has_number,has_capital,has_symbol = False, False, False
has_len = len(password) >= 8

for char in password:
    if char.isdigit(): has_number = True
    elif char.isupper(): has_capital = True
    elif not char.isalnum(): has_symbol = True

if has_len and has_number and has_capital and has_symbol:
    print("Strong password")
else:
    print("Weak password")

#Find GCD (Greatest Common Divisor)

"""
16. Find GCD (Greatest Common Divisor)
        Input two numbers
        Use while loop or Euclidean algorith

"""

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

while number2 != 0:
    number1, number2 = number2, number1 % number2

print(f"GCD is: {number1}")







