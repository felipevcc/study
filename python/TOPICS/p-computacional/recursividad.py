# RECURSIVIDAD

# El limite de recursividad es 1000

# Conocer/mostrar el limite de la recursividad:
"""import sys
print(sys.getrecursionlimit())"""

#===============================================

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

#=============================================
print('\n=======================================\n')

def pot2(n):
    if n == 0:
        resp = 20
    else:
        resp = 2 * pot2(n-1)
    return resp
print(pot2(5))

#=============================================
print('\n=======================================\n')

#potencias
def pot2(n):
   if(n==0):
      resp = 1 #caso base
   else:
      resp = 2 * pot2(n-1)#caso recursivo
   return resp

#factoriales
def fact(n):
   if(n==0):
      resp = 1 #caso base
   else:
      resp = n * fact(n-1)
   return resp

#fibonacci
def fibo(n):
   if(n==0):#caso base
      resp = 0
   elif(n==1):#caso base
      resp = 1
   else:
      resp = fibo(n-1)+fibo(n-2)
   return resp

#exponentes
print(pot2(0))#1
print(pot2(5))

#factoriales
print(fact(0))#1
print(fact(3))

#fibonacci
print(fibo(0))#0
print(fibo(1))#1
print(fibo(5))#5

#===============================================
print('\n=======================================\n')

def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
for i in range(10):
    print(rec_fib(i))

print('\nnumeros:\n')
print(rec_fib(5))
