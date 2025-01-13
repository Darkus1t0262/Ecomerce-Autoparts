from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/payment_processing/endpoint', methods=['GET'])
def get_payment_processing_endpoint():
    return jsonify({"message": "payment_processing service is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
