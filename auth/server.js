const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json());

const SECRET_KEY = "your_secret_key";

// ✅ Agregar una ruta para `/` (Solución al error 404)
app.get('/', (req, res) => {
    res.json({ message: "Auth Service is running!" });
});

// Endpoint para login
app.post('/login', (req, res) => {
    const { username } = req.body;
    const token = jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
});

// Verificar token
app.get('/verify', (req, res) => {
    const token = req.headers['authorization'];
    if (!token) return res.status(403).json({ message: "No token provided" });

    jwt.verify(token, SECRET_KEY, (err, decoded) => {
        if (err) return res.status(401).json({ message: "Unauthorized" });
        res.json({ user: decoded });
    });
});

// Iniciar el servidor en el puerto 3000
app.listen(3000, () => console.log('Auth service running on port 3000'));
