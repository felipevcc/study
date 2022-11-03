#Andres Felipe Villamizar / Grupo 81
#Julian Sanchez / Grupo 81

#Datos de entrada
porcentaje_iva = .19
porcentaje_costo = .61
porcentaje_gn = .20

producto = input("Digite el nombre del producto")
precio = float(input("Digite el precio del producto"))

#Proceso
iva = precio * porcentaje_iva
costo = precio * porcentaje_costo
ganancia_neta = precio * porcentaje_gn

#Datos de salida
print("Producto:", producto)
print("IVA:", iva)
print("Costo:", costo)
print("Ganancia neta:", ganancia_neta)