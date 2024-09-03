from tkinter import *
from tkinter import ttk
import sqlite3 

root = Tk()  # cria a janela (precisa de um loop)
corzim = 'blue'
tamanho_tela = "788x588"

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.cidade_entry.delete(0,END) 

    def conecta_db(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor()
        print('Conectando ao banco')

    def desconecta_db(self):
        self.conn.close()
        print('Desconectou o db')

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

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

    def add_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" 
            INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)
        """, (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" 
            SELECT cod, nome_cliente, telefone, cidade FROM clientes ORDER BY nome_cliente ASC; 
        """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_db()

    def DoubleClick(self, event):
        self.limpa_tela()
        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo,))
        self.conn.commit()
        self.desconecta_db()
        self.limpa_tela()
        self.select_lista()
    
    def altera_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ? , telefone = ? , cidade = ? 
                            WHERE cod = ? """, (self.nome,self.telefone,self.cidade,self.codigo))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpa_tela()

    def mostra_aba(self, aba):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        if aba == 1:
            self.frame1.pack(fill=BOTH, expand=True)
        elif aba == 2:
            self.frame2.pack(fill=BOTH, expand=True)
    

    
class Application(Funcs): 
    def __init__(self):
        self.root = root  # permite que a variável root seja chamada dentro da classe
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.cria_db()
        self.select_lista()
        self.Menus()
        root.mainloop()  # Loop que mantém a janela

    def tela(self):  # Configura as dimensões da tela e sua cor
        self.root.title('Cadastro de cliente')  # Coloca um título na janela
        self.root.configure(background=corzim)  # Define a cor de fundo
        self.root.geometry(tamanho_tela)  # Define o tamanho da janela
        self.root.resizable(True, True)  # Define se o tamanho da tela pode ser alterado
        self.root.maxsize(width=988, height=700)  # Define o tamanho máximo da janela
        self.root.minsize(width=550, height=450)  # Define o tamanho mínimo da janela

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='pink', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='pink', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):

        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background= 'gray')
        self.aba2.configure(background='white')

        self.abas.add(self.aba1, text = 'Aba 1')
        self.abas.add(self.aba2, text = 'Aba 2')

        self.abas.place(relx = 0, rely = 0, relwidth= 0.98, relheight= 0.98)



        # Botão limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                                command=self.limpa_tela)  # Especifica o frame onde o botão será inserido
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=2, bg='#107db2', fg='white',
                                 font=('verdana', 8, 'bold'),command= lambda: self.mostra_aba(1))  # Especifica o frame onde o botão será inserido
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão novo
        self.bt_novo = Button(self.aba1, text="Novo", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                              command=self.add_cliente)  # Especifica o frame onde o botão será inserido
        self.bt_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Alterar
        self.bt_alterar = Button(self.aba1, text="Alterar", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                                 command= self.altera_cliente )  # Especifica o frame onde o botão será inserido
        self.bt_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), 
                                command=self.deleta_cliente)  # Especifica o frame onde o botão será inserido
        self.bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Label e entrada || código
        self.lb_codigo = Label(self.aba1, text='Código', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.aba1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Label e entrada || nome
        self.lb_nome = Label(self.aba1, text='Nome', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ## Label entrada || Telefone
        self.lb_telefone = Label(self.aba1, text='Telefone', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.55)

        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx=0.05, rely=0.65, relwidth=0.35)

        ## Label entrada || Cidade
        self.lb_cidade = Label(self.aba1, text='Cidade', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_cidade.place(relx=0.45, rely=0.55)

        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.45, rely=0.65, relwidth=0.40)

    def lista_frame2(self):

        self.listaCli = ttk.Treeview(self.frame2, height=3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Codigo')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')

        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.03, rely=0.1, relwidth=0.90, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.93, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind('<Double-1>', self.DoubleClick)
    
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
