#las tuplas se utilizan para almacenar varios elementos dentro de una variable


#listas siempre se crean con corchetes []
#las tuplas siempre se crean con parentesis ()

vehiculos1 = ("carro", "moto", "bicicleta", "patineta")
print(type(vehiculos1))

#las tuplas son inmutables, no se pueden añadir, eliminar, ni crear

#vehiculos[1] = "camion"
#print(vehiculos1)

print(len(vehiculos1))

#como crear una tupla con un solo elementos
pais = ("colombia",)
print(pais)
print(type(pais))


#tuplas de deferentes tipos de datos
paises = (True,"colombia",45,1.8)
print(type(paises))

#tuplas del mismo tipo de dato
paises2 = ("colombia","ecuador")
print(paises2)

#accediendo a elementos de una tuplas por medio de su indice
pais3 = ("brazil", "ecuador", "argentina")
elementos_encontrado = pais3[1:]
print(elementos_encontrado)

#metodos para las tuplas
colores = ("rojo", "naranja", "azul")
print(colores)
lista_colores = list(colores)
lista_colores.append("morado") #append es para agregar
colores = tuple(lista_colores)
print(colores)

#agregar una tupla a otra tupla
tupla1 = ("hola", "mundo")
tupla2 = ("como estas",)#si solo es uno debe siempre tener ,
tupla1 += tupla2
print(tupla1)

frutas = ("naranja", "mora")
multi_frutas = frutas * 2
print(multi_frutas)
