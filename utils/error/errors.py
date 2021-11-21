import enum


class APIError(enum.Enum):
    BAD_REQUEST = {
        'status_code': 400,
        'message': 'Bad Request'
    }
    UNAUTHORIZED = {
        'status_code': 401,
        'message': 'Unauthorized'
    }
    FORBIDDEN = {
        'status_code': 403,
        'message': 'Forbidden'
    }
    NOT_FOUND = {
        'status_code': 404,
        'message': 'Not Found'
    }
    METHOD_NOT_ALLOWED = {
        'status_code': 405,
        'message': 'Method Not Allowed'
    }
