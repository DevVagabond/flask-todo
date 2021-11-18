from ..models.task_model import TaskModel
from flask import jsonify, Response
from typing import List

TASKS: List[TaskModel] = []


class TaskController:
    def __init__(self, task_model) -> None:
        self.task_model = task_model

    def create_task(self, id, title, description):
        new_task = TaskModel(id, title, description)
        TASKS.append(new_task)
        return Response(new_task.to_json(), status=200, mimetype='application/json')

    def get_all_tasks():
        return TASKS

    def get_task_by_id(id):
        for task in TASKS:
            if task.id == id:
                return task
        return None
