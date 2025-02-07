//Props -> Props são dados passados de um componente pai para um componente filho
function Salute(props) {
    return <h1>Wassup, {props.name}!</h1>;
}

function App() {
    return <Salute name='Arthur'/>
}

//State -> State é um conjunto de dados interno ao componente que pode mudar ao longo do tempo.
import useState from 'react';

function Counter() {
    const [count, setCount] = useState(0);

    return (
        <div>
            <p>Contador: {count}</p>
            <button onClick={() => setCount(count + 1)}>Incrementars</button>
        </div>
    )
}