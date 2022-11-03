# CLOSURES /cloushur/

# Nested functions = funciones anidadas

"""
Closures es cuando una variable que esta
en un scope superior es recordada por una 
funcion que esta en un scope inferior y 
desde la funcion superior debe retornar la 
nested function 

(Aunque se elimine la funcion superior podemos
seguir accediendo a la variable)

"""

# ejemplo:

def main():
    a = 1

    def nested():
        print(a)

    return nested 

my_func = main()
my_func()

del(main)

my_func()

"""
Reglas para encontrar un closure:

- Debemos tener una nested function
- La nested function debe referenciar un valor de un scope superior
- La función que envuelve la nested debe retornarla también

"""

# ejemplo 2:

def make_multiplier(x):

    def multiplier(n):
        return x * n 

    return multiplier 

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # 30
print(times4(5)) # 20
print(times10(times4(2))) # 80

"""
¿Donde se suelen ver los closures?

- En las clases, cuando una clase tiene solo un metodo
  se puede aplicar clousure como alternativa

- Cuando se trabaja con decoradores

"""

# ejemplo 3:

# que se repita un string segun las veces que le digamos

def repeater(n):

    def nested_repeater(string):
        assert type(string) == str, "Solo puedes utilizar strings"
        return string * n 

    return nested_repeater

def run():
    repeat = repeater(5)
    print(repeat("Hola"))
run()


# ejemplo 4:

def division(x):
    return lambda n: x/n

div1 = division(10)
print(div1(2)) # 5

div2 = division(30)
print(div2(3)) # 10

