// Connect to the admin database
db = db.getSiblingDB("admin");

// Create `products_db` and add sample products
db = db.getSiblingDB("products_db");
db.createCollection("products");
db.products.insertMany([
  { _id: 1, name: "Brake Pads", price: 50 },
  { _id: 2, name: "Oil Filter", price: 15 },
  { _id: 3, name: "Car Battery", price: 120 }
]);

// Create `orders_db` and add a sample order
db = db.getSiblingDB("orders_db");
db.createCollection("orders");
db.orders.insertOne({
  _id: 1,
  product_id: 1,
  quantity: 2,
  customer: "John Doe",
  status: "Pending"
});

print("✅ MongoDB Initialized Successfully!");
