import random

n = random.randint(1, 1000)
vidas = 10
print('Tienes 10 vidas')

for i in range(vidas, 0, -1):

    if i <= 9:
        print('Te quedan: ', i, ' vidas\n')
    
    num = int(input('Digite un número (1 - 1000)'))

    if num >= 1 and num <= 1000:

        if num == n:
            print('Ganaste!, el número correcto era: ', n)
            break
        elif num != n and i == 1:
            print('Has perdido, el número correcto era: ', n)
        else:
            if num < n:
                print('El número es mas alto')

            elif num > n:
                print('El número es mas bajo')

    else:
        print('El número digitado no esta dentro del rango')
        break 
