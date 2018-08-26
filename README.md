# Airflow + dspreview (Python 3.5)

This repository contains DAGs and Bash scripts for operating the [`dspreview`](https://github.com/thiagolcmelo/dspreview) tool under Airflow. It must be cloned such that it becomes the `$AIRFLOW_HOME` folder.

In the root is a `airflow.cfg` file, with the necessary configuration for flying Airflow.

Besides the environment variables specified in the [tool's page](https://github.com/thiagolcmelo/dspreview), it is also necessary to specify:

- `AIRFLOW__CORE__SQL_ALCHEMY_CONN` the connection string for the Airflow database
- `AIRFLOW__CELERY__BROKER_URL` the connection string for the RabbitMQ used by Celery
- `AIRFLOW__CELERY__CELERY_RESULT_BACKEND` the connection string for the database used by Celery

```bash
$ export AIRFLOW__CORE__SQL_ALCHEMY_CONN="mysql://db_user:db_pass@db_host:3306/db_name"
$ export AIRFLOW__CELERY__BROKER_URL="amqp://mq_user:mq_pass@mq_host:5672/mq_vhost"
$ export AIRFLOW__CELERY__CELERY_RESULT_BACKEND="db+mysql://db_user:db_pass@db_host:3306/db_name"
```

The `requirements_airflow.txt` provides necessary packages for achieving a stable configuration for Airflow.

```bash
$ virtualenv -p python3 airflow-env3
$ source airflow-env3/bin/activate
$ pip install -r requirements_airflow.txt
```

The files under `worker` are used for using the `dspreview` tool. The file `requirements_worker.txt` provides necessary packages for using the worker:

```bash
$ cd worker
$ virtualenv -p python3 worker-env3
$ source worker-env3/bin/activate
$ pip install -r requirements_worker.txt
```

## Start Airflow

Although it would be better to properly set systemd configuration, the Airflow can be execute through:

```bash
$ cd $AIRFLOW_HOME
$ mkdir logs
$ nohup airflow webserver >> logs/webserver.logs &
$ nohup airflow scheduler >> logs/scheduler.logs &
```

The default port in `airflow.cfg` is `9512`.

## `dspreview` operation

Therer three Bash scripts inside `worker`.

- `serve.sh` that lauches a web server where it is possible to configure classifications, as well as watch the DSP report.
- `update.sh` this is called by the DAGs for inserting items in queues to be consumed by the workers
- `listen.sh` this is the actual worker which runs in a loop listening to a queue and taking care of the ETL process.

It can also be executed through:

```bash
$ cd $AIRFLOW_HOME
$ mkdir logs
$ nohup listen.sh >> logs/worker.logs &
$ nohub serve.sh >> logs/server.logs &
```
