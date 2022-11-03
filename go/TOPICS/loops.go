// CICLOS

package main

import "fmt"

func main() {

	/*
		Keywords
			continue = salta a la sgte iteracion del ciclo
			break = termina el ciclo
	*/

	//For conditional
	for i := 0; i <= 10; i++ {
		fmt.Println(i)
	}

	fmt.Printf("\n")

	// For while
	counter := 0
	for counter < 10 {
		fmt.Println(counter)
		counter++
	}

	// For forever (nunca parara de ejecutarse)
	/*
		counterForever := 0
		for {
			fmt.Println(counterForever)
			counterForever++
		}
	*/

}
