#strip
#Ejemplos de palindromo: Luz azul, oso

def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    if palabra[::] == palabra[::-1]:
        return True
    else:
        return False

def run():
    palabra = input('Digite una palabra: ')
    if palindromo(palabra):
        print('Es palíndromo')
    else:
        print('No es palíndromo')

if __name__=='__main__':
    run()
