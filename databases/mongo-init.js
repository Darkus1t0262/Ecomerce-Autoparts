db = db.getSiblingDB('admin');

db.createUser({
  user: "admin",
  pwd: "password",
  roles: [
    { role: "readWrite", db: "orders_db" },
    { role: "readWrite", db: "products_db" },
    { role: "dbAdmin", db: "admin" }
  ]
});

db = db.getSiblingDB('orders_db');
db.createCollection("orders");

db = db.getSiblingDB('products_db');
db.createCollection("products");

print("✅ MongoDB initialization completed!");
