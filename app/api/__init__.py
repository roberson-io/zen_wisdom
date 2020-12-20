from flask import Blueprint

api = Blueprint("api", __name__)

from . import errors, wisdom  # noqa: F401, E402
