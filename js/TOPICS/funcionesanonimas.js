function calcular (numero1, numero2, desarrollo, sumapordos){
    var sumar = numero1 + numero2;

    desarrollo(sumar);
    sumapordos(sumar);

    return sumar;
}

calcular(1, 2, resultado =>{
    console.log("la suma normal es:", resultado);
},
function(resultado){
    console.log("La suma por dos es:", resultado * 2);
});