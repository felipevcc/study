#Realizar un programa que represente las figuras geometricas dependiendo de la clase punto
#2 o 3 figuras (sacandole el area)
print('Sistema de calculo de areas')
class Areas:
    def __init__(self, n1, n2):
        self.base = n1
        self.altura = n2
    def figuras(self):
        rectangulo = int(self.base * self.altura)
        print(f'El area del rectangulo es: {rectangulo}')

        triangulo_rec = int((self.base * self.altura)/2)
        print(f'El area del triangulo rectangulo es: {triangulo_rec}')

base = int(input('Digite la base'))
altura = int(input('Digite la altura'))

obj1 = Areas(base, altura)
obj1.figuras()
