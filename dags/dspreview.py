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
          schedule_interval="@hourly", dagrun_timeout=timedelta(minutes=3))

dcm_task = BashOperator(task_id='update_dspreview_dcm',
               bash_command='/home/airflow/worker/update.sh "dcm" ',
               dag=dag)

dbm_task = BashOperator(task_id='update_dspreview_dbm',
               bash_command='/home/airflow/worker/update.sh "dsp.dbm" ',
               dag=dag)

mediamath_task = BashOperator(task_id='update_dspreview_mediamath',
               bash_command='/home/airflow/worker/update.sh "dsp.mediamath" ',
               dag=dag)


report_task = BashOperator(task_id='update_dspreview_report',
               bash_command='/home/airflow/worker/update.sh "report" ',
               dag=dag)

# in this case, it will work because there will be a single worker
# that handle tasks sequentially, we need to figure out a way to truly
# grantee that these tasks succeeded prior to generating the report
# it would allow us to work in a more distributed manner, but for now
# it will work
report_task.set_upstream(dcm_task)
report_task.set_upstream(dbm_task)
report_task.set_upstream(mediamath_task)
