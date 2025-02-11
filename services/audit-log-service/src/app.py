from flask import Flask  # Import the Flask framework

app = Flask(__name__)  # Create a Flask application instance

@app.route("/")  # Define a route for the root URL
def home():
    return "Hello from Python Microservice!"  # Return a response when accessed

if __name__ == "__main__":
    # Run the Flask application on port 5000, accessible from any IP (0.0.0.0)
    app.run(host="0.0.0.0", port=5000)
