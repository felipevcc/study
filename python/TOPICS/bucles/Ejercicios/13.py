#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

print('NÚMEROS NEGATIVOS')
valores = int(input('¿Cuántos valores va a introducir? '))
negativos = 0 #contador
if valores < 0:
    print('¡Imposible!')
else:
    for i in range(1, valores + 1):
        numero = int(input(f'Escriba el número {i}: '))
        if numero < 0:
            negativos = negativos + 1
    if negativos == 0:
        print('No ha escrito ningún número negativo.')
    elif negativos == 1:
        print(f'Ha escrito {negativos} número negativo.')
    else:
        print(f'Ha escrito {negativos} números negativos.')