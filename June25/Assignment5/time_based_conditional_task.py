from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime
import pendulum

def check_time():
    now = pendulum.now()
    weekday = now.weekday()
    hour = now.hour

    if weekday >= 5: return "skip_task"
    if 6 <= hour < 12: return "task_a"
    if 12 <= hour < 18: return "task_b"
    return "skip_task"

def task_a():
    print("Running task A: Morning task")

def task_b():
    print("Running task B: Afternoon task")

def cleanup_task():
    print("Cleaning the tasks")

def skip_task():
    print("Weekend dags skipped")

with DAG(
    dag_id ="time_based_conditional_tasks",
    start_date = datetime(2025, 6, 25),
    schedule_interval = "0 * * * *",  # Runs every hour
    catchup = False,
    tags = ["assignment5"]
) as dag:

    decide_task = BranchPythonOperator(
        task_id = "decide_task",
        python_callable = check_time
    )

    task_a_op = PythonOperator(
        task_id ="task_a",
        python_callable = task_a
    )

    task_b_op = PythonOperator(
        task_id="task_b",
        python_callable=task_b
    )

    skip_op = PythonOperator(
        task_id = "skip_task",
        python_callable = skip_task
    )

    cleanup_op = PythonOperator(
        task_id = "cleanup_task",
        python_callable = cleanup_task,
        trigger_rule = TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS, # Cleaning the runs
    )

    decide_task >> [task_a_op, task_b_op, skip_op] >> cleanup_op
