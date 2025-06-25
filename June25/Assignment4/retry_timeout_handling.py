from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time
import logging

# Function for long running work
def long_running_work():
    logging.info("Starting long-running work")
    time.sleep(30)
    logging.info("Long-running work completed successfully")

with DAG(
    dag_id = "retry_timeout_handling",
    start_date = datetime(2025, 6, 25),
    schedule_interval = None,
    catchup = False,
    default_args =
    {
        'retries': 3,                            
        'retry_delay': timedelta(seconds=10),  
        'retry_exponential_backoff': True,     
        'max_retry_delay': timedelta(minutes=2) 
    },
    tags = ["assignment4"]

) as dag:

    task = PythonOperator(
        task_id = "long_running_work",
        python_callable = long_running_work,
        execution_timeout = timedelta(seconds=50) 
    )
