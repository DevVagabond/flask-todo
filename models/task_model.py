import json
from pydantic import BaseModel, ValidationError, validator


class TaskModel(BaseModel):
    taskId: int
    title: str
    description: str
    status: str
