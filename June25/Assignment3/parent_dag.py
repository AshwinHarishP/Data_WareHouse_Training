from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

def parent_task():
    print("Parent dag executed")

with DAG(
    dag_id="parent_dag",
    start_date=datetime(2025, 6, 25),
    schedule_interval=None,
    catchup=False,
    tags=["assignment3"]
) as parent:

    task1 = PythonOperator(
        task_id="parent_task",
        python_callable=parent_task
    )

    trigger_child = TriggerDagRunOperator(
        task_id="trigger_child_dag",
        trigger_dag_id="child_dag",
        conf={"trigger_date": "{{ ds }}"},  # Pass execution date to child
        wait_for_completion=True,
        reset_dag_run=True,
        poke_interval=10,
    )

    task1 >> trigger_child
