from flask import Flask  # Import the Flask framework

# Create a Flask application instance
app = Flask(__name__)  

@app.route("/")  # Define a route for the root URL
def home():
    return "Hello from Python Microservice!"  # Return a response when accessed

if __name__ == "__main__":
    # Run the Flask application on port 5000 and make it accessible from any IP
    app.run(host="0.0.0.0", port=5000)

