#Escriba un programa que pregunte cuantos números se van a introducir, pida esos números (que puedan ser decimales) y calcule su suma.

def nums_cantidad():
    x = int(input("Cuantos numeros se van a introducir? "))
    return x 

def nums(cantidad): 
    n = []
    for i in range(1, cantidad + 1): 
        num = float(input(f"Numero {i}: ")) 
        n.append(num) 
    return sum(n)

if __name__ == '__main__':
    print('La suma total de los numeros es:', nums(nums_cantidad()))


    
