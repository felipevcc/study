"""
PROBLEMA:
Presente la función asociada al botón de tal
forma que se calculen 3 datos: el total a pagar (DVD a
$23000 y Blu-ray a $65000), el IVA (16%) y la ganancia
neta (total-IVA)
"""

from tkinter import *

ventana = Tk()
ventana.geometry('300x220')
ventana.title('CALCULO')
ventana.configure(bg='grey')

#-------------ENTRADAS-------------

titulo1 = Label(ventana, text="Cantidad DVD", bg='grey', foreground= 'white', font=('Helvetica', 11))
titulo1.pack()
titulo1.place(x=44,y=25)
cdvd = Entry(ventana, width=12)
cdvd.pack()
cdvd.place(x=160, y=20)

titulo2 = Label(ventana, text="Cantidad Blu-ray", bg='grey', foreground= 'white', font=('Helvetica', 11))
titulo2.pack()
titulo2.place(x=44, y=48)
cbr = Entry(ventana, width=12)
cbr.pack()
cbr.place(x=160, y=45)

#-------------PROCESO--------------

DVD = 23000
BLURAY = 65000
IVA_POR = .16

def calculo():
    dvd = int(cdvd.get())* DVD
    bluray = int(cbr.get())*BLURAY
    precio = dvd + bluray
    valor_pagar.delete(0, END) #elimina desde el inicio hasta el final
    valor_pagar.insert(0, precio) 

    iva = precio * IVA_POR
    iva_recaudado.delete(0,END)
    iva_recaudado.insert(0, iva)

    val_neto = precio - iva #total de todo
    ganancia_neta.delete(0, END)
    ganancia_neta.insert(0, val_neto)

#Boton confirmacion
boton = Button(ventana, text="Calcular valores", command=calculo, bg='white')
boton.pack()
boton.place(x=90,y=82)

#-------------SALIDAS---------------

titulo3 = Label(ventana, text="Valor a pagar", bg='grey', foreground= 'white', font=('Helvetica', 11))
titulo3.pack()
titulo3.place(x=44, y=128)
valor_pagar = Entry(ventana, width=12)
valor_pagar.pack()
valor_pagar.place(x=160, y=125)

titulo4 = Label(ventana, text="IVA recaudado", bg='grey', foreground= 'white', font=('Helvetica', 11))
titulo4.pack()
titulo4.place(x=44, y=153)
iva_recaudado = Entry(ventana, width=12)
iva_recaudado.pack()
iva_recaudado.place(x=160, y=150)

titulo5 = Label(ventana, text="Ganancia neta", bg='grey', foreground= 'white', font=('Helvetica', 11))
titulo5.pack()
titulo5.place(x=44, y=178)
ganancia_neta = Entry(ventana, width=12)
ganancia_neta.pack()
ganancia_neta.place(x=160, y=175)

ventana.mainloop()