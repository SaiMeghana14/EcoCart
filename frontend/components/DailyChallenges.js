import React, { useEffect, useState } from 'react';

function DailyChallenges() {
    const [challenges, setChallenges] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/challenges')
            .then(res => res.json())
            .then(data => setChallenges(data.challenges));
    }, []);

    return (
        <div>
            <h2>Daily Eco Challenges</h2>
            <ul>
                {challenges.map((c, idx) => (<li key={idx}>{c}</li>))}
            </ul>
        </div>
    );
}
export default DailyChallenges;
