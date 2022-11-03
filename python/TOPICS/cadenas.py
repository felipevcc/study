#INTRUMENTO DE CUERDA

#_______________________________________________

#Cuerdas multilineas
nombre = """Hola, como estas? Mi nombre es:
Felipe Villamizar"""
print(nombre)
#(tambien se puede con comillas simples)

#_______________________________________________

#Las cadenas en python son matrices de bytes
# (0), (1), (2), (3) = Hola
#H=0, O=1, L=2, A=3

texto = "hola"
print(texto[1])

#comienza a contar desde 0

#_______________________________________________

#funcion len
texto2 = "holamundo"
print(len(texto2))

#comienza a contar desde 1

#_______________________________________________

#comprobar cadena (in)

texto_prueba = "buenos dias"
print("tardes" in texto_prueba)

texto_prueba2 = "buenos dias"
print("tardes" not in texto_prueba2)

#_______________________________________________

rebanar = "hola mundo desde python"
print(rebanar[2:6])

rebanar_principio = "buenas"
print('\n',rebanar_principio[2:3])
print('AQUI:', rebanar_principio[1:6:2])
#parte desde 1, va hasta 5 (6-1), y va de dos en dos

print(rebanar_principio[::])
#parte desde el inicio, hasta el final y de uno en uno

print(rebanar_principio[::-1], '\n')
#Desde el inicio hasta el final, al reves

#_______________________________________________

#Indexacion negativa
texto= "hola mundo, buenas noches"
print(texto[-5:-1])
#con el 0 no lo reconoce

#_______________________________________________

#modifica cadenas

#upper() metodo de python que convierte a mayuscula el texto
mayuscula = "hola mundo"
print(mayuscula.upper())

#lower() metodo de python que convierte a minuscula el texto
minuscula = "BUENAS NOCHES"
print(minuscula.lower())

#strip() me permite eliminar los espacios en blanco
espacio_blanco = " hola como estas"
print(espacio_blanco.strip())

#replace() reemplaza caracteres de una cadena de texto
texto_rempla = "hola mundo desde python"
print(texto_rempla.replace("h","s")) #letra o palabra

#split() permite crear un separador
separador = "mundo, python"
print(separador.split(","))

#___________________________________________________

#formato de cadenas

#format() marcador de posicion
age = 17
nombre = "luis carlos {}"
print(nombre.format(age))

age1 = 14
age2 = 15
age3 = 16
nombre = "mario tiene {1}, juan tiene {0}, luis tiene {2}"
print(nombre.format(age1, age2, age3))

#___________________________________________________

#PERSONAJES DE ESCAPE

#permite los caracteres invalidos
texto_cualquiera = "hola mundo desde python \"buenas noches\" a todos"
print(texto_cualquiera)

texto_salto = "hola \nmundo"
print(texto_salto)

texto_espaciado= "h\rmundo"
print(texto_espaciado)

print(max('a,b,c,d'))
print(min('a,b,c,d'))
