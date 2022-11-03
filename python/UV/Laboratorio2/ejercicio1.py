#Johan Andres Lopez Garcia - 2179543
#Andrés Felipe Villamizar C. - 2180436

def programa():
    nombre = input('Cual es tu nombre? ')
    peso = float(input('Digite su peso: '))
    altura = float (input('Digite su altura: '))

    def paciente(nombre, peso, altura):
        print('\nPACIENTE: ', nombre)
        imc = peso / altura ** 2 
        print('IMC: ', imc)
    
        if imc > 0 and imc < 18.5:
            print('Categoria: Infrapeso')
        elif imc >= 18.5 and imc < 25.0:
            print('Categoria: Normal')
        elif imc >= 25.0:
            print('Categoria: Sobrepeso')
        else:
            print('Valor inexacto')
    paciente(nombre, peso, altura)

    def opcion():
        pregunta = input('\nDesea calcular el imc de otra persona? [s/n]')
        if pregunta == 's':
            return programa()
        elif pregunta == 'n':
            print('Salida exitosa')
        else:
            print('No coincide, vuelve a intentarlo')
            return opcion()
    opcion()
programa()
