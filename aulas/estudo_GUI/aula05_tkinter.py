# criando entradas no tkinter ENTRY

import tkinter as tk

window = tk.Tk()

window.title('Entry')

window.geometry('400x400')

entry = tk.Entry( # Entry() cria um input na tela, para que o usuário digite algo
    window,
    width=12,
)

label = tk.Label(
    window,
    text='Nome:'
)

label.grid(
    row=0,
    column=0
)

entry.grid(
    row=0,
    column=1
)

def Limpa():
    nome = entry.get()
    label.configure(text=nome)
    entry.delete('0', 'end')

button = tk.Button(
    text='limpar',
    command=Limpa
)

button.grid(
    row=1,
    column=0
)

entryDisable = tk.Entry(
    window,
    width=20,
    state='disable' # state define se o texto será possível editar ou não
)

entryDisable.grid(row=2, column=0)

window.mainloop()