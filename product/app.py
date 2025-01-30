from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, List, Schema

app = Flask(__name__)

class Product(ObjectType):
    id = String()
    name = String()
    price = String()

class Query(ObjectType):
    products = List(Product)
    def resolve_products(self, info):
        return [
            Product(id="1", name="Brake Pads", price="50"),
            Product(id="2", name="Oil Filter", price="15")
        ]

schema = Schema(query=Query)
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)