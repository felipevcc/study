"""Una función que permite construir una nueva matriz que contiene el cuadrado de cada componente de una matriz dada"""

matriz1 = [[1,-3,2],[4,11,-1]]   

matriz2 = [[1,-3,2],[4,11,-1]]
r = [[0,0,0],[0,0,0]]

def funcion(m1, m2, r):

    for i in range(len(m1)):
        for x in range(len(m1[1])):
            r[i][x] = m1[i][x] * m2[i][x]
    print(r)

funcion(matriz1, matriz2, r)

print('\n==================================\n')

"""Una función que permite obtener un arreglo con los elementos que están en la diagonal de una matriz cuadrada"""
