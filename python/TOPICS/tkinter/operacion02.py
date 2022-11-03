from tkinter import *

ventana = Tk()

ventana.title("Operacion")
ventana.geometry('200x100')
ventana.configure(bg= 'CadetBlue')
def suma():
    resultado = 3*4
    mensaje = Message(ventana, text= resultado)
    mensaje.pack()
    mensaje.place(x=160, y=0)


button = Button(text= 'calcular', command= suma, bg= 'white')
button.pack()
button.place(x=10, y=32)

ventana.mainloop()