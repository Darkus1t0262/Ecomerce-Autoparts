from flask import Flask, jsonify
from flask_graphql import GraphQLView
from graphene import ObjectType, String, List, Schema
from flask_cors import CORS  # Allows frontend requests (fixes CORS issues)

# Initialize Flask App
app = Flask(__name__)
CORS(app)  # Enable CORS

# Define GraphQL Schema
class Product(ObjectType):
    id = String()
    name = String()
    price = String()

class Query(ObjectType):
    products = List(Product)

    def resolve_products(self, info):
        return [
            Product(id="1", name="Brake Pads", price="50"),
            Product(id="2", name="Oil Filter", price="15"),
            Product(id="3", name="Engine Oil", price="25")
        ]

schema = Schema(query=Query)

# GraphQL Endpoint
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

# Root Route (Fix 404 Issue)
@app.route("/")
def home():
    return jsonify({"message": "Product GraphQL API is running. Access GraphQL UI at /graphql"}), 200

# Run the Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
