"""
ARCHIVOS


MODOS DE APERTURA:
r -> Solo lectura
r+ -> Lectura y escritura
w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
a -> Añadido (agregar contenido). Crea el archivo si éste no existe
a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

"""

#------ WITH Y OPEN --------

"""With = En python se denomina como un “manejador contextual”. 
Controla el flujo del archivo y se asegura que el archivo no 
se rompa en caso de que se cierre inesperadamente.""" 

"""Open = Abre el archivo. Recibe parámetros, obligatoriamente 2:
- ruta del archivo y modo de apertura"""

# --- asi:
#with open('../files.txt', 'r+') as f:
#    jpgdata = f.read()
#f.close()

"""r: Abre el fichero en modo lectura.
r+: Si quieres leer y escribir en el fichero.
w: Para sobreescribir el contenido.
a: Para añadir al final del fichero en el caso de que ya exista."""

#mas info: https://python-intermedio.readthedocs.io/es/latest/open_function.html#:~:text=La%20funci%C3%B3n%20open%20devuelve%20lo,es%20importante%20devolverlo%20y%20cerrarlo.

# - Se suele colocar "as f" debido a que hace referencia a file
