#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

dag_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 8, 25, 0, 0, 0),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    #    'queue': 'rawToSQL'
}

dag = DAG('dspreview', default_args=dag_args,
          schedule_interval=timedelta(minutes=30), dagrun_timeout=timedelta(minutes=3))

run_dcm_task = BashOperator(task_id='update_dspreview',
               bash_command='/home/airflow/worker/update.sh ',
               dag=dag)
