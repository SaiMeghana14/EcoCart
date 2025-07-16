```javascript
import React from 'react';
import ProductList from './components/ProductList';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
    return (
        <div>
            <h1>EcoCart - Sustainable Shopping</h1>
            <ProductList />
            <Dashboard />
        </div>
    );
}
export default App;
```