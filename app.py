from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask API is running"
    })


@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")

    return jsonify({
        "message": f"Hello, {name}!"
    })


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify({
        "message": "User created",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
