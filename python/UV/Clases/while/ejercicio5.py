#Calculo de la pension de una persona

print('\n---PENSIÓN---')
año = int(input('\nDigite su año de ingreso: '))
edad = int(input('\nDigite su edad de ingreso: '))
año_final = int(input('\nHasta que año desea calcular: ')) #El ejercicio no dice hasta que año hay que calcular
val_nuevo = 80
val_antiguo = 100
salud_porcentaje = 0.12

if año >= 1995 and año <= año_final:
    pension = (val_nuevo * año) + edad
    while año < año_final:
        año = año + 1
        edad = edad + 1
        pension = pension + (val_nuevo * año) + edad
    salud = pension * salud_porcentaje
    pension_neta = pension - salud
    print('\nRESULTADOS')
    print(f'\nSueldo bruto para el {año_final}: ${pension}\nDescuento por salud: ${salud}\nSueldo neto: ${pension_neta}')

elif año < 1995 and año <= año_final:
    pension = (val_antiguo * año) + edad
    while año < año_final:
        año = año + 1
        edad = edad + 1
        pension = pension + (val_antiguo * año) + edad
    salud = pension * salud_porcentaje
    pension_neta = pension - salud
    print('\nRESULTADOS')
    print(f'\nSueldo bruto para el {año_final}: ${pension}\nDescuento por salud: ${salud}\nSueldo neto: ${pension_neta}')
else: 
    print('\nNo coincide')

