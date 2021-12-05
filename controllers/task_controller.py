from ..models.task_model import StatusEnum
from ..utils.response.message import APIResponseMessage
from ..utils.response.response_handler import ResponseHandler
from ..utils.error.error_handler import ErrorHandler
from ..utils.error.errors import APIError
from ..db.__init__ import getDbModels


class TaskController:
    def __init__(self, task_model) -> None:
        self.task_model = task_model

    def create_task(taskId, title, description, status):
        try:
            status = status if status else StatusEnum.PENDING
            Models = getDbModels()
            new_task = Models["TaskModel"](uuid=taskId, title=title,
                                           description=description, status=status)

            Models["DB"].session.add(new_task)
            Models["DB"].session.commit()

            response = {
                'id': new_task.id,
                'uuid': new_task.uuid,
                'title': new_task.title,
                'description': new_task.description,
            }

            return ResponseHandler.create_response(response, APIResponseMessage.SUCCESS)

        except Exception as e:
            return ErrorHandler.handle_error(error=APIError.BAD_REQUEST, message=str(e))

    def get_all_tasks(params):
        try:
            Models = getDbModels()
            taskObject = Models["TaskModel"].query.paginate(
                page=params.get("page"), per_page=params.get("per_page"), error_out=False)
            total = taskObject.total
            tasks = taskObject.items
            taskList = []
            for task in tasks:
                taskList.append({
                    'id': task.id,
                    'uuid': task.uuid,
                    'title': task.title,
                    'description': task.description,
                    'status': task.status
                })
            response = {
                'total': total,
                'page': params["page"],
                'per_page': params["per_page"],
                'tasks': taskList
            }
            return ResponseHandler.create_response(response, APIResponseMessage.SUCCESS)
        except Exception as e:
            return ErrorHandler.handle_error(error=APIError.BAD_REQUEST, message=str(e))

    def get_task_by_id(taskId):
        try:
            Models = getDbModels()
            task = Models["TaskModel"].query.get(taskId)

            if (task is None):
                return ErrorHandler.handle_error(error=APIError.NOT_FOUND, message=f"Task with id {taskId} not found")

            response = {
                'id': task.id,
                'uuid': task.uuid,
                'title': task.title,
                'description': task.description,
                'status': task.status
            }
            return ResponseHandler.create_response(response, APIResponseMessage.SUCCESS)
        except Exception as e:
            return ErrorHandler.handle_error(error=APIError.BAD_REQUEST, message=str(e))
