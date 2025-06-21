from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago
import os

DATA_FILE = '/opt/airflow/dags/data/inventory.csv'
SIZE_THRESHOLD = 500 * 1024  # 500 KB 

def check_file_size():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"{DATA_FILE} not found")
    size = os.path.getsize(DATA_FILE)
    if size < SIZE_THRESHOLD:
        return 'task_light_summary'
    else:
        return 'task_detailed_processing'

def light_summary():
    print("Running light summary...")

def detailed_processing():
    print("Running detailed processing...")

def cleanup():
    print("Running cleanup task...")

with DAG(
    dag_id='Assignment4',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False
) as dag:

    check_size = BranchPythonOperator(
        task_id='check_file_size',
        python_callable=check_file_size
    )

    task_light_summary = PythonOperator(
        task_id='task_light_summary',
        python_callable=light_summary
    )

    task_detailed_processing = PythonOperator(
        task_id='task_detailed_processing',
        python_callable=detailed_processing
    )

    cleanup_task = PythonOperator(
        task_id='cleanup_task',
        python_callable=cleanup,
        trigger_rule='none_failed_min_one_success'
    )

    check_size >> [task_light_summary, task_detailed_processing] >> cleanup_task
