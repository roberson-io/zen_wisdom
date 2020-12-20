from flask import jsonify, request
from nltk.chat.zen import zen_chatbot

from app.constants import QUESTION_MAX, QUESTION_MISSING, QUESTION_TOO_LONG
from app.exceptions import ValidationError

from . import api


@api.route("/zen_wisdom")
def impart_wisdom():
    question = request.args.get("question")
    if question is None:
        raise ValidationError(QUESTION_MISSING)
    if len(question) > QUESTION_MAX:
        raise ValidationError(QUESTION_TOO_LONG)
    return jsonify({"wisdom": zen_chatbot.respond(question)})
