package main

import "fmt"

func main() {

	x := 10
	y := 50

	// Suma
	result := x + y
	fmt.Println("Suma:", result)

	// Resta
	result = x - y
	fmt.Println("Resta:", result)

	// Multiplicación
	result = x * y
	fmt.Println("Multiplicación:", result)

	// División
	result = x / y
	fmt.Println("División:", result)

	// Modulo
	result = x % y
	fmt.Println("Modulo:", result)

	// Incremental (Suma 1)
	x++
	fmt.Println("Incremental:", x)

	// Decremental (Resta 1)
	x--
	fmt.Println("Decremental:", x)
}
