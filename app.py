from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
students = [
    {
        "id": 1,
        "name": "Rahul",
        "course": "AIML",
        "email": "rahul@example.com"
    },
    {
        "id": 2,
        "name": "Priya",
        "course": "CSE",
        "email": "priya@example.com"
    },
    {
        "id": 3,
        "name": "Arun",
        "course": "ISE",
        "email": "arun@example.com"
    }
]


# GET /students
# Returns all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200


# GET /students/<id>
# Returns one student by ID
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


# PUT /students/<id>
# Updates an existing student's details
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    # Find the student
    student = None

    for item in students:
        if item["id"] == id:
            student = item
            break

    # Return 404 if student doesn't exist
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    # Get JSON data from the request
    data = request.get_json(silent=True)

    # Check whether valid JSON was provided
    if not isinstance(data, dict):
        return jsonify({
            "error": "Invalid or missing JSON data"
        }), 400

    # Validate required fields
    required_fields = ["name", "course", "email"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing required field: {field}"
            }), 400

    # Update student information
    student["name"] = data["name"]
    student["course"] = data["course"]
    student["email"] = data["email"]

    return jsonify({
        "message": "Student updated successfully",
        "student": student
    }), 200


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
