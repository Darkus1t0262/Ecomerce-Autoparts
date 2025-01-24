const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// In-memory database for promotions
let promotions = [
    { id: 1, code: "SUMMER20", description: "20% off during summer", discount: 20, isActive: true },
    { id: 2, code: "FREESHIP", description: "Free shipping on orders over $50", discount: 0, isActive: true },
    { id: 3, code: "WINTER15", description: "15% off during winter", discount: 15, isActive: false }
];

// Get all active promotions
app.get('/promotions', (req, res) => {
    const activePromotions = promotions.filter(promo => promo.isActive);
    res.status(200).json(activePromotions);
});

// Get a specific promotion by ID
app.get('/promotions/:id', (req, res) => {
    const promotion = promotions.find(promo => promo.id === parseInt(req.params.id));
    if (!promotion) {
        return res.status(404).json({ error: "Promotion not found" });
    }
    res.status(200).json(promotion);
});

// Add a new promotion
app.post('/promotions', (req, res) => {
    const { code, description, discount, isActive } = req.body;
    if (!code || !description || discount === undefined || isActive === undefined) {
        return res.status(400).json({ error: "All fields (code, description, discount, isActive) are required" });
    }

    const newPromotion = {
        id: promotions.length + 1,
        code,
        description,
        discount,
        isActive
    };
    promotions.push(newPromotion);
    res.status(201).json(newPromotion);
});

// Validate a promo code
app.post('/promotions/validate', (req, res) => {
    const { code } = req.body;
    if (!code) {
        return res.status(400).json({ error: "Promo code is required" });
    }

    const promotion = promotions.find(promo => promo.code === code && promo.isActive);
    if (!promotion) {
        return res.status(404).json({ error: "Invalid or inactive promo code" });
    }

    res.status(200).json({ valid: true, promotion });
});

// Start the server
const PORT = process.env.PORT || 5002; // Use PORT from environment variable or default to 5002
app.listen(PORT, () => {
    console.log(`Promotion Service running on http://localhost:${PORT}`);
});
