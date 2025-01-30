const express = require('express');
const jwt = require('jsonwebtoken');
const app = express();
app.use(express.json());

const SECRET_KEY = "your_secret_key";

app.post('/login', (req, res) => {
    const { username } = req.body;
    const token = jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
});

app.get('/verify', (req, res) => {
    const token = req.headers['authorization'];
    if (!token) return res.status(403).json({ message: "No token provided" });
    
    jwt.verify(token, SECRET_KEY, (err, decoded) => {
        if (err) return res.status(401).json({ message: "Unauthorized" });
        res.json({ user: decoded });
    });
});

app.listen(3000, () => console.log('Auth service running on port 3000'));

