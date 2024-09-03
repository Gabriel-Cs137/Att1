from tkinter import *
from tkinter import ttk
import sqlite3 

root = Tk()
corzim = 'gray'
tamanho_tela = "788x588"

class Funcs:
    def conecta_db(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor()
        print('Conectando ao banco')

    def desconecta_db(self):
        self.conn.close()
        print('Desconectou o db')

    def cria_db(self):
        self.conecta_db()
        # Criando DB
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_cliente varchar(40) NOT NULL,
                telefone integer(20),
                cidade varchar(40)
            );
        """)
        self.conn.commit()
        print('Db Criado')
        self.desconecta_db()

    def mostra_aba(self, aba):
        # Oculta todos os frames
        self.frame1.place_forget()
        self.frame2.place_forget()

        # Mostra o frame solicitado
        if aba == 1:
            self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        elif aba == 2:
            self.frame2.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
    def confirmar(self):
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            senha2 = self.conf_senha_entry.get()

            if nome:
                if senha:
                    if senha2:
                        if senha == senha2:
                            if senha == nome:
                                print('Usuário e senha não podem coincidir.')
                            else:
                                print('passou')
                                self.frame2.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
                        else:
                            print('Senhas não coincidem.')
                    else:
                        print('Confirme a senha.')
                else:
                    print('Senha não preenchida.')
            else:
                print('Nome de usuário não preenchido.')

class Aplication(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()

        self.mostra_aba(1)

        root.mainloop()
    
    def tela(self):
        self.root.title('Loja melhor que a da Edni')
        self.root.configure(background=corzim)
        self.root.geometry(tamanho_tela)
        self.root.resizable(True, True)
        self.root.maxsize(width=988, height=700)
        self.root.minsize(width=550, height=450)

    def frames(self):

        self.frame1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='pink', highlightthickness=3)
        self.frame2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='pink', highlightthickness=3)
    
    def widgets(self):
        # Botão para trocar para o frame1
        self.bt_mostra_frame1 = Button(self.frame2, text="Frame2", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                command=lambda: self.mostra_aba(1))
        self.bt_mostra_frame1.place(relx=0.90, rely=0.85, relwidth=0.1, relheight=0.15)

        # Botão para trocar para o frame2
        self.bt_mostra_frame2 = Button(self.frame1, text="Frame1", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                command=lambda: self.mostra_aba(2))
        self.bt_mostra_frame2.place(relx=0.90, rely=0.85, relwidth=0.1, relheight=0.15)

        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.frame2.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        # Label e entrada || Nome
        self.lb_nome = Label(self.frame1, text='Nome', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.02)

        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.05, relwidth=0.8)

        # Label e entrada || Senha
        self.lb_senha = Label(self.frame1, text='Senha', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_senha.place(relx=0.05, rely=0.12)

        self.senha_entry = Entry(self.frame1)
        self.senha_entry.place(relx=0.05, rely=0.15, relwidth=0.8)

        # Label e entrada || Nome
        self.lb_conf_senha = Label(self.frame1, text='Confirme a senha:', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_conf_senha.place(relx=0.05, rely=0.22)

        self.conf_senha_entry = Entry(self.frame1)
        self.conf_senha_entry.place(relx=0.05, rely=0.25, relwidth=0.8)

        # Botão para confirmar senha
        self.bt_passar = Button(self.frame1, text="Passar", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                command=self.confirmar)
        self.bt_passar.place(relx=0.73, rely=0.31, relwidth=0.12, relheight=0.10)

# Inicializa a aplicação
Aplication()
