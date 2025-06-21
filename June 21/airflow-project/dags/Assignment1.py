from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import os
import pandas as pd
import logging

DATA_FILE = '/opt/airflow/dags/data/customers.csv'
row_count_holder = {'count': 0}

def check_file_exists():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"{DATA_FILE} does not exist")

def count_csv_rows():
    df = pd.read_csv(DATA_FILE)
    row_count_holder['count'] = len(df)
    logging.info(f"Row count: {row_count_holder['count']}")

def should_send_message():
    return row_count_holder['count'] > 100

with DAG(
    dag_id='assignment1',
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False
) as dag:

    check_file = PythonOperator(
        task_id='check_file_exists',
        python_callable=check_file_exists
    )

    count_rows = PythonOperator(
        task_id='count_csv_rows',
        python_callable=count_csv_rows
    )

    send_message = BashOperator(
        task_id='send_message',
        bash_command='echo "Row count is greater than 100!"',
        trigger_rule='all_done'
    )

    check_file >> count_rows >> send_message
