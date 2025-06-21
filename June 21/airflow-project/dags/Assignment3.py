from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.exceptions import AirflowFailException
import random
import logging
from datetime import timedelta

def flaky_task():
    if random.random() < 0.5:
        raise AirflowFailException("Random failure occurred.")
    logging.info("API call succeeded!")

def success_only_task():
    logging.info("This runs only if the API succeeded.")

def alert_on_failure(context):
    logging.error("API failed after retries. Sending alert...")

default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(seconds=10),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='Assignment3',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False
) as dag:

    api_call = PythonOperator(
        task_id='flaky_api_call',
        python_callable=flaky_task,
        on_failure_callback=alert_on_failure
    )

    alert_task = BashOperator(
        task_id='alert_task',
        bash_command='echo "Final failure after retries"',
        trigger_rule='one_failed'
    )

    success_task = PythonOperator(
        task_id='success_task',
        python_callable=success_only_task,
        trigger_rule='all_success'
    )

    api_call >> [alert_task, success_task]
