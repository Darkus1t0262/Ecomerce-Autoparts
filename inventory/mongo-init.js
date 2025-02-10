db = db.getSiblingDB('inventory_db');  // Switch to inventory_db

// Create a user for inventory_db with read and write permissions
db.createUser({
    user: "admin",
    pwd: "password",
    roles: [{ role: "readWrite", db: "inventory_db" }]
});

// Create the inventory collection
db.createCollection("inventory");

// Optional: Insert sample data (uncomment if needed)
/*
db.inventory.insertMany([
    { item: "engine", quantity: 50, price: 500 },
    { item: "brake pad", quantity: 200, price: 20 },
    { item: "tire", quantity: 100, price: 80 }
]);
*/

print("✅ Inventory database initialized successfully!");
