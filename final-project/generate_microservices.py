import os

# Base directory for microservices
base_dir = "microservices"

# Define all 20 microservices with their API types
microservices = {
    "user_authentication": "REST",
    "product_management": "REST",
    "payment_processing": "REST",
    "notification_system": "WebSocket",
    "order_management": "REST",
    "inventory_management": "REST",
    "real_time_updates": "WebSocket",
    "shipping_tracking": "REST",
    "review_and_ratings": "GraphQL",
    "graphql_gateway": "GraphQL",
    "recommendation_system": "GraphQL",
    "webhook_notifications": "WebHook",
    "analytics_reporting": "REST",
    "customer_support": "WebSocket",
    "subscription_management": "REST",
    "external_api_integration": "SOAP",
    "legacy_soap_integration": "SOAP",
    "file_upload_download": "REST",
    "fraud_detection": "REST",
    "feedback_management": "REST",
}

# Templates for microservices
templates = {
    "REST": """from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/{service}/endpoint', methods=['GET'])
def get_{service}_endpoint():
    return jsonify({{"message": "{service} service is running"}}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
""",
    "GraphQL": """from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    {service} = String(description="Get {service} data")

    def resolve_{service}(root, info):
        return f"{service.capitalize()} Data"

schema = Schema(query=Query)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
""",
    "WebSocket": """from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    socketio.send(f"{service.capitalize()} Notification: {message}")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
""",
    "WebHook": """from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook/{service}/event', methods=['POST'])
def webhook_event():
    event_data = request.get_json()
    if event_data:
        print(f"Received webhook event: {event_data}")
        return jsonify({{"status": "received", "service": "{service}"}}), 200
    return jsonify({{"error": "No event data received"}}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
""",
    "SOAP": """<definitions xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
             xmlns:tns="http://example.com/soap" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
             name="{service}SOAPService" targetNamespace="http://example.com/soap">
    <message name="Request">
        <part name="input" type="xsd:string"/>
    </message>
    <message name="Response">
        <part name="output" type="xsd:string"/>
    </message>
    <portType name="{service}PortType">
        <operation name="{service}Operation">
            <input message="tns:Request"/>
            <output message="tns:Response"/>
        </operation>
    </portType>
    <binding name="{service}Binding" type="tns:{service}PortType">
        <soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
        <operation name="{service}Operation">
            <soap:operation soapAction="{service}Action"/>
            <input>
                <soap:body use="literal"/>
            </input>
            <output>
                <soap:body use="literal"/>
            </output>
        </operation>
    </binding>
    <service name="{service}Service">
        <port name="{service}Port" binding="tns:{service}Binding">
            <soap:address location="http://localhost:5003/{service}"/>
        </port>
    </service>
</definitions>
""",
}

# Create the microservices
for service, api_type in microservices.items():
    try:
        # Create the service directory
        service_dir = os.path.join(base_dir, service)
        os.makedirs(service_dir, exist_ok=True)

        # Write the main file (app.py or .wsdl)
        main_file = os.path.join(service_dir, "app.py" if api_type != "SOAP" else f"{service}.wsdl")
        with open(main_file, "w") as f:
            f.write(templates[api_type].format(service=service))

        # Write the Dockerfile for containerized services
        if api_type != "SOAP":
            dockerfile_path = os.path.join(service_dir, "Dockerfile")
            with open(dockerfile_path, "w") as f:
                f.write(f"""
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install flask{' flask-graphql' if api_type == 'GraphQL' else ''}{' flask-socketio' if api_type == 'WebSocket' else ''}

EXPOSE 5000

CMD ["python", "app.py"]
""")
        print(f"Created microservice: {service} ({api_type})")
    except Exception as e:
        print(f"Error creating microservice {service}: {e}")
