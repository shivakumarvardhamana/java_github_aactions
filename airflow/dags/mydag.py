from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Function to print Hello World
def print_hello():
    print("Hello World from Airflow!")

# Define DAG
with DAG(
    dag_id='hello_world_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval='*/5 * * * *',  # Runs every 5 minutes
    catchup=False
) as dag:

    hello_task = PythonOperator(
        task_id='print_hello_task',
        python_callable=print_hello
    )

    hello_task
