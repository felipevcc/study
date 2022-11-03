# DICTIONARY COMPREHENSIONS

# como buena practica solo se importa sqrt
# ya que solo vamos a utilizar esa funcionalidad
from math import sqrt

def run():
    """almacenar los numeros elevados al cubo del 1 al 100 que
    no sean divisibles entre 3"""
    my_dict = {}
    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i] = i**3
    print(my_dict)

    print('\n')
    # lo mismo pero con dictionary comprehensions
    dict2 = {j:j**3 for j in range(1,101) if j % 3 != 0}
    print(dict2)
    # al inicio se coloca: key:value (j:j**3)

    print('\n')

    # ---------- EJERCICIO ----------

    """Dict cuyas llaves sean los 1000 primeros numeros naturales
    con sus raices cuadradas como valores"""

    dict_ej ={x:sqrt(x) for x in range(1, 1001)} 
    print(dict_ej)

    # Para evitar math.sqrt se hace la raiz asi: i**0.5
    # Estamos expresando la raiz como potencia (propiedades de radicacion)
    # info: en discord/development/study-me/others
    print('\n')
    dict_ej2 = {x:round(x**0.5,2) for x in range(1, 1001)}
    print(dict_ej2)
    # se redondea a dos cifras para evitar tantos decimales

if __name__ == '__main__':
    run()

# MAS EJEMPLOS EN EJERCICIO 35
