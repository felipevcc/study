# manejo del error en palindromo al colocar algo vacio

def palindrome(string):
    try:
        # condicional para cadenas vacias
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings")