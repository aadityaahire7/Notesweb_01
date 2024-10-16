import pytest
from website import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to NotesApp' in response.data

def test_create_note(client):
    response = client.post('/notes', data={'title': 'Test Note', 'content': 'This is a test note.'})
    assert response.status_code == 201
    assert b'Test Note' in response.data

def test_read_note(client):
    response = client.get('/notes/1')  
    assert response.status_code == 200
    assert b'Test Note' in response.data

def test_update_note(client):
    response = client.put('/notes/1', data={'title': 'Updated Note', 'content': 'Updated content.'})
    assert response.status_code == 200
    assert b'Updated Note' in response.data

def test_delete_note(client):
    response = client.delete('/notes/1')  
    assert response.status_code == 204
