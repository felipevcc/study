#BOOLEANOS (bool)

#Son un tipo de dato
#Costan de 2 valores, True or False

booleanos_type = True 
print(type(booleanos_type))


#la terminal dice si es falso o verdadero
print(10 > 12)


#para convertir a booleanos
afirmaciones= bool("hola")
print(type(afirmaciones))


#da True siempre que el numero no sea 0 o no sean simbolos, de lo contrario dará False
afirmaciones2 = bool(5)
print(afirmaciones2)

afirmaciones2 = bool(0)
print(afirmaciones2)

#comparaciones
comparacion1 = 10
comparacion2 = 11
comparacion = comparacion1 == comparacion2
print(type(comparacion))
print(comparacion)

comp1 = 10
comp2 = 10
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
