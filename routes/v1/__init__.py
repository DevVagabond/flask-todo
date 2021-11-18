from flask_restful import Api
from ...resources.tasks_resources import TaskResource

V1_PREFIX = '/api/v1'


def configure_routes(api: Api):
    api.add_resource(TaskResource, V1_PREFIX + '/tasks')
