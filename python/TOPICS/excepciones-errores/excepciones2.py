#assert

#assert es si no se cumple imprima el mensaje como un error (AssertionError)

# syntax:
# assert condicion, "mensaje de error"

def celsius(kelvin):
    # la condición puede llevar parentesis (son arbitrarios)
    assert kelvin >= -273.15,'Estas dead pa'
    return kelvin - 273
print(celsius(273))
print(celsius(-273.16))

# otro ejemplo en ./ejemplos/04.py