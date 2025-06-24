import requests

BASE_URL = "http://127.0.0.1:5000"

def test_integration_add_student():
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/students", json=payload)
    assert response.status_code == 201
    assert response.json()['message'] == 'Student added successfully'

def test_integration_get_students():
    response = requests.get(f"{BASE_URL}/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
