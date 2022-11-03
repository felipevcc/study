"""Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese 
número separados por comas."""

numero = int(input("Digite un numero positivo"))
for x in range(1, numero, 2): 
    print(x, end = ", ")