// PROGRAMACIÓN ORIENTADA  A OBJETOS

function carro(marca, modelo, año){
    this.marca = marca;
    this.modelo = modelo;
    this.año = año;
}

// generar una nueva instancia a partir de otra instancia
var autoNuevo1 = new carro('Mazda', 'Model 3', 2020);
console.log(autoNuevo1);

var autoNuevo2 = new carro('Tesla', 'Model X', 2022);
console.log(autoNuevo2);

var autoNuevo3 = new carro('Kia', 'Model 5', 2018);
console.log(autoNuevo3);