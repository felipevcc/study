#Johan Andres Lopez Garcia - 2179543
#Andrés Felipe Villamizar C. - 2180436

def programa():
    nombre = input('Cual es tu nombre? ')
    edad = int(input('Digite su edad: '))
    meses = int(input('Digite la cantidad de meses a cancelar: '))

    def persona(nombre, edad, meses):
        print('\nNombre: ', nombre)
        if edad > 0 and edad < 12:
            print('Categoria: Infantil')
            valor_mes = 43000
            total = valor_mes * meses
            print('Valor a pagar: $', total)
        elif edad >= 12 and edad < 18:
            print('Categoria: Juvenil')
            valor_mes = 36000
            total = valor_mes * meses
            print('Valor a pagar: $', total)
        elif edad >= 18:
            print('Categoria: Mayores')
            valor_mes = 32000
            total = valor_mes * meses
            print('Valor a pagar: $', total)
        else:
            print('Valor inexacto')
    persona(nombre, edad, meses)

    def opcion():
        pregunta = input('\nDesea registrar a otra persona? [s/n]')
        if pregunta == 's':
            return programa()
        elif pregunta == 'n':
            print('Salida exitosa')
        else:
            print('No coincide, vuelve a intentarlo')
            return opcion()
    opcion()
programa()