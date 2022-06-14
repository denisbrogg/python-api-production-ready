#!/bin/bash

while [ $# -gt 0 ] ; do
  case $1 in
    -w | --which) W="$2" ;;
  esac
  shift
done

case $W in
    worker) celery --broker ${CELERY_BROKER_URL} --result-backend ${CELERY_BACKEND_URL} -A worker.celery worker --loglevel=INFO --queues ${CELERY_QUEUE};;
    flower) celery --broker ${CELERY_BROKER_URL} --result-backend ${CELERY_BACKEND_URL} -A worker.celery flower;;
    fastapi) uvicorn api.main:app --host 0.0.0.0 --port 80;;
esac
