#!/bin/bash

poetry run nohup flask run --host=0.0.0.0 --port=5001 --debug > api.log 2>&1 &

poetry run nohup celery -A app.celery worker -P gevent -c 1 --loglevel INFO -Q dataset,generation,mail,ops_trace > celery.log 2>&1 &

poetry run nohup celery -A app.celery beat --loglevel INFO > celery-beat.log 2>&1 &


