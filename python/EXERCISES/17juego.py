
import random


def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
    print(computadora)

    if usuario == computadora:
        return '¡Empate!'

    if ganó_el_jugador(usuario, computadora): #Se puede dejar sin == True unicamente si es verdadero
        return '¡Ganaste!'

    return '¡Perdiste!'


def ganó_el_jugador(jugador, oponente):
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())