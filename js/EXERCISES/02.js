// Cuadrado

// Para agrupar mensajes mostrados por consola
console.group('Cuadrado');

const ladoCuadrado = 5;
const perimetroCuadrado = ladoCuadrado*4;
const areaCuadrado = ladoCuadrado**2


console.log('Los lados del cuadrado miden:', ladoCuadrado, 'cm');
console.log('El perimetro del cuadrado es de:', perimetroCuadrado, 'cm');
console.log('El area del cuadrado es de:', areaCuadrado, 'cm^2');

console.groupEnd();


// Triangulo

console.group('Triángulo');


const ladoTriangulo1 = 6;
const ladoTriangulo2 = 6;
const baseTriangulo = 4;
const alturaTriangulo = 5.5;
const perimetroTriangulo = ladoTriangulo1 + ladoTriangulo2 + baseTriangulo;
const areaTriangulo = (baseTriangulo * alturaTriangulo)/2;

console.log(`Los lados del triángulo miden:
            Base= ${baseTriangulo} cm
            Lado 1= ${ladoTriangulo1} cm
            Lado 2= ${ladoTriangulo2} cm`);

console.log(`La altura del triángulo es de ${alturaTriangulo} cm`);
console.log(`El perimetro del triángulo es de ${perimetroTriangulo} cm`);
console.log(`El area del triángulo es de ${areaTriangulo} cm^2`);

console.groupEnd();

// Circunferencia

console.group('Circunferencia');

const radioc = 4;
const diametroc = radioc*2;
const PI = Math.PI;
const perimetroc = diametroc*PI;
const areac = (radioc**2)*PI;

console.log(`El radio de la circunferencia es de ${radioc} cm`);
console.log(`El diametro de la circunferencia es de ${diametroc} cm`);
console.log(`PI es ${PI}`);
console.log(`El perimetro de la circunferencia es de ${perimetroc} cm`);
console.log(`El área de la circunferencia es de ${areac} cm^2`);

console.groupEnd();