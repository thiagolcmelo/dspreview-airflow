#!/bin/bash
# this script is used for running the dspreview commands
# unfortunately it is incompatible with airflow

# ACTIVATE ENV
source /home/airflow/worker/worker-env3/bin/activate

# if there is a input param
if [ $# -ge 1 ];
then
    # dspreview --poke "${1}"
    for i in $(printf "a='${1}'.split('.'); print(' '.join(a))" | python)
    do
        if [ $i == 'dcm' ]
        then
            dspreview --worker dcm
        elif [ $i == 'dbm' ]
        then
            dspreview --worker dsp --dsp dbm
        elif [ $i == 'mediamath' ]
        then
            dspreview --worker dsp --dsp mediamath
        elif [ $i == 'report' ]
        then
            dspreview --generate-report
        fi
    done
else
    # POKE DCM
    # dspreview --poke "dcm"
    dspreview --worker dcm

    # SLEEP 10 seconds
    sleep 10

    # POKE DSP DBM
    # dspreview --poke "dsp.dbm"
    dspreview --worker dsp --dsp dbm

    # SLEEP 10 seconds
    sleep 10

    # POKE DSP MEDIAMATH
    # dspreview --poke "dsp.mediamath"
    dspreview --worker dsp --dsp mediamath

    # SLEEP 10 seconds
    sleep 10

    # GENERATE REPORT
    # dspreview --poke "report"
    dspreview --generate-report

    echo "done"
fi;
