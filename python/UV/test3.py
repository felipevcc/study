#Arreglos
#Van desde 0 
nombre = [None]*4
nombre[0] = 'Sarah'
nombre[1] = 'Felipe'
nombre[2] = 'Luis'
nombre[3] = 'Jorge'
print(f"Nombres: {' '.join(nombre)}")
print(nombre[2])

print('\n-------------------------\n')

Notas = [None]*3
Notas[0] = 2.7; Notas[1] = 3.1; Notas[2] = 2.5
print(Notas)
x = Notas[0] + Notas[1]
print(x)

print('\n----------------------------\n')

conj = [None]*10
conj_par = []
conj_impar = []

for i in range(len(conj)):
    conj[i] = int(input('Digite un numero: >'))
    if conj[i] % 2 == 0:
        conj_par.append(conj[i])
    else:
        conj_impar.append(conj[i])

#print(f'Numeros: {' - '.join(conj)}')
suma = sum(conj)
print('\nSuma de los numeros: ', suma)
print('\nNumeros pares: ', conj_par)
print('\nNumeros impares: ', conj_impar)