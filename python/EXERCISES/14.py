#1. Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. El algoritmo debe imprimir el valor ingresado, y 
# de ser una nota mayor o igual a 4.0, deberá imprimir un mensaje de felicitaciones.

def primero():
    nota = float(input('Digite la nota (0.0 - 5.0) '))

    if nota >= 4.0 and nota <= 5.0:
        print(nota)
        print('Felicitaciones')
    elif nota >= 0.0 and nota < 4.0:
        print(nota)
    else:
        print('No coincide')
primero()

#2. Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. El algoritmo debe imprimir el valor ingresado, y 
# un mensaje que indique si el estudiante “Ganó el curso” o “Perdió el curso”. Se gana el curso solo si la nota definitiva es mayor o igual a 3.0.

def segundo():
    nota = float(input('Digite la nota(0.0 - 5.0 '))

    if nota >= 3.0 and nota <= 5.0:
        print(nota)
        print('Ganó el curso')
    elif nota >= 0.0 and nota < 3.0:
        print(nota)
        print('Perdió el curso')
    else:
        print('No coincide')
segundo()

#3. Diseñe un algoritmo que permita solicitar tanto el nombre como la edad de una persona y posteriormente indicar si es 
# “Mayor de edad” o “Menor de edad” según la información ingresada. Una persona se considera mayor de edad si tiene 18 años o más.

nombre = input('Como te llamas? ')
edad = int(input('Cual es tu edad? '))

print(f'Hola {nombre}')
if edad >= 18:
    print('Eres mayor de edad')
elif edad > 0 and edad < 18:
    print('Eres menor de edad')
else:
    print('Edad inexacta')

#4. Diseñe un algoritmo que determina si un número es par o impar. Recuerde que un número es par si el resto de una división 
# entera con el número 2 es cero.

numero = int(input('Digite un numero: '))

if numero % 2 == 0:
    print(f'{numero} es par')
else:
    print('El numero digitado es impar')
