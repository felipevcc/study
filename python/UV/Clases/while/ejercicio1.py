n = int(input('\nDigite un numero: '))
if n >= 0:
    y = n
    while n >= 0:
        n = int(input('\nDigite un numero: '))
        if n >= 0:
            y = f'{y}, {n}'
    print(f'\nLos numeros digitados son:\n{y}')

else:
    print('\nNo hay numeros registrados')

