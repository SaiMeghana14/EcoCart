import React, { useState } from 'react';
import ProductList from './components/ProductList';
import Dashboard from './components/Dashboard';
import AdminPanel from './components/AdminPanel';
import BarcodeScanner from './components/BarcodeScanner';
import Login from './components/Login';
import Leaderboard from './components/Leaderboard';
import './App.css';

function App() {
    const [token, setToken] = useState(localStorage.getItem('token'));

    if (!token) return <Login setToken={setToken} />;

    return (
        <div>
            <h1>EcoCart - Sustainable Shopping</h1>
            <ProductList />
            <Dashboard />
            <BarcodeScanner />
            <AdminPanel />
            <Leaderboard />
        </div>
    );
}
export default App;
