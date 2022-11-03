#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y diga al final cuántos han sido pares y cuántos impares.

print('NÚMEROS NEGATIVOS')
valores = int(input('¿Cuántos valores va a introducir? '))
pares = 0 #contador negativos
#impares = 0 #contador positivos
if valores < 0:
    print('¡Imposible!')
elif valores == 0:
    print('No ha escrito ningún número')
else:
    for i in range(1, valores + 1):
        numero = int(input(f'Escriba el número {i}: '))
        if numero % 2 == 0:
            pares += 1
        impares = i - pares
    if pares == 1:
        print(f'Ha escrito {pares} número par.')
    if impares == 1:
        print(f'Ha escrito {impares} número impar.')
    if pares > 1:
        print(f'Ha escrito {pares} números pares.')
    if impares > 1:
        print(f'Ha escrito {impares} números impares.')
    print('Gracias por su colaboración.')