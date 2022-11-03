numero = 20
#bucle while
while numero > 10:
    print(numero)
    #iterador
    numero -= 1 #si se pone despues de break va a seguir
    break #para el bucle


#ejercicio ejecutando con el bucle while

#input es una funcion
#input hablamos de entrada de datos
#output hablamos de salida de datos
age = int(input("Cual es tu edad"))
if age >= 18:
    print("Puedes entrar a la pelicula")
else:
    print("No puedes entrar a la pelicula")
