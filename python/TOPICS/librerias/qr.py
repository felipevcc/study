import qrcode 
#from PIL import Image

def script():
    print('\n---GENERADOR DE CODIGOS QR---')
    contenido = input('\nEscribe lo que deseas codificar:\n')
    name = input('\nDigite el nombre del fichero: ')
    ext = input('\nDigite la extension: ')

    img=qrcode.make(contenido)
    try:
        f=open(f'{name}.{ext}', 'wb')
    except:
        print('\nUps! No coincide...\nVuelve a intentarlo')
    img.save(f)
    print('\nCodigo QR guardado exitosamente')

    def decision():
        pregunta = input('\n¿Deseas generar otro codigo QR? [si/no]')
        if pregunta == 'si':
            return script()
        elif pregunta == 'no':
            print('\nHas salido del sistema')
        else:
            print('\nNo coincide')
            return decision()
    decision()

script()

#________________________

#Otras formas de hacerlo:

#1:
"""
with open('test.png', 'wb') as f:
    img.save(f)"""

#2:
"""
data = ('holapeople')
filename = 'code.png'

img= qrcode.make(data)
img.save(filename)"""