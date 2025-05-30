import pandas as pd

"""
Q17. From employees.csv , filter all IT department employees with salary > 60000
"""
df = pd.read_csv(r"F:\Hexaware Training\Role Based Training\Python\May30\Python_Coding_Assessment\employees.csv")

filtered_data = df.query("Department == 'IT' and Salary > 60000")

print("Displaying the employees with IT Department and Salary > 60000")
print(filtered_data)

"""
Q18. Group by Department and get:
        Count of employees
        Total Salary
        Average Salary
"""

grouped_result = df.groupby('Department')

print("\nTotal employees in each department")
print(grouped_result.size().reset_index(name="EmployeeCount"))

print("\nTotal salary by department:")
print(grouped_result['Salary'].sum().reset_index(name="TotalSalary"))

print("\nAverage salary by department:")
print(grouped_result['Salary'].mean().reset_index(name="AverageSalary"))

"""
Q20. Sort all employees by salary in descending order.
"""

sorted_df = df.sort_values(by="Salary", ascending=False)

print("\nEmployees Salary in descending order")
print(sorted_df)