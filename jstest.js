// Spread Operator
const about = {
    if_you_are: 555
};

const updateAbout = {
    ...about,
    then_im: 666
};

//console.log(updateAbout);

// Rest Operator
const persona = {
    name: 'Arthur',
    age:18,
    country:"Zuca"
};

const {
    name,
    ...rest
} = persona;

//console.log(name);
//console.log(rest);s

// Map() -> cria um novo array aplicando uma função a cada elemento array original
const nums = [1, 2, 3, 4, 5];
const doubled = nums.map(num => num * 2);
//console.log(doubled)

//Filter() -> cria um novo array contendo os elementos que passam em um teste
const nums_2 = [6, 7, 8, 9, 10];
const evens = nums_2.filter(num => num % 2 === 0);
//console.log(evens)

//Reduce -> reduz um array a um único valor, acumulando os resultados
const nums_3 = [11, 12, 13, 14, 15];
const sum = nums_3.reduce((acc, num) => acc + num, 0);
//console.log(sum)

const FromSoftware = [
    {name: 'Dark Souls 3', price: 229},
    {name: 'Elden Ring', price: 250}
];

const totalPrice = FromSoftware.reduce((acc, game) => acc + game.price, 0);
//console.log(totalPrice);