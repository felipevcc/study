// FUNCIONES

// ---- Declarativas ------

/* A las funciones declarativas se les puede aplicar "hoisting",
que es llamar a una funcion antes de declararla*/

function mostrarnombre(texto, apellido, nombre, numero){
    console.log(texto);
    console.log(apellido);
    console.log(nombre);
    console.log(numero);
    // return numero
}
var apellido = "Villamizar";
var texto = "Hola como estas";
var numero = 456;
var nombre = "Felipe";

mostrarnombre(texto, apellido, nombre, numero);

// ----- Expresión ------

// se asignan a una variable
/* tambien se conocen como funciones anonimas, porque no se coloca 
un nombre a la funcion*/

var miFuncion = function(a,b){
    return a+b;
}
console.log(miFuncion(3,2));