```javascript
function calculateEcoScore(product) {
    let score = 100;
    if (!product.isOrganic) score -= 20;
    if (!product.fairTrade) score -= 20;
    if (product.carbonFootprint > 5) score -= 30;
    if (product.plasticPackaging) score -= 20;
    return score;
}
module.exports = { calculateEcoScore };
```