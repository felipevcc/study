"""
El juego consistirá en adivinar una cadena de números
distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
cadena de números. En cada intento, el programa informará de cuántos números
han sido acertados (el programa considerará que se ha acertado un número si
coincide el valor y la posición).

Ejemplo:
    Dime la longitud de la cadena: 4
    Intenta adivinar la cadena: 1234
    Con 1234 has adivinado 1 valores. Intenta adivinar
    la cadena: 1243
    Con 1243 has adivinado 0 valores. Intenta adivinar
    la cadena: 1432
    Con 1432 has adivinado 2 valores. Intenta adivinar
    la cadena: 2431
    Con 2431 has adivinado 4 valores.
    Felicidades

""" 

from random import randint

def cadena_random(length):
    cadena = []
    for _ in range(length): 
        num = randint(0,9)
        cadena.append(num) 
    return cadena

def adivinar(cadena): 
    length = False
    while length == False:
        inp = input('\nAdivina la cadena: ')
        if len(inp) == len(cadena):  
            length = True 
        else: 
            print(f'La longitud de la cadena es de {len(cadena)} cifras')
    
    inp_list = [int(i) for i in inp]
    #for i in inp: 
        #inp_list.append(int(i)) 

    aciertos = 0
    for num_cad, num_inp in zip(cadena, inp_list):  
        if num_cad == num_inp: 
            aciertos += 1 
        #print(num_cad, num_inp)
    if aciertos == len(cadena):
        print('¡Acertaste, Felicitaciones!') 
        return True 
    else: 
        print(f'Has adivinado {aciertos} valores') 
        return False  

def run():  
    print("ADVINAR")
    length = False 
    while length == False: 
        length_input = int(input('\nLongitud de la cadena: ')) 
        if length_input >= 2 and length_input <= 9:
            length = True  
        else: 
            print('La longitud de la cadena debe ser entre 2 y 9 cifras')
    
    cadena = cadena_random(length_input)
    
    acierto = False 
    while acierto == False:
        acierto = adivinar(cadena) 

if __name__ == '__main__':
    run()
