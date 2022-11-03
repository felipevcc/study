#TIPOS/CLASES
tipoString = "hola mundo" #string (str): cadenas de texto
tipoEntero = 4 #int: para especificar un entero
tipoFloat = 4.6 #float: para especificar un decimal

#______________________________________________________________
#para saber el tipo de dato que almacena una variable
nombre = "Felipe"
print(type(nombre)) 

edad = 17 
print (type(edad))

#______________________________________________________________
#para pasar de numero a texto
edad = str(17)
print (type(edad))

#ó

edad = "17"
print (type(edad))

#______________________________________________________________
#3 TIPOS DE DATOS EN PYTHON
#int
#float
#complex

tipoComplex = 2j
print(type(tipoComplex))

#complex solo se puede sumar o operar por si mismo
complex1 = 2j
complex2 = 3j
resultado = complex1 + complex2
print(resultado)

#se pueden transferir de int a float y de float a int
tipoFloat = int(2.5)
tipoInt = float(2)

#_________________________________________________________________
#TIPO BOOLEAN
#son para crear afirmaciones, falso o verdadero
tipoBoolean = True
print(type(tipoBoolean))