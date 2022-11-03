import random

print('\n---BIENVENIDO A CHO HAN---\n')
billetera = 10
partidas_ganadas = 0
continuar = 'si'

print(f'Usted ingresa jugando con ${billetera} dolares')

while billetera > 0 and continuar == 'si':
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dados = dado1 + dado2
    apuesta = int(input('\nIngrese apuesta: '))
    if apuesta > billetera:
        print('La apuesta es mayor a lo que tiene en su billetera')
    elif apuesta <= 0:
        print('La apuesta es menor que 0')
    else: 
        decision = input('\nAdivina ¿par o impar? ')
        print(f'\nSalió: {dado1} + {dado2} = {dados}')
        if decision == 'par':
            if dados % 2 == 0:
                billetera = billetera + apuesta
                print(f'\n¡Ganó!\n\nBilletera: {billetera}')
                partidas_ganadas += 1
            else:
                billetera = billetera - apuesta
                print(f'\nPerdió\n\nBilletera: {billetera}')
        elif decision == 'impar':
            if dados % 2 != 0:
                billetera = billetera + apuesta
                print(f'\n¡Ganó!\n\nBilletera: {billetera}')
                partidas_ganadas += 1
            else:
                billetera = billetera - apuesta
                print(f'\nPerdió\n\nBilletera: {billetera}')
        else:
            print('\nNo coincide')
        continuar = input('\n¿Deseas seguir jugando? [si/no]')
        print('\n------------------------------')
if billetera == 0:
    print('\nTe quedaste sin dinero...')
elif continuar == 'no':
    print(f'\nUsted ganó {partidas_ganadas} partidas')
    print('\n¡Gracias por jugar!')
else:
    print('\nNo coincide')
    print('\nHas salido del juego')

#2445