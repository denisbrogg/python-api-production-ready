from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult

from worker.tasks import predict
from .models import ModelInput, TaskTicket, ModelPrediction

app = FastAPI()

@app.post('/fakemodel/predict', response_model=TaskTicket, status_code=202)
async def schedule_prediction(model_input: ModelInput):
    """Create celery prediction task. Return task_id to client in order to retrieve result"""
    task_id = predict.delay(dict(model_input).get("x"))
    return {'task_id': str(task_id), 'status': 'Processing'}


@app.get('/fakemodel/result/{task_id}', response_model=ModelPrediction, status_code=200,
         responses={202: {'model': TaskTicket, 'description': 'Accepted: Not Ready'}})
async def get_prediction_result(task_id):
    """Fetch result for given task_id"""
    task = AsyncResult(task_id)
    if not task.ready():
        print(app.url_path_for('schedule_prediction'))
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})
    result = task.get()
    return {'task_id': task_id, 'status': 'Success', 'result': str(result)}