from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def child_task(**kwargs):
    dag_run = kwargs.get('dag_run')
    conf = dag_run.conf if dag_run else {}
    trigger_date = conf.get('trigger_date', 'No trigger_date found')
    print(f"Child DAG executed")
    print(f"\n Trigger date from parent: {trigger_date}")

with DAG(
    dag_id="child_dag",
    start_date=datetime(2025, 6, 25),
    schedule_interval=None,
    catchup=False,
    tags=["assignment3"],
) as dag:

    run_child = PythonOperator(
        task_id="child_task",
        python_callable=child_task,
        provide_context=True, 
    )
