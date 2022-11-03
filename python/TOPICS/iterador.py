# ITERADORES

"""
Los iteradores permiten ahorrar espacio, ya que no 
tenemos que crear una lista, ni almacenarlos en algun
lado, simplemente utilizamos y listo, no se almacenan todos

"""

frutas = ["manzana", "pera", "mora"]

iteracion = iter(frutas)
print(next(iteracion)) #Llama a manzana
print(next(iteracion)) #Llama a pera
print(next(iteracion)) #Llama a mora

print('')


# Para evitar hacer el next manualmente:

my_list = [1,2,3,4,5] # iterable
my_iter = iter(my_list) # iterador

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

"""
Esto se puede hacer de una manera mas sencilla:

for element in my_list:
    print(element)

"""

print('\n')

# ==============================
# Detro de funciones:

class MyClase:
    def __iter__(self):
        self.a = 1
        return self # devolviendo valores a mi funcion
    def __next__(self):
        x = self.a
        self.a += 1
        return x

objeto = MyClase()
objeto2 = iter(objeto)

print(next(objeto2))
print(next(objeto2))

print('')

# Otro ejemplo:

class EvenNumbers:
    
    """
    Clase que implementa un iterador de todos los números 
    pares, o los números pares hasta un maximo

    """

    def __init__(self, max=None):
        self.max = max 

    def __iter__(self):
        self.num = 0
        return self 

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num 
            self.num += 2 
            return result 
        else:
            raise StopIteration









