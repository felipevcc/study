package main

// VARIABLES, CONSTANTES Y ZERO VALUES

import (
	"fmt"
	"reflect"
)

func main() {
	//Declaracion de constantes
	const pi float64 = 3.14
	const pi2 = 3.16

	fmt.Println("Pi:", pi)
	fmt.Println("Pi2:", pi2)

	//Declaracion de varaibles
	base := 12          //Primera forma
	var altura int = 14 //Segunda forma
	var area int        //Go no compila si las variables no son usadas

	fmt.Println(base, altura, area)

	fmt.Println(reflect.TypeOf(base))

	//Zero values
	//Go asigna vaalores a variables vacías
	var a int     //0
	var b float64 //0
	var c string  //vacio
	var d bool    //false

	fmt.Println(a, b, c, d)

	//Ejercicio
	//Calcular el áera del cuadrado
	const baseCuadrado = 10
	areaCuadrado := baseCuadrado * baseCuadrado

	fmt.Println("El área del cuadrado es:", areaCuadrado)
}
