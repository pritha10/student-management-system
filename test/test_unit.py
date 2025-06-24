import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestStudentAPIUnit(unittest.TestCase):

    @patch('app.mysql')
    def test_add_student(self, mock_mysql):
        tester = app.test_client(self)
        payload = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 20
        }

        mock_conn = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_conn

        response = tester.post('/students', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Student added successfully', response.data)
