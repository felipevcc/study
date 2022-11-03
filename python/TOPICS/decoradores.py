# DECORADORES (decorators)

"""
Es una función que recibe como parametro otra funcion,
le añade cosas, y retorna una función diferente

Funcion que recibe como parametro otra funcion, la 
modifica creando una nested function porque es un 
closure ejecuta la funcion dentro y retorna esta funcion
a la funcion superior

"""

# Ejemplo 1

# decorador
def decorador(func):
    def nested():
        print('Esto se añade a mi función original')
        func()
    return nested 

# funcion original
def saludo():
    print('¡Hola!\n')
saludo()

saludo = decorador(saludo)
saludo()

"""
Es como un closure, pero añadiendole la funcionalidad
mencionada en la linea 4

"""

"""
______________________________

Para que esto se vea de una mejor manera usamos "sugar syntax"
(azucar sintáctica):

"""

# Ejemplo de sugar syntax:

def decor(func):
    def envoltura():
        print('Modificacion a funcion original')
        func()
    return envoltura

@decor
def greeting():
    print('Hello')

greeting()

"""
el @ indica que la funcion de abajo esta decorada
lo que hace es darle como parametro la funcion que esta abajo

"""

# ==============================

print('\n===== EJEMPLOS =====\n')

# EJEMPLOS

# 1: Pasar texto a mayusculas

def mayusculas(func):
    def nested(texto):
        return func(texto).upper()
    return nested

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje\n'

print(mensaje('Cesar'))


# 2: Medir el tiempo de ejecucion de funciones

from datetime import datetime

""" 
El metodo .now() devuelve la fecha y hora de cuando se 
ejecuta la linea de codigo

.total_seconds() devuelve unicamente los segundos calculados

"""

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {float(time_elapsed.total_seconds())} segundos')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo1(nombre='Cesar'):
    print('Hola ' + nombre)

random_func()
suma(5,5)
saludo1()

"""
*args = parametro de funcion que agarra todos los valores posicionales

**kwargs = parametro de funcion que agarra todos los valores nombrados

con esto no importa cuantos parametros le pasemos a la funcion, igual se va a ejecutar

"""


# 3 decoradores recibiendo parametros

print('\n')

def with_custom_message(message):

    def with_message(function):
        print(f'{message}')
    
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    
    return with_message

@with_custom_message('Hello')
def multiply(a, b):
    c = a * b
    print(f'The result of {a} * {b} is {c}')

multiply(10, 2)

