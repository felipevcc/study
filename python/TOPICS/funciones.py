#para crear una funcion

#funcion basica
def mifuncion():
    print("Hola, estoy dentro de la funcion")
mifuncion()

#Funcion pasandole parametros
def mifuncion1(numero):
    print("La operacion es:", (2 + numero) * 3)
mifuncion1(3)

#con varios parametros
def mifuncion2(numero, numero1):
    print("La operacion es:", (numero1 + numero) * 3)
mifuncion2(3,2)

#usando en el parametro el *
def mifuncion3(*frutas):
    print(frutas)
mifuncion3("manzana", "mora", "piña")


#scope global (espacio global)
variable = 10 #variable global
def myfuncion():
    variable = 20 #variable local
    print("variable dentro", variable)
myfuncion()
print("variable fuera", variable)


#scope global (espacio global)
def myfuncion1():
    global variable1 #pasamos una variable local a global
    variable1 = 30
myfuncion1()
print("variable global", variable1)


#scope global y local (funcion dentro de otra funcion)
def funcion():
    nombre = "luis" #global para funcion2, local para afuera
    def funcion2():
        print(nombre)
        nombre1 = "carlos" #local
    funcion2()
    #print(nombre1)
funcion()
#print(nombre)

edad = 17
def mensaje(mensaje):
    print("Hola puedes ingresar", mensaje)
if edad >= 18:
    mensaje(edad)
else:
    print("no cumples")

