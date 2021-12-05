from flask_restful import Resource
from ..controllers.task_controller import TaskController
from flask import request
import uuid


class TaskResource(Resource):
    def get(self):
        page = request.args.get('page') if request.args.get('page') else 1
        per_page = request.args.get(
            'per_page') if request.args.get('per_page') else 5

        return TaskController.get_all_tasks({
            'page': int(page),
            'per_page': int(per_page)
        })

    def post(self):
        json_data = request.get_json(force=True)
        self.title = json_data['title']
        self.description = json_data['description']
        self.status = json_data['status']
        self.task_id = str(uuid.uuid4())
        return TaskController.create_task(self.task_id, self.title, self.description, self.status)


class GetTaskById(Resource):
    def get(self, taskId):
        return TaskController.get_task_by_id(taskId)
