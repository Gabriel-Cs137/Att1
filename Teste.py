from tkinter import *
from tkinter import ttk
import tkinter as tk

x = 0
def soma():
    pass

root = tk.Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

def cor1():
    pass


ttk.Label(frm, text=f"Clique no botão :D, {x}").grid(column=0, row=0)
ttk.Button(frm, text="Botão", command = soma).grid(column=0, row=2)
root.mainloop()
