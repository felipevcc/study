#PRESTAMOS

def program():
    print('\n___PRESTAMOS___\n')
    prestamo = int(input('¿Cuanto dinero se va a prestar?\n'))
    i = int(input('¿A que interes?\n'))
    if i < 10 and i >= 0:
        i = f'0.0{i}'
    elif i >= 10:
        i = f'0.{i}'
    else:
        print('Valor inexacto')
    porcentaje = float(i)
    meses = int(input('¿Por cuantos meses?\n'))
    if meses == 0 or meses < 0:
        print('No coincide')
        return program()
    numero_cuotas = int(input('¿A cuantas cuotas?\n'))

    interes = int((prestamo * porcentaje) * meses)
    valor_total = interes + prestamo
    valor_cuotas = int(valor_total / numero_cuotas)

    print(f'Dinero a prestar: ${prestamo}')
    print(f'Interes del prestamo: ${interes}')
    print(f'Valor total: ${valor_total}')

    if meses == 1:
        print(f'\nA pagar:\nEn un mes, de {numero_cuotas} cuotas y cada cuota con un valor de: ${valor_cuotas}\n')
    else:
        print(f'\nA pagar:\nSon {meses} meses, de {numero_cuotas} cuotas y cada cuota con un valor de: ${valor_cuotas}\n')
    
    def pre():
        pregunta = input('¿Quiere calcular otro prestamo? [si/no]')
        if pregunta == 'si':
            return program()
        elif pregunta == 'no':
            print('Has salido del programa exitosamente')
        else:
            print('No coincide, vuelve a intentarlo')
            return pre()
    pre()
program()
