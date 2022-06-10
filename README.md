# FastAPI Boilerplate

Starting point for every python project that includes an API with FastAPI. Inspired by [this article](https://testdriven.io/blog/fastapi-and-celery/).

## Objective

The objective of this repo is to host a forkable micro-service base for a python API made with all the best practices, ready to go into production.

## Structure

- Nginx as reverse proxy / load balancer
- FastAPI as web app
- RabbitMQ as Job Broker
- Celery as Job Worker
- Redis as Results Cache
