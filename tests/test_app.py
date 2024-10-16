# tests/test_app.py

import pytest
from website import create_app  # Corrected import path

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to NotesApp' in response.data  # Adjust based on your homepage content

def test_create_note(client):
    # Assuming you have a '/notes' route for creating notes in views.py
    response = client.post('/notes', data={'title': 'Test Note', 'content': 'This is a test note.'})
    assert response.status_code == 201
    assert b'Test Note' in response.data

def test_read_note(client):
    # Adjust this based on your note-reading route in views.py
    response = client.get('/notes/1')  
    assert response.status_code == 200
    assert b'Test Note' in response.data

def test_update_note(client):
    # Adjust this based on your note-updating route in views.py
    response = client.put('/notes/1', data={'title': 'Updated Note', 'content': 'Updated content.'})
    assert response.status_code == 200
    assert b'Updated Note' in response.data

def test_delete_note(client):
    # Adjust this based on your note-deleting route in views.py
    response = client.delete('/notes/1')  
    assert response.status_code == 204
