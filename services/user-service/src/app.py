from flask import Flask, jsonify, request

app = Flask(__name__)

users = []  # In-memory "database"

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Both 'name' and 'email' fields are required."}), 400
    user = {"id": len(users) + 1, "name": data['name'], "email": data['email']}
    users.append(user)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
