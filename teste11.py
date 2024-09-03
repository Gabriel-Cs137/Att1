from tkinter import *
from tkinter import ttk
import sqlite3 

root = Tk()  # cria a janela (precisa de um loop)
corzim = 'blue'

class Funcs():
    # Suas funções já existentes...

    def troca_aba(self):
        # Obtém o índice da aba atual
        aba_atual = self.abas.index(self.abas.select())
        
        # Troca para a outra aba (índices 0 e 1)
        nova_aba = 1 if aba_atual == 0 else 0
        self.abas.select(nova_aba)
    
class Application(Funcs): 
    def __init__(self):
        self.root = root  # permite que a variável root seja chamada dentro da classe
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.cria_db()
        self.Menus()
        root.mainloop()  # Loop que mantém a janela

    def tela(self):  # Configura as dimensões da tela e sua cor
        self.root.title('Cadastro de cliente')  # Coloca um título na janela
        self.root.configure(background=corzim)  # Define a cor de fundo
        self.root.geometry("788x588")  # Define o tamanho da janela
        self.root.resizable(False, False)  # Define se o tamanho da tela pode ser alterado
        self.root.maxsize(width=988, height=700)  # Define o tamanho máximo da janela
        self.root.minsize(width=550, height=450)  # Define o tamanho mínimo da janela

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='pink', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def widgets_frame1(self):
        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background= '#dfe3ee')
        self.aba2.configure(background='white')

        self.abas.add(self.aba1, text = 'Aba 1')
        self.abas.add(self.aba2, text = 'Aba 2')

        self.abas.place(relx = 0, rely = 0, relwidth= 0.98, relheight= 0.98)

        # Botão para trocar de aba
        self.bt_troca_aba = Button(self.aba1, text="Trocar Aba", bd=2, bg='#107db2', fg='white', 
                                   font=('verdana', 8, 'bold'), command=self.troca_aba)
        self.bt_troca_aba.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # Seus outros widgets...

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label='Opções',menu = filemenu)
        menubar.add_cascade(label='Sobre', menu = filemenu2)

        filemenu.add_command(label='Sair', command = Quit)
        filemenu2.add_command(label= 'Limpa Cliente',command= self.limpa_tela) 

# Chama a classe para iniciar o programa 
Application()
