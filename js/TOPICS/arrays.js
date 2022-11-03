// ARRAYS

var frutas = ['Manzana', 'Pera', 'Fresa'];

// push = append en py
frutas.push('Cereza');
console.log('append= ', frutas);

// pop = eliminar el ultimo elemento del array
frutas.pop();
console.log('pop= ', frutas);

// unshift = agregar un elemento al inicio del array
frutas.unshift('Primero');
console.log('unshift= ', frutas);

// shift = elimina el elemento que este de primero en el array
frutas.shift();
console.log('shift= ', frutas);

// indexOf = devuelve la posicion del elemento indicado
var pos = frutas.indexOf('Pera');
console.log('indexOf= ', pos);

// splice = elimina un elemento con el indice
frutas.splice(1,2);
console.log('splice', frutas)

// MAS EN ./objects.js