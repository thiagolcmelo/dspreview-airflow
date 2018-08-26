#!/bin/bash
# this script is used for running the dspreview commands
# unfortunately it is incompatible with airflow

# ACTIVATE ENV
source /home/airflow/worker/worker-env3/bin/activate

# POKE DCM
dspreview --poke "dcm"

# SLEEP 10 seconds
sleep 10

# POKE DSP DBM
dspreview --poke "dsp.dbm"

# SLEEP 10 seconds
sleep 10

# POKE DSP MEDIAMATH
dspreview --poke "dsp.mediamath"

# SLEEP 10 seconds
sleep 10

# GENERATE REPORT
dspreview --poke "report"

echo "done"
