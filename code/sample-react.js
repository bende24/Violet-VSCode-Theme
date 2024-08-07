import React, { useState, useEffect } from 'react';

function App() {
    const [name, setName] = useState('Alice');
    const [numbers, setNumbers] = useState([1, 2, 3]);

    useEffect(() => {
        console.log(`Component mounted or updated: ${name}`);
        return () => {
            console.log(`Cleanup for: ${name}`);
        };
    }, [name]);

    const greet = () => {
        console.log(`Hello, ${name}!`);
    };

    const addNumber = () => {
        setNumbers([...numbers, numbers.length + 1]);
    };

    return (
        <div>
            <h1>Hello, World!</h1>
            <button onClick={greet}>Greet</button>
            <button onClick={addNumber}>Add Number</button>
            <ul>
                {numbers.map((n, index) => (
                    <li key={index}>Number: {n}</li>
                ))}
            </ul>
            <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
        </div>
    );
}

export default App;
