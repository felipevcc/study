/*console.log("Hola desde consola");
document.write("Hola desde pantalla");
alert("Hola desde alerta");*/

var nombre= "Felipe Villamizar";
var edad= 16;
var comida= "Lasagna";

/*console.log(nombre, edad, comida)
document.write(nombre, edad, comida)
alert(nombre+ edad+ comida)*/

console.log("Mi nombre es "+nombre+", Tengo "+edad+" años "+" y mi comida favorita es la "+comida);
document.write("Mi nombre es "+nombre+", Tengo "+edad+" años "+" y mi comida favorita es la "+comida);
alert("Mi nombre es "+nombre+", Tengo "+edad+" años "+" y mi comida favorita es la "+comida);

//_____________________________

var numero1 = parseInt(prompt('Digite un numero'));
var numero2 = parseInt(prompt('Digite otro numero'));

var resultado = numero1 + numero2;
console.log(resultado);

//_______________________________

var edad1 = parseInt(prompt('Cual es tu edad?'));
var imprime = '';
switch(edad){
    case 10:
        console.log = 'Eres niño';
    break;
    case 40:
        console.log = 'Eres adulto';
    break;
    default:
        console.log = 'No cumples ninguna edad';
    break;    
}