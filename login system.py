from tkinter import *
from tkinter import simpledialog, messagebox
import json
import time
import re


def entrar_conta():
    try:

        conta = {}

        with open("arquivo_login.json", "r") as r:
            conta = json.load(r)

        conta['login_nome'] = simpledialog.askstring("Login", "Digite seu nome:")
        if not conta['login_nome'] or len(conta['login_nome']) > 50 or conta['login_nome'] != conta['nome']:
            messagebox.showerror("Erro", "Nome inválido!")
            return

        conta['login_senha'] = simpledialog.askstring("Login", "Digite sua senha:", show="*")
        if not conta['login_senha'] or len(conta['login_senha']) > 50 or conta['login_senha'] != conta['senha']:
            messagebox.showerror("Erro", "Senha inválida!")
            return

        conta['ultimo_login'] = time.strftime("%H:%M:%S")
        
        try:
            with open("arquivo_login.json", "r") as u:
                dados = json.load(u)
        except FileNotFoundError:
            dados = {}

        dados['ultimo_login'] = conta['ultimo_login']

        with open("arquivo_login.json", "a") as u:
            json.dump(conta['ultimo_login'], u, indent=4)


        messagebox.showinfo("Sucesso", "Conta logada com sucesso!")

    except Exception as e:
        print(f"Error em: {e}")



def criar_conta():
    try:
        conta = {}
        padrao_email = r'^[0-9a-fA-F]{12}@pucmg\.puc\.com\.br'

        conta['nome'] = simpledialog.askstring("Cadastro", "Digite seu nome (máx. 50 caracteres):")
        if not conta['nome'] or len(conta['nome']) > 50:
            messagebox.showerror("Erro", "Nome inválido!")
            return

        conta['idade'] = simpledialog.askstring("Cadastro", "Digite sua idade:")
        if not conta['idade'].isdigit() or len(conta['idade']) > 2:
            messagebox.showerror("Erro", "Idade inválida!")
            return

        conta['sexo'] = simpledialog.askstring("Cadastro", "Digite seu sexo [M/F]:").strip().upper() [0]
        if conta['sexo'] not in ["M", "F"]:
            messagebox.showerror("Erro", "Sexo inválido! Use M ou F.")
            return

        conta['senha'] = simpledialog.askstring("Cadastro", "Crie uma senha forte:", show="*")
        if not conta['senha'] or len(conta['senha']) > 50:
            messagebox.showerror("Erro", "Senha inválida!")
            return

        conta['email'] = simpledialog.askstring("Cadastro", "Digite seu email:")
        if not conta['email'] or not re.match(padrao_email, conta['email']):
            messagebox.showerror("Erro", "Email inválido!")
            return
        

        conta['numero'] = simpledialog.askstring("Cadastro", "Digite seu número de telefone:")
        if not conta['numero'].isdigit() or len(conta['numero']) < 8:
            messagebox.showerror("Erro", "Número de telefone inválido!")
            return

        conta['data_de_criacao'] = time.strftime("%H:%M:%S")

        with open("arquivo_login.json", "w") as f:
            json.dump(conta, f, indent=4)

        messagebox.showinfo("Sucesso", "Conta criada com sucesso!\nArquivo salvo como 'arquivo_login.json'.")

    except Exception as e:
        messagebox.showerror(f"Erro inesperado: {e}")


janela = Tk()
janela.title("Login Conta")

texto = Label(janela, text="Clique no botão para criar ou entrar em sua conta")
texto.grid(column=0, row=0)

botao_criar = Button(janela, text="Criar conta", command=criar_conta)
botao_criar.grid(column=0, row=1)

botao_logar = Button(janela, text="Entrar na conta", command=entrar_conta)
botao_logar.grid(column=0, row=2)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2)

janela.mainloop()
