from flask import Flask, jsonify
from flask_graphql import GraphQLView
from graphene import ObjectType, String, List, Schema
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask App Initialization
app = Flask(__name__)
CORS(app)  # Enable CORS

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

if not MONGO_URI or not MONGO_DB_NAME:
    raise ValueError("❌ Missing MongoDB environment variables!")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# Define GraphQL Schema
class Product(ObjectType):
    id = String()
    name = String()
    price = String()

class Query(ObjectType):
    products = List(Product)

    def resolve_products(self, info):
        try:
            products_cursor = db.products.find()
            products = [
                Product(id=str(prod["_id"]), name=prod["name"], price=str(prod["price"]))
                for prod in products_cursor
            ]
            return products
        except Exception as e:
            print(f"❌ Error fetching products: {e}")
            return []

schema = Schema(query=Query)

# GraphQL Endpoint
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

# Root Route (Fixes 404 Issues)
@app.route("/")
def home():
    return jsonify({"message": "✅ Product GraphQL API is running. Access GraphQL UI at /graphql"}), 200

# Run the Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
