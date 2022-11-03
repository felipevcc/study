n = int(input('\nDigite un numero: '))
x = 0
if n != 0:
    while n > 0:
        x = x + n
        n = int(input('\nDigite un numero: '))     
    print('\nLa suma de los numeros digitados es:', x)
else:
    print('No hay numeros digitados')