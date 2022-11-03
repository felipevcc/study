from tkinter import *

window = Tk()

#Palco
#Pre-venta
#2

#---------Window Config---------

window.title("UV-Teatro")
window.geometry('400x260')
window.configure(bg="white")

#------------Inputs-------------

ubicacion = Label(window, text="Ubicación", bg='white', font=('helvetica', 11))
ubicacion.pack()
ubicacion.place(x=80, y=21)
eubicacion = Entry(window, width=20)
eubicacion.pack()
eubicacion.place(x=190, y=20)

tipo = Label(window, text="Tipo", bg='white', font=('helvetica', 11))
tipo.pack()
tipo.place(x=80, y=41)
etipo = Entry(window, width=20)
etipo.pack()
etipo.place(x=190, y=40)

cantidad = Label(window, text="Cantidad", bg='white', font=('helvetica', 11))
cantidad.pack()
cantidad.place(x=80, y=61)
ecantidad = Entry(window, width=20)
ecantidad.pack()
ecantidad.place(x=190, y=60)

#------------Process------------

def process():
    matriz = [['Palco', 'Pre-venta'],['Palco', 'Venta normal'],['Platea', 'Pre-venta'],['Platea', 'Venta normal']]
    precios = [22000,29000,30000,38000]
    m = [eubicacion.get(),etipo.get()]

    cant = ecantidad.get()
    for i in range(4):
        if m == matriz[i]:
            precio = precios[i] * int(cant)
            aporte = float(precio) * 0.15
            ev_venta.delete(0,END)
            ev_venta.insert(0,precio)

            ev_aporte.delete(0,END)
            ev_aporte.insert(0,aporte)

    
#opciones
calc = Button(window, text="Calcular valores", command=process, bg= 'white', activebackground='#EAEAEA')
calc.pack()
calc.place(x=140, y=120)

#------------Outputs-------------

v_venta = Label(window, text="Valor venta", bg='white', font=('helvetica', 11))
v_venta.pack()
v_venta.place(x=80, y=189)
ev_venta = Entry(window, width=20)
ev_venta.pack()
ev_venta.place(x=190, y=187)

v_aporte = Label(window, text="Valor aporte", bg='white', font=('helvetica', 11))
v_aporte.pack()
v_aporte.place(x=80, y=209)
ev_aporte = Entry(window, width=20)
ev_aporte.pack()
ev_aporte.place(x=190, y=207)

window.mainloop()
