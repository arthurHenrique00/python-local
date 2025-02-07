//Redux -> uma biblioteca para gerenciar estado global em aplicações React.
// Store - Onde o estado global é armazenado.
// Actions - Ações que descrevem mudanças no estado.
// Reducers - Funções que determinam como o estado muda.
// Dispatch - Envia ações para modificar o estado.

import {createStore} from 'redux';

const initialState = {count: 0};

function counterReducer(state = initialState, action) {
    switch (action.type) {
        case "INCREMENT":
            return {count: state.count + 1};
        case "DECREMENT":
            return {count: state.count - 1};
        default:
            return state;
    }
}

const store = createStore(counterReducer);

store.dispatch({type: "INCREMENT"});
console.log(store.getState());