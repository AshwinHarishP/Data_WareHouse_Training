from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago
import os
import pandas as pd

INPUT_FOLDER = '/opt/airflow/dags/data/input'
OUTPUT_FOLDER = '/opt/airflow/dags/data/output'
EXPECTED_HEADERS = ['customer_id', 'first_name', 'last_name', 'email']

with DAG(
    dag_id='Assignment5',
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
    tags=["assignment5"]
) as dag:

    @task
    def list_csv_files():
        return [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.csv')]

    @task
    def process_file(file_name: str):
        file_path = os.path.join(INPUT_FOLDER, file_name)
        df = pd.read_csv(file_path)

        if not all(col in df.columns for col in EXPECTED_HEADERS):
            raise ValueError(f"{file_name} has invalid headers.")

        row_count = len(df)
        summary = {
            'file': file_name,
            'row_count': row_count
        }
        
        summary_path = os.path.join(OUTPUT_FOLDER, f"{file_name}_summary.csv")
        pd.DataFrame([summary]).to_csv(summary_path, index=False)

        return summary_path

    @task
    def merge_summaries(summary_paths: list):
        all_summaries = pd.concat([pd.read_csv(p) for p in summary_paths])
        merged_path = os.path.join(OUTPUT_FOLDER, 'merged_summary.csv')
        all_summaries.to_csv(merged_path, index=False)

    files = list_csv_files()
    summaries = process_file.expand(file_name=files)
    merge_summaries(summaries)
