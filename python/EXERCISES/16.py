reprobados = 0
aprobados = 0
acum = 0.0

nota = 0.0
while nota >= 0 and nota <= 5:
    nota = float(input('\nDigite la nota: '))
    if nota >= 3:
        aprobados += 1
    else:
        reprobados += 1
    acum = acum + nota
    

if acum == 0:
    print(f'\nAPROBADOS: {aprobados}\nREPROBADOS: {reprobados}')
else:
    promedio = acum / (reprobados + aprobados)
    print(f'\nAPROBADOS: {aprobados}\nREPROBADOS: {reprobados}\nPROMEDIO DE NOTAS: {promedio}')

    
