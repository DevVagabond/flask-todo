from flask import Response
import jsonpickle
from .message import APIResponseMessage


class ResponseHandler:
    @staticmethod
    def create_response(data, message=APIResponseMessage.SUCCESS, headers=None):
        """
        :param data: data to be returned
        :param status_code: status code of response
        :param headers: headers of response
        :return: flask response object
        """
        response_dict = message.__dict__.get('_value_')
        responseData = {
            'statusCode': response_dict['status_code'],
            'message': response_dict['message'],
            'response': data,
        }
        response = Response(jsonpickle.encode(
            responseData), status=response_dict['status_code'], mimetype='application/json')
        if headers is not None:
            response.headers.extend(headers)
        return response
