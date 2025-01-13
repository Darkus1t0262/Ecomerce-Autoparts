from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/product_management/endpoint', methods=['GET'])
def get_product_management_endpoint():
    return jsonify({"message": "product_management service is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
