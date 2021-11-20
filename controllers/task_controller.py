from ..models.task_model import TaskModel
from flask import Response
from typing import List
import jsonpickle

TASKS: List[TaskModel] = []


class TaskController:
    def __init__(self, task_model) -> None:
        self.task_model = task_model

    def create_task(taskId, title, description, status):
        new_task = TaskModel(taskId=taskId, title=title,
                             description=description, status=status)
        TASKS.append(new_task)
        new_task_dict = new_task.__dict__

        response = {
            'taskId': new_task_dict['taskId'],
            'title': new_task_dict['title'],
            'description': new_task_dict['description'],
        }
        return Response(jsonpickle.encode(response), status=200, mimetype='application/json')

    def get_all_tasks():
        task_list = [task.__dict__ for task in TASKS]
        return Response(jsonpickle.encode(task_list), status=200, mimetype='application/json')

    def get_task_by_id(taskId):
        tasks = [task for task in TASKS if int(task.taskId) == int(taskId)]

        if tasks:
            task = tasks.__getitem__(0).__dict__
            response = {
                'taskId': task['taskId'],
                'title': task['title'],
                'description': task['description'],
            }
        else:
            response = {
                'message': 'Task not found'
            }
        return Response(jsonpickle.encode(response), status=404, mimetype='application/json')
