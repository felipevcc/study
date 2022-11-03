class Multiplicacion:
    def __init__(self,num1,num2):
        self.numero1 = num1
        self.numero2 = num2
    def operacion(self):
        resultado = self.numero1 * self.numero2
        print(resultado)

objeto = Multiplicacion(3,6)
objeto.operacion()