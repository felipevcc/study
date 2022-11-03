class Eps:
    def __init__(self, nombre, edad, telefono, genero):
        self.name = nombre
        self.age = edad
        self.cel = telefono
        self.genero = genero
    

class usuario1(Eps):
    def informacion(self):
        print(f'Hola {self.name}!, ya quedaste registrado en nuestro sistema con los siguientes datos:\nEdad: {self.age}, Telefono: {self.cel}, Genero: {self.genero}')
class usuario2(Eps):
    def informacion2(self):
        print(f'Hola {self.name}!, ya quedaste registrado en nuestro sistema con los siguientes datos:\nEdad: {self.age}, Telefono: {self.cel}, Genero: {self.genero}')

nombre = input('Como te llamas?')
edad = int(input('Cual es tu edad?'))
telefono = input('Cual es tu numero telefonico?')
genero = input('Que genero eres?')

usuario1 = usuario1(nombre, edad, telefono, genero)
usuario1.informacion()

nombre2 = input('Como te llamas?')
edad2 = int(input('Cual es tu edad?'))
telefono2 = input('Cual es tu numero telefonico?')
genero2 = input('Que genero eres?')

usuario2 = usuario2(nombre2, edad2, telefono2, genero2)
usuario2.informacion2()