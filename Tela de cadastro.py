from tkinter import *
from tkinter import ttk

root = Tk()  # cria a janela (precisa de um loop)

corzim = 'blue'

class Application:  # classe para organização
    def __init__(self):
        self.root = root  # permite que a variável root seja chamada dentro da classe
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        
        root.mainloop()  # Loop que mantém a janela

    def tela(self):  # Configura as dimensões da tela e sua cor
        self.root.title('Cadastro de cliente')  # Coloca um título na janela
        self.root.configure(background=corzim)  # Define a cor de fundo
        self.root.geometry("788x588")  # Define o tamanho da janela
        self.root.resizable(True, True)  # Define se o tamanho da tela pode ser alterado
        self.root.maxsize(width=988, height=700)  # Define o tamanho máximo da janela
        self.root.minsize(width=550, height=450)  # Define o tamanho mínimo da janela

    def frames_da_tela(self): 
        self.frame1 = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='pink', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='pink', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        # Label e entrada || Nome
        self.lb_nome = Label(self.frame1, text='Nome', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        # Label entrada || Senha
        self.lb_senha = Label(self.frame1, text='Senha', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_senha.place(relx=0.05, rely=0.55)

        self.senha_entry = Entry(self.frame1, text='Senha', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.senha_entry.place(relx=0.05, rely=0.65, relwidth=0.35)

        # Label entrada || Confirmação de Senha
        self.lb_senha2 = Label(self.frame1, text='Confirmação de senha', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_senha2.place(relx=0.45, rely=0.55)

        self.senha2_entry = Entry(self.frame1, text='Senha', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.senha2_entry.place(relx=0.45, rely=0.65, relwidth=0.40)

        # Label para exibir mensagens de erro ou sucesso
        self.lb_mensagem = Label(self.frame1, text='', bg='#dfe3ee', fg='Black', font=('verdana', 8, 'bold'))
        self.lb_mensagem.place(relx=0.05, rely=0.8, relwidth=0.9)

        def term():
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            senha2 = self.senha2_entry.get()

            if nome:
                if senha:
                    if senha2:
                        if senha == senha2:
                            if senha == nome:
                                self.lb_mensagem.config(text='Usuário e senha não podem coincidir.', foreground="red")
                            else:
                                self.lb_mensagem.config(text='Cadastro realizado com sucesso', foreground="green")
                        else:
                            self.lb_mensagem.config(text='Senhas não coincidem.', foreground="red")
                    else:
                        self.lb_mensagem.config(text='Confirme a senha.', foreground="red")
                else:
                    self.lb_mensagem.config(text='Senha não preenchida.', foreground="red")
            else:
                self.lb_mensagem.config(text='Nome de usuário não preenchido.', foreground="red")

        # Botão Cadastrar
        self.bt_cadastrar = Button(self.frame1, text="Cadastrar", bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=term)
        self.bt_cadastrar.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.15)

# Chama a classe para iniciar o programa
Application()
