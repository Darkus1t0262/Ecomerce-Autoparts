from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/shipping_tracking/endpoint', methods=['GET'])
def get_shipping_tracking_endpoint():
    return jsonify({"message": "shipping_tracking service is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
