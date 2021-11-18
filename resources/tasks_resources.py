from flask_restful import Resource
from ..controllers.task_controller import TaskController
from flask import request


class TaskResource(Resource):
    def get(self):
        return TaskController.get_all_tasks()

    def post(self):
        json_data = request.get_json(force=True)
        self.title = json_data['title']
        self.description = json_data['description']
        self.status = json_data['status'] if json_data['status'] else 'pending'
        return TaskController.create_task(1, self.title, self.description, self.status)
