from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/admin_panel'
db = SQLAlchemy(app)

class AdminLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

@app.route('/logs', methods=['POST'])
def log_action():
    data = request.get_json()
    action = AdminLog(action=data['action'])
    db.session.add(action)
    db.session.commit()
    return jsonify({'message': 'Action logged successfully!'})

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = AdminLog.query.all()
    return jsonify([{'id': log.id, 'action': log.action, 'timestamp': log.timestamp} for log in logs])

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
