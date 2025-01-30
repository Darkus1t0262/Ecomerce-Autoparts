const { MongoClient } = require("mongodb");
require("dotenv").config();

const uri = process.env.MONGO_URI;
const user = process.env.MONGO_USER;
const password = process.env.MONGO_PASSWORD;
const dbName = process.env.MONGO_DB_NAME;

if (!uri || !user || !password || !dbName) {
    console.error("❌ Missing MongoDB environment variables!");
    process.exit(1);
}

const client = new MongoClient(uri, {
    auth: { username: user, password: password },
    authMechanism: "SCRAM-SHA-256", // Secure auth
    useNewUrlParser: true,
    useUnifiedTopology: true
});

let db;

async function connectDB() {
    try {
        await client.connect();
        db = client.db(dbName);
        console.log(`✅ Connected to MongoDB - ${dbName}`);
    } catch (err) {
        console.error("❌ MongoDB Connection Error:", err);
        process.exit(1); // Exit process if DB connection fails
    }
}

function getDB() {
    if (!db) {
        throw new Error("❌ Database not initialized");
    }
    return db;
}

// Graceful shutdown on process exit
process.on("SIGINT", async () => {
    console.log("🔻 Closing MongoDB connection...");
    await client.close();
    process.exit(0);
});

module.exports = { connectDB, getDB };
