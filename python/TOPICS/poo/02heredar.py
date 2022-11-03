#Clase padre e hija
#Heredar

print('_______Ejemplo1_______\n')

class Carro():#Clase padre
    def __init__(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    def operacion(self):
        resultado = self.numero1 + self.numero2
        print(resultado)

class Carro1(Carro):#Clase hija
    pass

class Carro2(Carro1):#Clase hija
    pass

one = Carro(30,50)
one.operacion()


two = Carro1(10,20)
two.operacion()

three = Carro2(48, 50)
three.operacion()

#_________________________________

#clase padre

print('\n_______Ejemplo2_______\n')

class Operacion1:
    def __init__(self,numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2
    def suma(self):
        print("La suma es:", self.num1 + self.num2)
#clase hija
class Operacion2(Operacion1):
    def multiplicacion(self):
        print("La multiplicacion es: ", self.num1 * self.num2)
operacion1 = Operacion1(10,20)
operacion1.suma()
operacion2 = Operacion2(10,40)
operacion2.multiplicacion()

#_________________________________

print('\n_______Ejemplo3_______\n')

class Condicion:
    def __init__(self,nombre,edad):
        self.name = nombre
        self.age = edad
    def condicion(self):
        if self.age >= 18:
            print('Eres mayor de edad')
        else:
            print('Eres menor de edad')

edad2 = int(input('Cual es tu edad?'))
objeto1 = Condicion('Luis', edad2)
objeto1.condicion()