peso = float(input('Digite su peso'))
altura = float(input('Digite su estatura'))
sexo = input('Digite su sexo  m: masculino  n: femenino')

def entradas(p, a, s):

    print(f'Su peso es de: {p}  Su altura es: {a}  Su sexo es: {s}')

    if s == 'm':
        if a > 1.60 and p >= 75:
            print(f'Su dosis es de {a * .20} y de {p * .80}')
        elif a <= 1.60:
            print(f'Su dosis es de {a * .30} y de {p * .70}')
        else:
            print('No aprueba en ninguna dosis')

    elif s == 'f':
        if a >= 1.55 and p >= 65:
            print(f'Su dosis es de {a * .25} y de {p * .75}')
        elif p < 65:
            print(f'Su dosis es de {a * .35} y de {p * .65}')
        else:
            print('No aprueba en ninguna dosis')

    else:
        print('No coincide')

entradas(peso, altura, sexo)
