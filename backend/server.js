const express = require('express');
const cors = require('cors');
const axios = require('axios');
const admin = require('firebase-admin');
const serviceAccount = require('./firebaseServiceAccount.json');

const app = express();
const PORT = 5000;
const products = require('./data/productsData.json');
const { calculateEcoScore } = require('./ecoScore');

let leaderboard = [];
const dummyUsers = [{ username: 'user', password: 'pass', token: 'abc123' }];

// ✅ Firebase Setup
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
});
const db = admin.firestore();

app.use(cors());
app.use(express.json());

// ✅ Existing Product Routes ... (retain as-is)
// [previous code for /api/products, /api/openfood, /api/recommend stays unchanged]

// ✅ Google Maps API: Nearby Eco-Friendly Stores
const GOOGLE_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY';
app.get('/api/nearby-stores', async (req, res) => {
    const { lat, lng } = req.query;
    const radius = 5000;
    try {
        const response = await axios.get(`https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${lat},${lng}&radius=${radius}&keyword=organic|eco|sustainable&key=${GOOGLE_API_KEY}`);
        res.json(response.data);
    } catch (err) {
        res.status(500).json({ error: 'Google Maps API error' });
    }
});

// ✅ Firestore: Rewards System
app.post('/api/rewards', async (req, res) => {
    const { userId, points } = req.body;
    await db.collection('rewards').doc(userId).set({ points }, { merge: true });
    res.json({ message: 'Points Updated' });
});

app.get('/api/rewards/:userId', async (req, res) => {
    const snapshot = await db.collection('rewards').doc(req.params.userId).get();
    res.json(snapshot.exists ? snapshot.data() : { points: 0 });
});

// ✅ Firestore: Daily Eco Challenges
app.get('/api/challenges', async (req, res) => {
    const challenges = [
        'Avoid Plastic Today',
        'Buy a Local Product',
        'Walk or Cycle Instead of Driving',
        'Eat a Plant-Based Meal',
        'Use a Reusable Bottle'
    ];
    res.json({ challenges });
});

// ✅ Coupons API (dummy)
app.get('/api/coupons', (req, res) => {
    res.json([
        { code: 'ECO10', description: '10% off on sustainable items' },
        { code: 'GREEN20', description: '20% discount on eco-friendly brands' }
    ]);
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
