from tkinter import *

janela = Tk()

av1 = 0
entry_av1 = Entry(janela, width = 10)
entry_av1.pack()
entry_av1.place(x = 90, y = 50)

def somar_av1():
    global av1
    av1 = av1 + 1
    entry_av1.insert(0, int(av1))

botao_mais_av1 = Button(janela, text = '+', command = somar_av1)
botao_mais_av1.place(x = 40, y = 50)

janela.mainloop()