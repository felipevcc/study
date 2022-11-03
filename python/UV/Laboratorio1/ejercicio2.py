#Andres Felipe Villamizar / Grupo 81
#Julian Sanchez / Grupo 81

#Datos de entrada
gravedad_tierra = 9.8
gravedad_marte = 3.711
gravedad_jupiter = 24.79
gravedad_luna = 1.622

peso = float(input("Digite su peso"))

#Proceso
masa = peso/gravedad_tierra

peso_marte = masa * gravedad_marte
peso_jupiter = masa * gravedad_jupiter
peso_luna = masa * gravedad_luna

#Datos de salida
print("SU PESO EN LA LUNA ES", peso_luna, "kgs")
print("SU PESO EN JUPITER ES", peso_jupiter, "kgs")
print("SU PESO EN MARTE ES", peso_marte, "kgs")