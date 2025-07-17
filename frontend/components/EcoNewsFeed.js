import React, { useEffect, useState } from 'react';

function EcoNewsFeed() {
    const [articles, setArticles] = useState([]);

    useEffect(() => {
        const fetchRSS = async () => {
            const response = await fetch('https://api.rss2json.com/v1/api.json?rss_url=https://www.ecowatch.com/rss');
            const data = await response.json();
            setArticles(data.items.slice(0, 5));
        };
        fetchRSS();
    }, []);

    return (
        <div>
            <h2>Eco News Highlights</h2>
            <ul>
                {articles.map((article, idx) => (
                    <li key={idx}><a href={article.link} target="_blank" rel="noopener noreferrer">{article.title}</a></li>
                ))}
            </ul>
        </div>
    );
}
export default EcoNewsFeed;
