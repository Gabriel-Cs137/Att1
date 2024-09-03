from tkinter import *
from tkinter import ttk

nome = ''
senha1 = ''
senha2 = ''

def nomein():
    nome = entry_nome.get()
def senhain():
    senha1 = entry_senha1.get()
def senhacon():
    senha2 = entry_senha2.get()

    
def term():
    global nome
    global senha1
    global senha2

    if nome:
        if senha1:
            if senha2:
                if senha1 == senha2:
                    if senha1 == nome:
                        Label.config(text='Usuário e senha não podem coincidir.', foreground="red")
                    else:
                        Label.config(text='Cadastro realizado com sucesso', foreground="green")
                else:
                    Label.config(text='Senhas não coincidem.', foreground="red")
            else:
                Label.config(text='Confirme a senha.', foreground="red")
        else:
            Label.config(text='Senha não preenchida.', foreground="red")
    else:
        Label.config(text='Nome de usuário não preenchido.', foreground="red")
            
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text=f"Cadastro de usuario").grid(column=0, row=0)
ttk.Button(frm, text="Usuario: ", command = nomein).grid(column=0, row=2)
ttk.Button(frm, text="Senha: ", command = senhain).grid(column=0, row=3)
ttk.Button(frm, text="Confirme a senha: ", command = senhacon).grid(column=0, row=4)
ttk.Button(frm, text='Cadastrar' , command = term).grid(column=0, row=5)


root.mainloop()


