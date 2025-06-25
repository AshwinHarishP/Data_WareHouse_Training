from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta
import shutil
import os
import csv

INPUT_PATH = "/opt/airflow/dags/data/incoming/report.csv"
ARCHIVE_DIR = "/opt/airflow/dags/data/archive/"

# Processing Report
def process_report():
    with open(INPUT_PATH, "r") as f:
        reader = csv.DictReader(f)
        print("Students with marks > 85:")
        for row in reader:
            name = row["name"]
            marks = int(row["marks"])
            if marks > 85:
                print(f"  - {name} marks {marks}")

# Creating a report in the archive directory
def archive_report():
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
    destination = os.path.join(ARCHIVE_DIR, "report.csv")
    shutil.move(INPUT_PATH, destination)
    print(f"File moved to archive: {destination}")

with DAG(
    dag_id = "file_sensor_pipeline",
    start_date = datetime(2025, 6, 25),
    schedule_interval = None,
    catchup = False,
    tags = ["assignment 1", "file_sensor"]
) as dag:

    wait_for_report = FileSensor(
        task_id = "wait_for_report_file",
        filepath = "data/incoming/report.csv",
        fs_conn_id = "fs_default",
        poke_interval = 30,
        timeout = 600,      
        soft_fail = True,    
        mode = "poke"
    )

    process_task = PythonOperator(
        task_id = "process_report_file",
        python_callable = process_report
    )

    archive_task = PythonOperator(
        task_id = "archive_report_file",
        python_callable = archive_report
    )

    wait_for_report >> process_task >> archive_task
