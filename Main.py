from tkinter import filedialog
import mysql.connector
from PIL import ImageDraw
import base64
import binascii
import io
import ctypes
from Icones import *
from tkinter import ttk
import pandas as pd


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

class InterfaceEstoque:
    def __init__(self, root):
        self.root = root
        self.root.title("Módulo de Estoque")

        self.label_produto = ctk.Label(root, text="Produto:")
        self.label_produto.grid(row=0, column=0)

        self.entry_produto = ctk.Entry(root)
        self.entry_produto.grid(row=0, column=1)

        self.btn_adicionar = ctk.Button(root, text="Adicionar Produto", command=self.adicionar_produto)
        self.btn_adicionar.grid(row=1, column=0, )

        self.btn_listar = ctk.Button(root, text="Listar Produtos", command=self.listar_produtos)
        self.btn_listar.grid(row=2, column=0, )

    def adicionar_produto(self):
        produto = self.entry_produto.get()
        if produto:
            # Lógica para adicionar o produto no estoque (não implementado neste exemplo)
            self.limpar_campos()
            # messagebox.showinfo("Sucesso", "Produto adicionado ao estoque!")
        else:
            pass# messagebox.showwarning("Erro", "Por favor, insira o nome do produto!")

    def listar_produtos(self):
        # Lógica para listar os produtos do estoque (não implementado neste exemplo)
        pass# messagebox.showinfo("Produtos em Estoque", "Lista de produtos será exibida aqui!")

    def limpar_campos(self):
        self.entry_produto.delete(0, ctk.END)

class InterfaceGerenciarUsuarios: 

    def __init__(self, main_app, frame_resp):
        self.main_app = main_app
        self.frame_resp = frame_resp


        self.usuarios = []
        self.acesso = []
        self.status = []

        self.usuario_label = []
        self.status_label = []
        self.acesso_label = []
        self.editar_button = []

        self.salvar_button = []
        self.cancelar_button = []
        self.excluir_button = []
        self.Editar_Modulos = []

        self.cursor = self.main_app.ConexaoPrincipal.cursor()

        self.buscar_usuarios()
        self.interface()
   
    def reiniciar_listas(self):
        
        self.usuarios = []
        self.acesso = []
        self.status = []

        self.usuario_label = []
        self.status_label = []
        self.acesso_label = []
        self.editar_button = []

        self.salvar_button = []
        self.cancelar_button = []
        self.excluir_button = []
        self.Editar_Modulos = []

    def interface(self):
        
        self.salvar_button = [None] * len(self.usuarios)
        self.cancelar_button = [None] * len(self.usuarios)
        self.excluir_button = [None] * len(self.usuarios)
        self.Editar_Modulos = [None] * len(self.usuarios)


        self.LabelPesquisar = ctk.CTkLabel(self.frame_resp, text="Busca rapida", fg_color="transparent", font=self.main_app.SubTitle)
        self.LabelPesquisar.place(relx=0.36, rely=0.13, anchor="w")


        self.TotalPerfil = ctk.CTkLabel(self.frame_resp, text=f"Total de Perfils\n{len(self.usuarios)}", height=50, width=200,
                                    fg_color="white", text_color="black", font=self.main_app.SubTitle, corner_radius=6)
        self.TotalPerfil.place(relx=0.05, rely=0.3, anchor="w")


        self.TotalAdm = ctk.CTkLabel(self.frame_resp, text=f"Total de Administradores\n{self.totalizador(total='adm')}", height=50, fg_color="white",width=200,
                                text_color="black", font=self.main_app.SubTitle, corner_radius=6)
        self.TotalAdm.place(relx=0.35, rely=0.3, anchor="w")


        self.TotalUser = ctk.CTkLabel(self.frame_resp, text=f"Total de Usuarios\n{self.totalizador('usuarios')}",height=50, width=200,
                                fg_color="white", text_color="black", font=self.main_app.SubTitle, corner_radius=6)
        self.TotalUser.place(relx=0.65, rely=0.3, anchor="w")


        self.cabeçalho = ctk.CTkLabel(self.frame_resp, text="     Usuario             Acesso             Status", 
                                width=(self.main_app.screen_wedth)-270,corner_radius=5, fg_color=("white", "gray10"), text_color=("black", "white"), anchor="w", font=self.main_app.SubTitle)
        self.cabeçalho.place(relx=0.01, rely=0.443, anchor="w")



        self.Bt_Todos = ctk.CTkButton(self.frame_resp, text="TODOS", image=EntradaIcon, text_color=("black","white"), 
                                    width=80,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'))
        self.Bt_Todos.place(relx=0.7, rely=0.18, anchor="w")


        self.Bt_Pesquisar = ctk.CTkButton(self.frame_resp, image=VisualizarIcon, text_color=("black","white"), text="PESQUISAR",
                                        width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=self.busca_rapida)
        self.Bt_Pesquisar.place(relx=0.612, rely=0.18, anchor="w")

        self.Pesquisar = ctk.CTkEntry(self.frame_resp, placeholder_text="Digite o nome do usuario aqui:", width=550, height=40)
        self.Pesquisar.place(relx=0.2, rely=0.18, anchor="w")

        self.scrol = ctk.CTkScrollableFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=50)
        self.scrol.place(relx=0.01, rely=0.6, anchor="w")


        
    # adicionado nas lista os botoes com cada usuario cadastrado no banco de dados
        for i in range(len(self.usuarios)):
            self.usuario_label.append(ctk.CTkLabel(self.scrol, text=self.usuarios[i], fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
            self.usuario_label[i].grid(padx=2, pady=5, row=i, column=0)
                            
            self.acesso_label.append(ctk.CTkLabel(self.scrol, text=self.acesso[i],  fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
            self.acesso_label[i].grid(padx=2,pady=5, row=i, column=1)
            
            self.status_label.append(ctk.CTkLabel(self.scrol, text=self.status[i], fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
            self.status_label[i].grid(padx=2, pady=5, row=i, column=2)
    
            self.editar_button.append(ctk.CTkButton(self.scrol, text="Editar", text_color=("black","white"), image=EditarIcon, width=60, fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda i=i: self.editar_usuario(i)))
            self.editar_button[i].grid(padx=60,pady=5, row=i, column=3)

    def buscar_usuarios(self):

        self.cursor.execute("SELECT usuario, acesso, status FROM Usuarios")
        resultado = self.cursor.fetchall()
    
        for user in resultado:
            self.usuarios.append(user[0])
            self.acesso.append(user[1])
            self.status.append(user[2])

    def totalizador(self, total=str):
        resposta = total.upper()
        TotaldeAdmin = 0
        TotaldeUsuarios = 0

        for acesso in self.acesso:
            if acesso == 'ADM':
                TotaldeAdmin +=1
            else:
                TotaldeUsuarios +=1
        if resposta == "ADM":
            return TotaldeAdmin
        elif resposta == "USUARIOS":
            return TotaldeUsuarios
        else:
            return None

    def busca_rapida(self):
            self.main_app.msgbox("Pesquisa", "Usuario nao encontrado", 0)
                
    def modulos_usuario(self, indice, usuario_entry, status_menu, acesso_menu):
        
        self.cursor.execute(f"select * from modulos where id = '{self.usuarios[indice]}'")

        self.indice_usuario = indice
        self.ModulosDoUsuario = self.cursor.fetchall()

        usuario_entry.grid_remove()
        acesso_menu.grid_remove()
        status_menu.grid_remove()


        self.salvar_button[indice].grid_remove()
        self.cancelar_button[indice].grid_remove()
        self.excluir_button[indice].grid_remove()
        self.Editar_Modulos[indice].grid_remove()

        
        outros_usuarios = len(self.usuario_label)-1
        for c in range(0, outros_usuarios+1):
            self.usuario_label[c].grid_remove()
            self.acesso_label[c].grid_remove()
            self.status_label[c].grid_remove()
            self.editar_button[c].grid_remove()

        self.cabeçalho.configure(text='     Usuario             Modulo             Submodulo             visualizar             Novo             Editar             Remover')

        self.usuario_label_modulo = []

        modulo_label_modulo = []
        submodulo_label_modulo = []
        visualizar_menu_modulo = []
        novo_menu_modulo = []
        editar_menu_modulo = []
        remover_menu_modulo = []


        for i, linha in enumerate(self.ModulosDoUsuario):
            self.usuario_label_modulo.append(ctk.CTkLabel(self.scrol, text=linha[1], fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
            self.usuario_label_modulo[i].grid(padx=2, pady=5, row=i, column=0)

            modulo_label_modulo.append(ctk.CTkLabel(self.scrol, text=linha[2], fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
            modulo_label_modulo[i].grid(padx=2, pady=5,  row=i, column=1)

            submodulo_label_modulo.append(ctk.CTkLabel(self.scrol, text=linha[3].capitalize(), fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
            submodulo_label_modulo[i].grid(padx=2, pady=5,  row=i, column=2)

            visualizar_menu_modulo.append(ctk.CTkOptionMenu(self.scrol, values=(("liberado", "bloqueado") if linha[4] == 'liberado' else ("bloqueado", "liberado")), width=100, height=26))
            visualizar_menu_modulo[i].grid(padx=2, pady=5,  row=i, column=3)

            novo_menu_modulo.append(ctk.CTkOptionMenu(self.scrol, values=(("liberado", "bloqueado") if linha[4] == 'liberado' else ("bloqueado", "liberado")), width=100, height=26))
            novo_menu_modulo[i].grid(padx=2, pady=5, row=i, column=4)

            editar_menu_modulo.append(ctk.CTkOptionMenu(self.scrol,  values=(("liberado", "bloqueado") if linha[4] == 'liberado' else ("bloqueado", "liberado")), width=100, height=26))
            editar_menu_modulo[i].grid(padx=2, pady=5,  row=i, column=5)

            remover_menu_modulo.append(ctk.CTkOptionMenu(self.scrol, values=(("liberado", "bloqueado") if linha[4] == 'liberado' else ("bloqueado", "liberado")), width=100, height=26))
            remover_menu_modulo[i].grid(padx=2, pady=5, row=i, column=6)



        def salvar():
            resp = self.main_app.msgbox("Salvar", "Deseja salvar as alterações feita?", 4)
            if resp == 6:
                for pos, modulo in enumerate(self.ModulosDoUsuario):

                    visualizar = visualizar_menu_modulo[pos].get()
                    novo =  novo_menu_modulo[pos].get()
                    editar = editar_menu_modulo[pos].get()
                    remover =  remover_menu_modulo[pos].get()
                    
                    self.cursor.execute(f'''UPDATE modulos SET 
                                    visualizar = "{visualizar}", 
                                    novo = "{novo}", 
                                    editar = "{editar}", 
                                    remover = "{remover}" 
                                    WHERE usuario = "{self.usuarios[indice]}" AND submodulo = "{modulo[3]}"''')
                    self.main_app.ConexaoPrincipal.commit()



            
                    
                    
              
                self.main_app.msgbox("Salvar", "Alterações salvas com Sucesso", 0)


        def cancelar():
            self.cursor.execute(f"SELECT acesso FROM Usuarios  WHERE BINARY  usuario = '{self.main_app.usuario_logado}' ")
            self.acesso_usuario = str(self.cursor.fetchall()[0][0])

                
            Bt_Salvar_modulo.destroy()
                                
            Bt_Cancelar_modulo.destroy()
            self.reiniciar_listas()
            self.buscar_usuarios()
            self.interface()

    


        Bt_Salvar_modulo = ctk.CTkButton(self.frame_resp, text="Salvar",  image=SalvarIcon, text_color=("black","white"), 
                                    width=100,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=lambda:salvar())
        
        Bt_Salvar_modulo.place(relx=0.4, rely=0.8, anchor="w")


        Bt_Cancelar_modulo = ctk.CTkButton(self.frame_resp, text="Voltar",  image=
                                            VoltarIcon, text_color=("black","white"), 
                                    width=100,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), anchor="w", command= lambda: cancelar())
        
        Bt_Cancelar_modulo.place(relx=0.3, rely=0.8, anchor="w")

        self.Pesquisar.configure(state="disabled")
        self.Bt_Todos.configure(state="disabled")
        self.Bt_Pesquisar.configure(state="disabled")

    def salvar_usuario(self, i, usuario_entry, status_menu, acesso_menu):
        self.editar_button[i].configure(state="normal")
        # Salva as alterações nas listas 

        NovoUser = usuario_entry.get()
        NovoAcesso = acesso_menu.get()
        NovoStatus =  status_menu.get()

        if NovoUser != self.usuarios[i]:
            self.cursor.execute(f"SELECT usuario FROM Usuarios WHERE BINARY usuario = '{usuario_entry.get()}'")
            resp = self.cursor.fetchall()
            if not resp:
                self.cursor.execute(f"UPDATE Usuarios SET usuario = '{usuario_entry.get()}' WHERE BINARY usuario = '{self.usuarios[i]}'")
                self.main_app.usuario_logado = usuario_entry.get()
                self.usuarios[i] = usuario_entry.get()
                self.main_app.ConexaoPrincipal.commit()
            else:
                self.main_app.msgbox("USUARIO", "Ja existe um usuario com este nome!!!", 0)

        if NovoAcesso != self.acesso[i] :
            self.cursor.execute(f"UPDATE Usuarios SET acesso = '{acesso_menu.get()}' WHERE BINARY usuario = '{self.usuarios[i]}'")
            self.acesso[i] = acesso_menu.get()
            self.main_app.ConexaoPrincipal.commit()

        if NovoStatus != self.status[i]:
            self.cursor.execute(f"UPDATE Usuarios SET status = '{status_menu.get()}' WHERE BINARY usuario = '{self.usuarios[i]}'")
            self.status[i] = status_menu.get()
            self.main_app.ConexaoPrincipal.commit()
            
        # Atualiza os rótulos com as novas informações

            
            self.TotalPerfil.configure(text=f"Total de Perfils\n{len(self.usuarios)}")
                                
            self.TotalAdm.configure(text=f"Total de Administradores\n{self.totalizador('adm')}")
                            
            self.TotalUser.configure(text=f"Total de Usuarios\n{self.totalizador('usuarios')}")



        self.usuario_label[i].configure(text=self.usuarios[i])
        self.acesso_label[i].configure(text=self.acesso[i])
        self.status_label[i].configure(text=self.status[i])
        
        # Mostra os rótulos e esconde os campos de entrada
        self.usuario_label[i].grid()
        self.acesso_label[i].grid()
        self.status_label[i].grid()
        
        usuario_entry.grid_remove()
        acesso_menu.grid_remove()
        status_menu.grid_remove()
        

        self.salvar_button[i].grid_remove()
        self.Editar_Modulos[i].grid_remove()
        self.cancelar_button[i].grid_remove()
        self.excluir_button[i].grid_remove()
        self.editar_button[i].grid()

    def excluir_usuario(self, i, usuario_entry, status_menu, acesso_menu):
        resp = self.main_app.msgbox("EXCLUIR USUARIO", "Deseja realmente excluir este usuario?", 4)


        if resp == 6:
            self.editar_button[i].configure(state="normal")
            # Salva as alterações nas listas
          

            self.cursor.execute(f"delete from Usuarios where binary usuario ='{self.usuarios[i]}' ")

            self.main_app.ConexaoPrincipal.commit()
            self.usuarios.pop(i)
            self.acesso.pop(i) 
            self.status.pop(i) 
            
        
 
            
            self.TotalPerfil.configure(text=f"Total de Perfils\n{len(self.usuarios)}")
                                
            self.TotalAdm.configure(text=f"Total de Administradores\n{self.totalizador('adm')}")
                            
            self.TotalUser.configure(text=f"Total de Usuarios\n{self.totalizador('usuarios')}")

            self.usuario_label[i].destroy()
            self.acesso_label[i].destroy()
            self.status_label[i].destroy()
            

            usuario_entry.grid_remove()
            acesso_menu.grid_remove()
            status_menu.grid_remove()
            

            self.salvar_button[i].destroy()
            self.cancelar_button[i].destroy()
            self.Editar_Modulos[i].destroy()
            self.excluir_button[i].destroy()
            self.editar_button[i].destroy()

            self.gerenciar_user(frame_resp=self.frame_resp)

    def cancelar_usuario(self, i, usuario_entry, status_menu,acesso_menu ):
        self.editar_button[i].configure(state="normal")

        # Descarta as alterações e esconde os campos de entrada
        usuario_entry.grid_remove()
        acesso_menu.grid_remove()
        status_menu.grid_remove()

        self.usuario_label[i].grid(row=i, column=0)

        self.acesso_label[i].grid(row=i, column=1)
        
        self.status_label[i].grid(row=i, column=2)
        

        




        self.salvar_button[i].grid_remove()
        self.cancelar_button[i].grid_remove()
        self.excluir_button[i].grid_remove()
        self.Editar_Modulos[i].grid_remove()
        self.editar_button[i].grid()

    def editar_usuario(self, i):
        # Cria os campos de entrada com as informações atuais do usuário
        self.editar_button[i].configure(state="disabled")


        usuario_entry = ctk.CTkEntry(self.scrol,  width=100)
        usuario_entry.insert(0, self.usuarios[i])
        usuario_entry.grid(padx=2, pady=5,row=i, column=0)

        Menu1 = ("USUARIO", "ADM")
        Menu2 = ("ADM", "USUARIO")

        Status1 = ("ATIVO", "DESATIVADO")
        Status2 = ("DESATIVADO", "ATIVO")


        acesso_menu =  ctk.CTkOptionMenu(self.scrol, values=(Menu1 if self.acesso[i] == "USUARIO" else Menu2), width=100, height=26)
        acesso_menu.grid(padx=2, pady=5,row=i, column=1)
        
        
        status_menu = ctk.CTkOptionMenu(self.scrol, values=(Status1 if  self.status[i] == "ATIVO" else Status2), width=100, height=26)
        status_menu.grid(padx=2, pady=5,row=i, column=2)
        


        
        # Cria os botões Salvar e Cancelar
        self.salvar_button[i] = ctk.CTkButton(self.scrol, text="Salvar", text_color=("black","white"), image=SalvarIcon, width=60,  fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda:  self.salvar_usuario(i, usuario_entry, status_menu, acesso_menu))
        self.salvar_button[i].grid(row=i, column=4)
        
        self.cancelar_button[i] =ctk.CTkButton(self.scrol, text="Cancelar", text_color=("black","white"), image=VoltarIcon, width=60,  fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda:  self.cancelar_usuario(i, usuario_entry, status_menu, acesso_menu))
        self.cancelar_button[i].grid(padx=5, row=i, column=5)

        self.Editar_Modulos[i] =ctk.CTkButton(self.scrol, text="Modulos", text_color=("black","white"),image=EditarIcon, width=60,  fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda:  self.modulos_usuario(i, usuario_entry, status_menu, acesso_menu))
        self.Editar_Modulos[i].grid(padx=5, row=i, column=6)

        self.excluir_button[i] =ctk.CTkButton(self.scrol, text="Deletar", text_color=("black","white"),image=DeletarIcon, width=60, fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda:  self.excluir_usuario(i, usuario_entry, status_menu, acesso_menu))
        self.excluir_button[i].grid(padx=5, row=i, column=7)
        
        # Esconde os rótulos e o botão Editar
        self.usuario_label[i].grid_remove()
        self.status_label[i].grid_remove()
        self.acesso_label[i].grid_remove()
        
class InterfaceNovoCliente: 

    def __init__(self, main_app, frame_resp):
        self.main_app = main_app
        self.frame_resp = frame_resp
        self.cursor =  self.main_app.ConexaoPrincipal.cursor()
        self.limite_view = 10
        self.ListaClientes = None
        self.totalClientes = 0
        self.Cliente_select = None
        

        self.LabelTitulo =ctk.CTkLabel(self.frame_resp, text=f"CLIENTES",fg_color="transparent", text_color=("black", "white"),  font=(ctk.CTkFont(size=14, weight="bold")), corner_radius=6)
        self.LabelTitulo.place(x=1,y=1)

        self.interface_tabela()
    
    def acao_widget(self, acao):
        if acao == 'ocultar':
            for widget in self.frame_resp.winfo_children():
                    if widget != self.LabelTitulo:
                        widget.place_forget()
        if acao == 'reexibir':
            for widget in self.frame_resp.winfo_children():
                if widget != self.LabelTitulo:
                    widget.place(x=widget.winfo_x(), y=widget.winfo_y())
                
    def interface_tabela(self): 
        


        frame = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=305, corner_radius=0)
        frame.place(x=25, y=300)

        self.tree = ttk.Treeview(frame, show="headings")
        self.tree.place(x=0, y=0, width=(self.main_app.screen_wedth)-270, height=390)  # Adjust width and height as needed

        self.scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_x.place(x=0, y=290, width=(self.main_app.screen_wedth)-270, height=15) 

        self.LabelPesquisar = ctk.CTkLabel(self.frame_resp, text="Busca rapida", fg_color="transparent",font=(ctk.CTkFont(size=14, weight="bold")))
        self.LabelPesquisar.place(relx=0.36, rely=0.13, anchor="w")


        self.Label_Select = ctk.CTkLabel(self.frame_resp, text=f"SELECIONADO: ", height=37, width=250, fg_color="white", text_color="black", 
                                         font=(ctk.CTkFont(size=12, weight="bold")), corner_radius=6, anchor="w")
        self.Label_Select.place(x=50,y=250)
        self.Label_LimiteView = ctk.CTkLabel(self.frame_resp,  height=37, text=f"01 A {self.limite_view} DE {self.totalClientes}", 
                                        font=(ctk.CTkFont(size=12, weight="bold")), anchor="w")
        self.Label_LimiteView.place(x=820,y=255)

        self.Entry_Pesquisar = ctk.CTkEntry(self.frame_resp, placeholder_text="Pesquise por ID, CNPJ, CPF, ou razão social:", width=550, height=40)
        self.Entry_Pesquisar.place(relx=0.2, rely=0.18, anchor="w")

        self.Bt_Todos = ctk.CTkButton(self.frame_resp, text="TODOS", image=EntradaIcon, text_color=("black","white"), 
                                    width=80,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=self.todos)
        self.Bt_Todos.place(relx=0.7, rely=0.18, anchor="w")

        self.Bt_Pesquisar = ctk.CTkButton(self.frame_resp, image=VisualizarIcon, text_color=("black","white"), text="PESQUISAR",
                                        width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=self.Pesquisar_Cliente)
        self.Bt_Pesquisar.place(relx=0.612, rely=0.18, anchor="w")



        self.Bt_EditarCliente = ctk.CTkButton(self.frame_resp, text="Editar", text_color=("black","white"), image=EditarIcon,  
                                         width=40, fg_color=("transparent"), hover_color=("white", '#191919'), state="disabled", command=self.editar_Cliente)
        self.Bt_EditarCliente.place(x=320,y=250)

        self.Bt_ExcluirCliente = ctk.CTkButton(self.frame_resp, text="Excluir", text_color=("black","white"), image=DeletarIcon,  
                                         width=40, fg_color=("transparent"), hover_color=("white", '#191919'), state="disabled")
        self.Bt_ExcluirCliente.place(x=420,y=250)

        self.Bt_Excel = ctk.CTkButton(self.frame_resp, text="Excel", text_color=("black","white"), image=ExcelIcon,  
                                 width=40, fg_color=("transparent"), hover_color=("white", '#191919'), command=self.excel)
        self.Bt_Excel.place(x=1020,y=250)

        self.Bt_NovoCLiente = ctk.CTkButton(self.frame_resp, text="NOVO",  image=AdicionarIcon, text_color=("black","white"), 
                                    width=100,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=lambda: self.interface_create('CREATE'))       
        self.Bt_NovoCLiente.place(relx=0.36, rely=0.85, anchor="w")

        self.Bt_Sincronizar = ctk.CTkButton(self.frame_resp, text="",  image=sincronizar, text_color=("black","white"),fg_color=('transparent'), hover_color=("white", '#191919'), command=self.sincronizar_tabela)
        self.Bt_Sincronizar.place(x=575,y=250)

        self.Menu_LimiteView = ctk.CTkOptionMenu(self.frame_resp,  height=37, width=80, font=(ctk.CTkFont(size=11, weight="bold")), values=['10','100','1000','10000'], command=self.Atualizar_limiteView)
        self.Menu_LimiteView.place(x=920,y=250)

   
        style = ttk.Style()
        # style.theme_use("clam")
        style.configure('Treeview.Heading', background="white")
        style.configure("Treeview.Heading", font=('Roboto', 11, "bold"))
        style.configure('Treeview', font=('Roboto', 11))
        style.map("Treeview", background=[('selected', 'gray90')], foreground=[('selected', 'black')])  
        self.tree.bind("<<TreeviewSelect>>", self.click_select)

    def sincronizar_tabela(self):
        self.Bt_Sincronizar.destroy()
        self.cursor.execute("SELECT * FROM Clientes limit 10")

        self.ListaClientes = self.cursor.fetchall()
        self.column_names = self.cursor.column_names
        

        self.cursor.execute("SELECT COUNT(*) AS total_linhas FROM Clientes ")
        self.totalClientes = int((self.cursor.fetchone()[0]))

        self.tree.configure(columns=([f'coluna{c}' for c in range(1,len(self.column_names)+1)]))
        
        self.Atualizar_limiteView(10)

    def Reexibir_treeview(self, lista):
        self.tree.column("coluna1", width=50)
        self.tree.column("coluna10", width=50)
        self.tree.column("coluna14", width=50)


       
        for cliente in lista:
            self.tree.insert("", "end", values=cliente)
            self.tree.tag_configure("center", anchor="center")

      
        for i, coluna in enumerate(self.tree['columns']):
            nome = str(self.column_names[i]).capitalize()
            
            self.tree.heading(coluna, text=f"{nome}")

            self.tree.column(coluna, stretch=False)

    def Atualizar_limiteView(self, novo_limite):
        try:
            self.tree.delete(*self.tree.get_children())
        except:
            pass

        



        self.cursor.execute(f"SELECT * FROM Clientes limit {int(novo_limite)}")
        self.ListaClientes = self.cursor.fetchall()


        self.Label_LimiteView.configure(text=f"01 A {novo_limite if int(novo_limite) < self.totalClientes else self.totalClientes} DE {self.totalClientes}")
        self.limite_view = int(novo_limite)

        self.Reexibir_treeview(self.ListaClientes)
  
    def click_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            if len(selected_item) ==1:
                unico = self.tree.item(selected_item, "values")
                self.Cliente_select = unico
                self.Label_Select.configure(text=f"SELECIONADO: {unico[6][0:20]}")
                self.Bt_EditarCliente.configure(state="normal")
                self.Bt_ExcluirCliente.configure(state="normal")

                                        
            else:
                self.Bt_EditarCliente.configure(state="disabled")
                self.Bt_ExcluirCliente.configure(state="normal")
                for item_id in selected_item:
                    valor = self.tree.item(item_id, "values")
                    self.Label_Select.configure(text=f"SELECIONADO: {len(selected_item)}")

    def todos(self):
        info_digitada = str(self.Entry_Pesquisar.get())
        if info_digitada:
            try:
                self.tree.delete(*self.tree.get_children())      
            except:
                pass
            self.Reexibir_treeview(self.ListaClientes)
            
    def editar_Cliente(self):
        lista = self.Cliente_select
        tipo_cliente = str(lista[1])
        


        ('id', 'tipo_de_cliente', 'cpf', 'cnpj', 'email', 
         'razao_social', 'nome', 'cep', 'endereco', 'numero', 
         'complemento', 'bairro', 'cidade', 'uf', 'fone', 
         'celular', 'questionario', 'observacoes')   


        ('143', 'Pessoa Jurídica', 'None', '12.345.678/0001-99', 'empresa1@example.com', 
         'Empresa XYZ Ltda.', 'Empresa XYZ', '54321-876', 'Avenida dos Negócios', '456', 
         'None', 'Bairro Comercial', 'Rio de Janeiro', 'RJ', '(21) 2222-2222', 
         '(21) 98888-8888', 'Respondeu parcialmente ao questionário.', 'Informações adicionais importantes.')
        
        self.interface_create('UPDATE')

        self.menu_tipocliente.set(f'{str(lista[1]).upper()}')
        self.entry_nome.insert(0, f'{lista[6]}')

        
        if tipo_cliente == 'PESSOA FISICA':
            cpf = int(str(lista[2]).replace(".", "").replace("-",""))

            self.entry_cpf_cnpj.insert(0,f'{cpf}')


            
    

        elif tipo_cliente == 'PESSOA JURIDICA':
            cnpj = int(str(lista[3]).replace(".", "").replace("-","").replace("/",""))

            self.entry_cpf_cnpj.insert(0, f'{cnpj}')
            self.entry_razao_social.inset(0,f'{str(lista[5])}')

        self.entry_email.insert(0, f'{str(lista[4])}')

        self.entry_cep.insert(0, f"{int(str(lista[7]).replace('-',''))}")

        self.entry_endereco.insert(0, f"{str(lista[8])}")
        self.entry_numero.insert(0, f"{int(lista[9])}")
        self.entry_complemento.insert(0,f"{str(lista[10])}")
        self.entry_bairro.insert(0,f"{str(lista[11])}")
        self.entry_cidade.insert(0,f"{str(lista[12])}")
        self.entry_uf.insert(0,f"{str(lista[13])}")

        self.entry_fone.insert(0,f"{int(str(lista[14]).replace('(','').replace(')','').replace(' ','').replace('-',''))}")

        self.entry_celular.insert(0,f"{int(str(lista[15]).replace('(','').replace(')','').replace(' ','').replace('-',''))}")

        self.menu_questionario.set(f'{str(lista[16])}')

        self.entry_observacoes.insert('1.0',f"{str(lista[17])}")
   
    def Pesquisar_Cliente(self):
        info_digitada = str(self.Entry_Pesquisar.get())
        if info_digitada:
            
            self.cursor.execute(f"select * from Clientes WHERE razao_social LIKE'%{info_digitada}%' OR cpf LIKE'%{info_digitada}%' OR cnpj LIKE'%{info_digitada}%' OR id LIKE'%{info_digitada}%' OR nome LIKE'%{info_digitada}%' ")
            lista = self.cursor.fetchall()
            
            self.tree.delete(*self.tree.get_children())
            self.Reexibir_treeview(lista=lista)

    def interface_create(self, tipo=str):
        # Esconder os widgets em vez de destruí-los
        self.acao_widget('ocultar')

        
        self.LabelTitulo.configure(text=('CADASTRAR CLIENTE' if tipo.upper() == "CREATE"
                                    else 'EDITAR CLIENTE' if tipo.upper() == "UPDATE"
                                    else ''))
        # Crie o widget para a opção 'tipo_de_cliente'


        self.label_tipo_cliente = ctk.CTkLabel(self.frame_resp, text='Tipo de Cliente:', font=(None, 12, "bold"))
        self.label_tipo_cliente.place(x=50, y=50, anchor="w")

        self.menu_tipocliente = ctk.CTkOptionMenu(self.frame_resp, values=['PESSOA FISICA', 'PESSOA JURIDICA'], command=self.definir_cliente)
        self.menu_tipocliente.place(x=50, y=80, anchor="w")


        self.label_cpf_cnpj = ctk.CTkLabel(self.frame_resp, text='CPF/CNPJ:', font=(None, 12, "bold"))
        self.label_cpf_cnpj.place(x=250, y=50, anchor="w")

        self.entry_cpf_cnpj = ctk.CTkEntry(self.frame_resp,  width=150)
        self.entry_cpf_cnpj.place(x=250, y=80, anchor="w")


        self.label_email = ctk.CTkLabel(self.frame_resp, text='Email:', font=(None, 12, "bold"))
        self.label_email.place(x=450, y=50, anchor="w")
        self.entry_email = ctk.CTkEntry(self.frame_resp, width=300)
        self.entry_email.place(x=450, y=80, anchor="w")


        self.label_razao_social = ctk.CTkLabel(self.frame_resp, text='Razão Social:', font=(None, 12, "bold"))
        self.label_razao_social.place(x=800, y=50, anchor="w")
        self.entry_razao_social = ctk.CTkEntry(self.frame_resp, width=300)
        self.entry_razao_social.place(x=800, y=80, anchor="w")


        self.label_nome = ctk.CTkLabel(self.frame_resp, text='Nome:', font=(None, 12, "bold"))
        self.label_nome.place(x=50, y=140, anchor="w")
        self.entry_nome = ctk.CTkEntry(self.frame_resp, width=300)
        self.entry_nome.place(x=50, y=170, anchor="w")


        self.label_cep = ctk.CTkLabel(self.frame_resp, text='CEP:', font=(None, 12, "bold"))
        self.label_cep.place(x=400, y=140, anchor="w")

        self.entry_cep = ctk.CTkEntry(self.frame_resp, validate="key", validatecommand=(self.main_app.validate_cmd_numeric, "%P", 8))
        self.entry_cep.place(x=400, y=170, anchor="w")


        self.label_endereco = ctk.CTkLabel(self.frame_resp, text='Endereço:', font=(None, 12, "bold"))
        self.label_endereco.place(x=600, y=140, anchor="w")
        self.entry_endereco = ctk.CTkEntry(self.frame_resp, width=300)
        self.entry_endereco.place(x=600, y=170, anchor="w")


        self.label_numero = ctk.CTkLabel(self.frame_resp, text='N°:', font=(None, 12, "bold"))
        self.label_numero.place(x=950, y=140, anchor="w")
        self.entry_numero = ctk.CTkEntry(self.frame_resp, width=50, validate="key", validatecommand=(self.main_app.validate_cmd_numeric, "%P", 5))
        self.entry_numero.place(x=950, y=170, anchor="w")


        self.label_complemento = ctk.CTkLabel(self.frame_resp, text='Complemento:', font=(None, 12, "bold"))
        self.label_complemento.place(x=50, y=230, anchor="w")

        self.entry_complemento = ctk.CTkEntry(self.frame_resp,  width=300)
        self.entry_complemento.place(x=50, y=260, anchor="w")


        self.label_bairro = ctk.CTkLabel(self.frame_resp, text='Bairro:', font=(None, 12, "bold"))
        self.label_bairro.place(x=400, y=230, anchor="w")
        self.entry_bairro = ctk.CTkEntry(self.frame_resp)
        self.entry_bairro.place(x=400, y=260, anchor="w")


        self.label_cidade = ctk.CTkLabel(self.frame_resp, text='Cidade:', font=(None, 12, "bold"))
        self.label_cidade.place(x=600, y=230, anchor="w")

        self.entry_cidade = ctk.CTkEntry(self.frame_resp)
        self.entry_cidade.place(x=600, y=260, anchor="w")


        self.label_uf = ctk.CTkLabel(self.frame_resp, text='UF:', font=(None, 12, "bold"))
        self.label_uf.place(x=800, y=230, anchor="w")
        self.entry_uf = ctk.CTkEntry(self.frame_resp,width=50, validate="key", validatecommand=(self.main_app.validade_cmd_text, "%P", 2))
        self.entry_uf.place(x=800, y=260, anchor="w")


        self.label_fone = ctk.CTkLabel(self.frame_resp, text='Telefone:', font=(None, 12, "bold"))
        self.label_fone.place(x=900, y=230, anchor="w")
        self.entry_fone = ctk.CTkEntry(self.frame_resp,placeholder_text="(xx) 0000-0000", validate="key", validatecommand=(self.main_app.validate_cmd_numeric, "%P", 10))
        self.entry_fone.place(x=900, y=260, anchor="w")


        self.label_celular = ctk.CTkLabel(self.frame_resp, text='Celular:', font=(None, 12, "bold"))
        self.label_celular.place(x=50, y=320, anchor="w")
        self.entry_celular = ctk.CTkEntry(self.frame_resp, placeholder_text="(xx)9 0000-0000",validate="key", validatecommand=(self.main_app.validate_cmd_numeric, "%P", 11))
        self.entry_celular.place(x=50, y=360, anchor="w")


        self.label_questionario = ctk.CTkLabel(self.frame_resp, text='Como conheceu a empresa:', font=(None, 12, "bold"))
        self.label_questionario.place(x=250, y=320, anchor="w")
        self.menu_questionario = ctk.CTkOptionMenu(self.frame_resp, values=['INSTAGRAM', 'FACEBOOK', 'SITE', 'TIKTOK', 'INDICAÇÃO', 'OUTRO'])
        self.menu_questionario.place(x=250, y=360, anchor="w")


        self.label_observacoes = ctk.CTkLabel(self.frame_resp, text='Observações:', font=(None, 12, "bold"))
        self.label_observacoes.place(x=50, y=420, anchor="w")
        self.entry_observacoes = ctk.CTkTextbox(self.frame_resp, width=(self.main_app.screen_wedth)-310, height=100) 
        self.entry_observacoes.place(x=50, y=450)



        self.Bt_Voltar = ctk.CTkButton(self.frame_resp, text="Voltar",  image=
                                            VoltarIcon, text_color=("black","white"), 
                                    width=100,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), anchor="w", command= lambda: self.voltar('ocultar'))
        
        self.Bt_Voltar.place(relx=0.3, rely=0.85, anchor="w")



        self.Bt_NovoCLiente = ctk.CTkButton(self.frame_resp, text="SALVAR",  image=SalvarIcon, text_color=("black","white"), 
                                    width=100,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'))       
        self.Bt_NovoCLiente.place(relx=0.4, rely=0.85, anchor="w")

        self.definir_cliente(resposta="PESSOA FISICA")

    def voltar(self, opcao):
        
        self.acao_widget(acao=opcao)
        self.interface_tabela()
        self.LabelTitulo.configure(text=('CLIENTES'))
        
    def excel(self):
        resp = self.main_app.msgbox("Excel", "Deseja exportar todos os registros?",4)


        def destino(df):
            folder_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
        
            if folder_path:
                # Definir o nome do arquivo
                file_path = folder_path
                
                # Verificar se a extensão .xlsx foi adicionada
                if not file_path.endswith('.xlsx'):
                    file_path += '.xlsx'
                    
                df.to_excel(file_path, index=False)
                self.main_app.msgbox("Excel", "Arquivo salvo com sucesso",0)
                


        if resp ==6 :
           print("esta vazio, puxando valores no banco de dados")
           if self.ListaClientes == None:
            self.cursor.execute("SELECT * FROM Clientes")
            self.ListaClientes = self.cursor.fetchall()
            self.column_names = self.cursor.column_names
            df = pd.DataFrame(self.ListaClientes, columns=self.column_names)    
            destino(df=df)

           else:
                print("NAO ESTA VAZIA")
                df = pd.DataFrame(self.ListaClientes, columns=self.column_names)    
                destino(df=df)

           
    



    def salvar(self, tipo):
        if tipo == 'CREATE':
            pass
        elif tipo == 'UPDATE':
            pass
        else:
            pass

    def definir_cliente(self, resposta):
        
    
        if resposta == 'PESSOA FISICA':
             
             self.entry_cpf_cnpj.configure(validate="key", validatecommand=(self.main_app.validate_cmd_numeric, "%P", 11))


        elif resposta == "PESSOA JURIDICA":
            self.entry_cpf_cnpj.configure(validate="key", validatecommand=(self.main_app.validate_cmd_numeric, "%P", 14))
        
class InterfaceNovoUsuario: 

    def __init__(self, main_app, frame_resp):
        self.main_app = main_app
        self.frame_resp = frame_resp

        self.FrameModuloEstoqueResp = None
        self.FrameModuloCadastroResp = None
        self.FrameModuloAgendaResp = None
        self.FrameModuloCarteiraResp = None
        self.FrameModuloFinancasResp = None
        self.FrameModuloUsuarioResp = None
        self.FrameModuloConfiguracoesResp = None
        self.cor_destaque = ("#FFD6D6", "gray17")
        self.listaBTS = []

        self.interface()

    def interface(self):

        Painel_NovoUsuario = ctk.CTkButton(self.frame_resp, text="", width=(self.main_app.screen_wedth)-270, height=90, border_width=3,
                                           fg_color="transparent",hover=False)
        Painel_NovoUsuario.place(relx=0.02, rely=0.1, anchor="w")

        TituloUsuario = ctk.CTkLabel(Painel_NovoUsuario, text="USUARIO")
        TituloUsuario.place(x=63, y=15)

        TituloSenha = ctk.CTkLabel(Painel_NovoUsuario, text="SENHA")
        TituloSenha.place(x=265, y=15)

        TituloAcesso = ctk.CTkLabel(Painel_NovoUsuario, text="ACESSO")
        TituloAcesso.place(x=465, y=15)

        TituloStatus = ctk.CTkLabel(Painel_NovoUsuario, text="STATUS")
        TituloStatus.place(x=663, y=15)

        self.EntryUsuario = ctk.CTkEntry(Painel_NovoUsuario, placeholder_text="Digite aqui:", width=150)
        self.EntryUsuario.place(x=10, y=45)

        self.EntrySenha = ctk.CTkEntry(Painel_NovoUsuario, placeholder_text="Senha temporaria:", width=150)
        self.EntrySenha.place(x=210, y=45)

        self.MenuAcesso = ctk.CTkOptionMenu(Painel_NovoUsuario, values=["USUARIO", "ADM"], width=150)
        self.MenuAcesso.place(x=410, y=45)

        self.MenuStatus = ctk.CTkOptionMenu(Painel_NovoUsuario, values=["ATIVO", "DESATIVADO"], width=150)
        self.MenuStatus.place(x=610, y=45)


        self.Bt_SalvarModulos = ctk.CTkButton(Painel_NovoUsuario, image=SalvarIcon, text_color=("black", "white"),
                                              text="Salvar Alterações",
                                              width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'),
                                              command=self.SalvarGetSwitch)
        self.Bt_SalvarModulos.place(x=900, y=25)




        PainelBotoes = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=50, corner_radius=0, fg_color="transparent")
        PainelBotoes.place(relx=0.02, rely=0.19)

        self.BT_ModuloEstoque = ctk.CTkButton(PainelBotoes, image=EstoqueIcon, text="Estoque",
                                              text_color=("black", "white"), fg_color="transparent",
                                              hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40, width=100,
                                              anchor="w", command=lambda: self.Modulo_Estoque(frame_resp=self.frame_resp))
        self.BT_ModuloEstoque.place(relx=0.0, rely=0.5, anchor="w", )

        self.BT_ModuloCadastro = ctk.CTkButton(PainelBotoes, image=CadastroIcon, text="Cadastro",
                                               text_color=("black", "white"), fg_color="transparent",
                                               hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40, width=100,
                                               anchor="w", command=lambda: self.Modulo_Cadastro(frame_resp=self.frame_resp))
        self.BT_ModuloCadastro.place(relx=0.1, rely=0.5, anchor="w", )

        self.BT_ModuloAgenda = ctk.CTkButton(PainelBotoes, image=AgendaIcon, text="Agenda",
                                             text_color=("black", "white"), fg_color="transparent",
                                             hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40, width=100,
                                             anchor="w", command=lambda: self.Modulo_Agenda(frame_resp=self.frame_resp))
        self.BT_ModuloAgenda.place(relx=0.2, rely=0.5, anchor="w", )

        self.BT_ModuloCarteira = ctk.CTkButton(PainelBotoes, image=carteiraIcon, text="Carteira",
                                               text_color=("black", "white"), fg_color="transparent",
                                               hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40, width=100,
                                               anchor="w", command=lambda: self.Modulo_Carteira(frame_resp=self.frame_resp))
        self.BT_ModuloCarteira.place(relx=0.3, rely=0.5, anchor="w", )

        self.BT_ModuloFinancas = ctk.CTkButton(PainelBotoes, image=FinancasIcon, text="Finanças",
                                               text_color=("black", "white"), fg_color="transparent",
                                               hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40, width=100,
                                               anchor="w", command=lambda: self.Modulo_Financas(frame_resp=self.frame_resp))
        self.BT_ModuloFinancas.place(relx=0.4, rely=0.5, anchor="w", )

        self.BT_ModuloUsuarios = ctk.CTkButton(PainelBotoes, image=UsuarioIcon, text="Usuarios",
                                               text_color=("black", "white"), fg_color="transparent",
                                               hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40, width=100,
                                               anchor="w", command=lambda: self.Modulo_Usuario(frame_resp=self.frame_resp))
        self.BT_ModuloUsuarios.place(relx=0.5, rely=0.5, anchor="w", )

        self.BT_ModuloConfiguracoes = ctk.CTkButton(PainelBotoes, image=ConfiguracoesIcon, text="Configurações",
                                                    text_color=("black", "white"), fg_color="transparent",
                                                    hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40,
                                                    width=100, anchor="w",
                                                    command=lambda: self.Modulo_Configuracoes(frame_resp=self.frame_resp))
        self.BT_ModuloConfiguracoes.place(relx=0.6, rely=0.5, anchor="w", )

        self.listaBTS = [self.BT_ModuloEstoque, self.BT_ModuloCadastro, self.BT_ModuloAgenda, self.BT_ModuloCarteira, self.BT_ModuloFinancas, 
                         self.BT_ModuloUsuarios, self.BT_ModuloConfiguracoes]


        self.FrameModuloResp = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=900, corner_radius=0)
        self.FrameModuloResp.place(relx=0.02, rely=0.24)

    def AtivarSwitch(self, principal, visualizar, novo, editar, remover):
        valor = principal.get()
        try:
            if valor == "liberado":
                visualizar.configure(state="normal")
                novo.configure(state="normal")
                editar.configure(state="normal")
                remover.configure(state='normal')
            else:

                visualizar.deselect()
                novo.deselect()
                editar.deselect()
                remover.deselect()

                visualizar.configure(state="disabled")
                novo.configure(state="disabled")
                editar.configure(state="disabled")
                remover.configure(state='disabled')
             
        except Exception as erro:
            print(erro)

            pass

    def SalvarGetSwitch(self):
        resp = self.main_app.msgbox("SALVAR", "Deseja salvar as alterações nos módulos?", 4)
        try:
            if resp == 6:
                login_digitado = self.EntryUsuario.get()
                senha_digitada = self.EntrySenha.get()
                acesso = self.MenuAcesso.get()
                status = self.MenuStatus.get()

                if len(login_digitado) <= 2:
                    self.main_app.msgbox("USUARIO", "Nome de usuario deve conter pelo menos 3 caracteres", 0)
                elif len(senha_digitada) <= 5:
                    self.main_app.msgbox("SENHA", "Sua senha deve ter no minimo 6 caracteres", 0)
                else:

                    cursor =  self.main_app.ConexaoPrincipal.cursor()
                    cursor.execute(f"SELECT usuario FROM Usuarios where binary usuario = '{login_digitado}'")
                    resp = cursor.fetchall()
                    if resp:
                        self.main_app.msgbox("USUARIO", "Ja existe um usuario com este nome, por favor escolha outro", 0)
                    else:

                        modules = {
                            "Estoque": {
                                "ENTRADA": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "Entrada_visualizar") else self.Entrada_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self,
                                                                       "Entrada_novo") else self.Entrada_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "Entrada_editar") else self.Entrada_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "Entrada_remover") else self.Entrada_remover.get()
                                },
                                "SAIDA": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "saida_visualizar") else self.saida_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "saida_novo") else self.saida_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "saida_editar") else self.saida_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "saida_remover") else self.saida_remover.get()
                                },
                                "INVENTARIO": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "inventario_visualizar") else self.inventario_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self,
                                                                       "inventario_novo") else self.inventario_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "inventario_editar") else self.inventario_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "inventario_remover") else self.inventario_remover.get()
                                }
                            },
                            "Cadastro": {
                                "CAD ITEM": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "item_visualizar") else self.item_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "item_novo") else self.item_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "item_editar") else self.item_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "item_remover") else self.item_remover.get()
                                },
                                "CAD CLIENTE": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "cliente_visualizar") else self.cliente_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self,
                                                                       "cliente_novo") else self.cliente_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "cliente_editar") else self.cliente_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "cliente_remover") else self.cliente_remover.get()
                                },
                                "CAD USUARIO": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "criarusuario_visualizar") else self.criarusuario_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self,
                                                                       "criarusuario_novo") else self.criarusuario_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "criarusuario_editar") else self.criarusuario_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "criarusuario_remover") else self.criarusuario_remover.get()
                                },
                                "GERENCIAR USER": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "gerenciar_visualizar") else self.gerenciar_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self,
                                                                       "gerenciar_novo") else self.gerenciar_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "gerenciar_editar") else self.gerenciar_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "gerenciar_remover") else self.gerenciar_remover.get()
                                },

                            },
                            "Agenda": {
                                "AGENDA": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "agenda_visualizar") else self.agenda_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "agenda_novo") else self.agenda_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "agenda_editar") else self.agenda_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "agenda_remover") else self.agenda_remover.get()
                                }
                            },
                            "Carteira": {
                                "VENDAS": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "vendas_visualizar") else self.vendas_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "vendas_novo") else self.vendas_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "vendas_editar") else self.vendas_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "vendas_remover") else self.vendas_remover.get()
                                },
                                "FATURAMENTO": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "faturamento_visualizar") else self.faturamento_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self,
                                                                       "faturamento_novo") else self.faturamento_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "faturamento_editar") else self.faturamento_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "faturamento_remover") else self.faturamento_remover.get()
                                }
                            },
                            "Finanças": {
                                "DESPESAS": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "despesas_visualizar") else self.despesas_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self,
                                                                       "despesas_novo") else self.despesas_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "despesas_editar") else self.despesas_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "despesas_remover") else self.despesas_remover.get()
                                },
                                "OUTRAS RENDAS": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "rendas_visualizar") else self.rendas_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "rendas_novo") else self.rendas_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "rendas_editar") else self.rendas_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "rendas_remover") else self.rendas_remover.get()
                                }
                            },
                            "Usuario": {
                                "USUARIO": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "usuario_visualizar") else self.usuario_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self,
                                                                       "usuario_novo") else self.usuario_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "usuario_editar") else self.usuario_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "usuario_remover") else self.usuario_remover.get()
                                }
                            },
                            "Configurações": {
                                "CONFIGURACOES": {
                                    "visualizar": "bloqueado" if not hasattr(self,
                                                                             "configuracoes_visualizar") else self.configuracoes_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self,
                                                                       "configuracoes_novo") else self.configuracoes_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self,
                                                                         "configuracoes_editar") else self.configuracoes_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self,
                                                                          "configuracoes_remover") else self.configuracoes_remover.get()
                                }
                            }
                        }

                        cursor =  self.main_app.ConexaoPrincipal.cursor()

                        cursor.execute("""INSERT INTO Usuarios(usuario, senha, acesso, status)
                                        VALUES(%s, %s, %s, %s )""", (login_digitado, senha_digitada, acesso, status))
                        self.main_app.ConexaoPrincipal.commit()

                        # Itera sobre os dados do dicionário e insere no banco de dados
                        for modulo, submodulos in modules.items():
                            for submodulo, permissoes in submodulos.items():
                                visualizar = permissoes['visualizar']
                                novo = permissoes['novo']
                                editar = permissoes['editar']
                                remover = permissoes['remover']
                                cursor.execute("""
                                    INSERT INTO modulos (usuario, modulo, submodulo, visualizar, novo, editar, remover)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                                """, (login_digitado, modulo, submodulo, visualizar, novo, editar, remover))

                        # Efetua o commit da transação
                        self.main_app.ConexaoPrincipal.commit()

                        self.novo_user(frame_resp=self.frame_resp)
                        self.main_app.msgbox("SALVAR", "Usuario criado com sucesso!!!", 0)
        except Exception as erro:
            print(erro)

    def Modulo_Estoque(self, frame_resp):

        if self.FrameModuloEstoqueResp is None:

            self.FrameModuloEstoqueResp = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=900, corner_radius=0)
            self.FrameModuloEstoqueResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloEstoque, cor=self.cor_destaque)

            titulo_entrada = ctk.CTkLabel(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="ENTRADA",
                                          text_color=("black", "white"), height=38, width=200,
                                          fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_entrada.place(relx=0.1, rely=0.03, anchor="center")

            Entrada_switch = ctk.CTkSwitch(titulo_entrada, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                           offvalue="bloqueado",
                                           switch_height=25, switch_width=45, progress_color="#3DED9D",
                                           command=lambda: self.AtivarSwitch(Entrada_switch, self.Entrada_visualizar,
                                                                             self.Entrada_novo, self.Entrada_editar,
                                                                             self.Entrada_remover))
            
            Entrada_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.Entrada_visualizar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                                    text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                    switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                    state="disabled")
            self.Entrada_visualizar.place(x=10, y=50)

            self.Entrada_novo = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Novo",
                                              onvalue="liberado", offvalue="bloqueado",
                                              switch_height=25, switch_width=50, progress_color="#3DED9D",
                                              state="disabled")
            self.Entrada_novo.place(x=10, y=80)

            self.Entrada_editar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                                text="Editar", onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                state="disabled")
            self.Entrada_editar.place(x=10, y=110)

            self.Entrada_remover = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                                 text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                 switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                 state="disabled")
            self.Entrada_remover.place(x=10, y=140)

            # ____________________________________________________________________________________________________________________________________________________________________________________

            titulo_saida = ctk.CTkLabel(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="SAIDA",
                                        text_color=("black", "white"), height=38, width=200,
                                        fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_saida.place(relx=0.36, rely=0.03, anchor="center")

            saida_switch = ctk.CTkSwitch(titulo_saida, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                         offvalue="bloqueado",
                                         switch_height=25, switch_width=45, progress_color="#3DED9D",
                                         command=lambda: self.AtivarSwitch(saida_switch, self.saida_visualizar,
                                                                           self.saida_novo, self.saida_editar,
                                                                           self.saida_remover))
            saida_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.saida_visualizar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                                  text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                  switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                  state="disabled")
            self.saida_visualizar.place(x=300, y=50)

            self.saida_novo = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Novo",
                                            onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=50, progress_color="#3DED9D",
                                            state="disabled")
            self.saida_novo.place(x=300, y=80)

            self.saida_editar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                              text="Editar", onvalue="liberado", offvalue="bloqueado",
                                              switch_height=25, switch_width=50, progress_color="#3DED9D",
                                              state="disabled")
            self.saida_editar.place(x=300, y=110)

            self.saida_remover = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                               text="Remover", onvalue="liberado", offvalue="bloqueado",
                                               switch_height=25, switch_width=50, progress_color="#3DED9D",
                                               state="disabled")
            self.saida_remover.place(x=300, y=140)

            # ________________________________________________________________________________________________________________________________________-

            titulo_inventario = ctk.CTkLabel(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                             text="INVENTARIO", text_color=("black", "white"), height=38, width=200,
                                             fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_inventario.place(relx=0.632, rely=0.03, anchor="center")

            inventario_switch = ctk.CTkSwitch(titulo_inventario, font=ctk.CTkFont(weight="bold"), text="",
                                              onvalue="liberado", offvalue="bloqueado",
                                              switch_height=25, switch_width=45, progress_color="#3DED9D",
                                              command=lambda: self.AtivarSwitch(inventario_switch,
                                                                                self.inventario_visualizar,
                                                                                self.inventario_novo,
                                                                                self.inventario_editar,
                                                                                self.inventario_remover))
            inventario_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.inventario_visualizar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                                       text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                       switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                       state="disabled")
            self.inventario_visualizar.place(x=600, y=50)

            self.inventario_novo = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                                 text="Novo", onvalue="liberado", offvalue="bloqueado",
                                                 switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                 state="disabled")
            self.inventario_novo.place(x=600, y=80)

            self.inventario_editar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                                   text="Editar", onvalue="liberado", offvalue="bloqueado",
                                                   switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                   state="disabled")
            self.inventario_editar.place(x=600, y=110)

            self.inventario_remover = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"),
                                                    text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                    switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                    state="disabled")
            self.inventario_remover.place(x=600, y=140)
        else:
            self.FrameModuloEstoqueResp.tkraise()
            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloEstoque, cor=self.cor_destaque)

    def Modulo_Cadastro(self, frame_resp):

        if self.FrameModuloCadastroResp is None:

            self.FrameModuloCadastroResp = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=900, corner_radius=0)
            self.FrameModuloCadastroResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloCadastro, cor=self.cor_destaque)

            titulo_item = ctk.CTkLabel(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="CAD ITENS",
                                       text_color=("black", "white"), height=38, width=200,
                                       fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_item.place(relx=0.1, rely=0.03, anchor="center")

            item_switch = ctk.CTkSwitch(titulo_item, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                        offvalue="bloqueado",
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(item_switch, self.item_visualizar,
                                                                          self.item_novo, self.item_editar,
                                                                          self.item_remover))
            item_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.item_visualizar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                 text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                 switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                 state="disabled")
            self.item_visualizar.place(x=10, y=50)

            self.item_novo = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Novo",
                                           onvalue="liberado", offvalue="bloqueado",
                                           switch_height=25, switch_width=50, progress_color="#3DED9D",
                                           state="disabled")
            self.item_novo.place(x=10, y=80)

            self.item_editar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                             text="Editar", onvalue="liberado", offvalue="bloqueado",
                                             switch_height=25, switch_width=50, progress_color="#3DED9D",
                                             state="disabled")
            self.item_editar.place(x=10, y=110)

            self.item_remover = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                              text="Remover", onvalue="liberado", offvalue="bloqueado",
                                              switch_height=25, switch_width=50, progress_color="#3DED9D",
                                              state="disabled")
            self.item_remover.place(x=10, y=140)

            # ____________________________________________________________________________________________________________________________________________________________________________________

            titulo_cliente = ctk.CTkLabel(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                          text="CAD CLIENTES", text_color=("black", "white"), height=38, width=200,
                                          fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_cliente.place(relx=0.36, rely=0.03, anchor="center")

            cliente_switch = ctk.CTkSwitch(titulo_cliente, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                           offvalue="bloqueado",
                                           switch_height=25, switch_width=45, progress_color="#3DED9D",
                                           command=lambda: self.AtivarSwitch(cliente_switch, self.cliente_visualizar,
                                                                             self.cliente_novo, self.cliente_editar,
                                                                             self.cliente_remover))
            cliente_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.cliente_visualizar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                    text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                    switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                    state="disabled")
            self.cliente_visualizar.place(x=300, y=50)

            self.cliente_novo = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                              text="Novo", onvalue="liberado", offvalue="bloqueado",
                                              switch_height=25, switch_width=50, progress_color="#3DED9D",
                                              state="disabled")
            self.cliente_novo.place(x=300, y=80)

            self.cliente_editar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                text="Editar", onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                state="disabled")
            self.cliente_editar.place(x=300, y=110)

            self.cliente_remover = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                 text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                 switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                 state="disabled")
            self.cliente_remover.place(x=300, y=140)

            # ________________________________________________________________________________________________________________________________________-

            titulo_criarusuario = ctk.CTkLabel(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                               text="CAD USUARIO", text_color=("black", "white"), height=38, width=200,
                                               fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_criarusuario.place(relx=0.632, rely=0.03, anchor="center")

            criarusuario_switch = ctk.CTkSwitch(titulo_criarusuario, font=ctk.CTkFont(weight="bold"), text="",
                                                onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=45, progress_color="#3DED9D",
                                                command=lambda: self.AtivarSwitch(criarusuario_switch,
                                                                                  self.criarusuario_visualizar,
                                                                                  self.criarusuario_novo,
                                                                                  self.criarusuario_editar,
                                                                                  self.criarusuario_remover))
            criarusuario_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.criarusuario_visualizar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                         text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                         switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                         state="disabled")
            self.criarusuario_visualizar.place(x=600, y=50)

            self.criarusuario_novo = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                   text="Novo", onvalue="liberado", offvalue="bloqueado",
                                                   switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                   state="disabled")
            self.criarusuario_novo.place(x=600, y=80)

            self.criarusuario_editar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                     text="Editar", onvalue="liberado", offvalue="bloqueado",
                                                     switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                     state="disabled")
            self.criarusuario_editar.place(x=600, y=110)

            self.criarusuario_remover = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                      text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                      switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                      state="disabled")
            self.criarusuario_remover.place(x=600, y=140)

            # ________________________________________________________________________________________________________________________________________-

            titulo_gerenciarUser = ctk.CTkLabel(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                text="GERENCIAR USER", text_color=("black", "white"), height=38,
                                                width=200,
                                                fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_gerenciarUser.place(relx=0.1, rely=0.26, anchor="center")

            gerenciar_switch = ctk.CTkSwitch(titulo_gerenciarUser, font=ctk.CTkFont(weight="bold"), text="",
                                             onvalue="liberado", offvalue="bloqueado",
                                             switch_height=25, switch_width=45, progress_color="#3DED9D",
                                             command=lambda: self.AtivarSwitch(gerenciar_switch,
                                                                               self.gerenciar_visualizar,
                                                                               self.gerenciar_novo,
                                                                               self.gerenciar_editar,
                                                                               self.gerenciar_remover))
            gerenciar_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.gerenciar_visualizar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                      text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                      switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                      state="disabled")
            self.gerenciar_visualizar.place(x=10, y=260)

            self.gerenciar_novo = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                text="Novo", onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                state="disabled")
            self.gerenciar_novo.place(x=10, y=290)

            self.gerenciar_editar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                  text="Editar", onvalue="liberado", offvalue="bloqueado",
                                                  switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                  state="disabled")
            self.gerenciar_editar.place(x=10, y=320)

            self.gerenciar_remover = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                   text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                   switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                   state="disabled")
            self.gerenciar_remover.place(x=10, y=350)
        else:
            self.FrameModuloCadastroResp.tkraise()
            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloCadastro, cor=self.cor_destaque)

    def Modulo_Agenda(self, frame_resp):

        if self.FrameModuloAgendaResp is None:

            self.FrameModuloAgendaResp = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=900, corner_radius=0)
            self.FrameModuloAgendaResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloAgenda, cor=self.cor_destaque)

            titulo_agenda = ctk.CTkLabel(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"), text="AGENDA",
                                         text_color=("black", "white"), height=38, width=200,
                                         fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_agenda.place(relx=0.1, rely=0.03, anchor="center")

            agenda_switch = ctk.CTkSwitch(titulo_agenda, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                          offvalue="bloqueado",
                                          switch_height=25, switch_width=45, progress_color="#3DED9D",
                                          command=lambda: self.AtivarSwitch(agenda_switch, self.agenda_visualizar,
                                                                            self.agenda_novo, self.agenda_editar,
                                                                            self.agenda_remover))
            agenda_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.agenda_visualizar = ctk.CTkSwitch(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"),
                                                   text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                   switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                   state="disabled")
            self.agenda_visualizar.place(x=10, y=50)

            self.agenda_novo = ctk.CTkSwitch(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"), text="Novo",
                                             onvalue="liberado", offvalue="bloqueado",
                                             switch_height=25, switch_width=50, progress_color="#3DED9D",
                                             state="disabled")
            self.agenda_novo.place(x=10, y=80)

            self.agenda_editar = ctk.CTkSwitch(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"),
                                               text="Editar", onvalue="liberado", offvalue="bloqueado",
                                               switch_height=25, switch_width=50, progress_color="#3DED9D",
                                               state="disabled")
            self.agenda_editar.place(x=10, y=110)

            self.agenda_remover = ctk.CTkSwitch(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"),
                                                text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                state="disabled")
            self.agenda_remover.place(x=10, y=140)
        else:
            self.FrameModuloAgendaResp.tkraise()
            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloAgenda, cor=self.cor_destaque)

    def Modulo_Carteira(self, frame_resp):

        if self.FrameModuloCarteiraResp is None:

            self.FrameModuloCarteiraResp = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=900, corner_radius=0)
            self.FrameModuloCarteiraResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloCarteira, cor=self.cor_destaque)

            titulo_vendas = ctk.CTkLabel(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="VENDAS",
                                         text_color=("black", "white"), height=38, width=200,
                                         fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_vendas.place(relx=0.1, rely=0.03, anchor="center")

            vendas_switch = ctk.CTkSwitch(titulo_vendas, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                          offvalue="bloqueado",
                                          switch_height=25, switch_width=45, progress_color="#3DED9D",
                                          command=lambda: self.AtivarSwitch(vendas_switch, self.vendas_visualizar,
                                                                            self.vendas_novo, self.vendas_editar,
                                                                            self.vendas_remover))
            vendas_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.vendas_visualizar = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"),
                                                   text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                   switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                   state="disabled")
            self.vendas_visualizar.place(x=10, y=50)

            self.vendas_novo = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="Novo",
                                             onvalue="liberado", offvalue="bloqueado",
                                             switch_height=25, switch_width=50, progress_color="#3DED9D",
                                             state="disabled")
            self.vendas_novo.place(x=10, y=80)

            self.vendas_editar = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"),
                                               text="Editar", onvalue="liberado", offvalue="bloqueado",
                                               switch_height=25, switch_width=50, progress_color="#3DED9D",
                                               state="disabled")
            self.vendas_editar.place(x=10, y=110)

            self.vendas_remover = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"),
                                                text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                state="disabled")
            self.vendas_remover.place(x=10, y=140)

            # ____________________________________________________________________________________________________________________________________________________________________________________

            titulo_faturamento = ctk.CTkLabel(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"),
                                              text="FATURAMENTO", text_color=("black", "white"), height=38, width=200,
                                              fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_faturamento.place(relx=0.36, rely=0.03, anchor="center")

            faturamento_switch = ctk.CTkSwitch(titulo_faturamento, font=ctk.CTkFont(weight="bold"), text="",
                                               onvalue="liberado", offvalue="bloqueado",
                                               switch_height=25, switch_width=45, progress_color="#3DED9D",
                                               command=lambda: self.AtivarSwitch(faturamento_switch,
                                                                                 self.faturamento_visualizar,
                                                                                 self.faturamento_novo,
                                                                                 self.faturamento_editar,
                                                                                 self.faturamento_remover))
            faturamento_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.faturamento_visualizar = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"),
                                                        text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                        switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                        state="disabled")
            self.faturamento_visualizar.place(x=300, y=50)

            self.faturamento_novo = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"),
                                                  text="Novo", onvalue="liberado", offvalue="bloqueado",
                                                  switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                  state="disabled")
            self.faturamento_novo.place(x=300, y=80)

            self.faturamento_editar = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"),
                                                    text="Editar", onvalue="liberado", offvalue="bloqueado",
                                                    switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                    state="disabled")
            self.faturamento_editar.place(x=300, y=110)

            self.faturamento_remover = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"),
                                                     text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                     switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                     state="disabled")
            self.faturamento_remover.place(x=300, y=140)
        else:
            self.FrameModuloCarteiraResp.tkraise()
            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloCarteira, cor=self.cor_destaque)

    def Modulo_Financas(self, frame_resp):

        if self.FrameModuloFinancasResp is None:

            self.FrameModuloFinancasResp = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=900, corner_radius=0)
            self.FrameModuloFinancasResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloFinancas, cor=self.cor_destaque)

            titulo_despesas = ctk.CTkLabel(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                           text="DESPESAS", text_color=("black", "white"), height=38, width=200,
                                           fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_despesas.place(relx=0.1, rely=0.03, anchor="center")

            despesas_switch = ctk.CTkSwitch(titulo_despesas, font=ctk.CTkFont(weight="bold"), text="",
                                            onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=45, progress_color="#3DED9D",
                                            command=lambda: self.AtivarSwitch(despesas_switch, self.despesas_visualizar,
                                                                              self.despesas_novo, self.despesas_editar,
                                                                              self.despesas_remover))
            despesas_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.despesas_visualizar = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                                     text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                     switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                     state="disabled")
            self.despesas_visualizar.place(x=10, y=50)

            self.despesas_novo = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                               text="Novo", onvalue="liberado", offvalue="bloqueado",
                                               switch_height=25, switch_width=50, progress_color="#3DED9D",
                                               state="disabled")
            self.despesas_novo.place(x=10, y=80)

            self.despesas_editar = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                                 text="Editar", onvalue="liberado", offvalue="bloqueado",
                                                 switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                 state="disabled")
            self.despesas_editar.place(x=10, y=110)

            self.despesas_remover = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                                  text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                  switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                  state="disabled")
            self.despesas_remover.place(x=10, y=140)

            # ____________________________________________________________________________________________________________________________________________________________________________________

            titulo_rendas = ctk.CTkLabel(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                         text="OUTRAS RENDAS", text_color=("black", "white"), height=38, width=200,
                                         fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_rendas.place(relx=0.36, rely=0.03, anchor="center")

            rendas_switch = ctk.CTkSwitch(titulo_rendas, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                          offvalue="bloqueado",
                                          switch_height=25, switch_width=45, progress_color="#3DED9D",
                                          command=lambda: self.AtivarSwitch(rendas_switch, self.rendas_visualizar,
                                                                            self.rendas_novo, self.rendas_editar,
                                                                            self.rendas_remover))
            rendas_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.rendas_visualizar = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                                   text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                   switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                   state="disabled")
            self.rendas_visualizar.place(x=300, y=50)

            self.rendas_novo = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"), text="Novo",
                                             onvalue="liberado", offvalue="bloqueado",
                                             switch_height=25, switch_width=50, progress_color="#3DED9D",
                                             state="disabled")
            self.rendas_novo.place(x=300, y=80)

            self.rendas_editar = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                               text="Editar", onvalue="liberado", offvalue="bloqueado",
                                               switch_height=25, switch_width=50, progress_color="#3DED9D",
                                               state="disabled")
            self.rendas_editar.place(x=300, y=110)

            self.rendas_remover = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                                text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                state="disabled")
            self.rendas_remover.place(x=300, y=140)

        else:
            self.FrameModuloFinancasResp.tkraise()
            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloFinancas, cor=self.cor_destaque)

    def Modulo_Usuario(self, frame_resp):

        if self.FrameModuloUsuarioResp is None:
            self.FrameModuloUsuarioResp = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=900, corner_radius=0)
            self.FrameModuloUsuarioResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloUsuarios, cor=self.cor_destaque)

            titulo_usuario = ctk.CTkLabel(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"), text="USUARIO",
                                          text_color=("black", "white"), height=38, width=200,
                                          fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_usuario.place(relx=0.1, rely=0.03, anchor="center")

            usuario_switch = ctk.CTkSwitch(titulo_usuario, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                           offvalue="bloqueado",
                                           switch_height=25, switch_width=45, progress_color="#3DED9D",
                                           command=lambda: self.AtivarSwitch(usuario_switch, self.usuario_visualizar,
                                                                             self.usuario_novo, self.usuario_editar,
                                                                             self.usuario_remover))
            usuario_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.usuario_visualizar = ctk.CTkSwitch(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"),
                                                    text="Visualizar", onvalue="liberado", offvalue="bloqueado",
                                                    switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                    state="disabled")
            self.usuario_visualizar.place(x=10, y=50)

            self.usuario_novo = ctk.CTkSwitch(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"), text="Novo",
                                              onvalue="liberado", offvalue="bloqueado",
                                              switch_height=25, switch_width=50, progress_color="#3DED9D",
                                              state="disabled")
            self.usuario_novo.place(x=10, y=80)

            self.usuario_editar = ctk.CTkSwitch(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"),
                                                text="Editar", onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                state="disabled")
            self.usuario_editar.place(x=10, y=110)

            self.usuario_remover = ctk.CTkSwitch(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"),
                                                 text="Remover", onvalue="liberado", offvalue="bloqueado",
                                                 switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                 state="disabled")
            self.usuario_remover.place(x=10, y=140)
        else:
            self.FrameModuloUsuarioResp.tkraise()
            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloUsuarios, cor=self.cor_destaque)

    def Modulo_Configuracoes(self, frame_resp):

        if self.FrameModuloConfiguracoesResp is None:

            self.FrameModuloConfiguracoesResp = ctk.CTkFrame(self.frame_resp, width=(self.main_app.screen_wedth)-270, height=900, corner_radius=0)
            self.FrameModuloConfiguracoesResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloConfiguracoes, cor=self.cor_destaque)

            titulo_configuracoes = ctk.CTkLabel(self.FrameModuloConfiguracoesResp, font=ctk.CTkFont(weight="bold"),
                                                text="CONFIGURAÇÕES", text_color=("black", "white"), height=38,
                                                width=200,
                                                fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_configuracoes.place(relx=0.1, rely=0.03, anchor="center")

            configuracoes_switch = ctk.CTkSwitch(titulo_configuracoes, font=ctk.CTkFont(weight="bold"), text="",
                                                 onvalue="liberado", offvalue="bloqueado",
                                                 switch_height=25, switch_width=45, progress_color="#3DED9D",
                                                 command=lambda: self.AtivarSwitch(configuracoes_switch,
                                                                                   self.configuracoes_visualizar,
                                                                                   self.configuracoes_novo,
                                                                                   self.configuracoes_editar,
                                                                                   self.configuracoes_remover))
            configuracoes_switch.place(relx=0.94, rely=0.5, anchor="center")

            self.configuracoes_visualizar = ctk.CTkSwitch(self.FrameModuloConfiguracoesResp,
                                                          font=ctk.CTkFont(weight="bold"), text="Visualizar",
                                                          onvalue="liberado", offvalue="bloqueado",
                                                          switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                          state="disabled")
            self.configuracoes_visualizar.place(x=10, y=50)

            self.configuracoes_novo = ctk.CTkSwitch(self.FrameModuloConfiguracoesResp, font=ctk.CTkFont(weight="bold"),
                                                    text="Novo", onvalue="liberado", offvalue="bloqueado",
                                                    switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                    state="disabled")
            self.configuracoes_novo.place(x=10, y=80)

            self.configuracoes_editar = ctk.CTkSwitch(self.FrameModuloConfiguracoesResp,
                                                      font=ctk.CTkFont(weight="bold"), text="Editar",
                                                      onvalue="liberado", offvalue="bloqueado",
                                                      switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                      state="disabled")
            self.configuracoes_editar.place(x=10, y=110)

            self.configuracoes_remover = ctk.CTkSwitch(self.FrameModuloConfiguracoesResp,
                                                       font=ctk.CTkFont(weight="bold"), text="Remover",
                                                       onvalue="liberado", offvalue="bloqueado",
                                                       switch_height=25, switch_width=50, progress_color="#3DED9D",
                                                       state="disabled")
            self.configuracoes_remover.place(x=10, y=140)

        else:
            self.FrameModuloConfiguracoesResp.tkraise()
            self.main_app.destacar(self.listaBTS, botão=self.BT_ModuloConfiguracoes, cor=self.cor_destaque)
    



        print("em construção")

class InterfaceUsuario:

    def __init__(self, main_app, frame_resp, bt_perfil):

        self.main_app = main_app
        self.frame_resp = frame_resp
        self.bt_perfil = bt_perfil
        self.conexao = self.main_app.ConexaoPrincipal

        self.interface()

    def interface(self):


        Painel_FtPerfil = ctk.CTkButton(self.frame_resp, text="", width=(self.main_app.screen_wedth)-270, height=90, border_width=1,
                                        fg_color="transparent",hover=False)
        Painel_FtPerfil.place(relx=0.02, rely=0.1, anchor="w")

        Label_FtPerfil = ctk.CTkLabel(Painel_FtPerfil, text="Foto de perfil", font=self.main_app.FontTitle, fg_color="transparent")
        Label_FtPerfil.place(x=10, y=5)
        bt = ctk.CTkButton(Painel_FtPerfil, image=ImagemIcon, text="Alterar", command=self.Trocar_img,
                           text_color=("black", "white"),
                           width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'))
        bt.place(x=10, y=50)

        Painel_Usuario = ctk.CTkButton(self.frame_resp, text="", width=(self.main_app.screen_wedth)-270, height=90, border_width=1,
                                       fg_color="transparent",hover=False)
        Painel_Usuario.place(relx=0.02, rely=0.25, anchor="w")

        TituloUsuario = ctk.CTkLabel(Painel_Usuario, text="Usuario", font=self.main_app.FontTitle, fg_color="transparent")
        TituloUsuario.place(x=10, y=5)

        self.LabelUsuario = ctk.CTkLabel(Painel_Usuario, text=f"{self.main_app.usuario_logado}", font=self.main_app.FontBody, fg_color="transparent")
        self.LabelUsuario.place(x=10, y=50)

        TituloAcesso = ctk.CTkLabel(Painel_Usuario, text="Acesso", font=self.main_app.FontTitle, fg_color="transparent")
        TituloAcesso.place(x=100, y=5)

        LabelAcesso = ctk.CTkLabel(Painel_Usuario, text=f"{self.main_app.acesso_usuario.upper()}",  font=self.main_app.FontBody,
                                   fg_color="transparent")
        LabelAcesso.place(x=100, y=50)

        BtEditarUser = ctk.CTkButton(Painel_Usuario, image=EditarIcon2, text="Editar", text_color=("black", "white"),
                                     width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'),
                                     command=self.Editar_Usuario)
        BtEditarUser.place(x=165, y=28)


        Painel_Senha = ctk.CTkButton(self.frame_resp, text="", width=(self.main_app.screen_wedth)-270, height=90, border_width=1, fg_color="transparent",
                                     hover=False)
        Painel_Senha.place(relx=0.02, rely=0.4, anchor="w")


        LabelSenha = ctk.CTkLabel(Painel_Senha, text="Senha", font=self.main_app.FontTitle, fg_color="transparent")
        LabelSenha.place(x=10, y=5)


        BtTrocarSenha = ctk.CTkButton(Painel_Senha, image=SenhaIcon, text="Alterar", text_color=("black", "white"),
                                      width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'),
                                      command=self.Trocar_senha)
        BtTrocarSenha.place(x=10, y=50)


        Painel_Excluir = ctk.CTkButton(self.frame_resp, text="", width=(self.main_app.screen_wedth)-270, height=90, border_width=1,
                                       fg_color="transparent", hover=False)
        Painel_Excluir.place(relx=0.02, rely=0.55, anchor="w")


        LabelExcluir = ctk.CTkLabel(Painel_Excluir, text="Conta", font=self.main_app.FontTitle, fg_color="transparent")
        LabelExcluir.place(x=10, y=5)

        BtExcluir = ctk.CTkButton(Painel_Excluir, image=DeletarIcon2, text="Excluir Conta",
                                  text_color=("black", "white"),
                                  width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'),
                                  command=self.Excluir_conta)
        BtExcluir.place(x=10, y=50)

    def Trocar_img(self):
        imagem = self.bt_perfil

        CarregarIMG(main_app=self.main_app).select_image(imagem, usuario=self.main_app.usuario_logado)

    def Editar_Usuario(self):
        dialog = ctk.CTkInputDialog(text="DIGITE SEU NOVO NOME DE USUARIO:", title="Editar",
                                    button_fg_color="#323232", button_hover_color='#191919')
        usuarioDigitado = dialog.get_input()

        if usuarioDigitado != None:

            if len(usuarioDigitado) >= 3:
                
                cursor = self.main_app.ConexaoPrincipal.cursor()
                cursor.execute(f"SELECT usuario FROM Usuarios WHERE BINARY usuario = '{usuarioDigitado}'")
                respostaBD = cursor.fetchall()
                if not respostaBD:
                    cursor.execute(f"UPDATE Usuarios SET usuario = '{usuarioDigitado}' WHERE usuario = '{self.main_app.usuario_logado}'")
                    self.main_app.usuario_logado = str(usuarioDigitado)
                    self.main_app.ConexaoPrincipal.commit()
                    self.LabelUsuario.configure(text=usuarioDigitado)

                elif usuarioDigitado == self.main_app.usuario_logado:
                    self.main_app.msgbox("USUARIO", "Este ja é o seu nome de usuario\n Informe um nome diferente.", 0)

                else:
                    self.main_app.msgbox("USUARIO", "Ja existe um usuario com este nome!!!", 0)
                   

            elif 1 <= len(usuarioDigitado) <= 2:
                self.main_app.msgbox("USUARIO", "Seu novo nome de usuario deve conter pelo menos 3 caracteres", 0)

    def Trocar_senha(self):

        dialog = ctk.CTkToplevel()
        dialog.title("SENHA")
        dialog.geometry("340x250")
        dialog.resizable(0, 0)
        dialog.grab_set()

        def requisitos_atual(event):
            msgatual = ctk.CTkLabel(dialog, text="Senha atual", height=3)
            msgatual.place(relx=0.15, rely=0.2, anchor="center")

        def requisitos_senha1(event):
            nova = str(NovaSenha.get())
            if len(nova) <= 5:
                msgnova = ctk.CTkLabel(dialog, text="Nova senha", height=3)
                msgnova.place(relx=0.15, rely=0.4, anchor="center")
                resposta.configure(text="Sua senha deve ter no minimo 6 caracteres.", text_color="red")
                Okbt.configure(state="disabled")
            else:
                resposta.configure(text="", text_color="green")

                if len(str(ConfirmacaoSenha.get())) > 5:
                    Okbt.configure(state="normal")

        def requisitos_senha2(event):
            nova = str(NovaSenha.get())
            confir = str(ConfirmacaoSenha.get())

            msgconfir = ctk.CTkLabel(dialog, text="Redigite a nova senha", height=3)
            msgconfir.place(relx=0.23, rely=0.6, anchor="center")

            if confir == nova and len(confir) > 5:
                resposta.configure(text="", text_color="Green")
                Okbt.configure(state="normal")
                if len(nova) > 5:
                    Okbt.configure(state="normal")

            else:
                resposta.configure(text="A nova senha não é igual à redigitada.", text_color="red")
                Okbt.configure(state="disabled")

        def salvar():
            atual = str(SenhaAtual.get())
            nova = str(NovaSenha.get())

            cursor =  self.main_app.ConexaoPrincipal.cursor()
            cursor.execute(
                f"SELECT senha FROM Usuarios WHERE usuario = '{self.main_app.usuario_logado}' AND senha = '{atual}'")
            resultado_bd = cursor.fetchall()

            if resultado_bd:
                cursor.execute(f"UPDATE Usuarios SET senha = '{nova}' WHERE usuario = '{self.main_app.usuario_logado}'")
                self.main_app.ConexaoPrincipal.commit()
                resposta.configure(text="Senha atualizada com sucesso!", text_color="green")
                Okbt.configure(state="disabled")
            else:
                resposta.configure(text="Senha atual esta incorreta", text_color="red")

        def fechar():
                dialog.destroy()

        msg = ctk.CTkLabel(dialog, text="TROCAR SENHA", font=self.main_app.FontTitle)
        msg.place(relx=0.5, rely=0.1, anchor="center")

        SenhaAtual = ctk.CTkEntry(dialog, placeholder_text="Digite sua senha atual", width=320)
        SenhaAtual.place(relx=0.5, rely=0.3, anchor="center")
        SenhaAtual.bind('<KeyRelease>', requisitos_atual)

        NovaSenha = ctk.CTkEntry(dialog, placeholder_text="Digite sua nova senha", width=320, show="*")
        NovaSenha.place(relx=0.5, rely=0.5, anchor="center")
        NovaSenha.bind('<KeyRelease>', requisitos_senha1)

        ConfirmacaoSenha = ctk.CTkEntry(dialog, placeholder_text="Confirmar nova senha", width=320, show="*")
        ConfirmacaoSenha.place(relx=0.5, rely=0.7, anchor="center"),
        ConfirmacaoSenha.bind('<KeyRelease>', requisitos_senha2)

        resposta = ctk.CTkLabel(dialog, text="", height=2)
        resposta.place(relx=0.5, rely=0.81, anchor="center")

        Okbt = ctk.CTkButton(dialog, text="SALVAR", fg_color="#323232", hover_color='#191919', command=salvar,
                                state='disabled')
        Okbt.place(relx=0.25, rely=0.92, anchor="center")

        CancelarBT = ctk.CTkButton(dialog, text="Fechar", fg_color="#323232", hover_color='#191919',
                                    command=fechar)
        CancelarBT.place(relx=0.75, rely=0.92, anchor="center")
      
    def Excluir_conta(self):

        dialog = ctk.CTkToplevel()
        dialog.title("EXCLUIR")
        dialog.geometry("340x120")
        dialog.resizable(0, 0)
        dialog.grab_set()

        def fechar():
            dialog.destroy()

        def conta_delete():
            cursor = self.main_app.ConexaoPrincipal.cursor()
            cursor.execute(f"DELETE FROM Usuarios where usuario = '{self.main_app.usuario_logado}'")
            self.main_app.ConexaoPrincipal.commit()
            dialog.destroy()

            self.main_app.root.geometry(f"400x430")
            self.main_app.login()

        msg = ctk.CTkLabel(dialog, text="DESEJA REALMENTE EXCLUIR SUA CONTA?", font=self.main_app.SubTitle)
        msg.place(relx=0.5, rely=0.1, anchor="center")

        Okbt = ctk.CTkButton(dialog, text="EXCLUIR", fg_color="#323232", hover_color='#191919',
                                command=conta_delete)
        Okbt.place(relx=0.25, rely=0.79, anchor="center")

        CancelarBT = ctk.CTkButton(dialog, text="Fechar", fg_color="#323232", hover_color='#191919',
                                    command=fechar)
        CancelarBT.place(relx=0.75, rely=0.79, anchor="center")

class CarregarIMG:

    def __init__(self, main_app):

        self.main_app = main_app
        self.conexao = self.main_app.ConexaoPrincipal

    def verificar_foto(self, label_img, usuario):

        cursor =  self.conexao.cursor()
        # Buscar a imagem no banco de dados
        cursor.execute(f"SELECT img FROM Usuarios WHERE BINARY usuario = '{usuario}'")
        result = cursor.fetchone()

        if result[0] is not None:
            try:
                # Converter o valor binário para imagem
                image_binary = result[0]  # A coluna 'img' é o índice 2 no resultado
                image = Image.open(io.BytesIO(image_binary))

                # Redimensionar a imagem se necessário
                image = image.resize((100, 100))
                # Crie uma nova imagem circular de fundo transparente
                image_circular = Image.new("RGBA", image.size, (0, 0, 0, 0))

                # Crie um objeto de desenho
                draw = ImageDraw.Draw(image_circular)

                # Calcule as coordenadas do círculo
                center_x = image_circular.width // 2
                center_y = image_circular.height // 2
                radius = min(center_x, center_y)

                # Desenhe o círculo
                draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill="white")

                # Recorte a imagem usando o círculo como máscara
                image_circular.paste(image, (0, 0), mask=image_circular)

                # Converter a imagem circular para o formato suportado pelo Tkinter
                photo = ctk.CTkImage(image_circular, size=(100,100))
                # Atualizar o widget Label com a nova imagem
                label_img.configure(image=photo, text="")
                label_img.image = photo
            except Exception as erro:
                print(erro)

        else:
            print("não existe nenhuma img no banco de dados")

    def select_image(self, label_img, usuario):  # Função para selecionar a imagem
        # Abrir o diálogo de seleção de arquivo
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])

        # Verificar se um arquivo foi selecionado
        if file_path:
            # Carregar a imagem selecionada
            self.load_image(file_path, label_img)

            # Converter a imagem para bytes
            with open(file_path, "rb") as f:
                image_bytes = f.read()

            # Converter os bytes para base64
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            # Inserir ou atualizar a imagem no banco de dados
            self.insert_image(image_base64, usuario)

    def load_image(self, file_path, label_img):  # Função para carregar a imagem
        # Carregar a imagem
        image = Image.open(file_path)

        # Redimensionar a imagem se necessário
        image = image.resize((100, 100))
        # Crie uma nova imagem circular de fundo transparente
        image_circular = Image.new("RGBA", image.size, (0, 0, 0, 0))

        # Crie um objeto de desenho
        draw = ImageDraw.Draw(image_circular)

        # Calcule as coordenadas do círculo
        center_x = image_circular.width // 2
        center_y = image_circular.height // 2
        radius = min(center_x, center_y)

        # Desenhe o círculo
        draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill="white")

        # Recorte a imagem usando o círculo como máscara
        image_circular.paste(image, (0, 0), mask=image_circular)

        # Converter a imagem circular para o formato suportado pelo Tkinter
        photo = ctk.CTkImage(image_circular, size=(100,100))

        # Atualizar o widget Label com a nova imagem
        label_img.configure(image=photo, text="")
        label_img.image = photo

    def insert_image(self, image_base64, usuario):  # Função para inserir ou atualizar a img no BD



        cursor =  self.conexao.cursor()

        # Converter a imagem base64 para dados binários
        image_binary = binascii.a2b_base64(image_base64)

        # Verificar se já existe uma imagem com o ID 1
        cursor.execute(f"SELECT COUNT(*) FROM Usuarios WHERE usuario = '{usuario}'")
        count = cursor.fetchone()[0]

        if count > 0:
            # Atualizar a imagem existente
            cursor.execute("UPDATE Usuarios SET img = %s WHERE usuario = %s", (image_binary, usuario))
        else:
            self.main_app.msgbox("ERRO", "NAO ENCONTRADO USUARIO NO BD PARA INSERIR A NOVA IMAGEM", 0)

        # Salvar as alterações e fechar a conexão
        self.conexao.commit()

class MenuOpcoes:

    def __init__(self, root, main_app):
        self.rootHome = root
        self.main_app = main_app

        self.conexao = self.main_app.ConexaoPrincipal

        self.rootHome.title("SYS COMERCIAL")
        self.rootHome.state('zoomed')

        self.screen_height = self.rootHome.winfo_screenheight()
        self.screen_wedth = self.rootHome.winfo_screenwidth()

        self.listaBTS = []

        self.cor_destaque = ("white", "#880016")

        

        self.frame_MenuLateralEsq = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, corner_radius=0)
        self.frame_MenuLateralEsq.grid(row=0, column=0)


        self.frame_MenuLateralDir = ctk.CTkFrame(self.rootHome,width=37, height=self.screen_height, corner_radius=0,fg_color=self.cor_destaque)
        self.frame_MenuLateralDir.grid(row=0, column=1)


        self.frame_resposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=self.screen_wedth, height=self.screen_height, corner_radius=0)
        self.frame_resposta.grid(row=0, column=2)


        self.BtOcultar = ctk.CTkButton(self.frame_MenuLateralDir, text="", image=MenuIcon, anchor="w", width=23, height=23,
                                    fg_color="transparent", text_color=("black", "white"),
                                    command=lambda:self.main_app.ocultar_Janela(self.frame_MenuLateralEsq))

        

        self.bt_opcoes()

    def limpar_frames(self, laterial_direito, resposta, pos = 0, excluir = False):
       
        
        # Esconder os widgets em vez de destruí-los
        for widget in laterial_direito.winfo_children():
            widget.place_forget()

        if excluir:
            for widget in resposta.winfo_children():
                widget.place_forget()


        self.frame_MenuLateralDir.configure(width=37)
        self.BtOcultar.place(x=pos, y=1)
        
    def bt_opcoes(self):

        self.BtHome = ctk.CTkButton(self.frame_MenuLateralEsq, text="Home", image=HomeIcon, anchor="w",
                                    width=176, corner_radius=0, fg_color="transparent", text_color=("black", "white"),command=self.frame_home)
        self.BtHome.place(x=0, y=120)

        self.BtEstoque = ctk.CTkButton(self.frame_MenuLateralEsq, text="Estoque ", image=EstoqueIcon, anchor="w",
                                    width=176, corner_radius=0, fg_color="transparent",
                                    text_color=("black", "white"),command=self.frame_estoque)
        self.BtEstoque.place(x=0, y=160)

        self.BtCadastros = ctk.CTkButton(self.frame_MenuLateralEsq, text="Cadastro", image=CadastroIcon, anchor="w",
                                        width=176, corner_radius=0, fg_color="transparent",
                                        text_color=("black", "white"), command=self.frame_cadastro)
        self.BtCadastros.place(x=0, y=200)

        self.BtAgenda = ctk.CTkButton(self.frame_MenuLateralEsq, text="Agenda", image=AgendaIcon, anchor="w",
                                    width=176, corner_radius=0, fg_color="transparent", text_color=("black", "white"),
                                    command=self.frame_agenda)
        self.BtAgenda.place(x=0, y=240)

        self.Btcarteira = ctk.CTkButton(self.frame_MenuLateralEsq, text="Carteira", image=carteiraIcon, anchor="w",
                                        width=176, corner_radius=0, fg_color="transparent",
                                        text_color=("black", "white"), command=self.frame_carteira)
        self.Btcarteira.place(x=0, y=280)

        self.BtFinancas = ctk.CTkButton(self.frame_MenuLateralEsq, text="Finanças", image=FinancasIcon, anchor="w",
                                        width=176, corner_radius=0, fg_color="transparent",
                                        text_color=("black", "white"), command=self.frame_financas)
        self.BtFinancas.place(x=0, y=320)

        self.BtUsuario = ctk.CTkButton(self.frame_MenuLateralEsq, text="Usuario", image=UsuarioIcon, anchor="w",
                                    width=176, corner_radius=0, fg_color="transparent",
                                    text_color=("black", "white"), command=self.frame_usuario)
        self.BtUsuario.place(x=0, y=360)

        self.BtConfiguracoes = ctk.CTkButton(self.frame_MenuLateralEsq, text="Configuracoes", image=ConfiguracoesIcon,
                                            anchor="w",
                                            width=176, corner_radius=0, text_color=("black", "white"),
                                            fg_color="transparent",command=self.frame_configuracoes)
        self.BtConfiguracoes.place(x=0, y=400)

        self.Btfoto_perfil = ctk.CTkButton(self.frame_MenuLateralEsq, text="", image=perfilIcon, fg_color="transparent", command=self.frame_usuario)
        self.Btfoto_perfil.place(relx=0.5, rely=0.07, anchor="center")



        self.listaBTS = [self.BtHome, self.BtEstoque,  self.BtCadastros, self.BtAgenda, self.Btcarteira, 
                            self.BtFinancas, self.BtUsuario, self.BtConfiguracoes]
        

        self.LabelLogo = ctk.CTkLabel(self.frame_MenuLateralEsq, text="", image=SeuLogo2)
        self.LabelLogo.place(x=-10, y=(self.screen_height - 300))


        
        appearance_mode_optionemenu = ctk.CTkOptionMenu(self.frame_MenuLateralEsq, font=self.main_app.FontBody, width=150,
                                                        height=30, values=["Dark", "light"], command=self.main_app.aparencia)
        appearance_mode_optionemenu.place(x=10, y=(self.screen_height - 100))
        
        self.main_app.desativar_modulos()
        CarregarIMG(main_app=self.main_app).verificar_foto(self.Btfoto_perfil, self.main_app.usuario_logado)
        self.frame_home()

    def frame_home(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtHome, cor=self.cor_destaque)

        texto = ctk.CTkLabel(self.frame_resposta, text="",image=img_apresentacao)
        texto.place(x=1,y=1)

    def frame_estoque(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=138)
        self.frame_MenuLateralDir.configure(width = 176)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtEstoque, cor=self.cor_destaque)

        self.BTEntrada = ctk.CTkButton(self.frame_MenuLateralDir, text="Entrada", image=EntradaIcon, anchor="w", width=155,
                                    fg_color=("#FFD6D6", "gray17"), text_color=("black", "white"),
                                    hover_color=("#ff9ea2", "black"))
        self.BTEntrada.place(x=10, y=120)

        self.BTSaida = ctk.CTkButton(self.frame_MenuLateralDir, text="Saida", image=SaidaIcon, anchor="w", width=155,
                                    fg_color=("#FFD6D6", "gray17"), text_color=("black", "white"),
                                    hover_color=("#ff9ea2", "black"))
        self.BTSaida.place(x=10, y=160)

        self.BTInventario = ctk.CTkButton(self.frame_MenuLateralDir, text="Inventario", image=InventarioIcon, anchor="w",
                                        width=155, fg_color=("#FFD6D6", "gray17"), text_color=("black", "white"),
                                        hover_color=("#ff9ea2", "black"))
        self.BTInventario.place(x=10, y=200)

        self.main_app.desativar_submodulos(modulo='Estoque')

    def frame_cadastro(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=138)
        self.frame_MenuLateralDir.configure(width = 176)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtCadastros, cor=self.cor_destaque)

        self.BTCadastrarItens = ctk.CTkButton(self.frame_MenuLateralDir, text="Cadastrar Itens", image=EstoqueIcon,
                                              anchor="w", width=155, fg_color=("#FFD6D6", "gray17"),
                                              text_color=("black", "white"),
                                              hover_color=("#ff9ea2", "black"))
        self.BTCadastrarItens.place(x=10, y=160)

        self.BTCadastrarClientes = ctk.CTkButton(self.frame_MenuLateralDir, text="Cadastrar Clientes", image=CadastroIcon,
                                                 anchor="w", width=155, fg_color=("#FFD6D6", "gray17"),
                                                 text_color=("black", "white"),
                                                 hover_color=("#ff9ea2", "black"),
                                                 command=lambda: self.frame_novocliente())
        self.BTCadastrarClientes.place(x=10, y=200)

        self.BTCriarNovoUsuario = ctk.CTkButton(self.frame_MenuLateralDir, text="Novo Usuario", image=UsuarioIcon,
                                                anchor="w", width=155, fg_color=("#FFD6D6", "gray17"),
                                                text_color=("black", "white"),
                                                hover_color=("#ff9ea2", "black"), command=lambda: self.frame_novo_user())
        self.BTCriarNovoUsuario.place(x=10, y=240)

        self.BTGerenciarUsuario = ctk.CTkButton(self.frame_MenuLateralDir, text="Gerenciar Usuarios",
                                                image=GerenciarUserIcon, anchor="w", width=155,
                                                fg_color=("#FFD6D6", "gray17"), text_color=("black", "white"),
                                                hover_color=("#ff9ea2", "black"),
                                                command=lambda: self.frame_gerenciar_user())
        
        self.main_app.desativar_submodulos(modulo='Cadastro')

        self.BTGerenciarUsuario.place(x=10, y=280)

    def frame_novocliente(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=0, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtCadastros, cor=self.cor_destaque)

        self.main_app.exibir_novocliente(self.frame_resposta)

    def frame_novo_user(self):
        
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=0, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtCadastros, cor=self.cor_destaque)

        # LabelTitulo = ctk.CTkLabel(self.frame_resposta, text=f"NOVO USUARIO",fg_color="transparent", text_color=("black", "white"), 
        #                            font=self.main_app.SubTitle, corner_radius=6)
        # LabelTitulo.place(relx=0.001, rely=0.02, anchor="w")

        self.main_app.exibir_novousuario(self.frame_resposta)

    def frame_gerenciar_user(self):
        
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=0, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtCadastros, cor=self.cor_destaque)
        
        LabelTitulo = ctk.CTkLabel(self.frame_resposta, text=f"GERENCIAR USUARIOS",fg_color="transparent", text_color=("black", "white"), 
                                   font=self.main_app.SubTitle, corner_radius=6)
        LabelTitulo.place(relx=0.001, rely=0.02, anchor="w")
        self.main_app.exibir_gerenciarusuarios(self.frame_resposta)

    def frame_agenda(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtAgenda, cor=self.cor_destaque)

        LabelTitulo = ctk.CTkLabel(self.frame_resposta, text=f"AGENDA",fg_color="transparent", text_color=("black", "white"), 
                                   font=self.main_app.SubTitle, corner_radius=6)
        LabelTitulo.place(relx=0.001, rely=0.02, anchor="w")

    def frame_carteira(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=138)
        self.frame_MenuLateralDir.configure(width = 176)

        self.main_app.destacar(lista=self.listaBTS, botão=self.Btcarteira, cor=self.cor_destaque)


        self.BTRegistrarVenda = ctk.CTkButton(self.frame_MenuLateralDir, text="Registrar Venda", image=VendasIcon,
                                              anchor="w", width=155, fg_color=("#FFD6D6", "gray17"),
                                              text_color=("black", "white"),
                                              hover_color=("#ff9ea2", "black"))
        self.BTRegistrarVenda.place(x=10, y=280)

        self.BTFaturamento = ctk.CTkButton(self.frame_MenuLateralDir, text="Faturamento", image=FaturamentoIcon,
                                           anchor="w", width=155, fg_color=("#FFD6D6", "gray17"),
                                           text_color=("black", "white"),
                                           hover_color=("#ff9ea2", "black"))
        self.BTFaturamento.place(x=10, y=320)

        self.main_app.desativar_submodulos(modulo='carteira')

    def frame_financas(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=138)
        self.frame_MenuLateralDir.configure(width = 176)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtFinancas, cor=self.cor_destaque)



        self.BTRegistrarDespesas = ctk.CTkButton(self.frame_MenuLateralDir, text="Registrar Despesas", image=DespesaIcon,
                                                 anchor="w", width=155, fg_color=("#FFD6D6", "gray17"),
                                                 text_color=("black", "white"),
                                                 hover_color=("#ff9ea2", "black"))
        self.BTRegistrarDespesas.place(x=10, y=320)

        self.BTOutrasRendas = ctk.CTkButton(self.frame_MenuLateralDir, text="Outras Rendas +", image=ReceitaIcon,
                                            anchor="w", width=155, fg_color=("#FFD6D6", "gray17"),
                                            text_color=("black", "white"),
                                            hover_color=("#ff9ea2", "black"))
        self.BTOutrasRendas.place(x=10, y=360)
        self.main_app.desativar_submodulos(modulo='Finanças')

    def frame_usuario(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtUsuario, cor=self.cor_destaque)


        LabelTitulo = ctk.CTkLabel(self.frame_resposta, text=f"USUARIO",fg_color="transparent", text_color=("black", "white"), 
                                   font=self.main_app.SubTitle, corner_radius=6)
        LabelTitulo.place(relx=0.001, rely=0.02, anchor="w")

        self.main_app.exibir_usuario(self.frame_resposta, self.Btfoto_perfil)

    def frame_configuracoes(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botão=self.BtConfiguracoes, cor=self.cor_destaque)

        LabelTitulo = ctk.CTkLabel(self.frame_resposta, text=f"CONFIGURAÇÕES",fg_color="transparent", text_color=("black", "white"), 
                                   font=self.main_app.SubTitle, corner_radius=6)
        LabelTitulo.place(relx=0.001, rely=0.02, anchor="w")

class TelaLogin:
    def __init__(self, root, main_app):
        self.Root_login = root
        self.main_app = main_app
        self.Root_login.title("Login")
        self.Root_login.geometry(f"400x430")

        self.conexao = self.main_app.ConexaoPrincipal



        LabelTxt = ctk.CTkLabel(self.Root_login, text="Bem Vindo", font= self.main_app.FontTitle)
        LabelTxt.place(relx=0.5, rely=0.2, anchor="center")

        def mostrar_senha():
            if self.MostrarSenha.get():
                self.SenhaDigitado.configure(show="")
            else:
                self.SenhaDigitado.configure(show="*")

        def ativar_enter(Event):
            self.fazer_login()

            # Aqui você pode adicionar a lógica que deseja executar quando a tecla Enter for pressionada
            # Por exemplo, você pode chamar uma função de verificação de login ou qualquer outra ação desejada
            

        self.LoginDigitado = ctk.CTkEntry(self.Root_login, placeholder_text="Digite seu login", width=200)
        self.LoginDigitado.place(relx=0.5, rely=0.3, anchor='center')

        self.SenhaDigitado = ctk.CTkEntry(self.Root_login, placeholder_text="Digite sua senha", width=200, show="*")
        self.SenhaDigitado.place(relx=0.5, rely=0.4, anchor='center')

        self.MostrarSenha = ctk.CTkCheckBox(self.Root_login, text="Mostrar senha", font= self.main_app.FontBody,
                                            command=mostrar_senha)
        self.MostrarSenha.place(relx=0.5, rely=0.5, anchor="center")

        self.BtEntrar = ctk.CTkButton(self.Root_login, text="Entrar", command=self.fazer_login,
                                      hover_color=("#880016", "#880016"),
                                      text_color=("white", "white"))
        self.BtEntrar.place(relx=0.5, rely=0.6, anchor="center")
        self.BtEntrar.bind("<Return>", ativar_enter)


        self.LabelLogo = ctk.CTkLabel(self.Root_login, text="", image=SeuLogo)
        self.LabelLogo.place(relx=0.5, rely=0.8, anchor="center")

        self.LabelTxt2 = ctk.CTkLabel(self.Root_login, text="Modo")
        self.LabelTxt2.place(relx=0.15, rely=0.90, anchor="center")


        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.Root_login, font= self.main_app.FontBody, width=100, height=20,
                                                        values=["Dark", "light"], command= self.main_app.aparencia)
        self.appearance_mode_optionemenu.place(relx=0.15, rely=0.95, anchor="center")

    def fazer_login(self):
        self.usuario_logado = self.LoginDigitado.get()
        self.senha_logado = self.SenhaDigitado.get()

        if len(self.usuario_logado) == 0 or len(self.senha_logado) == 0:
           self.main_app.msgbox("Login", "Preencha todos os campos", 0)
        else:

            cursor = self.conexao.cursor()
            cursor.execute(
                f"SELECT * FROM Usuarios WHERE BINARY usuario = '{self.usuario_logado}' "
                f"AND senha = '{self.senha_logado}' AND status = '{'ATIVO'}'")
            resultado = cursor.fetchall()
            if resultado:
                cursor.execute(f"SELECT acesso FROM Usuarios  WHERE BINARY  usuario = '{self.usuario_logado}' ")
                self.acesso_usuario = str(cursor.fetchall()[0][0])

                cursor.execute(f"select * from modulos where usuario = '{self.usuario_logado}'")
                self.main_app.ModulosDoUsuario = cursor.fetchall()
                self.main_app.usuario_logado = self.usuario_logado
                self.main_app.acesso_usuario = self.acesso_usuario
                self.main_app.login_sucesso()

            else:
                self.main_app.msgbox("Login", "Login ou senha incorretos, Tente novamente", 0)

class MainApp:
    ArqJson = r'liftam.JSON'
    ctk.set_default_color_theme(ArqJson)

    @staticmethod
    def _conectaBD(database, host, port, user, password):

        conexao = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
        # Verifique se a conexão foi estabelecida
        if conexao.is_connected():
            print('Conexão bem-sucedida ao banco de dados')
            return conexao

    def __init__(self, root):
        self.root = root
        self.root.title("SYS Comercial")    
        self.root.geometry(f"400x430")
        self.root.protocol("WM_DELETE_WINDOW", self.sair)

        self.FontTitle = ctk.CTkFont(size=20, weight="bold")
        self.SubTitle = ctk.CTkFont(size=14, weight="bold")
        self.FontBody = ctk.CTkFont(size=12)

        self.validate_cmd_numeric = root.register(self.validate_numeric_input)
        self.validade_cmd_text = root.register(self.validate_text_input)

        self.screen_height = self.root.winfo_screenheight()
        self.screen_wedth = self.root.winfo_screenwidth()

        self.ModulosDoUsuario = None

        self.usuario_logado = None

        self.acesso_usuario = None
        
        # self.ArqJson = r'liftam.JSON'
        # ctk.set_default_color_theme(self.ArqJson)


        self.ConexaoPrincipal = MainApp._conectaBD(database='railway', host='containers-us-west-1.railway.app', 
                                                   port=5474, user='root', password="JThLpvacyDNwzFLPyLhX")
        
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

    def ocultar_Janela(self, menulateral):

        larguraJanelaAtual = menulateral.winfo_width()

        if larguraJanelaAtual > 35:
            menulateral.configure(width=28)

        else:
            menulateral.configure(width=176)

    def exibir_gerenciarusuarios(self, frame_resposta):
        if self.acesso_usuario == "ADM":
            self.gerenciarusuarios = InterfaceGerenciarUsuarios(self, frame_resp=frame_resposta)

    def exibir_novocliente(self, frame_resposta):
        self.interface_NovoUsuario = InterfaceNovoCliente(self, frame_resp=frame_resposta)

    def exibir_novousuario(self, frame_resposta):
        self.interface_NovoUsuario = InterfaceNovoUsuario(self, frame_resp=frame_resposta)

    def exibir_usuario(self, frame_resposta, bt_perfil):
        self.Interface_Usuario = InterfaceUsuario(self, frame_resposta, bt_perfil)

    def exibir_estoque(self):
        self.clear_screen()
        self.interface_estoque = InterfaceEstoque(self.root)
   
    def msgbox(self, title, text, style):
        #  Styles:
        #  0 : OK
        #  1 : OK | Cancel
        #  2 : Abort | Retry | Ignore
        #  3 : Yes | No | Cancel 6, 7, 2
        #  4 : Yes | No
        #  5 : Retry | Cancel
        #  6 : Cancel | Try Again | Continue
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def aparencia(self, new_appearance_mode: str):
        # função que altera o modo de aparencia da janela entre ligth e dark
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        try:
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            ctk.set_widget_scaling(new_scaling_float)
        except:
            pass

    def desativar_modulos(self):
        estoque = 0
        cadastro = 0
        carteira = 0
        financas = 0

        resultado = self.ModulosDoUsuario
        for tupla in resultado:

            if tupla[2] == 'Agenda' and tupla[3] == 'AGENDA':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    self.BtAgenda.configure(state="disabled")



            elif tupla[2] == 'Usuario' and tupla[3] == 'USUARIO':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    self.BtUsuario.configure(state="disabled")


            elif tupla[2] == 'Configurações' and tupla[3] == 'CONFIGURACOES':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    self.BtConfiguracoes.configure(state="disabled")




            elif tupla[2] == 'Estoque' and tupla[3] == 'ENTRADA':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    estoque += 1

            elif tupla[2] == 'Estoque' and tupla[3] == 'SAIDA':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    estoque += 1

            elif tupla[2] == 'Estoque' and tupla[3] == 'INVENTARIO':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    estoque += 1




            elif tupla[2] == 'Cadastro' and tupla[3] == 'CAD ITEM':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    cadastro += 1

            elif tupla[2] == 'Cadastro' and tupla[3] == 'CAD CLIENTE':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    cadastro += 1

            elif tupla[2] == 'Cadastro' and tupla[3] == 'CAD USUARIO':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    cadastro += 1

            elif tupla[2] == 'Cadastro' and tupla[3] == 'GERENCIAR USER':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    cadastro += 1





            elif tupla[2] == 'Carteira' and tupla[3] == 'VENDAS':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    carteira += 1


            elif tupla[2] == 'Carteira' and tupla[3] == 'FATURAMENTO':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    carteira += 1




            elif tupla[2] == 'Finanças' and tupla[3] == 'DESPESAS':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    financas += 1


            elif tupla[2] == 'Finanças' and tupla[3] == 'OUTRAS RENDAS':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    financas += 1

        if estoque == 3:
            self.BtEstoque.configure(state='disabled')

        if cadastro == 4:
            self.BtCadastros.configure(state='disabled')

        if carteira == 2:
            self.Btcarteira.configure(state='disabled')

        if financas == 2:
            self.BtFinancas.configure(state='disabled')

    def desativar_submodulos(self, modulo):
        resultado = self.ModulosDoUsuario
        try:
            if modulo == 'Estoque':
                for tupla in resultado:

                    if tupla[2] == 'Estoque' and tupla[3] == 'ENTRADA':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTEntrada.configure(state="disabled")

                    elif tupla[2] == 'Estoque' and tupla[3] == 'SAIDA':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTSaida.configure(state="disabled")

                    elif tupla[2] == 'Estoque' and tupla[3] == 'INVENTARIO':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTInventario.configure(state="disabled")

            elif modulo == 'Cadastro':
                for tupla in resultado:
                    if tupla[2] == 'Cadastro' and tupla[3] == 'CAD ITEM':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTCadastrarItens.configure(state="disabled")


                    elif tupla[2] == 'Cadastro' and tupla[3] == 'CAD CLIENTE':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTCadastrarClientes.configure(state="disabled")


                    elif tupla[2] == 'Cadastro' and tupla[3] == 'CAD USUARIO':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTCriarNovoUsuario.configure(state="disabled")


                    elif tupla[2] == 'Cadastro' and tupla[3] == 'GERENCIAR USER':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTGerenciarUsuario.configure(state="disabled")

            elif modulo == 'Carteira':
                for tupla in resultado:

                    if tupla[2] == 'Carteira' and tupla[3] == 'VENDAS':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTRegistrarVenda.configure(state="disabled")


                    elif tupla[2] == 'Carteira' and tupla[3] == 'FATURAMENTO':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTFaturamento.configure(state="disabled")

            elif modulo == 'Finanças':
                for tupla in resultado:

                    if tupla[2] == 'Finanças' and tupla[3] == 'DESPESAS':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTRegistrarDespesas.configure(state="disabled")


                    elif tupla[2] == 'Finanças' and tupla[3] == 'OUTRAS RENDAS':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTOutrasRendas.configure(state="disabled")

        except Exception as erro:
            print(erro)

    def destacar(self, lista = list, botão = object, cor = tuple, fg2 = "transparent"):
        
        for valor in lista:
            if valor == botão:      
                if cor == "white":
                    botão.configure(fg_color=cor)
                else:
                    botão.configure(fg_color=cor)
            else:
                valor.configure(fg_color=fg2)

    def sair(self):
        resp = self.msgbox("SAIR", "Deseja realmente encerrar o sistema?", 4)
        if resp == 6:
            self.ConexaoPrincipal.close()
            self.root.destroy()

    def validate_numeric_input(self,P, max_length):
        # Verifica se P é vazio ou um número decimal válido
        return P == "" or P.replace(".", "", 1).isdigit() and len(P) <= int(max_length)

    def validate_text_input(self, P, max_length):
            return P == "" or (isinstance(P, str) and P.isalpha() and len(P) <= int(max_length))



if __name__ == "__main__":
    root = ctk.CTk()

    app = MainApp(root)

    root.mainloop()