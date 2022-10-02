import tkinter
from tkinter import ttk

ventana = tkinter.Tk()

ventana.geometry('175x300')
ventana.title('Comida Favorita')

v = tkinter.StringVar(ventana, '1')

values = {
    'Pizza': 'Pizza',
    'Hamburguesa': 'Hamburguesa',
    'Papas Fritas': 'Papas Fritas',
    'Ensalada': 'Ensalada',
    'Sushi': 'Sushi',
    'Tacos': 'Tacos',
    'Otro': 'Otro'}

for (text, value) in values.items():
    tkinter.Radiobutton(ventana, text=text, variable=v, value=value).pack(side='top', ipady=5)


# RESET RADIO BUTTON
def reset():
    v.set('1')


tkinter.Button(ventana, text='Reiniciar', command=reset).pack(side='bottom', ipady=5)

ventana.mainloop()
