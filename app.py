
from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Amit", "course": "Computer Engineering"},
    {"id": 2, "name": "Priya", "course": "Information Technology"}
]

@app.route("/")
def home():
    return "Student Management System is running!"

@app.route("/students")
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
