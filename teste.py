import tkinter as tk
from tkinter import messagebox

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, E-mail: {self.email}"


class CadastroPessoas:
    def __init__(self):
        self.pessoas = []

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def listar_pessoas(self):
        return self.pessoas

    def remover_pessoa(self, pessoa):
        self.pessoas.remove(pessoa)


class ArquivoPessoas:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def salvar_pessoas(self, pessoas):
        with open(self.nome_arquivo, "w") as file:
            for pessoa in pessoas:
                file.write(f"{pessoa.nome},{pessoa.idade},{pessoa.email}\n")

    def carregar_pessoas(self):
        pessoas = []
        try:
            with open(self.nome_arquivo, "r") as file:
                for line in file:
                    nome, idade, email = line.strip().split(",")
                    pessoa = Pessoa(nome, idade, email)
                    pessoas.append(pessoa)
        except FileNotFoundError:
            pass
        return pessoas


class MenuOpcoes:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app

        self.frame = tk.Frame(root, bg="gray", width=150)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

        self.btn_cadastro = tk.Button(self.frame, text="Cadastro", command=self.main_app.exibir_cadastro)
        self.btn_cadastro.pack()

        self.btn_estoque = tk.Button(self.frame, text="Estoque", command=self.main_app.exibir_estoque)
        self.btn_estoque.pack()

        # Adicione mais botões para outros módulos aqui


class TelaLogin:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app
        self.root.title("Login")

        self.label_usuario = tk.Label(root, text="Usuário:")
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.pack()

        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()

        self.btn_login = tk.Button(root, text="Login", command=self.fazer_login)
        self.btn_login.pack()

    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        # Simulação de verificação de usuário e senha (substitua essa parte pela verificação real)
        if usuario == "admin" and senha == "1234":
            self.main_app.login_sucesso()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")


class InterfaceCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Pessoas")

        self.cadastro = CadastroPessoas()
        self.arquivo = ArquivoPessoas("pessoas.txt")
        self.menu = MenuOpcoes(self.root, self)

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1)

        self.label_idade = tk.Label(root, text="Idade:")
        self.label_idade.grid(row=1, column=0)

        self.entry_idade = tk.Entry(root)
        self.entry_idade.grid(row=1, column=1)

        self.label_email = tk.Label(root, text="E-mail:")
        self.label_email.grid(row=2, column=0)

        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=2, column=1)

        self.btn_adicionar = tk.Button(root, text="Adicionar Pessoa", command=self.adicionar_pessoa)
        self.btn_adicionar.grid(row=3, column=0, columnspan=2)

        self.btn_listar = tk.Button(root, text="Listar Pessoas", command=self.listar_pessoas)
        self.btn_listar.grid(row=4, column=0, columnspan=2)

        self.btn_remover = tk.Button(root, text="Remover Pessoa", command=self.remover_pessoa)
        self.btn_remover.grid(row=5, column=0, columnspan=2)

    def adicionar_pessoa(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        email = self.entry_email.get()

        if nome and idade and email:
            pessoa = Pessoa(nome, idade, email)
            self.cadastro.adicionar_pessoa(pessoa)
            self.limpar_campos()
            messagebox.showinfo("Sucesso", "Pessoa cadastrada com sucesso!")
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos!")

    def listar_pessoas(self):
        pessoas = self.cadastro.listar_pessoas()
        if pessoas:
            lista = "\n".join([str(pessoa) for pessoa in pessoas])
            messagebox.showinfo("Pessoas Cadastradas", lista)
        else:
            messagebox.showinfo("Aviso", "Nenhuma pessoa cadastrada!")

    def remover_pessoa(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        email = self.entry_email.get()

        if nome and idade and email:
            pessoa = Pessoa(nome, idade, email)
            try:
                self.cadastro.remover_pessoa(pessoa)
                self.limpar_campos()
                messagebox.showinfo("Sucesso", "Pessoa removida com sucesso!")
            except ValueError:
                messagebox.showwarning("Erro", "Pessoa não encontrada!")
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos!")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)


class InterfaceEstoque:
    def __init__(self, root):
        self.root = root
        self.root.title("Módulo de Estoque")

        self.label_produto = tk.Label(root, text="Produto:")
        self.label_produto.grid(row=0, column=0)

        self.entry_produto = tk.Entry(root)
        self.entry_produto.grid(row=0, column=1)

        self.btn_adicionar = tk.Button(root, text="Adicionar Produto", command=self.adicionar_produto)
        self.btn_adicionar.grid(row=1, column=0, columnspan=2)

        self.btn_listar = tk.Button(root, text="Listar Produtos", command=self.listar_produtos)
        self.btn_listar.grid(row=2, column=0, columnspan=2)

    def adicionar_produto(self):
        produto = self.entry_produto.get()
        if produto:
            # Lógica para adicionar o produto no estoque (não implementado neste exemplo)
            self.limpar_campos()
            messagebox.showinfo("Sucesso", "Produto adicionado ao estoque!")
        else:
            messagebox.showwarning("Erro", "Por favor, insira o nome do produto!")

    def listar_produtos(self):
        # Lógica para listar os produtos do estoque (não implementado neste exemplo)
        messagebox.showinfo("Produtos em Estoque", "Lista de produtos será exibida aqui!")

    def limpar_campos(self):
        self.entry_produto.delete(0, tk.END)


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro")
        self.login()

    def login(self):
        self.clear_screen()
        self.tela_login = TelaLogin(self.root, self)

    def login_sucesso(self):
        self.clear_screen()
        self.menu_lateral = MenuOpcoes(self.root, self)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def exibir_cadastro(self):
        self.clear_screen()
        self.interface_cadastro = InterfaceCadastro(self.root)

    def exibir_estoque(self):
        self.clear_screen()
        self.interface_estoque = InterfaceEstoque(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

