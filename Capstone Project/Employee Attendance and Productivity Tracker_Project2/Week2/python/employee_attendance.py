import pandas as pd
import numpy as np
from datetime import datetime

"""
    Loading data from CSV file
"""
attendance_df = pd.read_csv("attendance.csv")
task_df = pd.read_csv("tasks.csv")

"""
    Clean missing or invalid entries
"""
# 1. Converting to correct date format
attendance_df['clock_in'] = pd.to_datetime(attendance_df['clock_in'])
attendance_df['clock_out'] = pd.to_datetime(attendance_df['clock_out'])
attendance_df['break_start'] = pd.to_datetime(attendance_df['break_start'])
attendance_df['break_end'] = pd.to_datetime(attendance_df['break_end'])

# 2. Removing missing values
attendance_df.dropna(inplace=True)
task_df.dropna(inplace=True)

"""
    Calculations
"""
# 1. Calculating break duration
attendance_df['break_duration'] = (attendance_df['break_end'] - attendance_df['break_start']).dt.total_seconds()

# 2. Calculating total work hours
attendance_df['work_duration'] = (attendance_df['clock_out'] - attendance_df['clock_in']).dt.total_seconds()
attendance_df['total_work_hours'] = (attendance_df['work_duration'] - attendance_df['break_duration']) / 3600

# 3. Counting tasks completed
task_df['task_date'] = pd.to_datetime(task_df['task_date']).dt.date.astype(str)
attendance_df['date'] = attendance_df['clock_in'].dt.date.astype(str)
tasks_per_day = task_df.groupby(['employee_id', 'task_date']).size().reset_index(name='tasks_completed_count')


merged_df = pd.merge(attendance_df, tasks_per_day,left_on=['employee_id', 'date'],right_on=['employee_id', 'task_date'],how='left')
# Cleaning the null records
merged_df['tasks_completed_count'] = merged_df['tasks_completed_count'].fillna(0)

# 4. Calculating productivity score
merged_df['productivity_score'] = merged_df['tasks_completed_count'] / merged_df['total_work_hours']

"""
    Summary
"""

summary = merged_df.groupby('employee_id')[['total_work_hours', 'productivity_score']].mean().reset_index()

print("summary")
print(summary)

# Top Performers and Bottom Performers
top_performers = summary.sort_values(by='productivity_score', ascending=False).head(5)
bottom_performers = summary.sort_values(by='productivity_score').head(5)

# Absentees and frequent absentees count
attendance_counts = attendance_df.groupby('employee_id').size().reset_index(name='days_present')
frequent_absentees = attendance_counts.sort_values(by='days_present').head(5)

"""
    Storing the summary in csv file
"""
summary.to_csv("summary.csv", index=True)
print("Summary exported to summary.csv")

"""
    Displaying the summary
"""

print("\nTop Performers:")
print(top_performers)

print("\nBottom Performers:")
print(bottom_performers)

print("\nFrequent Absentees:")
print(frequent_absentees)


