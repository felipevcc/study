#TRIANGULO 2

#datos de entrada
base = 35
#altura =
#proceso
residuo = base%25 
lados = residuo ** 3
perimetro =  (lados * 2) + base

#datos de salida
print(lados)
print(f"El perimetro del triangulo 2 es: {perimetro} ")