from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/user_authentication/endpoint', methods=['GET'])
def get_user_authentication_endpoint():
    return jsonify({"message": "user_authentication service is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
