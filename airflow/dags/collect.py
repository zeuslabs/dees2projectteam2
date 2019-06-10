"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 6, 9),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('collect', default_args=default_args, schedule_interval=timedelta(seconds=60))

cmd = '''
cd ~/workspace/dees2projectteam2/
sh ./bin/collect.sh
'''
t1 = BashOperator(
     task_id='print_date',
     bash_command='date',
     dag=dag)

t2 = BashOperator(
     task_id='collect_task',
     bash_command=cmd,
     dag=dag)

t1.set_downstream(t2)



