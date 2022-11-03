#Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

print('PARES E IMPARES')

n1 = int(input('Escriba un número entero: '))
n2 = int(input(f'Escriba un número entero mayor o igual que {n1}: '))

if n2 >= n1:
    for i in range(n1, n2+1):
        if i % 2 == 0:
            print(f'El numero {i} es par')
        elif i % 2 != 0:
            print(f'El numero {i} es impar')
else:
    print(f'¡Le he pedido un número entero mayor o igual que {n1}!')
