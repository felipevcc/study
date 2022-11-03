package main

import "fmt"

func main() {

	// ----- Print y Println -----
	// Print es sin salto de linea
	// Println es con salto de linea

	// ----- Printf -------
	// para imprimir facilmente variables dentro de un texto
	// imprime de seguido sin salto de linea
	numero := 10
	palabra := "Fabian"
	fmt.Printf("%s tiene %d años\n", palabra, numero)
	// %s para strings
	// %d para enteros
	// $v si no sabemos que tipo de dato va

	// ----- Sprintf -------
	// para asignar a una variable un texto con variables
	message := fmt.Sprintf("%s tiene %d años\n", palabra, numero)
	fmt.Println("Desde variable:", message)

	// ----- Tipo de dato ------
	fmt.Printf("Tipo de dato numero: %T\n", numero)
	fmt.Printf("Tipo de dato palabra: %T\n", palabra)
	// %T para ver tipo de dato de una variable

}
