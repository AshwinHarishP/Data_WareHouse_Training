from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
import os
import shutil
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': 60,  
}

DATA_DIR = '/opt/airflow/dags/data'
ARCHIVE_DIR = '/opt/airflow/dags/archive'

def read_and_process_sales(**kwargs):
    filepath = os.path.join(DATA_DIR, 'sales.csv')
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} does not exist!")

    df = pd.read_csv(filepath)
    summary = df.groupby('category')['amount'].sum().reset_index()
    summary_file = os.path.join(DATA_DIR, 'sales_summary.csv')
    summary.to_csv(summary_file, index=False)

def archive_original_file(**kwargs):
    src = os.path.join(DATA_DIR, 'sales.csv')
    if not os.path.exists(src):
        raise FileNotFoundError("sales.csv not found for archiving!")

    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(ARCHIVE_DIR, f"sales_{timestamp}.csv")
    shutil.move(src, dest)

with DAG(
    dag_id='Assignment2',
    default_args=default_args,
    description='Daily sales summarization and archival',
    schedule_interval='0 6 * * *', #Runs the DAG every day at 6:00 AM.
    start_date=days_ago(1),
    catchup=False,
    max_active_runs=1
) as dag:

    process_sales = PythonOperator(
        task_id='process_sales',
        python_callable=read_and_process_sales,
    )

    archive_sales = PythonOperator(
        task_id='archive_sales',
        python_callable=archive_original_file,
    )

    process_sales >> archive_sales