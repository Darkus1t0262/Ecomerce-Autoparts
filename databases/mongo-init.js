db = db.getSiblingDB("products_db");
db.createUser({
  user: "admin",
  pwd: "password",
  roles: [{ role: "readWrite", db: "products_db" }]
});

db = db.getSiblingDB("orders_db");
db.createUser({
  user: "admin",
  pwd: "password",
  roles: [{ role: "readWrite", db: "orders_db" }]
});

db.products.insertMany([
  { _id: "1", name: "Brake Pads", price: 50 },
  { _id: "2", name: "Oil Filter", price: 15 },
  { _id: "3", name: "Engine Oil", price: 25 }
]);

db.orders.insertMany([]); // Empty order collection
