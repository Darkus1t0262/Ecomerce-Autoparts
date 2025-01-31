from flask import Flask, jsonify
from flask_graphql import GraphQLView
from graphene import ObjectType, String, List, Schema
from flask_cors import CORS
from pymongo import MongoClient
import os

# Configuración de la base de datos desde variables de entorno
MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:password@3.84.196.21:27017/products_db")

client = MongoClient(MONGO_URI)
db = client["products_db"]
collection = db["products"]

# Inicializar Flask
app = Flask(__name__)
CORS(app)

# Definir el esquema GraphQL
class Product(ObjectType):
    id = String()
    name = String()
    price = String()

class Query(ObjectType):
    products = List(Product)

    def resolve_products(self, info):
        products = collection.find({}, {"_id": 0})  # Excluir _id
        return list(products)

schema = Schema(query=Query)

# Endpoint GraphQL
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

# Endpoint raíz
@app.route("/")
def home():
    return jsonify({"message": "Product GraphQL API is running. Access GraphQL UI at /graphql"}), 200

# Iniciar el servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
