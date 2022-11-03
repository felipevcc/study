lambda es una pequeña funcion anonima

# lambda parametros: expresion
# lamda puede contener infinitos parametros

def myfuncion(b):
    return lambda a : a / b
variable = myfuncion(5) #valor de b
print(variable(10)) #se le da el valor a la funcion anonima (a)


#Realizar una funcion lamba con diferentes datos
def function(y, z):
    return lambda x: x * y /z
numero = function(5,3)
print(numero(10)) #como es una funcion anonima el valor se le da a otra variable (numero_a)

#a = 5
#b = 3

#_________________________
# recorderis de funcion
# Def es una palabra reservada
numero = 20
def suma (numero):
    print(numero)
suma(numero) # siempre se debe volver a llamar la funcion para poder verlo

def fruta(pera):
    print(pera)
fruta(3)

print('\n')
#_________________________
palindrome = lambda string: string == string[::-1]
print(palindrome('ana'))
