"""
1.Prime Number Checker: Write a function  is_prime(n) that returns
True if n is prime, else False . Use it to print all prime numbers between 1 and 100
"""

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

prime_list = []
for i in range(1, 101):
    if is_prime(i):
        prime_list.append(i)
print(prime_list)
