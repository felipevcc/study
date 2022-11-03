from tkinter import *

ventana = Tk()

ventana.geometry('350x235')
ventana.title('Formulario')
ventana.configure(bg='grey')

nombre = StringVar()
apellido = StringVar()

def mensaje():
    mensaje = Message(ventana, text= f'Hola {nombre.get()} {apellido.get()}', width=140, bg='white')
    mensaje.place(x=105, y=188)

h1 = Label(ventana, text= 'FORMULARIO', bg= 'grey', foreground= 'white', font=('Helvetica', 13, 'bold')).place(x=115, y=20)

etiqueta1 = Label(ventana, text = 'Digita tu nombre', bg='grey', foreground= 'white', font=('Helvetica', 11, 'bold')).place(x=20, y=61)
nombreCaja = Entry(ventana, textvariable= nombre).place(x=150, y=60)

etiqueta2 = Label(ventana, text = 'Digita tu apellido', bg='grey', foreground= 'white', font=('Helvetica', 11, 'bold')).place(x=20, y=101)
cadaApellido = Entry(ventana, textvariable= apellido).place(x=150, y=100)

button = Button(ventana, text= 'Enviar', command= mensaje, bg='white').place(x=140, y=140)


ventana.mainloop()