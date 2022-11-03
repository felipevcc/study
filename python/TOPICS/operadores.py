#OPERADORES

#Operadores Arimetricos
# + suma
# - esta
# * multiplicacion
# / division
# % modulo (para obtener el residuo de la division)
# ** exponenciacion
# // aproximacion 

#Operadores Relacionales
# == comparacion
# < > menor que..., mayor que... 
# != diferente a...
# += , -= , /= , <= , etc...

#Operadores Logicos
# and, or, not = line 50
# in, not in

#entero (int), float, complex
 
numero1 = 10 
numero2 = 20
resultado = numero1 + numero2
print(resultado)

#da 2.2, pero como es aproximacion da 2
numero3 = 11
numero4 = 5
resultado1 = numero3 // numero4
print(resultado1)

#sumar en la misma variable
numero5 = 10
numero5 += 15
print(numero5)

numero_1 = 10
numero_2 = 15
numero_1 += numero_2
print(numero_1)

#comparacion 
comp1 = 10
comp2 = 15
print(comp1 == comp2)

comp3 = 10
comp4 = 15
print(comp1 != comp2)



#DOS CONDICIONES EN UNA (and, or, not)

#and (las dos condiciones se deben cumplir)
x = 3
y = 5
print(x == 3 and y == 6)

#or (solo una condicion se debe cumplir)
a = 3
b = 5
print(a == 3 or b == 6) 

#not (negacion)
c = 3
d = 5
print(not(c == d))
    #c NO es igual a d

#True o False
frutas = ["manzana", "pera"] 
print("banano" in frutas)
print("banano" not in frutas)





