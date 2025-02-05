// Spread Operator
const about = {
    if_you_are: 555
};

const updateAbout = {
    ...about,
    then_im: 666
};

console.log(updateAbout);

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
//console.log(rest);