#tkinter

#En linux manjaro se debe intalar el paquete tk, sudo pacman -S tk
#En linux ubuntu es sudo apt-get install python3-tk

from tkinter import * #importar todos los modulos de tkinder

ventana = Tk() #frame principal #siempre debe ir de primero

ventana.title("Hola mundo")
ventana.geometry('400x300') #tamaño de la vente

def myfuncion(): #aqui no hay necesidad de cerrarla
    #print('hola mundo')
    ventana.configure(bg='CadetBlue')

texto = Label(ventana, text='Digite su nombre', bg= 'CadetBlue', foreground= 'white').place(x=50, y=40) #x = horizontal, y = vertical
#label.place() = asi tambien se coloca
boton = Button(ventana, text= 'Click\npls', command= myfuncion, bg= 'orange', activebackground='CadetBlue', foreground= 'white', activeforeground='white', width=4, height=2, anchor= 'center', justify= 'center', relief= 'groove', overrelief= 'raised', borderwidth=5)
#n, ne, e, se, s, sw, w, nw, or center para: ,anchor('')
boton.pack() #Tambien se puede colocar asi en vez de a la derecha
boton.place(x=50, y=90)

boton2 = Button(ventana, bitmap= 'error', width=40, height=20, bg='pink', bd=None, disabledforeground=None) #bd es border
#Para bitmap: error, hourglass, question, warning, questhead
#diabledforeground para no poder dar click
boton2.pack()

entry = Entry(ventana).place(x=40, y=65)

variable = StringVar()
def prueba():
    print('Se ha elegido la opcion ' + variable.get())


radiobutton = Radiobutton(text= 'Opcion1', value= 1, variable= variable, command= prueba)
radiobutton.pack()
radiobutton.place(x = 130, y=95)
radiobutton2 = Radiobutton(text= 'Opcion2', value= 2, variable= variable, command= prueba)
radiobutton2.pack()
radiobutton2.place(x = 130, y=115)

ventana.mainloop() #abrir ventana, para que se ejecute el frame principal, siempre debe ir de ultimo
