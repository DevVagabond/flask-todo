from ..models.task_model import TaskModel, StatusEnum
from flask import Response
from typing import List
import jsonpickle
from ..utils.response.message import APIResponseMessage
from ..utils.response.response_handler import ResponseHandler
from ..utils.error.error_handler import ErrorHandler
from ..utils.error.errors import APIError

TASKS: List[TaskModel] = []


class TaskController:
    def __init__(self, task_model) -> None:
        self.task_model = task_model

    def create_task(taskId, title, description, status):
        try:
            status = status if status else StatusEnum.PENDING
            new_task = TaskModel(taskId=taskId, title=title,
                                 description=description, status=status)
            TASKS.append(new_task)
            new_task_dict = new_task.__dict__

            response = {
                'taskId': new_task_dict['taskId'],
                'title': new_task_dict['title'],
                'description': new_task_dict['description'],
            }

            return ResponseHandler.create_response(response, APIResponseMessage.SUCCESS)

        except Exception as e:
            return ErrorHandler.handle_error(error=APIError.BAD_REQUEST, message=str(e))

    def get_all_tasks():
        task_list = [task.__dict__ for task in TASKS]
        return ResponseHandler.create_response(task_list, APIResponseMessage.SUCCESS)

    def get_task_by_id(taskId):
        try:
            tasks = [task for task in TASKS if task.taskId == taskId]

            if tasks:
                task = tasks.__getitem__(0).__dict__
                response = {
                    'taskId': task['taskId'],
                    'title': task['title'],
                    'description': task['description'],
                }
                return ResponseHandler.create_response(response, APIResponseMessage.SUCCESS)
            else:
                return ErrorHandler.handle_error(error=APIError.NOT_FOUND, message=f'Task with taskId "{taskId}" not found')
        except Exception as e:
            return ErrorHandler.handle_error(error=APIError.BAD_REQUEST, message=str(e))
