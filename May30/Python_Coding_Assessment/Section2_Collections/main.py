"""
Q4. Create a dictionary from the following lists:
    keys = ['a', 'b', 'c']
    values = [100, 200, 300]
"""

keys = ['a', 'b', 'c']
values = [100, 200, 300]
dict_a = {}

for key, value in zip(keys, values):
    dict_a[key] = value

print(dict_a)

"""
Q5. From a list Of employee salaries, extract:
        The maximum salary
        All salaries above average
        A sorted version in descending order
"""

salaries = [100000, 50000, 48000, 10000, 60000, 78000, 54000]

max_salary = max(salaries)
avg_salary = sum(salaries) / len(salaries)
above_avg = [s for s in salaries if s > avg_salary]
sorted_salary = sorted(salaries, reverse=True)

print(f"Maximum salary: {max_salary}")
print(f"Average salary: {avg_salary}")
print(f"Salaries above average: {above_avg}")
print(f"Salaries in descending order: {sorted_salary}")

"""
Q6. Create a set from a list and remove duplicates. Show the difference between two
    sets: a = [1, 2, 3, 4]  b = [3, 4, 5, 6]
"""

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

set_a = set(a)
set_b = set(b)

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Difference of two sets: {set_a.difference(set_b)}")