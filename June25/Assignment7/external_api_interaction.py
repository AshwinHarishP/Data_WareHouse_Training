from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.http_sensor import HttpSensor
from datetime import datetime, timedelta
import json
import logging

DEST_FILE = '/opt/airflow/dags/data/incoming/weather.txt'

# XCom to pull the data 
def parse_response(**context):
    response_text = context['ti'].xcom_pull(task_ids='get_weather_data')
    parse_and_log_data(response_text)

# Reading the API data
def parse_and_log_data(response_text):
    data = json.loads(response_text)
    temperature = data['current']['temperature_2m']
    windspeed = data['current']['windspeed_10m']
    timestamp = data['current']['time']

    logging.info(f"Temperature (°C): {temperature}")
    logging.info(f"Windspeed (km/h): {windspeed}")
    logging.info(f"Timestamp: {timestamp}")

    with open(DEST_FILE, 'a') as f:
        f.write(f"Temp: {temperature}°C, Wind: {windspeed}km/h, Time: {timestamp}\n\n")

# Failing if status is not 200 
def check_status(response):
    if response.status_code != 200:
        raise ValueError(f"API returned status code {response.status_code}")
    return True

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='external_api_weather_interaction',
    start_date=datetime(2025, 6, 25),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    tags=['assignment7']
) as dag:

    # Check if API is available
    check_api_available = HttpSensor(
        task_id='check_api_available',
        http_conn_id='weather_api',  # Set this connection in Airflow UI
        endpoint='v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,windspeed_10m',
        poke_interval=5,
        timeout=20
    )

    # Calling the API with response check
    get_weather_data = SimpleHttpOperator(
        task_id='get_weather_data',
        http_conn_id='weather_api',
        endpoint='v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,windspeed_10m',
        method='GET',
        response_filter=lambda response: response.text,
        response_check=check_status,
        log_response=True
    )

    # Parse weather data
    parse_response_task = PythonOperator(
        task_id='parse_response',
        python_callable=parse_response,
        provide_context=True
    )

    # Define task execution order
    check_api_available >> get_weather_data >> parse_response_task
