import pandas as pd
from datetime import datetime

"""
Q14. Load both  employees.csv and projects.csv using Pandas.
"""
employee = pd.read_csv(r"F:\Hexaware Training\Role Based Training\Python\May30\Python_Coding_Assessment\employees.csv")
project = pd.read_csv(r"F:\Hexaware Training\Role Based Training\Python\May30\Python_Coding_Assessment\projects.csv")

print("\nEmployee csv file")
print(employee)

print("\nproject csv file")
print(project)

"""
Q15. Display: First 2 rows of employees 
              Unique values in the  Department column
              Average salary by department
"""

print("\n First 2 rows of employees")
print(employee.head(2))

print("\n Unique values in the  Department column")
print(employee['Department'].unique())

print("\n Average salary by department")
dept = employee.groupby('Department')
print(dept['Salary'].mean().reset_index(name="Average"))


"""
Q16. Add a column 
TenureInYears = current year - joining year.
"""
employee['JoiningDate'] = pd.to_datetime(employee['JoiningDate'])

current_year = datetime.now().year
employee['TenureInYears'] = current_year - employee['JoiningDate'].dt.year

print("\nEmployee data with TenureInYears:")
print(employee)