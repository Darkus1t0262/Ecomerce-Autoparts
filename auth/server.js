require('dotenv').config(); // ✅ Load environment variables
const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json());

// ✅ Use JWT_SECRET from .env or fallback to a default
const SECRET_KEY = process.env.JWT_SECRET || "fallback_secret_key";

// ✅ Root endpoint
app.get('/', (req, res) => {
    res.json({ message: "Auth Service is running!" });
});

// ✅ Login endpoint to generate token
app.post('/login', (req, res) => {
    const { username } = req.body;
    if (!username) return res.status(400).json({ message: "Username is required" });

    const token = jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
});

// ✅ Token verification endpoint
app.get('/verify', (req, res) => {
    const token = req.headers['authorization']?.split(' ')[1]; // ✅ Extract token properly
    if (!token) return res.status(403).json({ message: "No token provided" });

    jwt.verify(token, SECRET_KEY, (err, decoded) => {
        if (err) return res.status(401).json({ message: "Unauthorized" });
        res.json({ user: decoded });
    });
});

// ✅ Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`✅ Auth service running on port ${PORT}`));
