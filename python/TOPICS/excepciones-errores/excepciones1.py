#EXCEPCIONES

x = 'Luis' #si se quita esta variable entra a except

try: #si no hay errores y se cumple entra aqui
    print(x)
     
except: #excepcion, si hay errores o no se cumple algo
    print('No tienes definida la variable')

print('\n')

#_____________________________________________________
#un error puede ser si se opera con 0, aunque la sintaxis este bien 

def divide(num1,num2):
    #Asi se soluciona para que siga corriendo el programa
    try:
        return num1/num2
    except ZeroDivisionError:
        print('No se puede divir entre 0')
        return 'operacion erronea'
print(divide(8,0))

print('terminado')

#_____________________________________________________
print('\n')

#Para saber que error es:
try:
    a=float('ayy')
except ValueError as e:
    print(e)

print('\n')

#_______________________________________________________
#raise es para mostrar un error personalizado

def evaluaEdad(edad):

    if edad < 0:
        raise TypeError('No se permiten edades negativas') 
        #la extension y el mensaje son personalizables
        #Lo unico es que la extension del error debe existir en python

    if edad < 20:
        return 'Eres muy joven'
    elif edad < 40:
        return 'Eres joven'
    elif edad < 65:
        return 'Eres maduro'
    elif edad < 100:
        return 'Cuidate...'

print(evaluaEdad(-15))

# otro ejemplo de raise en ./ejemplos/03.py
