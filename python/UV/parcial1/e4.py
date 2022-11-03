personas = int(input('Cantidad de personas: '))
tiempo_libre = 0
actividad = 0
tv = 0
leer_hrs = 0

for i in range(personas+1):
    tiempo_libre = int(input('\nTiempo libre:\n1 = Menos de 6 horas | 2 = Entre 6 y 9 horas | 3 = Mas de 9 horas\n'))

    actividad = int(input('\nActividad principal:\n1 = Leer | 2 = Ver television | 3 = Hacer deporte | 4 = Dormir\n'))

    if tiempo_libre >= 1 and tiempo_libre <= 3 and actividad >= 1 and actividad <= 4:
        
        if tiempo_libre == 3 and actividad == 1:
            leer_hrs += 1
        if actividad == 2:
            tv += 1
    else:
        print('No coincide')

caso1 = (leer_hrs * 100)/personas

print(f'\nPorcentaje de personas que tienen más de 9 horas libres y que prefieren leer: %{caso1}')
print('\nPersonas que prefieren ver television:', tv)
