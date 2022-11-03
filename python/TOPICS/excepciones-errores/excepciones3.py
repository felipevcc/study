#finally

"""
TRY: (intentar) En el try se coloca código que esperamos que pueda lanzar algún error.
EXCEPT: (excepto) En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
FINALLY: Siempre se va a ejecutar.

"""

try:
    a = input('Introduce el primer numero: ')
    b = input('Introduce el segundo numero: ')
    resultado = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print('Hay un error...')
else:
    print('Es posible elevar al cuadrado: ', resultado**2)
finally:
    print('Favor de revisar tus procedimientos')

"""
Un ejemplo de finally es si abrimos un archivo en un try en finally pordemos colocar 
que cierre ese archivo:

try:
    f = open("archivo.txt")
finally:
    f.close()

"""