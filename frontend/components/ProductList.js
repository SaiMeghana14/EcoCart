```javascript
import React, { useEffect, useState } from 'react';

function ProductList() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/products')
            .then(res => res.json())
            .then(data => setProducts(data));
    }, []);

    return (
        <div>
            <h2>Products</h2>
            {products.map(p => (
                <div key={p.id}>
                    <h3>{p.name}</h3>
                    <p>Eco Score: {p.ecoScore}/100</p>
                </div>
            ))}
        </div>
    );
}
export default ProductList;
```