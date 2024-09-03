from tkinter import *
from tkinter import ttk

def term():
    nome = entry_nome.get()
    senha1 = entry_senha1.get()
    senha2 = entry_senha2.get()

    if nome:
        if senha1:
            if senha2:
                if senha1 == senha2:
                    if senha1 == nome:
                        label_resultado.config(text='Usuário e senha não podem coincidir.', foreground="red")
                    else:
                        label_resultado.config(text='Cadastro realizado com sucesso', foreground="green")
                else:
                    label_resultado.config(text='Senhas não coincidem.', foreground="red")
            else:
                label_resultado.config(text='Confirme a senha.', foreground="red")
        else:
            label_resultado.config(text='Senha não preenchida.', foreground="red")
    else:
        label_resultado.config(text='Nome de usuário não preenchido.', foreground="red")

root = Tk()
root.title("Cadastro de Usuário")

# Frame para organizar os elementos
frm = ttk.Frame(root, padding=20)
frm.grid()

# Rótulos e campos de entrada
ttk.Label(frm, text="Cadastro de Usuário").grid(column=0, row=0, columnspan=2, pady=10)

ttk.Label(frm, text="Usuário:").grid(column=0, row=1, sticky=W)
entry_nome = ttk.Entry(frm, width=30)
entry_nome.grid(column=1, row=1, pady=5)

ttk.Label(frm, text="Senha:").grid(column=0, row=2, sticky=W)
entry_senha1 = ttk.Entry(frm, show="*", width=30)
entry_senha1.grid(column=1, row=2, pady=5)

ttk.Label(frm, text="Confirme a Senha:").grid(column=0, row=3, sticky=W)
entry_senha2 = ttk.Entry(frm, show="*", width=30)
entry_senha2.grid(column=1, row=3, pady=5)

# Botão para cadastrar
ttk.Button(frm, text='Cadastrar', command=term).grid(column=0, row=4, columnspan=2, pady=10)

# Label para exibir o resultado
label_resultado = ttk.Label(frm, text="")
label_resultado.grid(column=0, row=5, columnspan=2)

root.mainloop()
