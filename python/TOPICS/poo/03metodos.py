#__init__
#Almacena o hereda valores

class Ropa:
    def __init__(self):
        self.marca = "Nike"
        self.talla = "M"
        self.color = "Blanco"

camiseta = Ropa()
print(camiseta.marca, camiseta.talla, camiseta.color)


class Carro:
    def __init__(self, precio, categoria):
        self.price = precio
        self.category = categoria
        
chevrolet = Carro(1000, "4x4")
print(f"El precio y la categoria son: {chevrolet.price} {chevrolet.category}")


class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 + n2
        self.producto = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(2,3)
print(operacion.producto)

#____________________________

#__iter__
#Realiza iteraciones

class Numero:
    def __iter__(self):
        self.x = 2
        return self
    def __next__(self):
        i = self.x
        self.x += 1
        return i

obj1 = Numero()
obj2 = iter(obj1)
print(next(obj2))
print(next(obj2))