from celery import Celery

# worker = Celery("proj", broker="amqp://", backend="redis://", include=["worker.tasks"])
worker = Celery("proj", include=["worker.tasks"])

# Optional configuration, see the application user guide.
worker.conf.update(
    result_expires=3600,
)

if __name__ == "__main__":
    worker.start()