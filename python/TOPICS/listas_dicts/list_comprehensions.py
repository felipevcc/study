# LIST COMPREHENSIONS

def run():

    squares = [i**2 for i in range(1, 101) if i % 3 !=0]
    print(squares)
    """i se elevara al cuadrado las veces del range unicamente si cumple
    con la ultima condicion"""
    # La condicion a lo ultimo es opcional

    print('\n')
    # Lo del ejemplo 1 es lo mismo que hacer esto:
    squares2 = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares2.append(i**2)
    print(squares2)

    print('\n')

    # ---------- EJERCICIO ----------

    # almacenar multiplos de 4,6 y 9; y que vaya hasta el numero maximo de 5 digitos
    lista = [j for j in range(1,100000) if j % 36 == 0]
    print(lista)
    # solamente coloca el 36 porque es el numero multiplo de 4,6 y 9 al mismo tiempo

if __name__=='__main__':
    run()

# MAS EJEMPLOS EN EJERCICIO 35