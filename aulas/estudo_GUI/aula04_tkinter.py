# Maneiras de renderizar widgets no tkinter

import tkinter as tk

window = tk.Tk()

window.title('Geometria Place')

window.geometry('400x400')

# METODO PLACE

buttonPlace = tk.Button(
    window,
    text='place'
)

buttonPlace.place(x=200, y=200) # place() renderiza o widget com base na coordenada em que foi passada (x, y)

buttonPlace = tk.Button(
    window,
    text='place'
)

buttonPlace.place(x=100, y=80)


# METODO PACK

buttonPack = tk.Button( # Pack() renderiza o widget com base na rosa dos ventos, left, right, top, bottom
    window,
    text='esquerda',
    bg='red'
)

buttonPack.pack(
    side='left'
)

buttonPack = tk.Button(
    window,
    text='direita',
    bg='yellow'
)

buttonPack.pack(
    side='right'
)

buttonPack = tk.Button(
    window,
    text='cima',
    bg='blue'
)

buttonPack.pack(
    side='top'
)

buttonPack = tk.Button(
    window,
    text='baixo',
    bg='green'
)

buttonPack.pack(
    side='bottom'
)

window.mainloop()