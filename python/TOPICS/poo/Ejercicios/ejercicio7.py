#Realizar un programa que le pregunte al usuario por una pregunta y a medida que falle le muestre el
#el numero de vidas que le quedan de la siguiente forma

# |-|
# |--|
# |---|

x = 3
print('|---|')
for i in range(x, 0, -1):
    
    x = input('Cual es la capital de Colombia?')
    
    class Funcion:
        def __init__(self, pregunta):
            self.pregunta = pregunta

        def respuesta(self):
            if self.pregunta == 'cali':
                print('Respuesta correcta')
                exit()
            else:
                print('Respuesta incorrecta')
                if i == 3:
                    print('|--|')
                elif i == 2:
                    print('|-|')
                elif i == 1:
                    print('| |')
                    print('Se te agotaron las vidas')
                else:
                    print('Error 104')
    
    obj1 = Funcion(x)
    obj1.respuesta()

