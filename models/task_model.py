import json


class TaskModel:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.status = 'pending'

    def __to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }

    def to_json(self):
        return json.dumps(self.__to_dict())
