import React, { useState } from 'react';

function BarcodeScanner() {
    const [barcode, setBarcode] = useState('');
    const [product, setProduct] = useState(null);

    const fetchProduct = async () => {
        const res = await fetch(`http://localhost:5000/api/openfood/${barcode}`);
        const data = await res.json();
        setProduct(data.product);
    };

    return (
        <div>
            <h2>Barcode Lookup</h2>
            <input placeholder="Enter barcode" value={barcode} onChange={(e) => setBarcode(e.target.value)} />
            <button onClick={fetchProduct}>Fetch Product</button>
            {product && (
                <div>
                    <h3>{product.product_name}</h3>
                    <img src={product.image_small_url} alt="product" />
                    <p>Categories: {product.categories}</p>
                </div>
            )}
        </div>
    );
}
export default BarcodeScanner;
