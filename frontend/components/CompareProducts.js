import React, { useState } from 'react';

function CompareProducts() {
    const [ids, setIds] = useState('');
    const [products, setProducts] = useState([]);

    const compare = async () => {
        const idList = ids.split(',').map(id => id.trim());
        const promises = idList.map(id => fetch(`http://localhost:5000/api/products/${id}`).then(res => res.json()));
        const results = await Promise.all(promises);
        setProducts(results);
    };

    return (
        <div>
            <h2>Compare Products</h2>
            <input placeholder="Enter Product IDs (comma-separated)" value={ids} onChange={(e) => setIds(e.target.value)} />
            <button onClick={compare}>Compare</button>
            <div style={{ display: 'flex', gap: '10px' }}>
                {products.map(p => (
                    <div key={p.id} style={{ border: '1px solid gray', padding: '10px' }}>
                        <h3>{p.name}</h3>
                        <p>EcoScore: {p.ecoScore}</p>
                        <p>Category: {p.category}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
export default CompareProducts;
