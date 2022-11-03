#DICCIONARIOS

diccionario = {
    #clave:valor
    "marca":"bmw",
    "color":"rojo",
    "precio":20000
}
print(type(diccionario))
print(diccionario)

#accediendo a un elemento de ese diccionario
print(diccionario["marca"])

#elemento repetidos dentro del diccionario
diccionario2 = {
    #clave:valor
    "marca":"bmw",
    "color":"amarillo",
    "color":"rojo",
    "precio":20000
}
print(diccionario2["color"])

diccionario3 = {
    "marca":"bmw",
    "colores":["rojo", "amarillo", "morado"],
    "precio":20000
}
print(diccionario3)

carro = {
    "marca":"honda",
    "color":"rojo",
    "año":2021
}
#.get() para sacar elementos por medio de la clave
y = carro.get("marca") #mostrar unicamente claves
print(y)
#.values() para conocer los valores

#agregar clave y valor
carro["motor"] = "8v"
print(carro)

#para copiar el conjunto
carro2 = carro.copy()
print(carro2)


poblacion_paises = {
    'Argentina':23423523,
    'Brasil':234234235,
    'Colombia':2525235
}

print('\n')

#.keys() para mostrar las llaves
for pais1 in poblacion_paises.keys():
    print(pais1)

print('\n')

#.items() para mostrar las llaves y el valor
# por eso se colocan dos variables
for pais, poblacion in poblacion_paises.items():
    print(pais, poblacion)


