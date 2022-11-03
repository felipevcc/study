candidatos = [[2, 'Camilo'], [1, 'Felipe'], [3, 'Juan'], [1, 'Sebastian']]

#Ejemplo para operar los numeros
def x():
    candidatos[2][0] += 1
x()

#Ver el mayor
mayor = candidatos[0]
for i in range(1,4):
    if candidatos[i] > mayor:
        mayor = candidatos[i]
print(f'El ganador es {mayor[1]}, con una cantidad de votos de {mayor[0]}')


