// OTHERS

package main

import (
	"fmt"
	"log"
	"strconv"
)

func main() {

	// Convertir texto a numero
	value, err := strconv.Atoi("53")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Value:", value)

	// defer
	// ejecuta algo al final de una funcion (antes de que muera la funcion)
	defer fmt.Println("Hola")
	fmt.Println("Mundo")

}
