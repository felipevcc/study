#______________________________________

#FUNCION INPUT
#edad = input("Cual es tu edad")
#print("tu edad es", edad)

#______________________________________

#CONDICIONALES
#regulares, anidados y ternarios

# = es asignar, == es de igual o comparar
a = 10
b = 20 

if a == b:
    print("a es igual a b")

#si se cumple la condicion lo imprime, si no no

#_______________________________________

#elif sirve para colocar mas condiciones

# if = si....
# elif = y si....
# else: = y si no....

"""edad = int(input("Cual es tu edad"))
#pasar_entero = int(edad)
if edad <= 13:
    print("Eres un niño")
elif edad < 17:
    print("Eres un adolecente")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("No cumples ninguno de los requisitos")"""

#_____________________________

"""calificacion = int(input("Cual fue la calificacion de alumno"))
condicional_ternario = "green" if calificacion > 3 else "red"
print(condicional_ternario)"""

#_____________________________

#declaracion de varias condiciones en una sola linea

"""calificacion1 = int(input("Cual fue la calificacion de alumno"))
condicional_varias = "green" if calificacion1 == 5 else "blue" if calificacion1 == 4 else "pink" if calificacion1 == 3 else "No tiene ningun valor"
print(condicional_varias)"""

#_____________________________-

#Con operadores logicos

x = 10 
y = 20
f = x + y

if f < 19 or f < 31 :
    print("Esta dentro del rango")
else:
    print("No esta dentro del rango")

"""edad = int(input("cual es tu edad?"))
if edad >= 0 and edad <= 10:
    print("Eres un niño")
else:
    print("Eres mayor de 10 años")"""

#__________________________

#pass es para evitar el error

d = 30
f = 40
t = d + f
print(t)
if d < f:
    #pass
    d = 60
print(d)
t = d + f
print(t)


t= "rojo"
if_ternario = "rojo" if t == "rojo" else "amarillo" if t == "amarillo" else "ninguna condicion se cumplio"
print(if_ternario)


colores = input("Cual es tu color favorito para tu camiseta?")
print("Color rojo") if colores == "rojo" else print("Color verde") if colores == "verde" else print("No tenemos ninguno de los colores digitados")