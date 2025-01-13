from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/file_upload_download/endpoint', methods=['GET'])
def get_file_upload_download_endpoint():
    return jsonify({"message": "file_upload_download service is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
