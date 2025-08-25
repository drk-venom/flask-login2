from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend (Netlify) to connect

# Hardcoded credentials
USERNAME = "cyberexpert"
PASSWORD = "venom"

@app.route("/")
def home():
    return jsonify({"message": "Backend is running! Use /login endpoint."})

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"success": False, "message": "No data received"}), 400

        username = data.get("username")
        password = data.get("password")

        if username == USERNAME and password == PASSWORD:
            return jsonify({"success": True, "message": "Login successful"})
        else:
            return jsonify({"success": False, "message": "Invalid username or password"}), 401

    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    # Debug only for local testing
    app.run(host="0.0.0.0", port=5000, debug=True)