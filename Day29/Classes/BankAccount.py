"""
5. Class: BankAccount
Attributes:
            name,
            balance
Methods:
            deposit(amount),
            withdraw(amount),
            get_balance(),
Prevent withdrawal if balance is insufficient
"""


class BankAccount:
    def __init__(self, name, balance=1000):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance


name = input("Enter your name: ")
account = BankAccount(name)

while True:
    print("\n1. Amount Deposit \n2. Amount Withdraw \n3. Check Balance \n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to be deposited: "))
        if account.deposit(amount):
            print(f"Amount {amount} deposited successfully.")

    elif choice == "2":
        amount = float(input("Enter amount to be withdrawn: "))
        if account.withdraw(amount):
            print(f"Amount {amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    elif choice == "3":
        print(f"Your account balance is: {account.get_balance()}")

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Please try again.")
