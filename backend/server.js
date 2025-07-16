```javascript
const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 5000;
const products = require('./data/products.json');
const { calculateEcoScore } = require('./ecoScore');

app.use(cors());

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

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```