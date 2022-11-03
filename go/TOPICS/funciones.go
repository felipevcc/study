package main

import "fmt"

// Las funciones se declaran de la segunda palabra en adelante
// con la primera letra en mayuscula

/* defer = ejecuta algo al final de una funcion
(antes de que muera la funcion)
Ejemplo = ./other.go
*/

func normalFuncion(letter int) {
	fmt.Printf("Persona numero %d\n", letter)
}

func argumentos(a, b int, c string) {
	// Cuando tienen el mismo tipo de dato se pueden poner juntos
	// a,b int
	fmt.Println(a, b, c)
}

func returnValue(a int) int {
	// Se coloca el tipo de dato al final indicando que asi
	// va a ser el valor de salida
	return a * 2
}

func doubleReturn(a int) (c, d int) {
	return a, a * 2
}

func main() {
	normalFuncion(1)
	argumentos(1, 2, "Hola")

	value := returnValue(2)
	fmt.Println(value)

	// Para rescatar de la funcion los dos valores retornados
	value1, value2 := doubleReturn(5)
	fmt.Println(value1, value2)

	// Para rescatar de la funcion solamente un valor
	valueUno, _ := doubleReturn(3)
	fmt.Println(valueUno)
	// Asi o alreves

}
