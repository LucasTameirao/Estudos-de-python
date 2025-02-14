import tkinter as tk
import tkinter.ttk

window = tk.Tk()

comboBox = tkinter.ttk.Combobox(window, state='readonly')

comboBox['values'] = ('selecione', "masculino", 'feminino', 'não binário', 'outros', 'prefiro não informar')
comboBox.current(0)
comboBox.grid(row=0, column=0)

window.mainloop()