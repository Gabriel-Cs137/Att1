from tkinter import *

root = Tk()  # cria a janela (precisa de um loop)

corzim = 'blue'

def atualizar_cor_fundo(app, nova_cor):
    global corzim
    corzim = nova_cor
    app.root.configure(background=corzim)  # Atualiza a cor de fundo da janela
    print(corzim)

class Application:  # classe para organização
    def __init__(self):
        self.root = root  # permite que a variável root seja chamada dentro da classe
        self.tela()
        self.frames_da_tela()
        self.criar_botoes()
        
        root.mainloop()  # Loop que mantém a janela

    def tela(self):  # Configura as dimensões da tela e sua cor
        self.root.title('Cadastro de cliente')  # Coloca um título na janela
        self.root.configure(background=corzim)  # Define a cor de fundo
        self.root.geometry("788x588")  # Define o tamanho da janela
        self.root.resizable(True, True)  # Define se o tamanho da tela pode ser alterado
        self.root.maxsize(width=988, height=700)  # Define o tamanho máximo da janela
        self.root.minsize(width=400, height=300)  # Define o tamanho mínimo da janela

    def frames_da_tela(self):  # Adiciona o parâmetro self
        self.frame1 = Frame(self.root, bd=4, bg='white',
                            highlightbackground='pink', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg='white',
                            highlightbackground='pink', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def criar_botoes(self):
        # Botão azul
        self.bt_azul = Button(self.frame1, text="Azul", command=lambda: atualizar_cor_fundo(self, 'blue'))
        self.bt_azul.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão rosa
        self.bt_rosa = Button(self.frame1, text="Rosa", command=lambda: atualizar_cor_fundo(self, 'pink'))
        self.bt_rosa.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão branco
        self.bt_branco = Button(self.frame1, text="Branco", command=lambda: atualizar_cor_fundo(self, 'white'))
        self.bt_branco.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)

# Chama a classe para iniciar o programa
app = Application()
