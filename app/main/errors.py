from flask import jsonify, render_template, request

from app.constants import INTERNAL_SERVER_ERROR, NOT_FOUND

from . import main


def returns_json(request):
    return (
        request.accept_mimetypes.accept_json
        and not request.accept_mimetypes.accept_html
        or request.path.startswith("/api/")
    )


@main.app_errorhandler(NOT_FOUND)
def not_found(e):
    if returns_json(request):
        response = jsonify({"error": "Not Found"})
        response.status_code = NOT_FOUND
        return response
    print(request.path)
    return render_template("404.jinja2"), NOT_FOUND


@main.app_errorhandler(INTERNAL_SERVER_ERROR)
def internal_server_error(e):
    if returns_json(request):
        response = jsonify({"error": "Internal Server Error"})
        response.status_code = INTERNAL_SERVER_ERROR
        return response
    return render_template("500.jinja2"), INTERNAL_SERVER_ERROR
