from pydantic import BaseModel

class ModelInput(BaseModel):
    """Model features as input for prediction"""
    x: float

class TaskTicket(BaseModel):
    """ID and status for the async tasks"""
    task_id: str
    status: str

class ModelPrediction(BaseModel):
    """Final result"""
    task_id: str
    status: str
    result: float