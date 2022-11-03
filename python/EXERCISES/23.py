"""
Haz un programa que vaya leyendo números hasta que el usuario
introduzca un número negativo. En este momento, el programa
mostrará por pantalla el número mayor de cúantos ha visto.
"""
x = 0
num = 0
while num >= 0:
    num = int(input('Numero: >'))
    if num >= x:
        x = num
print('\nEl numero mayor es:', x)