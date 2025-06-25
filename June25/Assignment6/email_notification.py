from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.email import send_email
from airflow.models import Variable
from datetime import datetime, timedelta
import logging

def task_1():
    total = sum(range(1, 11))
    print(f"The sum of numbers 1 to 10 is: {total}")
    print("\n Task 1 executed")


def task_2():
    total = sum(range(11, 21))
    print(f"The sum of numbers 11 to 20 is: {total}")
    print("\n Task 2 executed")


def send_success_email(**context):
    to_mail = Variable.get("to_mail", default_var="ashwinharishp@gmail.com")
    subject = "Airflow DAG success notification"
    html_content = f"All tasks completed successfully: {context['dag'].dag_id}"
    send_email(to=to_mail, subject=subject, html_content=html_content)

def send_failure_mail(context):
    to_mail = Variable.get("to_mail", default_var="ashwinharishp@gmail.com")
    task_id = context.get('task_instance').task_id
    dag_id = context.get('dag').dag_id
    execution_date = context.get('execution_date')
    
    subject = f"Airflow Task Failure notification: {dag_id} : {task_id}"
    body = f"Task {task_id} in DAG {dag_id} failed on: {execution_date}."
    
    logging.error(body)
    send_email(to=to_mail, subject=subject, html_content=body)


with DAG(
    dag_id = "email_notification_workflow",
    start_date = datetime(2025, 6, 25),
    schedule_interval = None,
    catchup = False,
    default_args = 
    {
        'retry_delay': timedelta(minutes=1),
        'retries': 3,
    },
    tags = ["assignment6"]
) as dag:

    task1 = PythonOperator(
        task_id = "task_1",
        python_callable = task_1,
        on_failure_callback = send_failure_mail
    )

    task2 = PythonOperator(
        task_id = "task_2",
        python_callable = task_2,
        on_failure_callback = send_failure_mail
    )

    success_email = PythonOperator(
        task_id="send_success_email",
        python_callable = send_success_email,
        trigger_rule = 'all_success',
    )

    task1 >> task2 >> success_email