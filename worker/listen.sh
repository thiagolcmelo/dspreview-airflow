#!/bin/bash
# this script is used for running the dspreview deamon
# unfortunately it is incompatible with airflow

# ACTIVATE ENV
source /home/airflow/worker/worker-env3/bin/activate

# OPERATE
dspreview operate
