import pytest


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Zen Wisdom API" in response.data
    assert not response.is_json


def test_html_404(client):
    response = client.get("/not_found")
    assert response.status_code == 404
    assert not response.is_json
