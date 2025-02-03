from flask import Flask, jsonify
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation
from flask_cors import CORS
from pymongo import MongoClient
import os

# ✅ Use correct MongoDB URI with authentication
MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:password@54.90.243.16:27017/products_db?authSource=admin")

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

# ✅ Define GraphQL Schema
class Product(ObjectType):
    id = String()
    name = String()
    price = String()
    available_units = Int()

# ✅ Define Mutations
class AddProduct(Mutation):
    class Arguments:
        id = String(required=True)
        name = String(required=True)
        price = String(required=True)
        available_units = Int(required=True)

    product = Field(lambda: Product)

    def mutate(self, info, id, name, price, available_units):
        new_product = {"id": id, "name": name, "price": price, "available_units": available_units}
        collection.insert_one(new_product)
        return AddProduct(product=new_product)

class UpdateProduct(Mutation):
    class Arguments:
        id = String(required=True)
        name = String()
        price = String()
        available_units = Int()

    product = Field(lambda: Product)

    def mutate(self, info, id, name=None, price=None, available_units=None):
        update_data = {}
        if name:
            update_data["name"] = name
        if price:
            update_data["price"] = price
        if available_units is not None:
            update_data["available_units"] = available_units

        collection.update_one({"id": id}, {"$set": update_data})
        updated_product = collection.find_one({"id": id}, {"_id": 0})
        return UpdateProduct(product=updated_product)

class DeleteProduct(Mutation):
    class Arguments:
        id = String(required=True)

    success = String()

    def mutate(self, info, id):
        result = collection.delete_one({"id": id})
        if result.deleted_count > 0:
            return DeleteProduct(success="✅ Product deleted successfully!")
        else:
            return DeleteProduct(success="❌ Product not found!")

# ✅ Define Query and Mutation
class Query(ObjectType):
    products = List(Product)

    def resolve_products(self, info):
        products = collection.find({}, {"_id": 0})  # ✅ Exclude `_id` field
        return list(products)

class Mutation(ObjectType):
    add_product = AddProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

schema = Schema(query=Query, mutation=Mutation)  # ✅ Add mutation support

# GraphQL Endpoint
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

# Root Endpoint
@app.route("/")
def home():
    return jsonify({"message": "✅ Product GraphQL API is running. Access GraphQL UI at /graphql"}), 200

# Start the Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
