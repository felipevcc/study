"""
FACTORIALES
0! =                   = 1
1! = 1                 = 1
2! = 1 * 2             = 2
3! = 1 * 2 * 3         = 6
4! = 1 * 2 * 3 * 4     = 24
5! = 1 * 2 * 3 * 4 * 5 = 120

Lo que hace es multiplicar 5 por el fact de 4
Despues 4 por el factorial de 3
Despues 3 por el factorial de 2
Y asi sucesivamente 
"""

def fact_recursivo(n):
    if n == 0 or n == 1: #Caso base
        return 1
    return n * fact_recursivo(n-1) #Caso recursivo
    
print(fact_recursivo(5))
