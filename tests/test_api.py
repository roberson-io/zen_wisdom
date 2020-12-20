import pytest

from app.constants import QUESTION_MAX, QUESTION_MISSING, QUESTION_TOO_LONG


def test_wisdom_success(client):
    response = client.get("/api/zen_wisdom?question=Why%3F")
    assert response.status_code == 200
    assert response.is_json
    doc = response.get_json()
    assert doc.get("wisdom")


def test_question_missing(client):
    response = client.get("/api/zen_wisdom")
    assert response.status_code == 400
    assert response.is_json
    doc = response.get_json()
    assert not doc.get("wisdom")
    assert doc.get("message") == QUESTION_MISSING


def test_question_too_long(client):
    question = "x" * (QUESTION_MAX + 1)
    response = client.get(
        "/api/zen_wisdom?question={question}".format(question=question)
    )
    assert response.status_code == 400
    assert response.is_json
    doc = response.get_json()
    assert not doc.get("wisdom")
    assert doc.get("message") == QUESTION_TOO_LONG


def test_json_404(client):
    response = client.get("/api/not_found")
    assert response.status_code == 404
    assert response.is_json
