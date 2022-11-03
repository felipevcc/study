from tkinter import *
from googletrans import Translator

window = Tk()

#---------Window Config---------

window.title("Translate")
window.geometry('600x330')
window.configure(bg="white")

#------------Inputs-------------

title = Label(window, text="TRANSLATE", font=('Helvetica', 11, 'bold'), bg='#44A8F7', foreground='white', width=600, height=3)
title.pack()

ingrese = Label(window, text="Enter text", bg='white', font=('helvetica', 11))
ingrese.pack()
ingrese.place(x=265, y=80)
text = Entry(window, width=80)
text.pack()
text.place(x=16, y=110)

#------------Process------------

def translate(l):
    t = text.get()
    trans = Translator()
    try:
        t = trans.translate(t, dest=l)
        output = t.text
    except:
        output = '--No coincide--'
    output_final.delete(0,END)
    output_final.insert(0,output)

#langs
def lang1():
    translate('en')
def lang2():
    translate('de')
def lang3():
    translate('it') 

#opciones
lang_english = Button(window, text="English", command=lang1, bg= 'white', activebackground='#EAEAEA')
lang_english.pack()
lang_english.place(x=180, y=180)

lang_german = Button(window, text="German", command=lang2, bg= 'white', activebackground='#EAEAEA')
lang_german.pack()
lang_german.place(x=258, y=180)

lang_french = Button(window, text="French", command=lang3, bg= 'white', activebackground='#EAEAEA')
lang_french.pack()
lang_french.place(x=340, y=180)

#------------Outputs-------------

output_final = Entry(window, width=80)
output_final.pack()
output_final.place(x=16, y=260)

window.mainloop()