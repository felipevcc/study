#Error de division

def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1,num2):
    #Asi se soluciona para que siga corriendo el programa
    try:
        return num1/num2
    except ZeroDivisionError:
        print('No se puede divir entre 0')
        return 'operacion erronea'


op1=int(input("Introduce el primer número: "))

op2=int(input("Introduce el segundo número: "))

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
    print(suma(op1,op2))

elif operacion=="resta":
    print(resta(op1,op2))

elif operacion=="multiplica":
    print(multiplica(op1,op2))

elif operacion=="divide":
    print(divide(op1,op2))

else:
    print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")