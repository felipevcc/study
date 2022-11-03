print ("===========La empresa mi futuro===========\n")
n = int (input ("Digite la cantidad n de empleados: "))
m = int (input ("Digite la cantidad m de semanas: "))
datos = [[0 for x in range (m+1)] for y in range (n)]      
data2 = []

for j in range (n):
  name = (str (input ("\nDigite el nombre del empleado "+str(j+1)+": ")))
  datos [j][0]  = name 
  for c in range (m):
    horas = (int (input ("Digite la cantidad de horas trabajadas en la semana "+ str(c+1) +": ")))
    datos [j][c+1] = horas   
    total = sum (datos[j][1:])
  data2.append (total)

opc = int (input ("\nDigite 1 para ver los salarios ó digite 2 para ver la nómina semanal: "))
if (opc == 1):
  print ("Pagos por empleado:")
  for i in range (n):
    print ("El salario del empleado", datos[i][0] , "es $" ,float(10000*data2[i]))   

# Suma de cada semana
data = []
if (opc == 2):
  print ("\nPagos por semana:")
  for h in range (n): 
    for z in range(1,m+1): 
      if h == 0:
        total = datos[h][z]
        data.append(total)
      else:
        k = z-1
        data[k] = data[k] + datos[h][z]
        
for d in range(1, len(data)+1):
  ubic = d-1
  print ("En la semana", d ,"se pagó de nómina: $",10000*data[ubic])