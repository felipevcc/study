# HIGH ORDER FUNCTION
# filter, map, reduce

# MAS EJEMPLOS EN EJERCICIO 35

# para reduce:
from functools import reduce

# son funciones que reciben como parametro a otra funcion

# ----- filter ------
# filtrar por condicion
list1 = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 != 0, list1))
print(odd)
# se pasa a lista porque por defecto esta en "class=filter"

# ------ map -------
# mostrar elementos elevados al cuadrado
list2 = [1,2,3,4,5]
squares = list(map(lambda x: x**2, list2))
print(squares)

# ----- reduce ------
# reducir valores de una lista a un unico valor
# De functools se debe importar reduce 

list3 = [2,2,2,2,2]
all_multiplied = reduce(lambda a,b: a*b, list3)
print(all_multiplied)

# a es la variable acumuladora de cada resultado por multiplicacion
# b es la variable de cada 2, va a ir cambiando de posicion en la lista



