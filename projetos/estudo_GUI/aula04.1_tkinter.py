import tkinter as tk

window = tk.Tk()

window.title('geometria grid')

window.geometry('300x300')

# METODO GRID

buttonGrid = tk.Button(
    window,
    text='grid',
    width='12'
)

buttonGrid.grid( # grid() renderiza o widget em forma de tabela, utilzando dos paramentros: column e row, para alterar as posições horizontais e verticais
    row=0,
    column=0
)

buttonGrid = tk.Button(
    window,
    text='grid',
    width=20,
)

buttonGrid.grid(
    row=1,
    column=0
)

buttonGrid = tk.Button(
    window,
    text='grid',
    width=20
)

buttonGrid.grid(
    row=1,
    column=1,
    padx=2,     # pad: padding externo do objeto
    ipadx=10,   # ipad: padding interno do objeto
    ipady=10,
    rowspan=2,
    columnspan=2
)

buttonGrid = tk.Button(
    window,
    text='grid',
    width='12'
)

buttonGrid.grid(
    row=2,
    column=0
)

buttonGrid = tk.Button(
    window,
    text='grid',
    width='12'
)

buttonGrid.grid(
    row=3,
    column=0
)

window.mainloop()