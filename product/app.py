from flask import Flask, jsonify
from flask_graphql import GraphQLView
from graphene import ObjectType, String, List, Schema
from flask_cors import CORS
from pymongo import MongoClient
import os

# ✅ Use correct MongoDB URI with authentication
MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:password@18.212.193.5:27017/products_db?authSource=admin")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client["products_db"]
    collection = db["products"]
    client.server_info()  # ✅ Test connection
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ MongoDB Connection Error: {e}")
    exit(1)

# Initialize Flask
app = Flask(__name__)
CORS(app)

# Define GraphQL Schema
class Product(ObjectType):
    id = String()
    name = String()
    price = String()

class Query(ObjectType):
    products = List(Product)

    def resolve_products(self, info):
        products = collection.find({}, {"_id": 0})  # ✅ Exclude `_id` field
        return list(products)

schema = Schema(query=Query)

# GraphQL Endpoint
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

# Root Endpoint
@app.route("/")
def home():
    return jsonify({"message": "✅ Product GraphQL API is running. Access GraphQL UI at /graphql"}), 200

# Start the Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000) 
