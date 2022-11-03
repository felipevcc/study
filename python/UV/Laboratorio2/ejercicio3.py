#Johan Andres Lopez Garcia - 2179543
#Andrés Felipe Villamizar C. - 2180436

def programa():
    valor_x = int(input('Digite el valor e X a calcular : '))

    def calcularX(valor_x):
            
        if valor_x > 0 :
            resultado_x = (3*valor_x) + 5
            print('El resultado del valor de x es : ', resultado_x)
        elif valor_x <= 0:
            resultado_x = (8*(valor_x**2)) - 6
            print('El resultado del valor de x es : ', resultado_x)
    calcularX(valor_x)    

    def opcion():
        pregunta = input('\nDesea calcular otro valor de x? [s/n]')
        if pregunta == 's':
            return programa()
        elif pregunta == 'n':
            print('Salida exitosa')
        else:
            print('No coincide, vuelve a intentarlo')
            return opcion()
    opcion()

programa()