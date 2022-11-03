## Ejercicio 1
#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

"""numero1 = int(input('Digite numero1'))
numero2 = int(input('Digite numero2'))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    resultado = numero1 + numero2
    print(f'{resultado} es par')
else:
    print('Es impar')"""

## Ejercicio 2
#A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. 
# Si la cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las horas  extras.  Calcular  el  salario  del  trabajador  dadas  las  horas  trabajadas  
# y  la  tarifa ingresadas por el usuario.

"""horas = int(input('Digite la cantidad de horas trabajadas'))
salario_hora = int(input('Cuanto dinero ganó?'))
if horas > 40:
    h_extra = horas - 40 
    tarifa = salario_hora * .50
    valor_h_extra = (salario_hora + tarifa)*h_extra
    total = (salario_hora * 40)+valor_h_extra
    print('Salario: ', total)
    print('Salario por hora: ', total / horas)
else:
    print('Horas trabajadas: ', horas)
    print('Salario: ', salario_hora * horas)
    print('Salario por hora: ', salario_hora)"""

## Ejercicio 3
#Hacer un algoritmo que calcule el total a pagar por la compra de camisas. 
# Si se compran tres  camisas  o  más  se  aplica  un  descuento  del  20%  sobre  el  total  de  la  compra  y  
# si  son menos de tres camisas un descuento del 10%

"""camisas = int(input('Cuantas camisas compra'))
precio = int(input('Precio'))
if camisas >= 3:
    descuento1 = precio * .20
    valor1 = precio - descuento1
    print('Precio total a pagar: ', valor1)
else:
    descuento2 = precio * .10
    valor2 = precio - descuento2
    print('Precio total a pagar: ', valor2)"""
    
## Ejercicio 4
#Escribir un programa que pregunte el nombre del usuario en la consola y 
# un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

## Ejercicio 5
#Escribir un programa que pregunte el nombre del usuario en la consola y 
# después de que el usuario lo introduzca muestre por pantalla "`<NOMBRE>` tiene `<n>` letras", donde `<NOMBRE>` es el nombre de usuario en mayúsculas 
# y `<n>` es el número de letras que tienen el nombre.