import pytest
import app as app_module
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Task Management API" in response.data


def test_add_todo_route(client):
    response = client.post(
        '/add',
        data={'task': 'Write Pytest Suite'},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Write Pytest Suite" in response.data


def test_toggle_todo_route(client):
    response = client.get('/toggle/1', follow_redirects=True)
    assert response.status_code == 200


def test_delete_todo_route(client):
    response = client.get('/delete/1', follow_redirects=True)
    assert response.status_code == 200
    assert not any(t['id'] == 1 for t in app_module.todos)