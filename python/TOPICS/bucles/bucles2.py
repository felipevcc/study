#el bucle me permite ejecutar un conjunto de sentencias
#listas, tuplas, diccionarios, conjuntos o cadenas

x = ["papaya", "mango", "pera", "fresa"]
for y in x:
    if y == "pera":
        break
    print(y)

#el pass es para si alguien no pone nada o pone algo erronero no de error

#range
for r in range(40,100,2):
    #comienza desde 40 hasta uno menos de 100, y va de 2 en 2
    print(r)