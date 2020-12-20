# Zen Wisdom API
A simple web API demonstration written with [Flask](https://flask.palletsprojects.com) that imparts Zen wisdom via the Python [Natural Language Toolkit](https://www.nltk.org/).

## Getting Started
Create a virtualenv:
```
python3 -m venv venv
```

Activate the virtualenv:
```
. venv/bin/activate
```

Install requirements:
```
pip install -r requirements/development.txt
```
There is a smaller production requirements file that does not include packages for unit testing, linting, and other code quality checks.

Set a `FLASK_APP` environment variable to `wisdom.py`:
```
export FLASK_APP=wisdom.py
```

Run the application:
```
flask run
```

There is a page to test the API endpoint and access API documentation at [http://localhost:5000/](http://localhost:5000/).

## Example
The endpoint is `/api/zen_wisdom` and there is a required `question` parameter.

For example:
[http://localhost:5000/api/zen_wisdom?question=Who+is+the+master+who+makes+the+grass+green%3F](http://localhost:5000/api/zen_wisdom?question=Who+is+the+master+who+makes+the+grass+green%3F)

Sample response:
```json
{
  "wisdom": "You seek the truth. Does the truth seek you?"
}
```

The application returns a JSON document with an HTTP 400 status code if the `question` parameter is missing or if the value of `question` is greater than 200 characters in length. Note: if the `FLASK_DEBUG` variable is enabled, you will get a Flask debug page rather than a JSON response.
