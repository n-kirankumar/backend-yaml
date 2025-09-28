from flask import Flask, jsonify, request

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
    app.run(host="0.0.0.0", port=5000, debug=True)
