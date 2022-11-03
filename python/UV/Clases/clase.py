#Rango de edades
"""edad = int(input("Digite su edad"))
if edad >= 1 and edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 60:
    print("Eres mayor de edad")
elif edad >= 60 and edad < 100:
    print("Eres un adulto de tercera edad")
else:
    print("No coincide, vuelve a intentarlo")"""


#hallar numero al cubo
"""numero = int(input("Digite un numero entero"))

resultado = numero * numero * numero

print(f" {numero} al cubo es {resultado} ")"""


#(desde, hasta, de cuanto en cuanto)
"""for i in range(1, 101, 1):
    numero = int(input("Digite un numero entero"))
    resultado = numero * numero * numero
    print(f" {numero} al cubo es {resultado} ")"""



"""import datetime

def obtenerEdad(anioNacimiento):
    date        = datetime.date.today()
    anioActual  = date.strftime("%Y")
    edadPersona = int(anioActual) - int(anioNacimiento)

    return edadPersona


anioNacimiento = int(input("Ingrese el año de nacimiento : "))

edadCalculada = obtenerEdad(anioNacimiento)

print("La edad de la persona es ", edadCalculada)"""

#_______________________________________

#funciones
def edad(nacimiento):
    años = 2021 - nacimiento
    print('Tienes actualmente', años, 'años')
edad(2003)

"""def multiplicar(a,b):
    return a * b
multiplicar(10,5)
print(multiplicar(10,5))"""

def multiplicar2(a,b):
    return a * b #retorna a el llamado de abajo

resultado = multiplicar2(10,5) + 5
print(resultado)
