from flask import render_template

from app.constants import QUESTION_MAX

from . import main


@main.route("/")
def index():
    return render_template("index.jinja2", question_max=QUESTION_MAX)


@main.route("/docs")
def api_docs():
    return render_template("api_docs.jinja2")
