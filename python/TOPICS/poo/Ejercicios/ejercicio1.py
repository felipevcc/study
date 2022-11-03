#1
class Carro:
    def __init__(self, precio, categoria):
        self.price = precio
        self.category = categoria
        
chevrolet = Carro(1000, "4x4")
print(f"El precio y la categoria son: {chevrolet.price} {chevrolet.category}")
#print("El precio y la categoria son:", chevrolet.price , chevrolet.category)


#2
class Calculadora:
    def __init__(self,numero1,numero2):
        self.one = numero1
        self.two = numero2

suma = Calculadora(30,10)
resultado = suma.one + suma.two
print("30 + 10 = ", resultado)
