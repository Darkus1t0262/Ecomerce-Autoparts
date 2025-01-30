const { MongoClient } = require("mongodb");
require("dotenv").config();

const uri = process.env.MONGO_URI;
const user = process.env.MONGO_USER;
const password = process.env.MONGO_PASSWORD;
const dbName = process.env.MONGO_DB_NAME;

const client = new MongoClient(uri, {
    auth: { username: user, password: password }
});

let db;

async function connectDB() {
    try {
        await client.connect();
        db = client.db(dbName);
        console.log(`✅ Connected to MongoDB - ${dbName}`);
    } catch (err) {
        console.error("❌ MongoDB Connection Error:", err);
    }
}

function getDB() {
    if (!db) {
        throw new Error("❌ Database not initialized");
    }
    return db;
}

module.exports = { connectDB, getDB };
