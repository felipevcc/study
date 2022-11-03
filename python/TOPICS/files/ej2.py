# line 2 y 3 para que la ruta del file funcione desde cualquier parte
import os
FILE_PATH=os.path.dirname(__file__)

#Ruta normal= ./test-files/numbers.txt

def read():
    numbers = []
    # con utf aseguramos que el file no tenga caracteres raros
    with open(f"{FILE_PATH}/test-files/numbers.txt", "r", encoding="utf-8") as f:
        # leer cada linea con ciclo
        for line in f:
            numbers.append(int(line))
    print(numbers)

    # COLOCAMOS LA RUTA ASI COMO EN LOS OPEN PARA QUE FUNCIONE

def write():
    names = ["Facundo", "Miguel", "Pepe", "Christian"]
    # se crea el file names
    with open(f"{FILE_PATH}/test-files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name + '\n')

def run():
    read()
    write()

if __name__ == '__main__':
    run()

"""
NOTAS

Para que podamos correr la ruta desde cualquier parte entonces
lo hacemos como en el ejemplo anterior

-------------------

Cuando se trabaje con datos y tenga un .csv con los decimales en , y no .
en:
with open("./archivos/numeros.csv", “r”, encoding=“utf-8”, decimal=",") as f
con añadir decimal="," no tendrán que editar nada y pasan a procesar sus datos de inmediato.

-------------------

Si no se una el context manager (with) entonces siempre que
hagamos .write() tendremos que cerrar el archivo con .close(),
Asi:
f = open("/path/file.txt", "r")
f.write('something')
f.close()

"""
