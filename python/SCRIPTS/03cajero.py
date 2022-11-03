#CAJERO 

import random
from os import system
from time import sleep
from getpass import getpass

def clave():
    NUMS =  ['1', '2', '3', '4', '5', '6', '7', 
                 '8', '9', '0'] 
    cd = []
    for i in range(6):
        caracter_random = random.choice(NUMS)
        cd.append(caracter_random)
    cd = ''.join(cd)
    return cd

def main():   
    password = "1234"
    limite_login = 3

    while limite_login > 0:
    
        system("clear")
        print('\n'+'='*10+' CAJERO '+'='*10+'\n')

        # Validacion password
        login = getpass("Digite la contraseña: ") # input con caracteres ocultos
        if login != password:
            limite_login -= 1
            if limite_login > 0:
                print('Contraseña incorrecta\n')
                sleep(1.2)
                continue
            else:
                print('\nContraseña incorrecta\nLimite de intentos superado.')
                break
        
        limite_login = 0
             
        fondos = 0
        while True:
            system("clear")   
            key = clave()
            menu = ['\n'+'='*11+' MENU '+'='*11+'\n', 
                    f'Tus fondos son de: ${fondos} pesos', 
                    f'Clave dinamica: {key}',
                    f'¿Que desea hacer?',
                    '[1] Agregar fondos | [2] Retirar fondos | [3] Salir']
            for i in menu:
                print(i)

            opcion = int(input('\nSeleccione un número para continuar: '))
     
            if opcion == 1:
                system("clear")
                print('\n'+'='*6+' AGREGAR FONDOS '+'='*6+'\n')
                try:
                    opc = int(input('[0] Regresar a menu\n¿Cuanto dinero deseas agregar? '))
                except:
                    continue
                if opc > 0:
                    fondos += opc
                    print(f'Valor añadido: ${opc} pesos\nNuevo saldo en cajero: ${fondos} pesos\n\nVolviendo a menu...')
                    sleep(5)
                    continue
                else:
                    continue
        
            elif opcion == 2:
                system("clear")

                access = input(f'Clave dinamica: {key}\n> ')
                if access != key:
                    print('\nNo coincide')
                    sleep(1.2)
                    continue
                
                system("clear")
                print('\n'+'='*6+' RETIRAR FONDOS '+'='*6+'\n')
                try:
                    opc = int(input('[0] Regresar a menu\n¿Cuanto dinero deseas retirar? '))
                except:
                    continue
                if opc > 0 and opc <= fondos:
                    fondos -= opc
                    print(f'Valor retirado: ${opc} pesos\nNuevo saldo en cajero: ${fondos} pesos\n\nVolviendo a menu...')
                    sleep(5)
                    continue
                elif opc > 0 and opc > fondos:
                    print('No hay esa cantidad de fondos para retirar\n\nVolviendo a menu...')
                    sleep(3.5)
                    continue
                else:
                    continue

            elif opcion == 3:
                system("clear")
                print('\nSalida exitosa')
                break

            else:
                print('\nNo coincide')
                continue
    
if __name__=='__main__':
    main()
