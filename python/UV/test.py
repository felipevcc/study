def pot2(n):
   if(n==0):
      resp = 1 #caso base
   else:
      resp = 2 * pot2(n-1)#caso recursivo
   return resp

def fact(n):
   if(n==0):
      resp = 1 #caso base
   else:
      resp = n * fact(n-1)
   return resp

def fibo(n):
   if(n==0):#caso base
      resp = 0
   elif(n==1):#caso base
      resp = 1
   else:
      resp = fibo(n-1)+fibo(n-2)
   return resp


print(pot2(0))#1
print(pot2(5))

print(fact(0))#1
print(fact(3))

print(fibo(0))#0
print(fibo(1))#1
print(fibo(5))#5