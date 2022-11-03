#Generador de contraseñas

import random

def generar_contraseña():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
             'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 
             'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 
             'ñ', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'x', 'y', 'z']
    NUMS =  ['1', '2', '3', '4', '5', '6', '7', 
             '8', '9', '0']
    CHARS = ['+', '-', '/', '@', '_', '?', '!', 
             '>', '<', '&', '$', '#']
    
    caracteres = MAYUS + MINUS + NUMS + CHARS

    #contraseña['']*15
    contraseña = []

    for i in range(15):
        #Escoge caracteres aleatorios
        caracter_random = random.choice(caracteres) 
        contraseña.append(caracter_random)
        #contraseña[i] = caracter_random

    contraseña = ''.join(contraseña)
    return contraseña

def run():
    contraseña = generar_contraseña()
    print('Tu nueva contraseña es: ' + contraseña)

if __name__=='__main__':
    run()