from ..models.task_model import TaskModel
from flask import Response
from typing import List
import jsonpickle

TASKS: List[TaskModel] = []


class TaskController:
    def __init__(self, task_model) -> None:
        self.task_model = task_model

    def create_task(id, title, description, status):
        new_task = TaskModel(id, title, description, status)
        TASKS.append(new_task)
        return Response(new_task.to_json(), status=200, mimetype='application/json')

    def get_all_tasks():
        return Response(jsonpickle.encode(TASKS), status=200, mimetype='application/json')

    def get_task_by_id(id):
        for task in TASKS:
            if task.id == id:
                return task
        return None
