# Criação de botões em tkinter

import tkinter as tk

window = tk.Tk()

window.title('Buttons')

window.geometry("300x300")


label = tk.Label(window, text='primeiro botão')
label.grid(column=0, row=0)

button = tk.Button(     # Button() cria um botão na tela
    window, #parametro padrao (nao sei oq faz)
    text='explodir', # define o texto dentro do botão
    bg='#ebedef', # cor do fundo
    font=('malgun gothic', 8,'bold'), # propriedades da fonte
    width='20', # largura do botão, também existe a propriedade height
    fg='green', # cor da fonte
)

button.grid(column=1, row=0)

def MudarTexto(): # função que será atribuída ao botão
    print('olá mundo')
    label.configure(text='olá mundo!', fg='red')
    

button = tk.Button(
    window, 
    text='botão',
    command=MudarTexto # paramentro que atribui uma função ao clique do botão
)

button.grid(column=0, row=1) # renderiza o botão na tela


window.mainloop()