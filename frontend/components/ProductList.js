const [query, setQuery] = useState('');
const handleVoiceSearch = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.start();
    recognition.onresult = (event) => setQuery(event.results[0][0].transcript);
};
...
<button onClick={handleVoiceSearch}>🎤 Voice Search</button>
