// Hallar la moda

const lista = [1,2,3,1,2,3,2];

var elementos = {};

lista.map(
    function(numero){
        if(elementos[numero]){
            elementos[numero]++;
        } else{
            elementos[numero] = 1;
        }
    }
);

// Object.entries(elements) convierte un objeto a un array

function moda(elements){
    var elementsArray = Object.entries(elements);
    var elementModa = [0];
    for(i=0; i<elementsArray.length; i++){
        if (elementsArray[i][1]>elementModa[0]){
            var elementModa = elementsArray[i];
        } else if(elementsArray[i][1]==elementModa[0]){
            elementModa.push(elementsArray[i]);
        }
    }
    
    return elementModa;
}
console.log(moda(elementos));

