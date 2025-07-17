import React, { useState, useEffect } from 'react';
import ProductList from './components/ProductList';
import Dashboard from './components/Dashboard';
import AdminPanel from './components/AdminPanel';
import BarcodeScanner from './components/BarcodeScanner';
import Login from './components/Login';
import Leaderboard from './components/Leaderboard';
import CompareProducts from './components/CompareProducts';
import DailyChallenges from './components/DailyChallenges';
import Coupons from './components/Coupons';
import EcoNewsFeed from './components/EcoNewsFeed';
import './App.css';

function App() {
    const [token, setToken] = useState(localStorage.getItem('token'));
    const [darkMode, setDarkMode] = useState(false);
    const [language, setLanguage] = useState('en');

    useEffect(() => {
        document.body.className = darkMode ? 'dark' : 'light';
    }, [darkMode]);

    if (!token) return <Login setToken={setToken} />;

    return (
        <div>
            <h1>{language === 'en' ? 'EcoCart - Sustainable Shopping' : 'इकोकार्ट - पर्यावरण अनुकूल खरीदारी'}</h1>
            <button onClick={() => setDarkMode(!darkMode)}>Toggle Dark Mode</button>
            <button onClick={() => setLanguage(language === 'en' ? 'hi' : 'en')}>Switch Language</button>

            <ProductList language={language} />
            <Dashboard />
            <BarcodeScanner />
            <AdminPanel />
            <Leaderboard />
            <CompareProducts />
            <DailyChallenges />
            <Coupons />
            <EcoNewsFeed />
        </div>
    );
}

export default App;
