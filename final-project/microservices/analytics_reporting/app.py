from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/analytics_reporting/endpoint', methods=['GET'])
def get_analytics_reporting_endpoint():
    return jsonify({"message": "analytics_reporting service is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
