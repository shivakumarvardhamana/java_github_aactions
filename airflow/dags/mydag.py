from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# function to run
def hello_world():
    print("Hello World from Airflow!")

# define DAG
with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",   # ✅ new parameter
    catchup=False,
    tags=["example"]
) as dag:

    task1 = PythonOperator(
        task_id="hello_task",
        python_callable=hello_world
    )

    task1
