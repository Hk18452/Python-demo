import react from 'react';
import {useState} from 'react';
function App() {
    const [count, setCount] = useState(0)
    const style = {
        main:{
            padding: '20px',
            margin: '20px'
        },
        title:{
            color: 'blue'
        }
    };
    return (
        <div style={style.main}>
            <h1 style={style.title}>Counter App</h1>
            <div>
                <button onClick={() => setCount(count + 1)}>Increment</button>
                <p>Count: {count}</p>
            </div>