#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

print('MAYORES QUE EL PRIMERO')
valores = int(input('¿Cuántos valores va a introducir?'))
if valores > 0:
    numero_inicial = int(input('Escriba un número: '))
    for i in range(valores - 1): #-1 ya que el primer valor esta antes del ciclo
        numeros = int(input(f'Escriba un número más grande que {numero_inicial}: '))
        if numeros <= numero_inicial:
            print(f'¡{numeros} no es mayor que {numero_inicial}!')
    print('Gracias por su colaboración.')
else:
    print('¡Imposible!')