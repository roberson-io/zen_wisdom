from flask import Blueprint

main = Blueprint("main", __name__)

from app.main import errors, views  # noqa: F401, E402
