import tkinter
from tkinter import ttk

ventana = tkinter.Tk()

ventana.geometry('225x335')

label_saludo = tkinter.Label(ventana, text='Escoge tus deportes favoritos', bg='yellow', fg='black')
label_saludo.pack(ipadx=45, ipady=15, fill='x')

# CHECKBOX ABOUT SPORTS MULTIPLE SELECTS
v = tkinter.StringVar(ventana, '1')

values = {
    'Fútbol': 'Fútbol',
    'Baloncesto': 'Baloncesto',
    'Tenis': 'Tenis',
    'Natación': 'Natación',
    'Ciclismo': 'Ciclismo',
    'Atletismo': 'Atletismo',
    'Otro': 'Otro'}

for (text, value) in values.items():
    tkinter.Checkbutton(ventana, text=text, variable=v, onvalue=value).pack(side='top', ipady=5)


# RESET CHECKBOX
def reset():
    v.set('1')


tkinter.Button(ventana, text='Reiniciar', command=reset).pack(side='bottom', ipady=5)

ventana.mainloop()
