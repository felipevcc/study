#1) Recorrer los numeros del 1 al 20 y decir cuales son pares
for x in range(0, 21, 2):
    print(x)

#2) Mostra una tabla de multiplicar escogida por el usuario
"""tabla = int(input("¿Que tabla de multiplicar desea conocer?"))
for y in range(11):
    print(f"{tabla} x {y} = ", tabla * i)"""

#3) Realizar las tablas del 1 al 10
tablas = 10
i = 1
while i <= tablas:
    print(f"TABLA DEL {i} ")
    for numero in range(1,11):
        print(f" {i} x {numero} =", i * numero)
    i += 1

#4) Validar la entrada a un centro de atracciones, si la persona es mayor
#de edad aplicarle el 15% y si es menor de edad aplicarle el 50% al comprar su boleta  
edad = 17
boleta = 50
descuento_menor_edad = boleta * .50
descuento_mayor_edad = boleta * .15
if edad > 0 and edad < 18:
    descuento = boleta - descuento_menor_edad
    print(f"Tu boleta tiene un valor de {descuento} ")
elif edad >= 18:
    descuento = boleta - descuento_mayor_edad
    print(f"Tu boleta tiene un valor de {descuento} ")
else:
    print("no coincide")


#5) Realizar una función que realice la operación deseada por el usuario con dos datos introducidos por el usuario
numero1 = int(input("Digite un numero"))
numero2 = int(input("Digite otro numero"))
operacion = input("suma, resta, multiplicacion o division")
def funcion(numero1, numero2):
    if operacion == "suma":
        uno = numero1 + numero2
        print(uno)
    elif operacion == "resta":
        dos = numero1 - numero2
        print(dos)
    elif operacion == "multiplicacion":
        tres = numero1 * numero2
        print(tres)
    if operacion == "division":
        cuatro = numero1 / numero2
        print(cuatro)
    else:
        print("no coincide")
funcion(numero1, numero2)
    