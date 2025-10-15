from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Flask with Docker and VS Code!"})


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({
        "status": "User created successfully",
        "user": data
    }), 201


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)  # bandit:skip=B104
