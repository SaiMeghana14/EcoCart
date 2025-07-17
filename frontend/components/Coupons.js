import React, { useEffect, useState } from 'react';

function Coupons() {
    const [coupons, setCoupons] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/coupons')
            .then(res => res.json())
            .then(data => setCoupons(data));
    }, []);

    return (
        <div>
            <h2>Eco Rewards Coupons</h2>
            {coupons.map((coupon, idx) => (
                <div key={idx} style={{ border: '1px dashed green', padding: '10px', margin: '5px' }}>
                    <p><b>{coupon.code}</b>: {coupon.description}</p>
                </div>
            ))}
        </div>
    );
}
export default Coupons;
