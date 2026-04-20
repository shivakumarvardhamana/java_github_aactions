from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def start_task():
    print("Starting the workflow...")

def process_task():
    print("Processing data...")

def end_task():
    print("Workflow completed successfully!")

with DAG(
    dag_id="simple_test_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["test"]
) as dag:

    start = PythonOperator(
        task_id="start",
        python_callable=start_task
    )

    process = PythonOperator(
        task_id="process",
        python_callable=process_task
    )

    end = PythonOperator(
        task_id="end",
        python_callable=end_task
    )

    # Define task flow
    start >> process >> end
