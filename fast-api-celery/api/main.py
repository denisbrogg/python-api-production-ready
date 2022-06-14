from fastapi import FastAPI
from worker.tasks import add

app = FastAPI()

@app.get("/home")
def index():
    res = add.apply_async((5, 2, 2), queue='test')
    return {f"message": f"Hello World --> {str(res.id)}"}
