const { ApolloServer, gql } = require('apollo-server');
const { MongoClient } = require('mongodb');

const client = new MongoClient('mongodb://localhost:27017');
const db = client.db('product_catalog');
const products = db.collection('products');

const typeDefs = gql`
  type Product {
    id: ID!
    name: String!
    price: Float!
    stock: Int!
  }

  type Query {
    products: [Product]
  }
`;

const resolvers = {
  Query: {
    products: async () => {
      return await products.find().toArray();
    }
  }
};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
