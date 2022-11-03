class Calc():
    def __init__(self, par1, par2):
        self.one = par1
        self.two = par2
    def operacion(self):
        resultado = self.one * self.two
        print(resultado)

class Calc2(Calc):
    pass

obj1 = Calc2(20, 2)
obj1.operacion()