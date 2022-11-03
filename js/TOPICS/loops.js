// LOOPS

var estudiantes = ['Maria', 'Sergio', 'Rosa', 'Daniel'];

function saludarEstudiantes(estudiante){
    console.log(`Hola ${estudiante}`);
}

// --------- for -----------
// unicamente se pone < porque empieza desde 0 y va hasta 3

// desde donde inicia; hasta donde va; y de cuanto en cuanto va
for(var i=0; i<estudiantes.length;i++){
    saludarEstudiantes(estudiantes[i]);
}

console.log('\nFor of\n');

// ------- for .... of --------
// Recorre los valores de un objeto
for(var j of estudiantes){
    saludarEstudiantes(j);
}

console.log('\nFor in\n');

// ------- for .... in --------
// Recorre las propiedades de un objeto 
for(var x in estudiantes){
    // 0 1 2 3
    saludarEstudiantes(x);
}

console.log('\nWhile\n');

// ----------- while -----------
// se repite mientras se cumpla una condición
while(estudiantes.length > 0){
    var estudiante = estudiantes.shift();
    saludarEstudiantes(estudiante);
}

console.log('\nDo while\n');

// ---------- do while ----------
// tambien se repite mientras se cumpla una condición

/* dentro del do va el codigo a ejecutar, y de ultimo 
en el while va la condicion */
var y = 3;
do{
    console.log(y);
    y--;
} while(y > 0);

/* El codigo siempre se ejecutará al menos una vez.
debido a que el do esta antes de la condición*/

