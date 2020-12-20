from flask import jsonify

from app.constants import BAD_REQUEST
from app.exceptions import ValidationError

from . import api


def bad_request(message):
    response = jsonify(
        {
            "error": "Bad Request",
            "message": message,
        }
    )
    response.status_code = BAD_REQUEST
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
