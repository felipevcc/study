#RECURSIVIDAD

"""Escribir una funcion recursiva que reciba como parámetros dos strings a y b, 
y devuelva una lista con las posiciones en donde se encuentra b dentro de a."""

"""def lista(l1,l2):
    if l2 in l1:
        return 
lista('cualquier cosa', 'cual')"""

#==============================================================================

"""Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen 
la paridad del numero natural dado, conociendo solo que:
- 1 es impar.
- Si un número es impar, su antecesor es par; y viceversa."""

#============================

"""Escribir una funcion recursiva que encuentre el mayor elemento de una lista."""

def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

def main():
    #list = eval(input(" ingrese una lista de numeros: "))
    list = [1,4,2,3]
    print("el mayor es: ", Max(list))


main()

#===================================================
print('\n==========================================\n')

"""Crear una funcion recursiva para sumar los elementos de una lista"""

def sumar_lista(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sumar_lista(lista[1:])

numeros = [1,2,3,4,5]
resultado = sumar_lista(numeros)
print('La suma de los valores es igual a %i' % resultado)

#=====================================================
print('\n==========================================\n')

"""Sacar la suma de 1 al numero dado. Su nos dan el 5, 
devolvera un 5+4+3+2+1 = 15"""

def sumaRec(numero):
    if numero == 1:
        return 1
    else:
        return numero + sumaRec(numero - 1)
print(sumaRec(5))

#=====================================================
print('\n==========================================\n')

"""Recorrer una lista de forma recursiva"""

# index = indice

def mostrar(lista, index):
    if index != len(lista):
        print(lista[index])
        mostrar(lista, index+1)
lista = [1,2,3,4,5]
mostrar(lista,0)
