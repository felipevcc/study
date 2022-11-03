// CONDICIONALES    

// ---- if, else if, else ----
var x = true;
if (x === true){
    console.log('x es true');
} else if (x === false){
    console.log('x es false');
} else{
    console.log('x no es true, ni false');
}

// ---- condicional ternario ----

// condicion ? true: false;
// variable es igual a condicion ? if : else
var numero = 1;

var resultado = numero === 1 ? "Si soy un uno" : "No, no soy uno";
console.log(resultado);

// ---------- switch -----------

// el break ya no va a dejar que pase a los otros casos

var typeCard = 'Credit Card';

switch(typeCard){
    case 'Debid Card':
        console.log('This is a debid card');
        break;
    case 'Credit Card':
        console.log('This is a Credit Card');
        break;
    default:
        console.log('No card');
}