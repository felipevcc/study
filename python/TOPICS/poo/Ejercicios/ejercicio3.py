#1
class Suma:
    def __init__(self,n1,n2):
        self.numero1 = n1
        self.numero2 = n2
    def resultado(self):
        resultado = self.numero1 + self.numero2
        print(resultado)

objeto = Suma(4,3)
objeto.resultado()

#2
def pares():
    for x in range(0, 31, 2):
        print(x, end = ' ')
pares()
