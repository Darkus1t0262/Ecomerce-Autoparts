from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/fraud_detection/endpoint', methods=['GET'])
def get_fraud_detection_endpoint():
    return jsonify({"message": "fraud_detection service is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
