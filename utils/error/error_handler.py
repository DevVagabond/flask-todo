from typing import Literal
from flask import Response
import jsonpickle

from .errors import APIError


class ErrorHandler:
    @staticmethod
    def handle_custom_error(error: APIError):
        response = Response(
            mimetype="application/json",
            response=jsonpickle.encode(error.to_dict()),
            status=error.status_code
        )
        return response

    @staticmethod
    def handle_generic_error(error: Exception):
        response = Response(
            mimetype="application/json",
            response=jsonpickle.encode(error.args),
            status=500
        )
        return response

    @staticmethod
    def handle_error(error: Literal, message=None):
        error_dict = error.__dict__.get('_value_')
        errorMessage = {
            'error': error_dict['message'],
            'message': message
        }
        response = Response(
            jsonpickle.encode(errorMessage),
            mimetype="application/json",
            status=error_dict['status_code']
        )
        return response
