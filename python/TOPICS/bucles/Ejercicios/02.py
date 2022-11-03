"""Escribir un programa que pregunte al usuario su edad y muestre 
por pantalla todos los años que ha cumplido (desde 1 hasta su edad)"""

age = int(input("Digite su edad"))
for i in range(age):
    i += 1
    print(f"Has cumplido {i} años")