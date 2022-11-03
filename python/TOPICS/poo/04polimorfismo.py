class Carro:
    def __init__(self, precio, año):
        self.precio = precio
        self.año = año

#la clase responde a dos objetos
carro1 = Carro(2000, 1981)
print(carro1.precio)

carro2 = Carro(3000, 1985)
print(carro2.precio)