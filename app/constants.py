BAD_REQUEST = 400
NOT_FOUND = 404
INTERNAL_SERVER_ERROR = 500

QUESTION_MAX = 200
QUESTION_MISSING = "The 'question' parameter is required."
QUESTION_TOO_LONG = (
    "Exceeded maximum 'question' length ({max_length} characters)."
).format(max_length=QUESTION_MAX)
