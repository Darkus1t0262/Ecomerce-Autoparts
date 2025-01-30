db = db.getSiblingDB("products_db");
db.createCollection("products");
db.products.insertMany([
  { _id: ObjectId(), name: "Brake Pads", price: 50 },
  { _id: ObjectId(), name: "Oil Filter", price: 15 },
  { _id: ObjectId(), name: "Engine Oil", price: 25 }
]);
print("✅ Products inserted successfully!");
