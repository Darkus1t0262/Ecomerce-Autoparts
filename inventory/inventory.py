from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# 📌 Conect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:password@54.90.243.16:27017/inventory_db?authSource=admin")
client = MongoClient(MONGO_URI)
db = client["inventory_db"]
collection = db["inventory"]

# 📌 Get all products on Inventory
@app.route("/inventory", methods=["GET"])
def get_inventory():
    products = list(collection.find({}, {"_id": 0}))
    return jsonify(products), 200

# 📌 Add product to Inventory
@app.route("/inventory", methods=["POST"])
def add_product():
    data = request.json
    if not all(k in data for k in ("id", "name", "price", "available_units")):
        return jsonify({"message": "Missing fields"}), 400
    
    collection.insert_one(data)
    return jsonify({"message": "Product added successfully!"}), 201

# 📌 Update stock on product
@app.route("/inventory/<product_id>", methods=["PUT"])
def update_stock(product_id):
    data = request.json
    result = collection.update_one({"id": product_id}, {"$set": data})
    if result.matched_count == 0:
        return jsonify({"message": "Product not found"}), 404
    return jsonify({"message": "Product updated successfully!"}), 200

# 📌 Delete Product from Inventory
@app.route("/inventory/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    result = collection.delete_one({"id": product_id})
    if result.deleted_count == 0:
        return jsonify({"message": "Product not found"}), 404
    return jsonify({"message": "Product deleted successfully!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
