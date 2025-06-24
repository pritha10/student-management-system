import requests

BASE_URL = "http://127.0.0.1:5000"

def test_api_create_and_delete_student():
    # Create
    payload = {"name": "Bob", "email": "bob@example.com", "age": 30}
    res = requests.post(f"{BASE_URL}/students", json=payload)
    assert res.status_code == 201

    # Get ID of new student
    students = requests.get(f"{BASE_URL}/students").json()
    new_student = next(s for s in students if s['email'] == "bob@example.com")

    # Delete
    del_res = requests.delete(f"{BASE_URL}/students/{new_student['id']}")
    assert del_res.status_code == 200
    assert del_res.json()['message'] == 'Student deleted successfully'
