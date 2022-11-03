#MATRICES

num = [1]*5
print(num)

m = [[0,0,0,0],[0,0,0,0],[0,0,0,0]] #Matriz de 3 filas y 4 columnas
print(m)

otram = [[1 for columna in range(0,4)] for fila in range(0,3)]
#Matriz de 3 y 4 columnas 

print(otram)


#=============================================
print('\n=======================================\n')

"""Una función que permite construir una nueva matriz que contiene el cuadrado de cada componente de una matriz dada"""

matriz1 = [[1,-3,2],[4,11,-1]]   

r = [[0,0,0],[0,0,0]]

def funcion(m1, r):

    # Para llamar a todos los lugar de la matriz:
    for i in range(len(m1)):
        for x in range(len(m1[1])):
            r[i][x] = m1[i][x]**2
    print(r)

funcion(matriz1, r)

#=============================================
print('\n=======================================\n')

"""Una función que permite obtener un arreglo con los elementos que están en la diagonal de una matriz cuadrada"""

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

arreglo = ['','','']

def array(m,a):
    for i in range(3):
        for j in range(3):
            if i == j:
                a[i] = m[i][j]
array(matriz,arreglo)

print(arreglo)


