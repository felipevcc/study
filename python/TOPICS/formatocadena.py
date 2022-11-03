#FORMATO DE CADENA
#Marcador de posicion

edad = 17

mensaje = 'Hola Luis, tienes {:.2f} años' #para colocar decimales, el '.' hace referencia a que despues del punto coloque '2' decimales y la 'f' de float
#El 2 es arbitrario

print(mensaje.format(edad)) #la variable edad va a entrar en las llaves de la variable mensaje


variable1 = 'Carlos'
variable2 = 'Luis'

mensaje2 = 'Hola {}, como estas {}?'
print(mensaje2.format(variable2, variable1)) #Aqui se organizan como quiera que vayan

variable3 = 'Felipe'
variable4 = 'Andres'

mensaje3 = 'Hola {1}, como estas {0}?' #tambien se pueden organizar desde aqui, dependiendo de como se haya colocado en format
print(mensaje2.format(variable3, variable4)) 
