n = input('\nDigite una palabra: ')
if n != 'terminar':
    y = n
    while n != 'terminar':
        n = input('\nDigite una palabra: ')
        if n != 'terminar':
            y = f'{y} - {n}'
    print(f'\nLas palabras digitadas son:\n{y}')
else:
    print('No se digitó ninguna palabra')
