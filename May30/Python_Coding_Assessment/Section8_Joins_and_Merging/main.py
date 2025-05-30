import pandas as pd

"""
Q20. Merge employees.csv and projects.csv EmployeeID to show project allocations.
"""
employees = pd.read_csv(r"F:\Hexaware Training\Role Based Training\Python\May30\Python_Coding_Assessment\employees.csv")
projects = pd.read_csv(r"F:\Hexaware Training\Role Based Training\Python\May30\Python_Coding_Assessment\projects.csv")

merged_result = pd.merge(employees, projects, on='EmployeeID')
print(merged_result)

"""
21. List all employees who are not working on any project (left join logic).
"""
left_join = pd.merge(employees, projects, on='EmployeeID', how='left')
no_projects = left_join[left_join['ProjectID'].isnull()]

print("\nList of employees who not working on any project:")
print(no_projects[['EmployeeID', 'Name', 'Department']])

"""
Q22. Add a derived column TotalCost = HoursAllocated * (Salary / 160) in the merged dataset.
"""

merged_result['TotalCost'] = merged_result['HoursAllocated'] * (merged_result['Salary'] / 160)
print(merged_result)