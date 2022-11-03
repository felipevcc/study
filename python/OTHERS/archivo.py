import random

jugadores = []
tragamonedas = ("oso", "leon", "tiburon")
"""tragamonedas2 = ("oso", "leon", "tiburon")
tragamonedas3 = ("oso", "leon", "tiburon")"""

name = input('Ingrese su nombre: ')

def app():
    menu()
    
    validar = True
    while validar:
        try:
            opcion = int(input('Selecione una opción: \r\n'))
            if opcion == 1:
                tragamonedas()
                validar = False
            elif opcion == 2:
                print('Ruleta')
                validar = False
            elif opcion == 3:
                print('Salir')
                validar = False
            else:
                print('Opción no Válida.')
        except:
            print('Opción no válida.')

def menu():
    print('1) Traga monedas')
    print('2) Ruleta')
    print('3) Salir')

def tragamonedas():
    saldoInicial= 1000
    apuesta = -100
    saldoDisponible = [saldoInicial]
    seguir = True
    while sum(saldoDisponible) > 100 and seguir == True:
        print('------------------')
        print('Para ganar debe elegir una opción entre \r\n(oso, leon, tiburon)\r\n Si aciertas a dos ganas la cuota de x1.5\r\n Si aciertas a los 3 ganas la cuota de x2.5')
        print('------------------')

        #El sistema elige una opcion de manera aleatoria y pide la opcion a apostar.
        validar = True
        while validar:
            opcion = input('Elija su opción: ')
            if opcion == "oso" or opcion == "leon" or opcion == "tiburon":
                aleatorio1 = random.choice(tragamonedas)
                aleatorio2 = random.choice(tragamonedas)
                aleatorio3 = random.choice(tragamonedas)
                print('------------------')
                print(aleatorio1,aleatorio2,aleatorio3)
                validar = False
            else:
                print('Opción no válida')

        #Si gana con las 3 opciones
        if opcion == aleatorio1 == aleatorio2 == aleatorio3:
            saldoDisponible.append(apuesta)
            print('------------------')
            print(f'Felicidades {name} has ganado la cuota x2.5')
            saldoDisponible.append(-apuesta*2.5)
            print(f'Su saldo actual es de {sum(saldoDisponible)}')

            continuar = True
            while continuar:
                decision = input('¿Desea seguir jugando al tragamonedas?\r\n [s] [n] \r\n')
                if decision == 's':
                    seguir = True
                    continuar = False 
                elif decision == 'n':
                    print('Has salido de la ruleta')
                    seguir = False
                    continuar = False 
                else: 
                    print('Opción no válida')

        #Si gana con dos opciones   
        elif opcion == aleatorio1 == aleatorio2 or opcion == aleatorio1 == aleatorio3 or opcion == aleatorio2 == aleatorio3:
            saldoDisponible.append(apuesta)
            print('------------------')
            print(f'Felicidades {name} has ganado la cuota x1.5')
            saldoDisponible.append(-apuesta*1.5)
            print(f'Su saldo actual es de {sum(saldoDisponible)}')

            continuar = True
            while continuar:
                decision = input('¿Desea seguir jugando al tragamonedas?\r\n [s] [n] \r\n')
                if decision == 's':
                    seguir = True
                    continuar = False
                elif decision == 'n':
                    print('Has salido de la ruleta')
                    seguir = False
                    continuar = False  
                else: 
                    print('Opción no válida')
        #Si pierde
        else:
            saldoDisponible.append(apuesta)
            print('------------------')
            print(f'Más suerte para la próxima, su saldo actual es de {sum(saldoDisponible)} ')

            continuar = True
            while continuar:
                decision = input('¿Desea seguir jugando al tragamonedas?\r\n [s] [n] \r\n')
                if decision == 's':
                    seguir = True
                    continuar = False
                elif decision == 'n':
                    print('Has salido de la ruleta')
                    seguir = False
                    continuar = False 
                else: 
                    print('Opción no válida')


app()