import React, { useEffect, useState } from 'react';

function Leaderboard() {
    const [scores, setScores] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/leaderboard')
            .then(res => res.json())
            .then(data => setScores(data));
    }, []);

    return (
        <div>
            <h2>Leaderboard</h2>
            {scores.map((entry, idx) => (
                <p key={idx}>{idx + 1}. {entry.username}: {entry.points} pts</p>
            ))}
        </div>
    );
}
export default Leaderboard;
