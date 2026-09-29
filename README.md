Flask REST API - Student Management

A simple Python Flask application that demonstrates REST API operations using HTTP GET and PUT methods.

Project Structure
flask-rest-api/
├── app.py
├── requirements.txt
└── README.md

Requirements

Python 3.x

Flask

VS Code

Postman or curl (optional, for testing)

1. Create a Virtual Environment

Open the terminal inside the project folder.

Windows
python -m venv venv3

Activate in Windows Command Prompt
venv3\Scripts\activate

Activate in Git Bash
source venv3/Scripts/activate


After activation, the terminal should show:

(venv3)

2. Install Flask

Run:

pip install -r requirements.txt


Or:

pip install flask

3. Run the Application

Run:

python app.py


The application will start at:

http://127.0.0.1:5000

4. REST API Endpoints
Get All Students

Method: GET

URL:

http://127.0.0.1:5000/students


Example response:

[
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

5. Get Student by ID

Method: GET

URL:

http://127.0.0.1:5000/students/1


Example response:

{
    "id": 1,
    "name": "Rahul",
    "course": "AIML",
    "email": "rahul@example.com"
}


If the student does not exist:

{
    "error": "Student not found"
}


HTTP status:

404 Not Found

6. Update Student

Method: PUT

URL:

http://127.0.0.1:5000/students/1


Set the request header:

Content-Type: application/json


Request body:

{
    "name": "Rahul Kumar",
    "course": "AIML",
    "email": "rahulkumar@example.com"
}


Example response:

{
    "message": "Student updated successfully",
    "student": {
        "id": 1,
        "name": "Rahul Kumar",
        "course": "AIML",
        "email": "rahulkumar@example.com"
    }
}


HTTP status:

200 OK

7. Error Handling
Student Not Found

Request:

GET /students/99


Response:

{
    "error": "Student not found"
}


Status:

404 Not Found

Missing JSON Data

If a PUT request does not contain valid JSON:

{
    "error": "Invalid or missing JSON data"
}


Status:

400 Bad Request

Missing Required Field

For example:

{
    "name": "Rahul"
}


Response:

{
    "error": "Missing required field: course"
}


Status:

400 Bad Request

8. Testing Using curl
Get all students
curl http://127.0.0.1:5000/students

Get one student
curl http://127.0.0.1:5000/students/1

Update a student

Windows CMD:

curl -X PUT http://127.0.0.1:5000/students/1 -H "Content-Type: application/json" -d "{\"name\":\"Rahul Kumar\",\"course\":\"AIML\",\"email\":\"rahulkumar@example.com\"}"


Git Bash:

curl -X PUT http://127.0.0.1:5000/students/1 \
-H "Content-Type: application/json" \
-d '{"name":"Rahul Kumar","course":"AIML","email":"rahulkumar@example.com"}'

9. Testing Using Postman
GET All Students

Open Postman.

Select GET.

Enter:

http://127.0.0.1:5000/students


Click Send.

GET Student by ID

Select GET and enter:

http://127.0.0.1:5000/students/1


Click Send.

PUT Student

Select PUT.

Enter:

http://127.0.0.1:5000/students/1


Go to Body.

Select raw.

Select JSON.

Enter:

{
    "name": "Rahul Kumar",
    "course": "AIML",
    "email": "rahulkumar@example.com"
}


Click Send.

The updated student should be returned with HTTP status 200 OK.

10. Important HTTP Methods
Method	Endpoint	Purpose
GET	/students	Get all students
GET	/students/<id>	Get one student
PUT	/students/<id>	Update a student
11. Notes

This application uses an in-memory Python list instead of a database. Therefore, changes made using PUT will be lost when the Flask application is stopped and restarted.

This project is intended as a beginner-level REST API laboratory exercise.
