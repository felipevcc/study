#datetime
import datetime

#Fecha de hoy
fecha = datetime.datetime.now()
print(fecha)

#Fechas creadas
fecha1 = datetime.date(2032, 10, 13) #datetime.date() es para crear solo la fecha sin la hora
print(fecha1)

fecha2 = datetime.datetime(2022, 9, 11)
print(fecha2)

#Diferencia de fechas
fecha3 = fecha - fecha2

if fecha == fecha2:
    print("Hoy es tu cumpleaños")
else:
    print(f"Faltan {fecha3} ")


#Colocas solo lo que quieres que salga
print(fecha.strftime("%A")) 