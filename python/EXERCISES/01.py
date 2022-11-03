#EJERCICIOS


#1
latupla = ("yo", "el", "ella")
lista_latupla = list(latupla)
lista_latupla.remove("el")
latupla = tuple(lista_latupla)
print(latupla)


#2
latupla1 = ("nosotros", "vosotros", "ellos")
lista_latupla1 = list(latupla1)
lista_latupla1.insert(2,"yo")
latupla1 = tuple(lista_latupla1)
print(latupla1)


#3
ordenar = [4, 5, 8, 10, 6]
lista_ordenar = list(ordenar)
lista_ordenar.sort()
ordenar = tuple(lista_ordenar)
print(ordenar)


#4
#datos de entrada
frutas_añadidas = 5
frutas_iniciales = (frutas_añadidas/2)

#proceso
frutas_totales = frutas_iniciales + frutas_añadidas
valor_frutas = (7 % frutas_añadidas)
valor_total = (valor_frutas * frutas_totales)

#datos de salida
print(frutas_iniciales)
print(frutas_totales)
print(valor_frutas)
print(valor_total)


