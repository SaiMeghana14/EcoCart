```javascript
const express = require('express');
const cors = require('cors');
const axios = require('axios');
const app = express();
const PORT = 5000;
const products = require('./data/productsData.json');
const { calculateEcoScore } = require('./ecoScore');

let leaderboard = [];
const dummyUsers = [{ username: 'user', password: 'pass', token: 'abc123' }];

app.use(cors());
app.use(express.json());

// Existing Product Routes
app.get('/api/products', (req, res) => {
    const productsWithEco = products.map(p => ({
        ...p,
        ecoScore: calculateEcoScore(p)
    }));
    res.json(productsWithEco);
});

app.get('/api/products/:id', (req, res) => {
    const product = products.find(p => p.id === parseInt(req.params.id));
    if (product) {
        product.ecoScore = calculateEcoScore(product);
        res.json(product);
    } else {
        res.status(404).json({ error: 'Product not found' });
    }
});

app.post('/api/products', (req, res) => {
    const newProduct = req.body;
    newProduct.id = products.length + 1;
    products.push(newProduct);
    res.status(201).json(newProduct);
});

// ✅ Open Food Facts API Integration
app.get('/api/openfood/:barcode', async (req, res) => {
    try {
        const { barcode } = req.params;
        const response = await axios.get(`https://world.openfoodfacts.org/api/v0/product/${barcode}.json`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'OpenFoodFacts API error' });
    }
});

// ✅ Dummy Login
app.post('/api/auth/login', (req, res) => {
    const { username, password } = req.body;
    const user = dummyUsers.find(u => u.username === username && u.password === password);
    if (user) {
        res.json({ token: user.token });
    } else {
        res.status(401).json({ error: 'Invalid credentials' });
    }
});

// ✅ Leaderboard API
app.get('/api/leaderboard', (req, res) => {
    res.json(leaderboard);
});

app.post('/api/leaderboard', (req, res) => {
    const { username, points } = req.body;
    leaderboard.push({ username, points });
    leaderboard.sort((a, b) => b.points - a.points);
    res.status(201).json({ message: 'Score updated' });
});

// ✅ AI Recommendation via Hugging Face Proxy
app.post('/api/recommend', async (req, res) => {
    const { input } = req.body;
    try {
        const response = await axios.post(
            'https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2',
            { inputs: input },
            { headers: { Authorization: `Bearer YOUR_HF_TOKEN` } }
        );
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Hugging Face API Error' });
    }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
