adultos = int(input('Adultos que ingresan: '))
niños = int(input('Niños que ingresan: '))
dia = input('Dia de la funcion: ')

bol_adultos = 12000
bol_niños = 8000

oferta_jueves = 0.15

if adultos > 0:precio_adultos = bol_adultos * adultos

if niños > 0:
    precio_niños = bol_niños * niños

precio_total = precio_adultos + precio_niños

if dia == 'jueves':
    if adultos >= 3 and niños >= 2:
        oferta = precio_total * oferta_jueves
        precio_total = precio_total - oferta
        m = 'Utilizo la oferta de los jueves'
    else:
        m = 'No utilizo la oferta de los jueves'
else:
    m = 'No utilizo la oferta de los jueves'

print(f'\nPara el {dia}, {adultos} adultos y {niños} niños:\nEL valor a pagar es de ${precio_total} ({m}))')