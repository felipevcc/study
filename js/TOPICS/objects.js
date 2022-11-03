// OBJETOS

var auto = {
    marca:"Toyota",
    modelo:"TXL",
    año:"2020",
    detalles: function(){
        console.log(`Auto ${this.modelo} ${this.año}`)
        // this hace referencia al objeto (auto)
    }
};

// ------------ Mostrar todo el objeto ------------
console.log(auto);

// ----- Mostrar una caracteristica del objeto -----
// variable.caracteristica
console.log(auto.marca);

// ----- llamar una funcion dentro del objeto -----
auto.detalles()
// va parentesis por lo que adentro lleva una funcion

// this puede ser otra cosa en otros temas, pero en objetos es asi


// ====================================
// FUNCIÓN CONSTRUCTORA DE OBJETOS

// para crear objetos con mas facilidad
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


// ====================================
// OBJETOS DENTRO DE ARRAYS

var articulos = [
    {nombre:'Bici', costo:3000},
    {nombre:'Tv', costo:2500},
    {nombre:'Libro', costo:320},
    {nombre:'Celular', costo:10000},
    {nombre:'Laptop', costo:20000},
    {nombre:'Tecladop', costo:500},
    {nombre:'Audifonos', costo:1700}
];

// --------
// Filtrando elementos, creando un nuevo array
var articulosFiltrados = articulos.filter(function(articulo){
    // retornar por el costo
    return articulo.costo <= 500;
});
console.log(articulosFiltrados);
// filtra los elementos de un array que cumplan con la condicion

// --------
// Mapear articulos, creando un nuevo array
// solo retornara lo que estamos pidiendo
var nombreArticulos = articulos.map(function(articulo){
    // retornar por el nombre (solo retornará el nombre)
    return articulo.nombre;
});
console.log(nombreArticulos);
/* retorna los resultados de la llamada a la funcion aplicados
a cada uno de sus elementos*/

// --------
// Buscar elementos exactos, creando un nuevo array
var encuentraArticulo = articulos.find(function(articulo){
    return articulo.nombre === "Laptop";
});
console.log(encuentraArticulo);
// retorna el primer elemento de un array que cumple con la condicion

// --------
// Mostrar elementos sin crear array y sin modificar el anterior
articulos.forEach(function(articulo){
    // recorre solo los nombres
    console.log(articulo.nombre)
});
// ejecuta la funcion una vez por cada elemento del array

// --------
// Mostrar true o false para articulos que cumplan la validacion
var articulosBaratos = articulos.some(function(articulo){
    return articulo.costo <= 700;
});
console.log(articulosBaratos);

