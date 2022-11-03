# STATIC TYPING

# pasar a python de tipado dinamico a estatico

"""
mypy permite trabajar de una mejor manera con tipos:

desde consola: 
    mypy file.py --check-untyped-defs

con el comando nos dice los errores de tipos que hay
"""

# ejemplo con palindromo:

def palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
     print(palindrome("ana"))


# ejemplo con numero primo:

def primo(num: int) -> bool:
    verification = [i for i in range(1, num+1) if num % i == 0]
    return len(verification) == 2

def run2():
    print(primo(13))

# entry point
if __name__ == "__main__":
    run()
    run2()

var: str= "a"
print(type(var))
   
