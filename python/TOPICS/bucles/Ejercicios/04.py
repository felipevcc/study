"""Escribir un programa que pida al usuario un número entero 
positivo y muestre por pantalla la cuenta atrás desde ese 
número hasta cero separados por comas."""

numero = int(input("Escribir un numero positivo"))
for x in range(numero, -1, -1):
    print(x, end = ", ")
