#GENERADORES

# Ahorran memoria y puedo guardar secuencias infinitas
# Son iteradores con Sguar Syntax 
# ____________________________________ 

#Funcion normal que imprime pares:

def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num*2)
        num = num + 1

    return miLista

print(generaPares(10))

print(' ')

#____La misma funcion pero con yield:____

#yield es un return iterable

def genPares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num = num + 1

devuelvePares = genPares(10)

for i in devuelvePares:
    print(i)

print(' ')
#_____La misma funcion pero que devuelva de uno en uno_____

#next va de numero en numero
def genPars(limite):
    num = 1
    while num < limite:
        yield num * 2
        num = num + 1

devuelvePares = genPars(10)

print(next(devuelvePares))
print('Aqui podria ir mas codigo')

print(next(devuelvePares))
print('Aqui podria ir mas codigo')

print(next(devuelvePares))
print('Aqui podria ir mas codigo')

print('\n')
#____________________________________________________________

#Elementos y sub Elementos

#Con * significa que va a recibir un numero indeterminado de elementos y los recibe en forma de tupla
def devuelve_ciudades(*ciudades):
    #bucles for anidados
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento
ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

print(' ')

#____La misma funcion pero con yield from:____

#yield from es para tomar sub elementos de un elemento

def devuelve_ciudades1(*ciudades):
    #bucles for anidados
    for elemento in ciudades:
        yield from elemento
ciudades_devueltas1 = devuelve_ciudades1('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(ciudades_devueltas1))
print(next(ciudades_devueltas1))

# ========================================================== 

print('')

# Platzi

""" 
Yield funciona como un return, pero en vez de acabar la funcion,
la pausa hasta donde quede. Entonces al volver a llamar a la funcion 
va a comenzar despues de donde se pausó
"""

def my_gen():

    print("Hello world!") 
    n = 0 
    yield n 

    print("Hello heaven!")
    n = 1 
    yield n 

    print("Hello hell!")
    n = 2 
    yield n 

iterador = my_gen()
print(next(iterador)) # Hello world!
print(next(iterador)) # Hello heaven!
print(next(iterador)) # Hello hell!

# _________________________________________ 

print('')

"""
Es mejor usar generadores e iteradores en vez de ciclos o otras cosas 
cuando son demasiados datos
"""

# Generator expression 

my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list] # List comprehension
my_second_gen = (x*2 for x in my_list) # Generator expression 

print(my_second_gen) # cada llamado es un elemento, no todos de una 

# ========================================= 

print('\nFIBONACCI\n') 

from time import sleep

def fibo_gen(): 
    n1 = 0 
    n2 = 1
    counter = 0 
    
    while True:
        if counter == 0:
            counter += 1 
            yield n1 
        elif counter == 1:
            counter += 1 
            yield n2 
        else:
            aux = n1 + n2 
            n1, n2 = n2, aux 
            counter += 1 
            yield aux  
             
fibonacci = fibo_gen() 
for element in fibonacci:
    print(element) 
    sleep(1) # IMPORTANTE porque son numeros infinitos
    
