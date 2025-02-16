# Criação de Label em tkinter

import tkinter

window = tkinter.Tk()

window.title('Label')
window.geometry('200x300')

label = tkinter.Label(window, text='Primeiro Label', font=("Comic Sans MS", 20, 'bold'), bg="#ffed86", fg="#DE3163") 
# Label(
        # window, 
        # text='texto do label', -- texto da label
        # font=('nome da fonte', tamanho, 'propriedade da fonte'), -- qual fonte irá utilizar, o tamanho da fonte, se será negrito/sublinhado/itálico
        # bg='código hexadecimal', -- cor do fundo
        # fg='código hexadecimal' -- cor do texto
    # )

label.grid(column=0, row=0) # renderiza o widget na tela

window.mainloop()