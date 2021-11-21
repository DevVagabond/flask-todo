import enum


class APIResponseMessage(enum.Enum):
    SUCCESS = {
        'status_code': 200,
        'message': 'Success'
    }
    CREATED = {
        'status_code': 201,
        'message': 'Created'
    }
    DELETED = {
        'status_code': 204,
        'message': 'Deleted'
    }
    UPDATED = {
        'status_code': 200,
        'message': 'Updated'
    }
