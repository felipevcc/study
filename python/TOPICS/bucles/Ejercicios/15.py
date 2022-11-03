#Escriba un programa que pida un número entero mayor que 1 y que escriba si el número es un número primo o no.

print("NÚMERO PRIMO")
numero = int(input("Escriba un número entero mayor que 1: "))

if numero <= 1:
    print("¡Le he pedido un número entero mayor que 1!")
else:
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador = contador + 1
    if contador == 2:
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")