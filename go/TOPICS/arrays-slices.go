package main

import (
	"fmt"
)

func main() {

	// ------- Arrays --------
	/* son inmutables (solo se puede agregar la cantidad
	de valores que se le asigno)*/

	// El 4 entre corchetes es la cantidad de valores que va a tener
	var array [4]int
	// todos van a ser ceros, pq no se han modificado
	fmt.Println(array)

	// para editarlo:
	array[0] = 5
	array[1] = 2
	fmt.Println(array)

	// Ver cuantos elementos hay en un array:
	fmt.Println(len(array))

	// Ver capacidad maxima del array:
	fmt.Println(cap(array))

	// ------- Slices --------
	// son mutables
	// slices = para crear arrays ya definidos y mutables
	fmt.Println("")

	slice := []int{1, 2, 3, 4}
	fmt.Println(slice)

	// Para editar alguna posicion
	slice[3]++
	fmt.Println(slice)

	// otros ejemplos
	fmt.Println(slice[:2]) // imprime desde el indice 0 hasta el indice anterior del 2
	fmt.Println(slice[2:]) // imprime desde el indice 2 hacia adelante
	// el indice hasta donde va siempre es exclusivo (va hasta el indice anterior)

	// agregar valores
	slice = append(slice, 7)
	fmt.Println(slice)

	// agregar valores de una lista a otra lista
	newSlice := []int{9, 6, 10, 11}
	slice = append(slice, newSlice...)
	/* los tres puntos significa que golang va a
	descomprimir los numeros que hay dentro y los
	va a agregar independientemente*/
	fmt.Println(slice)

}
