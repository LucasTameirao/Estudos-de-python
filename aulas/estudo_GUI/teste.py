import tkinter as tk

flag = False
win=""

def setflag(event):
    global flag
    flag = False
    
#function that prints the entry
def entry_function(e=None):
    global flag,win
    name = entry.get()
    if not flag:
        win = tk.Toplevel()
        win.geometry('100x100')
        win.bind('<Destroy>', setflag)
        tk.Label(win, text=name).pack()
        flag = True
        win.geometry("+%d+%d" % (x + 600, y + 300))
    else:
        tk.Label(win, text=name).pack()
        
     

 #Setup for the window
window = tk.Tk()
window.title("Title_Name")
window.geometry("500x500")
window.bind('<Return>', entry_function)
x = window.winfo_x()
y = window.winfo_y()

#widgets
label = tk.Label(window, text = "Manual:", bg = "dark grey", fg = "white")
entry = tk.Entry(window)
button = tk.Button(window,text = "submit",
                   command = entry_function)

#widget placement
label.place(x=0,y=20)
entry.place(x=52,y=21)
button.place(x=177, y=18)

window.mainloop()