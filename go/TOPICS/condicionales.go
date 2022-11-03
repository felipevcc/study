// CONDICIONALES

// if, else if, else
// switch, case, default

package main

import "fmt"

// && AND
// || OR

func main() {

	// ========== if, else if, else ===========

	valor1 := 2
	valor2 := 2

	if valor1 == 1 && valor2 == 2 {
		fmt.Println("1 and 2")
	} else if valor1 == 2 {
		fmt.Println("valor1 = 2")
	} else {
		fmt.Println("not 1 and not 2")
	}

	// ================ switch =================

	v := 10

	switch v {
	case 0:
		fmt.Println("\nEs igual a cero")
	case 10:
		fmt.Println("\nEs igual a diez")
	default:
		fmt.Println("\nv != 0, 10")
	}

	// Otra forma de hacer switch:
	// se declara la variable dentro de switch; variable
	switch variable := 5; variable {
	case 5:
		fmt.Println("\nvariable es 5")
	default:
		fmt.Println("\nvariable != 5")
	}

	// Otra forma de hacer switch:
	// sin colocar variable al inicio
	value := 200

	switch {
	case value > 100:
		fmt.Println("\nEs mayor a 100")
	case value < 0:
		fmt.Println("\nEs menor a 0")
	default:
		fmt.Println("\nNo condicion")
	}

}
