from .celery import worker
import time

@worker.task(name="add")
def add(t, x, y):
    time.sleep(t)
    return x + y
