from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import json
import sys

INPUT_FILE = "/opt/airflow/dags/data/orders.csv"

def validate_data(**kwargs):
    required_columns = {"order_id", "customer_id", "order_date", "amount"}
    mandatory_fields = ["order_id", "customer_id", "order_date", "amount"]

    # Reading CSV file
    try:
        df = pd.read_csv(INPUT_FILE)
    except Exception as e:
        raise Exception(f"Failed to read {INPUT_FILE}: {e}")

    #Checking required columns are present
    missing_cols = required_columns - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Step 3: Check for nulls in mandatory fields
    nulls = df[mandatory_fields].isnull().any()
    if nulls.any():
        null_cols = nulls[nulls].index.tolist()
        raise ValueError(f"Null values found in mandatory fields: {null_cols}")

    print("Data validation passed!")

    # Pushing DataFrame to XCom
    kwargs['ti'].xcom_push(key='validated_df', value=df.to_json())

def summarize_data(**kwargs):

    # Pulling data from xcom 
    json_data = kwargs['ti'].xcom_pull(key='validated_df', task_ids='validate_data')
   
    if not json_data:
        raise ValueError("No validated data found! Skipping summarization.")

    df = pd.read_json(json_data)

    # Summarization
    total_orders = len(df)
    total_amount = df['amount'].sum()

    print(f"Summary: Total Orders = {total_orders}")
    print(f"Total Amount = {total_amount}")

with DAG(
    dag_id = "data_quality_validation",
    start_date = datetime(2025, 6, 25),
    schedule_interval = None,
    catchup = False,
    tags = ["assignment2", "data_quality"]
) as dag:

    validate_task = PythonOperator(
        task_id = "validate_data",
        python_callable = validate_data,
        provide_context = True,
    )

    summarize_task = PythonOperator(
        task_id = "summarize_data",
        python_callable = summarize_data,
        provide_context = True,
    )

    validate_task >> summarize_task
