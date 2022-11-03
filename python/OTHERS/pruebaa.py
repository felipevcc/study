"""datos = [[3,7,4],
         [9,6,2],
         [7,5,10]]"""


#s = 0
"""for i in range(0,3,1):
    for j in range(0,3,1):
        if (i<2 and datos[i][j]%2==0):
            s = s + datos[i][j]
print(s)"""

"""for i in range(0,3,1):
    for j in range(0,3,1):
        if (i+j==2):
            print(datos[i][j])"""

"""for i in range(0,3,1):
    for j in range(0,3,1):
        if (j==1):
            s = s + datos[i][j]
        else:
            s = s - datos[i][j]

print(s)
"""

"""def funcionMisterio(n):
    if n==0:
        return 1
    else:
        return (2*n) + funcionMisterio(n-1)
print(funcionMisterio(5))"""

matriz = [['Palco', 'Pre-venta'],['Palco', 'Venta normal'],['Platea', 'Pre-venta'],['Platea', 'Venta normal']]

m = ['Palco', 'Pre-venta']
if m == matriz[0]:
    print('funciona')


