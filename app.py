from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS  # Allow frontend access

app = Flask(__name__)
CORS(app)  # This will fix your frontend issue

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Srija@18'
app.config['MYSQL_DB'] = 'student_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return "Student Management API is running"

# Create (Add student)
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data['name']
    email = data['email']
    age = data['age']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Student added successfully'}), 201

# Read (Get all students)
@app.route('/students', methods=['GET'])
def get_students():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    student_list = []
    for student in students:
        student_list.append({
            'id': student[0],
            'name': student[1],
            'email': student[2],
            'age': student[3]
        })
    return jsonify(student_list)

# Update student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    name = data['name']
    email = data['email']
    age = data['age']
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE students SET name=%s, email=%s, age=%s WHERE id=%s", (name, email, age, id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Student updated successfully'})

# Delete student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Student deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
