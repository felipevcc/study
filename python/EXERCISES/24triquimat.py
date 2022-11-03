#Matriz (Juego)
triqui = [['O','X','O'],
          ['X','O','X'],
          ['X','O','O']] 

#Filas
f1 = ['']*3
f2 = ['']*3
f3 = ['']*3

#Columnas
c1 = ['']*3
c2 = ['']*3
c3 = ['']*3

#Diagonales
d1 = ['']*3
d2 = ['']*3

p1 = 0; p2 = 0; p3 = 0; p4 = 0; p5 = 0; p6 = 0; p7 = 0; p8 = 0

#Opciones
for i in range(3):
    for j in range(3):
        if i == 0:
            f1[p1] = triqui[i][j]
            p1 += 1
        if i == 1:
            f2[p2] = triqui[i][j]
            p2 += 1
        if i == 2:
            f3[p3] = triqui[i][j]
            p3 += 1
        if j == 0:
            c1[p4] = triqui[i][j]
            p4 += 1
        if j == 1:
            c2[p5] = triqui[i][j]
            p5 += 1
        if j == 2:
            c3[p6] = triqui[i][j]
            p6 += 1
        if i==j:
            d1[p7] = triqui[i][j]
            p7 += 1
        if i+j == 2:
            d2[p8] = triqui[i][j]
            p8 += 1

def verificacion(lista):
    if lista[1] == lista[0] and lista[2] == lista[0]:
        print('Ganó jugador', lista[1])

verificacion(f1)
verificacion(f2)
verificacion(f3)
verificacion(c1)
verificacion(c2)
verificacion(c3)
verificacion(d1)
verificacion(d2)
