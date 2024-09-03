from tkinter import *
from tkinter import ttk
x = 0

def soma():
    global x
    x += 1
    print(f'O botão foi clicado {x} vezes')
    ttk.Label(frm, text=f"Clique no botão :D, {x}").grid(column=0, row=0)

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text=f"Clique no botão :D, {x}").grid(column=0, row=0)
ttk.Button(frm, text="Botão", command = soma).grid(column=0, row=2)
root.mainloop()
