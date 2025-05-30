"""
Q10. Write to a file the names of employees who belong to the 'IT' department
"""
import pandas as pd

df = pd.read_csv(r"F:\Hexaware Training\Role Based Training\Python\May30\Python_Coding_Assessment\employees.csv")

it_department_employees = df[df['Department'] == 'IT']
with open('it_employee_list.txt', 'w') as file:
    for name in it_department_employees['Name']:
        file.write(name + '\n')

"""
Q11. Read from a text file and count the number of words.
"""
with open('it_employee_list.txt', 'r') as file:
    text = file.read()

words = text.split()
word_count = len(words)

print(f"Total number of words : {word_count}")
