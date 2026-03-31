
from airflow.decorators import task, dag
from datetime import datetime

@dag(
    dag_id = "my_first_dag",
    start_date = datetime(2024, 6, 1),
    schedule = "@daily",
    catchup = False
)
def my_first_dag():
    @task()
    def task_1():
        print("This is task 1")
    @task()
    def task2():
        print("this is task 2")
    t1 = task_1()
    t2 = task2()
    t1 >> t2
   
my_first_dag()

