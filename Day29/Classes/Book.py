"""
6. Class: Book
Attributes:
            title,
            author,
            price,
            in_stock

Method: sell(quantity)
    Reduces stock
    Throws an error if quantity exceeds stock
"""

class Book:
    def __init__(self, title, author, price, in_stock):
        self.title = title
        self.author = author
        self.price = price
        self.in_stock = in_stock

    def sell(self, quantity):
        if quantity > self.in_stock:
            raise ValueError("Quantity exceeds stock")
        self.in_stock -= quantity
        return True

title = input("Enter Book Title: ")
author = input("Enter Book Author: ")
price = float(input("Enter Book Price: "))
in_stock = int(input("Enter Total Stock: "))
book_obj = Book(title, author, price, in_stock)

try:
    quantity = int(input("Enter the quantity to be sold: "))
    if book_obj.sell(quantity):
        print(f"Book with quantity: {quantity} sold successfully")

except ValueError as Error:
    print(f"Error Occurred: {Error}")



