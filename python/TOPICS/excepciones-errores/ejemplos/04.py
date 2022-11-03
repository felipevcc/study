# ejemplo con assert

num = input('Ingresa un número: ')
assert num.isnumeric(), 'Debes ingresar un número'
print('Numero digitado:', num)

# .isnumeric() = metodo que devuelve True si es un numero o False si no lo es en una cadena de texto