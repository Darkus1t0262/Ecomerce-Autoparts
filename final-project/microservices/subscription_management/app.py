from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/subscription_management/endpoint', methods=['GET'])
def get_subscription_management_endpoint():
    return jsonify({"message": "subscription_management service is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
