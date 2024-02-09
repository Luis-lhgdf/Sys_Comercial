from tkinter import filedialog
import sqlite3
from PIL import ImageDraw
import base64
import pkg_resources
import binascii
import io
import ctypes
from Icones import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
import json


# Carregar configuracões do arquivo JSON
def load_config(value: bool, localfile=False):
    local = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/config.json")
    try:
        with open(local, "r") as config_file:
            config = json.load(config_file)
            if value:
                return config
            else:
                if localfile:
                    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/personalizado.json")
                else:
                    return str(config["theme"]["default_theme"][0])

    except FileNotFoundError:
        return {
            "theme": {
                "default_theme": ["blue"]
            }
        }


# Salvar configuracões no arquivo JSON
def save_config(config):
    local = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/config.json")
    with open(local, "w") as config_file:
        json.dump(config, config_file, indent=4)


# Funcão para alterar e salvar o tema
def change_and_save_theme(new_theme):
    config = load_config(True)
    config["theme"]["default_theme"][0] = new_theme
    save_config(config)


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

        self.LabelPesquisar = ctk.CTkLabel(self.frame_resp, text="Busca rapida", fg_color="transparent",
                                           font=self.main_app.SubTitle)
        self.LabelPesquisar.place(relx=0.36, rely=0.13, anchor="w")

        self.TotalPerfil = ctk.CTkLabel(self.frame_resp, text=f"Total de Perfils\n{len(self.usuarios)}", height=50,
                                        width=200,
                                        fg_color="white", text_color="black", font=self.main_app.SubTitle,
                                        corner_radius=6)
        self.TotalPerfil.place(relx=0.05, rely=0.3, anchor="w")

        self.TotalAdm = ctk.CTkLabel(self.frame_resp, text=f"Total de Administradores\n{self.totalizador('adm')}",
                                     height=50, fg_color="white", width=200,
                                     text_color="black", font=self.main_app.SubTitle, corner_radius=6)
        self.TotalAdm.place(relx=0.35, rely=0.3, anchor="w")

        self.TotalUser = ctk.CTkLabel(self.frame_resp, text=f"Total de Usuarios\n{self.totalizador('usuarios')}",
                                      height=50, width=200,
                                      fg_color="white", text_color="black", font=self.main_app.SubTitle,
                                      corner_radius=6)
        self.TotalUser.place(relx=0.65, rely=0.3, anchor="w")

        self.cabecalho = ctk.CTkLabel(self.frame_resp, text="     Usuario             Acesso             Status",
                                      width=self.main_app.screen_wedth - 270, corner_radius=5,
                                      fg_color=("white", "gray10"), text_color=("black", "white"), anchor="w",
                                      font=self.main_app.SubTitle)
        self.cabecalho.place(relx=0.01, rely=0.443, anchor="w")

        self.Bt_Todos = ctk.CTkButton(self.frame_resp, text="TODOS", image=EntradaIcon, text_color=("black", "white"),
                                      width=80, )
        self.Bt_Todos.place(relx=0.7, rely=0.18, anchor="w")

        self.Bt_Pesquisar = ctk.CTkButton(self.frame_resp, image=VisualizarIcon, text_color=("black", "white"),
                                          text="PESQUISAR",
                                          width=80, command=self.busca_rapida)
        self.Bt_Pesquisar.place(relx=0.612, rely=0.18, anchor="w")

        self.Pesquisar = ctk.CTkEntry(self.frame_resp, placeholder_text="Digite o nome do usuario aqui:", width=550,
                                      height=40)
        self.Pesquisar.place(relx=0.2, rely=0.18, anchor="w")

        self.scrol = ctk.CTkScrollableFrame(self.frame_resp, width=self.main_app.screen_wedth - 270, height=50)
        self.scrol.place(relx=0.01, rely=0.6, anchor="w")

        # adicionado nas listas os botoes com cada usuario cadastrado no banco de dados
        for id_usuario in range(len(self.usuarios)):
            self.usuario_label.append(
                ctk.CTkLabel(self.scrol, text=self.usuarios[id_usuario], fg_color="white", anchor="w", width=100,
                             corner_radius=6, text_color="black"))
            self.usuario_label[id_usuario].grid(padx=2, pady=5, row=id_usuario, column=0)

            self.acesso_label.append(
                ctk.CTkLabel(self.scrol, text=self.acesso[id_usuario], fg_color="white", anchor="w", width=100,
                             corner_radius=6,
                             text_color="black"))
            self.acesso_label[id_usuario].grid(padx=2, pady=5, row=id_usuario, column=1)

            self.status_label.append(
                ctk.CTkLabel(self.scrol, text=self.status[id_usuario], fg_color="white", anchor="w", width=100,
                             corner_radius=6,
                             text_color="black"))
            self.status_label[id_usuario].grid(padx=2, pady=5, row=id_usuario, column=2)

            self.editar_button.append(
                ctk.CTkButton(self.scrol, text="Editar", text_color=("black", "white"), image=EditarIcon, width=60,
                              fg_color="transparent", command=lambda i=id_usuario: self.editar_usuario(i)))
            self.editar_button[id_usuario].grid(padx=60, pady=5, row=id_usuario, column=3)

    def buscar_usuarios(self):

        self.cursor.execute("SELECT usuario, acesso, status FROM Usuarios")
        resultado = self.cursor.fetchall()

        for user in resultado:
            self.usuarios.append(user[0])
            self.acesso.append(user[1])
            self.status.append(user[2])

    def totalizador(self, total: str):
        resposta = total.upper()
        total_de_adm = 0
        total_de_usuarios = 0

        for acesso in self.acesso:
            if acesso == 'ADM':
                total_de_adm += 1
            else:
                total_de_usuarios += 1
        if resposta == "ADM":
            return total_de_adm
        elif resposta == "USUARIOS":
            return total_de_usuarios
        else:
            return None

    def busca_rapida(self):
        self.main_app.msgbox("Pesquisa", "Usuario nao encontrado", 0)

    def modulos_usuario(self, indice, usuario_entry, status_menu, acesso_menu):

        self.cursor.execute(f"select * from Modulos where usuario = '{usuario_entry.get()}'")

        self.indice_usuario = indice
        self.ModulosDoUsuario = self.cursor.fetchall()

        usuario_entry.grid_remove()
        acesso_menu.grid_remove()
        status_menu.grid_remove()

        self.salvar_button[indice].grid_remove()
        self.cancelar_button[indice].grid_remove()
        self.excluir_button[indice].grid_remove()
        self.Editar_Modulos[indice].grid_remove()

        outros_usuarios = len(self.usuario_label) - 1
        for c in range(0, outros_usuarios + 1):
            self.usuario_label[c].grid_remove()
            self.acesso_label[c].grid_remove()
            self.status_label[c].grid_remove()
            self.editar_button[c].grid_remove()

        self.cabecalho.configure(
            text='Usuario             Modulo             Submodulo             visualizar             Novo            '
                 ' Editar             Remover')

        self.usuario_label_modulo = []

        modulo_label_modulo = []
        submodulo_label_modulo = []
        visualizar_menu_modulo = []
        novo_menu_modulo = []
        editar_menu_modulo = []
        remover_menu_modulo = []

        for i, linha in enumerate(self.ModulosDoUsuario):
            self.usuario_label_modulo.append(
                ctk.CTkLabel(self.scrol, text=linha[1], fg_color="white", anchor="w", width=100, corner_radius=6,
                             text_color="black"))
            self.usuario_label_modulo[i].grid(padx=2, pady=5, row=i, column=0)

            modulo_label_modulo.append(
                ctk.CTkLabel(self.scrol, text=linha[2], fg_color="white", anchor="w", width=100, corner_radius=6,
                             text_color="black"))
            modulo_label_modulo[i].grid(padx=2, pady=5, row=i, column=1)

            submodulo_label_modulo.append(
                ctk.CTkLabel(self.scrol, text=linha[3].capitalize(), fg_color="white", anchor="w", width=100,
                             corner_radius=6, text_color="black"))
            submodulo_label_modulo[i].grid(padx=2, pady=5, row=i, column=2)

            visualizar_menu_modulo.append(ctk.CTkOptionMenu(self.scrol, values=(
                ["liberado", "bloqueado"] if linha[4] == 'liberado' else ["bloqueado", "liberado"]), width=100,
                                                            height=26))
            visualizar_menu_modulo[i].grid(padx=2, pady=5, row=i, column=3)

            novo_menu_modulo.append(ctk.CTkOptionMenu(self.scrol, values=(
                ["liberado", "bloqueado"] if linha[4] == 'liberado' else ["bloqueado", "liberado"]), width=100,
                                                      height=26))
            novo_menu_modulo[i].grid(padx=2, pady=5, row=i, column=4)

            editar_menu_modulo.append(ctk.CTkOptionMenu(self.scrol, values=(
                ["liberado", "bloqueado"] if linha[4] == 'liberado' else ["bloqueado", "liberado"]), width=100,
                                                        height=26))
            editar_menu_modulo[i].grid(padx=2, pady=5, row=i, column=5)

            remover_menu_modulo.append(ctk.CTkOptionMenu(self.scrol, values=(
                ["liberado", "bloqueado"] if linha[4] == 'liberado' else ["bloqueado", "liberado"]), width=100,
                                                         height=26))
            remover_menu_modulo[i].grid(padx=2, pady=5, row=i, column=6)

        def salvar():
            resp = self.main_app.msgbox("Salvar", "Deseja salvar as alteracões feita?", 4)
            if resp == 6:
                for pos, modulo in enumerate(self.ModulosDoUsuario):
                    visualizar = visualizar_menu_modulo[pos].get()
                    novo = novo_menu_modulo[pos].get()
                    editar = editar_menu_modulo[pos].get()
                    remover = remover_menu_modulo[pos].get()

                    self.cursor.execute(f'''UPDATE Modulos SET 
                                    visualizar = "{visualizar}", 
                                    novo = "{novo}", 
                                    editar = "{editar}", 
                                    remover = "{remover}" 
                                    WHERE usuario = "{self.usuarios[indice]}" AND submodulo = "{modulo[3]}"''')
                    self.main_app.ConexaoPrincipal.commit()

                self.main_app.msgbox("Salvar", "Alteracões salvas com Sucesso", 0)

        def cancelar():
            self.cursor.execute(f"SELECT acesso FROM Usuarios  where  usuario = '{self.main_app.usuario_logado}' ")
            self.acesso_usuario = str(self.cursor.fetchall()[0][0])

            bt_salvar_modulo.destroy()

            bt_cancelar_modulo.destroy()
            self.reiniciar_listas()
            self.buscar_usuarios()
            self.interface()

        bt_salvar_modulo = ctk.CTkButton(self.frame_resp, text="Salvar", image=SalvarIcon,
                                         text_color=("black", "white"),
                                         width=100, command=lambda: salvar())

        bt_salvar_modulo.place(relx=0.4, rely=0.8, anchor="w")

        bt_cancelar_modulo = ctk.CTkButton(self.frame_resp, text="Voltar", image=VoltarIcon,
                                           text_color=("black", "white"), width=100,
                                           anchor="w", command=lambda: cancelar())

        bt_cancelar_modulo.place(relx=0.3, rely=0.8, anchor="w")

        self.Pesquisar.configure(state="disabled")
        self.Bt_Todos.configure(state="disabled")
        self.Bt_Pesquisar.configure(state="disabled")

    def salvar_usuario(self, i, usuario_entry, status_menu, acesso_menu):
        self.editar_button[i].configure(state="normal")
        # Salva as alteracões nas listas 

        novo_user = usuario_entry.get()
        novo_acesso = acesso_menu.get()
        novo_status = status_menu.get()

        if novo_user != self.usuarios[i]:
            self.cursor.execute(f"SELECT usuario FROM Usuarios where usuario = '{usuario_entry.get()}'")
            resp = self.cursor.fetchall()
            if not resp:
                self.cursor.execute(
                    f"UPDATE Usuarios SET usuario = '{usuario_entry.get()}' where usuario = '{self.usuarios[i]}'")
                self.main_app.usuario_logado = usuario_entry.get()
                self.usuarios[i] = usuario_entry.get()
                self.main_app.ConexaoPrincipal.commit()
            else:
                self.main_app.msgbox("USUARIO", "Ja existe um usuario com este nome!!!", 0)

        if novo_acesso != self.acesso[i]:
            self.cursor.execute(
                f"UPDATE Usuarios SET acesso = '{acesso_menu.get()}' where usuario = '{self.usuarios[i]}'")
            self.acesso[i] = acesso_menu.get()
            self.main_app.ConexaoPrincipal.commit()

        if novo_status != self.status[i]:
            self.cursor.execute(
                f"UPDATE Usuarios SET status = '{status_menu.get()}' where usuario = '{self.usuarios[i]}'")
            self.status[i] = status_menu.get()
            self.main_app.ConexaoPrincipal.commit()

            # Atualiza os rótulos com as novas informacões

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
            # Salva as alteracões nas listas

            self.cursor.execute(f"delete from Usuarios where usuario ='{self.usuarios[i]}' ")

            self.cursor.execute(f"delete from Modulos where usuario ='{self.usuarios[i]}' ")

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

            InterfaceGerenciarUsuarios(main_app=self.main_app, frame_resp=self.frame_resp)

    def cancelar_usuario(self, i, usuario_entry, status_menu, acesso_menu):
        self.editar_button[i].configure(state="normal")

        # Descarta as alteracões e esconde os campos de entrada
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
        # Cria os campos de entrada com as informacões atuais do usuário
        self.editar_button[i].configure(state="disabled")

        usuario_entry = ctk.CTkEntry(self.scrol, width=100)
        usuario_entry.insert(0, self.usuarios[i])
        usuario_entry.grid(padx=2, pady=5, row=i, column=0)

        menu1 = ("USUARIO", "ADM")
        menu2 = ("ADM", "USUARIO")

        status1 = ("ATIVO", "DESATIVADO")
        status2 = ("DESATIVADO", "ATIVO")

        valores_acesso_menu = menu1 if self.acesso[i] == "USUARIO" else menu2
        acesso_menu = ctk.CTkOptionMenu(self.scrol, values=list(valores_acesso_menu), width=100, height=26)
        acesso_menu.grid(padx=2, pady=5, row=i, column=1)

        valores_status_menu = status1 if self.status[i] == "ATIVO" else status2
        status_menu = ctk.CTkOptionMenu(self.scrol, values=list(valores_status_menu), width=100, height=26)
        status_menu.grid(padx=2, pady=5, row=i, column=2)

        # Cria os botões Salvar e Cancelar
        self.salvar_button[i] = ctk.CTkButton(self.scrol, text="Salvar", text_color=("black", "white"),
                                              image=SalvarIcon, width=60, fg_color="transparent",
                                              command=lambda: self.salvar_usuario(i, usuario_entry, status_menu,
                                                                                  acesso_menu))
        self.salvar_button[i].grid(row=i, column=4)

        self.cancelar_button[i] = ctk.CTkButton(self.scrol, text="Cancelar", text_color=("black", "white"),
                                                image=VoltarIcon, width=60, fg_color="transparent",
                                                command=lambda: self.cancelar_usuario(i, usuario_entry, status_menu,
                                                                                      acesso_menu))
        self.cancelar_button[i].grid(padx=5, row=i, column=5)

        self.Editar_Modulos[i] = ctk.CTkButton(self.scrol, text="Modulos", text_color=("black", "white"),
                                               image=EditarIcon, width=60, fg_color="transparent",
                                               command=lambda: self.modulos_usuario(i, usuario_entry, status_menu,
                                                                                    acesso_menu))
        self.Editar_Modulos[i].grid(padx=5, row=i, column=6)

        self.excluir_button[i] = ctk.CTkButton(self.scrol, text="Deletar", text_color=("black", "white"),
                                               image=DeletarIcon, width=60, fg_color="transparent",
                                               command=lambda: self.excluir_usuario(i, usuario_entry, status_menu,
                                                                                    acesso_menu))
        self.excluir_button[i].grid(padx=5, row=i, column=7)

        # Esconde os rótulos e o botao Editar
        self.usuario_label[i].grid_remove()
        self.status_label[i].grid_remove()
        self.acesso_label[i].grid_remove()


class ModeloCadastro:
    def __init__(self, main_app, frame_resp, tabela_bd: str, titulo_janela: str, placeholder_text_pesquisar: str,
                 colunas_consulta: list,
                 func_interface, func_editar, func_create_update):

        self.main_app = main_app
        self.frame_resp = frame_resp
        self.tabela_bd = tabela_bd
        self.titulo_janela = titulo_janela
        self.colunas_consulta = colunas_consulta
        self.placeholder_text_pesquisar = placeholder_text_pesquisar
        self.func_interface = func_interface
        self.func_editar = func_editar
        self.func_create_update = func_create_update

        self.cursor = self.main_app.ConexaoPrincipal.cursor()
        self.limite_view = 10

        self.column_names = None
        self.lista_valores = None
        self.total_valores = 0

        self.valor_unico_selecionado = None
        self.valor_lista_selecionado = None

        self.LabelTitulo = ctk.CTkLabel(self.frame_resp, text=f"{str(titulo_janela).upper()}", fg_color="transparent",
                                        text_color=("black", "white"), font=(ctk.CTkFont(size=14, weight="bold")),
                                        corner_radius=6)
        self.LabelTitulo.place(x=1, y=1)

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
        frame_treeview = tk.Frame(self.frame_resp)
        frame_treeview.place(x=25, y=400, width=self.main_app.screen_wedth, height=305)

        self.tree = ttk.Treeview(frame_treeview, show="headings")
        self.tree.place(x=0, y=0, height=305)
        self.tree.bind("<<TreeviewSelect>>", self.click_select)

        self.scroll_x = ttk.Scrollbar(frame_treeview, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.scroll_y = ttk.Scrollbar(frame_treeview, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.LabelPesquisar = ctk.CTkLabel(self.frame_resp, text="Busca rapida", fg_color="transparent",
                                           font=(ctk.CTkFont(size=14, weight="bold")))
        self.LabelPesquisar.place(relx=0.36, rely=0.13, anchor="w")

        self.Label_Select = ctk.CTkLabel(self.frame_resp, text=f"SELECIONADO: ", height=37, width=250, fg_color="white",
                                         text_color="black",
                                         font=(ctk.CTkFont(size=12, weight="bold")), corner_radius=6, anchor="w")
        self.Label_Select.place(x=50, y=250)

        self.Label_LimiteView = ctk.CTkLabel(self.frame_resp, height=37,
                                             text=f"01 A {self.limite_view} DE {self.total_valores}",
                                             font=(ctk.CTkFont(size=12, weight="bold")), anchor="w")
        self.Label_LimiteView.place(x=820, y=255)

        self.Entry_Pesquisar = ctk.CTkEntry(self.frame_resp, placeholder_text=f"{self.placeholder_text_pesquisar}",
                                            width=550, height=40)
        self.Entry_Pesquisar.place(relx=0.2, rely=0.18, anchor="w")

        self.Bt_Todos = ctk.CTkButton(self.frame_resp, text="TODOS", image=EntradaIcon, text_color=("black", "white"),
                                      width=80, command=self.todos)
        self.Bt_Todos.place(relx=0.7, rely=0.18, anchor="w")

        self.Bt_Pesquisar = ctk.CTkButton(self.frame_resp, image=VisualizarIcon, text_color=("black", "white"),
                                          text="PESQUISAR",
                                          width=80,
                                          command=lambda: self.pesquisar(self.colunas_consulta, self.tabela_bd))
        self.Bt_Pesquisar.place(relx=0.612, rely=0.18, anchor="w")

        self.Bt_Editar = ctk.CTkButton(self.frame_resp, text="Editar", text_color=("black", "white"), image=EditarIcon,
                                       width=40, fg_color="transparent", state="disabled", command=self.func_editar)
        self.Bt_Editar.place(x=320, y=250)

        self.Bt_Excluir = ctk.CTkButton(self.frame_resp, text="Excluir", text_color=("black", "white"),
                                        image=DeletarIcon,
                                        width=40, fg_color="transparent", state="disabled", command=self.excluir)
        self.Bt_Excluir.place(x=420, y=250)

        self.Bt_Excel = ctk.CTkButton(self.frame_resp, text="Excel", text_color=("black", "white"), image=ExcelIcon,
                                      width=40, fg_color="transparent", command=self.excel)
        self.Bt_Excel.place(x=1020, y=250)

        self.Bt_Novo = ctk.CTkButton(self.frame_resp, text="NOVO", image=AdicionarIcon, text_color=("black", "white"),
                                     width=100, command=self.func_create_update)
        self.Bt_Novo.place(relx=0.36, rely=0.85, anchor="w")

        self.Bt_Sincronizar = ctk.CTkButton(self.frame_resp, text="", image=sincronizar, text_color=("black", "white"),
                                            fg_color='transparent',
                                            command=self.sincronizar_tabela)
        self.Bt_Sincronizar.place(x=575, y=250)

        self.Menu_LimiteView = ctk.CTkOptionMenu(self.frame_resp, height=37, width=80,
                                                 font=(ctk.CTkFont(size=11, weight="bold")),
                                                 values=['10', '100', '1000', '10000'],
                                                 command=self.atualizar_limiteview)
        self.Menu_LimiteView.place(x=920, y=250)

        style = ttk.Style()
        style.configure('Treeview.Heading', background="white")
        style.configure("Treeview.Heading", font=('Roboto', 11, "bold"))
        style.configure('Treeview', font=('Roboto', 11))
        style.map("Treeview", background=[('selected', 'gray90')], foreground=[('selected', 'black')])

    def sincronizar_tabela(self, attlimite=True):
        self.Bt_Sincronizar.destroy()


        self.cursor.execute(f"SELECT * FROM {self.tabela_bd} limit 10")

        self.lista_valores = self.cursor.fetchall()

        self.column_names = [description[0] for description in self.cursor.description]

        self.cursor.execute(f"SELECT COUNT(*) AS total_linhas FROM {self.tabela_bd} ")

        self.total_valores = int((self.cursor.fetchone()[0]))

        self.tree.configure(columns=([f'coluna{c}' for c in range(1, len(self.column_names) + 1)]))

        if attlimite:
            self.atualizar_limiteview(10)

    def atualizar_limiteview(self, novo_limite):
        try:
            self.tree.delete(*self.tree.get_children())  # exclui todos os itens de uma treeview
        except tk.TclError:
            pass
        self.cursor.execute(f"SELECT * FROM {self.tabela_bd} limit {int(novo_limite)}")
        self.lista_valores = self.cursor.fetchall()

        self.Label_LimiteView.configure(
            text=f"""01 A {novo_limite if int(novo_limite) < self.total_valores
            else self.total_valores} "f"DE {self.total_valores}""")

        self.limite_view = int(novo_limite)

        self.reexibir_treeview(self.lista_valores)

    def reexibir_treeview(self, lista):
        try:
            self.tree.column("coluna1", width=50)
            self.tree.column("coluna10", width=50)
            self.tree.column("coluna14", width=50)
        except tk.TclError:
            pass

        for valor in lista:
            self.tree.insert("", "end", values=valor)
            # self.tree.tag_configure("center", anchor="center")

        for i, coluna in enumerate(self.tree['columns']):
            nome = str(self.column_names[i]).capitalize()

            self.tree.heading(coluna, text=f"{nome}")

            self.tree.column(coluna, stretch=False)

    def click_select(self, event):
        selected_item = self.tree.selection()
        lista = []
        if selected_item:
            if len(selected_item) == 1:
                unico = self.tree.item(selected_item, "values")
                self.valor_unico_selecionado = unico
                self.Label_Select.configure(text=f"SELECIONADO: {unico[6][0:20]}")
                self.Bt_Editar.configure(state="normal")
                self.Bt_Excluir.configure(state="normal")

            else:
                self.Bt_Editar.configure(state="disabled")
                self.Bt_Excluir.configure(state="normal")

                for item_id in selected_item:
                    valor = self.tree.item(item_id, "values")
                    lista.append(valor)

                    self.Label_Select.configure(text=f"SELECIONADO: {len(selected_item)}")

                self.valor_lista_selecionado = lista

    def todos(self):
        info_digitada = str(self.Entry_Pesquisar.get())
        if info_digitada:
            try:
                self.tree.delete(*self.tree.get_children())
            except tk.TclError:
                pass
            self.reexibir_treeview(self.lista_valores)

    def pesquisar(self, colunas_consulta, tabela_name):

        #TODO corrigir futuramente para o modulo de pqsquisar os clientes

        info_digitada = self.Entry_Pesquisar.get()
        if info_digitada:
            print(f"Tentou pesquisar por {info_digitada} nas colunas {colunas_consulta}")

            # Construir a consulta SQL de forma segura usando placeholders '?' para os parâmetros
            query = f"SELECT {', '.join(colunas_consulta)} FROM {tabela_name} WHERE {' OR '.join([f'{col} LIKE ?' for col in colunas_consulta])}"

            # Criar os parâmetros para substituir os placeholders na consulta
            parametros = ['%' + info_digitada + '%' for _ in colunas_consulta]

            try:
                # Executar a consulta SQL
                self.cursor.execute(query, parametros)
                lista = self.cursor.fetchall()
                # Atualizar a visualização
                self.tree.delete(*self.tree.get_children())
                self.reexibir_treeview(lista=lista)
            except sqlite3.Error as e:
                # Lidar com erros de SQLite
                print("Erro ao executar a consulta SQL:", e)

    def voltar(self, opcao):

        self.acao_widget(acao=opcao)
        self.interface_tabela()
        self.LabelTitulo.configure(text=f'{self.titulo_janela}')

    def excel(self):
        resp = self.main_app.msgbox("Excel", "Deseja exportar todos os registros?", 4)

        def destino(dataframe):
            folder_path = filedialog.asksaveasfilename(defaultextension='.xlsx')

            if folder_path:
                # Definir o nome do arquivo
                file_path = folder_path

                # Verificar se a extensão .xlsx foi adicionada
                if not file_path.endswith('.xlsx'):
                    file_path += '.xlsx'

                dataframe.to_excel(file_path, index=False)
                self.main_app.msgbox("Excel", "Arquivo salvo com sucesso", 0)

        if resp == 6:
            print("esta vazio, puxando valores no banco de dados")
            if self.lista_valores is None:
                self.cursor.execute("SELECT * FROM Clientes")
                self.lista_valores = self.cursor.fetchall()
                self.column_names = self.column_names = [description[0] for description in self.cursor.description]
                df = pd.DataFrame(self.lista_valores, columns=self.column_names)
                destino(dataframe=df)

            else:
                print("NAO ESTA VAZIA")
                df = pd.DataFrame(self.lista_valores, columns=self.column_names)
                destino(dataframe=df)

    def excluir(self):
        resp = self.main_app.msgbox("EXCLUIR", "Tem certeza que deseja excluir este cliente?", 4)
        if resp == 6:
            lista = self.lista_valores
            for valor in lista:
                id_valor = int(valor[0])

                query = f"DELETE FROM {self.tabela_bd} WHERE id = {id_valor}"
                self.cursor.execute(query)
                self.main_app.ConexaoPrincipal.commit()
            self.main_app.msgbox("EXCLUIR", "Valor excluído com sucesso!", 0)
            self.sincronizar_tabela(attlimite=False)
            self.atualizar_limiteview(self.limite_view)


class InterfaceNovoItem(ModeloCadastro):

    def __init__(self, main_app, frame_resp):
        self.main_app = main_app
        self.frame_resp = frame_resp
        self.cursor = self.main_app.ConexaoPrincipal.cursor()
        self.placehold = 'Pesquise por Id, Descrição, Marca, Categoria ou Fornecedor'
        self.colunas_bd = ['Id', 'descricao_produto', 'marca', 'categoria', 'fornecedor']

        super().__init__(main_app=self.main_app, frame_resp=self.frame_resp, tabela_bd="Produtos",
                         titulo_janela="ITENS", placeholder_text_pesquisar=self.placehold,
                         colunas_consulta=self.colunas_bd,
                         func_interface=self.interface_create, func_editar=self.editar_produto,
                         func_create_update=lambda: self.interface_create('CREATE'))

    def editar_produto(self):
        lista = self.valor_unico_selecionado

        self.interface_create('UPDATE')

        # pegue o valor de cada entry
        self.entry_descricao_produto.insert(0, f'{lista[1]}')
        self.entry_unidade_medida.insert(0, f'{lista[2]}')
        self.entry_valor_unitario.insert(0, f'{lista[3]}')
        self.entry_marca.insert(0, f'{lista[4]}')
        self.entry_categoria.insert(0, f'{lista[5]}')
        self.entry_peso.insert(0, f'{lista[6]}')
        self.entry_fornecedor.insert(0, f'{lista[7]}')
        self.entry_info_adicionais.insert("1.0", f"{lista[8]}")

    def interface_create(self, tipo: str):
        # Esconder os widgets em vez de destruí-los

        # descricao_produto, unidade_medida, valor_unitario, marca, categoria, Peso, fornecedor, info_adicionais

        self.acao_widget('ocultar')

        self.LabelTitulo.configure(text=('CADASTRAR ITEM' if tipo.upper() == "CREATE"
                                         else 'EDITAR ITEM' if tipo.upper() == "UPDATE" else ''))

        self.label_descricao_produto = ctk.CTkLabel(self.frame_resp, text='Descricão do Produto:',
                                                    font=(None, 12, "bold"))
        self.label_descricao_produto.place(x=50, y=50, anchor="w")
        self.entry_descricao_produto = ctk.CTkEntry(self.frame_resp, width=300)
        self.entry_descricao_produto.place(x=50, y=80, anchor="w")

        self.label_unidade_medida = ctk.CTkLabel(self.frame_resp, text='Unidade de Medida:', font=(None, 12, "bold"))
        self.label_unidade_medida.place(x=400, y=50, anchor="w")

        self.entry_unidade_medida = ctk.CTkEntry(self.frame_resp, width=150)
        self.entry_unidade_medida.place(x=400, y=80, anchor="w")

        self.label_valor_unitario = ctk.CTkLabel(self.frame_resp, text='Valor Unitário:', font=(None, 12, "bold"))
        self.label_valor_unitario.place(x=600, y=50, anchor="w")
        self.entry_valor_unitario = ctk.CTkEntry(self.frame_resp, width=100)
        self.entry_valor_unitario.place(x=600, y=80, anchor="w")

        self.label_marca = ctk.CTkLabel(self.frame_resp, text='Marca:', font=(None, 12, "bold"))
        self.label_marca.place(x=750, y=50, anchor="w")
        self.entry_marca = ctk.CTkEntry(self.frame_resp, width=150)
        self.entry_marca.place(x=750, y=80, anchor="w")

        self.label_categoria = ctk.CTkLabel(self.frame_resp, text='Categoria:', font=(None, 12, "bold"))
        self.label_categoria.place(x=50, y=120, anchor="w")
        self.entry_categoria = ctk.CTkEntry(self.frame_resp, width=200)
        self.entry_categoria.place(x=50, y=150, anchor="w")

        self.label_peso = ctk.CTkLabel(self.frame_resp, text='Peso:', font=(None, 12, "bold"))
        self.label_peso.place(x=300, y=120, anchor="w")
        self.entry_peso = ctk.CTkEntry(self.frame_resp, width=100)
        self.entry_peso.place(x=300, y=150, anchor="w")

        self.label_fornecedor = ctk.CTkLabel(self.frame_resp, text='Fornecedor:', font=(None, 12, "bold"))
        self.label_fornecedor.place(x=450, y=120, anchor="w")
        self.entry_fornecedor = ctk.CTkEntry(self.frame_resp, width=250, validate="key",
                                             validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_fornecedor.place(x=450, y=150, anchor="w")

        self.label_info_adicionais = ctk.CTkLabel(self.frame_resp, text='Informacões Adicionais:',
                                                  font=(None, 12, "bold"))
        self.label_info_adicionais.place(x=50, y=190, anchor="w")
        self.entry_info_adicionais = ctk.CTkTextbox(self.frame_resp, width=self.main_app.screen_wedth - 310,
                                                    height=100)
        self.entry_info_adicionais.place(x=50, y=220)

        self.Bt_Voltar = ctk.CTkButton(self.frame_resp, text="Voltar", image=VoltarIcon,
                                       text_color=("black", "white"),
                                       width=100, anchor="w", command=lambda: self.voltar('ocultar'))

        self.Bt_Voltar.place(relx=0.3, rely=0.85, anchor="w")

        self.Bt_Novo_Cliente = ctk.CTkButton(self.frame_resp, text="SALVAR", image=SalvarIcon,
                                             text_color=("black", "white"),
                                             width=100, command=lambda: self.salvar_produto(tipo))
        self.Bt_Novo_Cliente.place(relx=0.4, rely=0.85, anchor="w")

    def salvar_produto(self, tipo):
        resp = self.main_app.msgbox("SALVAR", "Deseja salvar todas as informacões passadas?", 4)
        if resp == 6:

            # descricao_produto, unidade_medida, valor_unitario, marca, categoria, Peso, fornecedor, info_adicionais"

            # pegue o valor de cada entry
            descricao_produto = self.entry_descricao_produto.get()
            unidade_medida = self.entry_unidade_medida.get()
            valor_unitario = self.entry_valor_unitario.get()

            valor_unitario = float(valor_unitario) if valor_unitario and valor_unitario.replace(".",
                                                                                                "").isdigit() else None
            marca = self.entry_marca.get()
            categoria = self.entry_categoria.get()
            peso = self.entry_peso.get()
            peso = float(peso) if peso and peso.replace(".", "", 1).isdigit() else None
            fornecedor = self.entry_fornecedor.get()
            info_adicionais = self.entry_info_adicionais.get("0.0", "end")

            query = ()
            values = ()

            # Verifica se os campos obrigatórios estão preenchidos

            if not descricao_produto or not unidade_medida or not valor_unitario:
                # edite a cor para vermelho das entry
                self.entry_descricao_produto.configure(border_color="red")
                self.entry_unidade_medida.configure(border_color="red")
                self.entry_valor_unitario.configure(border_color="red")

                self.main_app.msgbox("Campos obrigatórios não preenchidos",
                                     "Por favor, preencha todos os campos obrigatórios antes de salvar.", 0)

                return

            if tipo == 'CREATE':

                query = """INSERT INTO Produtos (descricao_produto, unidade_medida, valor_unitario, 
                        marca, categoria, peso, fornecedor, info_adicionais)
                        VALUES (?, ?, ?, ?,?, ?, ?, ?) """
                values = (
                    descricao_produto, unidade_medida, valor_unitario, marca, categoria, peso, fornecedor,
                    info_adicionais)

            elif tipo == 'UPDATE':

                lista = self.valor_unico_selecionado
                id_produto = lista[0]

                query = """UPDATE Produtos SET descricao_produto = ?, unidade_medida = ?, valor_unitario = ?, 
                marca = ?, categoria = ?, peso = ?, fornecedor = ?, info_adicionais = ? WHERE id = ?"""

                values = (
                    descricao_produto, unidade_medida, valor_unitario, marca, categoria, peso, fornecedor,
                    info_adicionais,
                    id_produto)

                self.cursor.execute(query, values)

                self.main_app.ConexaoPrincipal.commit()

                self.entry_descricao_produto.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_unidade_medida.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_valor_unitario.configure(border_color=("#979DA2", "#565B5E"))

            self.cursor.execute(query, values)
            # Commit the changes to the database
            self.main_app.ConexaoPrincipal.commit()

            if tipo == 'CREATE':
                self.main_app.msgbox("NOVO PRODUTO", "Novo Produto adicionado com sucesso!", 0)
            elif tipo == 'UPDATE':
                self.main_app.msgbox("ATUALIZAR", "Informacões do Produto atualizadas com sucesso!", 0)

            self.entry_descricao_produto.delete(0, ctk.END)
            self.entry_unidade_medida.delete(0, ctk.END)
            self.entry_valor_unitario.delete(0, ctk.END)
            self.entry_marca.delete(0, ctk.END)
            self.entry_categoria.delete(0, ctk.END)
            self.entry_peso.delete(0, ctk.END)
            self.entry_fornecedor.delete(0, ctk.END)
            self.entry_info_adicionais.delete("0.0", "end")


class InterfaceNovoCliente(ModeloCadastro):

    def __init__(self, main_app, frame_resp):
        self.main_app = main_app
        self.frame_resp = frame_resp
        self.cursor = self.main_app.ConexaoPrincipal.cursor()
        self.placehold = 'Pesquise por ID, CNPJ, CPF, nome ou razão social'
        self.colunas_bd = ['razao_social', 'cpf', 'cnpj', 'id', 'nome']

        super().__init__(main_app=self.main_app, frame_resp=self.frame_resp, tabela_bd="Clientes",
                         titulo_janela="CLIENTES", placeholder_text_pesquisar=self.placehold,
                         colunas_consulta=self.colunas_bd,
                         func_interface=self.interface_create, func_editar=self.editar_cliente,
                         func_create_update=lambda: self.interface_create('CREATE'))

        self.Bt_Novo = ctk.CTkButton(self.frame_resp, text="NOVO", image=AdicionarIcon, text_color=("black", "white"),
                                     width=100, command=lambda: self.interface_create('CREATE'))

    def editar_cliente(self):
        lista = self.valor_unico_selecionado
        tipo_cliente = str(lista[1])

        # ('id', 'tipo_de_cliente', 'cpf', 'cnpj', 'email',
        #  'razao_social', 'nome', 'cep', 'endereco', 'numero',
        #  'complemento', 'bairro', 'cidade', 'uf', 'fone',
        #  'celular', 'questionario', 'observacoes')

        # ('143', 'Pessoa Jurídica', 'None', '12.345.678/0001-99', 'empresa1@example.com',
        #  'Empresa XYZ Ltda.', 'Empresa XYZ', '54321-876', 'Avenida dos Negócios', '456',
        #  'None', 'Bairro Comercial', 'Rio de Janeiro', 'RJ', '(21) 2222-2222',
        #  '(21) 98888-8888', 'Respondeu parcialmente ao questionário.', 'Informacões adicionais importantes.')

        self.interface_create('UPDATE')

        self.menu_tipocliente.set(f'{str(lista[1]).upper()}')
        self.entry_nome.insert(0, f'{lista[6]}')

        if tipo_cliente == 'PESSOA FISICA':
            cpf = int(str(lista[2]).replace(".", "").replace("-", ""))
            self.entry_cpf_cnpj.insert(0, f'{cpf}')

        elif tipo_cliente == 'PESSOA JURIDICA':
            cnpj = int(str(lista[3]).replace(".", "").replace("-", "").replace("/", ""))

            self.entry_cpf_cnpj.insert(0, f'{cnpj}')
            self.entry_razao_social.insert(0, f'{str(lista[5])}')

        self.entry_email.insert(0, f'{str(lista[4])}')
        self.entry_cep.insert(0, f"{int(str(lista[7]).replace('-', ''))}")
        self.entry_endereco.insert(0, f"{str(lista[8])}")
        self.entry_numero.insert(0, f"{int(lista[9])}")
        self.entry_complemento.insert(0, f"{str(lista[10])}")
        self.entry_bairro.insert(0, f"{str(lista[11])}")
        self.entry_cidade.insert(0, f"{str(lista[12])}")
        self.entry_uf.insert(0, f"{str(lista[13])}")
        self.entry_fone.insert(0,
                               f"{int(str(lista[14]).replace('(', '').replace(')', '').replace(' ', '').replace('-', ''))}")

        self.entry_celular.insert(0,
                                  f"{int(str(lista[15]).replace('(', '').replace(')', '').replace(' ', '').replace('-', ''))}")

        self.menu_questionario.set(f'{str(lista[16])}')
        self.entry_observacoes.insert('1.0', f"{str(lista[17])}")

    def interface_create(self, tipo: str):
        # Esconder os widgets em vez de destruí-los
        self.acao_widget('ocultar')

        self.LabelTitulo.configure(text=('CADASTRAR CLIENTE' if tipo.upper() == "CREATE"
                                         else 'EDITAR CLIENTE' if tipo.upper() == "UPDATE" else ''))
        # Crie o widget para a opcão 'tipo_de_cliente'

        self.label_tipo_cliente = ctk.CTkLabel(self.frame_resp, text='Tipo de Cliente:', font=(None, 12, "bold"))
        self.label_tipo_cliente.place(x=50, y=50, anchor="w")

        self.menu_tipocliente = ctk.CTkOptionMenu(self.frame_resp, values=['PESSOA FISICA', 'PESSOA JURIDICA'],
                                                  command=self.definir_cliente)
        self.menu_tipocliente.place(x=50, y=80, anchor="w")

        self.label_cpf_cnpj = ctk.CTkLabel(self.frame_resp, text='CPF/CNPJ:*', font=(None, 12, "bold"))
        self.label_cpf_cnpj.place(x=250, y=50, anchor="w")

        self.entry_cpf_cnpj = ctk.CTkEntry(self.frame_resp, width=150)
        self.entry_cpf_cnpj.place(x=250, y=80, anchor="w")

        self.label_email = ctk.CTkLabel(self.frame_resp, text='Email:', font=(None, 12, "bold"))
        self.label_email.place(x=450, y=50, anchor="w")
        self.entry_email = ctk.CTkEntry(self.frame_resp, width=300)
        self.entry_email.place(x=450, y=80, anchor="w")

        self.label_razao_social = ctk.CTkLabel(self.frame_resp, text='Razão Social:', font=(None, 12, "bold"))
        self.label_razao_social.place(x=800, y=50, anchor="w")
        self.entry_razao_social = ctk.CTkEntry(self.frame_resp, width=300, validate="key",
                                               validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_razao_social.place(x=800, y=80, anchor="w")

        self.label_nome = ctk.CTkLabel(self.frame_resp, text='Nome:*', font=(None, 12, "bold"))
        self.label_nome.place(x=50, y=140, anchor="w")
        self.entry_nome = ctk.CTkEntry(self.frame_resp, width=300, validate="key",
                                       validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_nome.place(x=50, y=170, anchor="w")

        self.label_cep = ctk.CTkLabel(self.frame_resp, text='CEP:*', font=(None, 12, "bold"))
        self.label_cep.place(x=400, y=140, anchor="w")

        self.entry_cep = ctk.CTkEntry(self.frame_resp, validate="key",
                                      validatecommand=(self.main_app.validate_cmd_numeric, "%P", 8))
        self.entry_cep.place(x=400, y=170, anchor="w")

        self.label_endereco = ctk.CTkLabel(self.frame_resp, text='Endereco:*', font=(None, 12, "bold"))
        self.label_endereco.place(x=600, y=140, anchor="w")
        self.entry_endereco = ctk.CTkEntry(self.frame_resp, width=300, validate="key",
                                           validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_endereco.place(x=600, y=170, anchor="w")

        self.label_numero = ctk.CTkLabel(self.frame_resp, text='N°:*', font=(None, 12, "bold"))
        self.label_numero.place(x=950, y=140, anchor="w")
        self.entry_numero = ctk.CTkEntry(self.frame_resp, width=50, validate="key",
                                         validatecommand=(self.main_app.validate_cmd_numeric, "%P", 5))
        self.entry_numero.place(x=950, y=170, anchor="w")

        self.label_complemento = ctk.CTkLabel(self.frame_resp, text='Complemento:', font=(None, 12, "bold"))
        self.label_complemento.place(x=50, y=230, anchor="w")

        self.entry_complemento = ctk.CTkEntry(self.frame_resp, width=300, validate="key",
                                              validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_complemento.place(x=50, y=260, anchor="w")

        self.label_bairro = ctk.CTkLabel(self.frame_resp, text='Bairro:*', font=(None, 12, "bold"))
        self.label_bairro.place(x=400, y=230, anchor="w")
        self.entry_bairro = ctk.CTkEntry(self.frame_resp, validate="key",
                                         validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_bairro.place(x=400, y=260, anchor="w")

        self.label_cidade = ctk.CTkLabel(self.frame_resp, text='Cidade:*', font=(None, 12, "bold"))
        self.label_cidade.place(x=600, y=230, anchor="w")

        self.entry_cidade = ctk.CTkEntry(self.frame_resp, validate="key",
                                         validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_cidade.place(x=600, y=260, anchor="w")

        self.label_uf = ctk.CTkLabel(self.frame_resp, text='UF:*', font=(None, 12, "bold"))
        self.label_uf.place(x=800, y=230, anchor="w")
        self.entry_uf = ctk.CTkEntry(self.frame_resp, width=50, validate="key",
                                     validatecommand=(self.main_app.validade_cmd_text, "%P", 2, False))
        self.entry_uf.place(x=800, y=260, anchor="w")

        self.label_fone = ctk.CTkLabel(self.frame_resp, text='Telefone:', font=(None, 12, "bold"))
        self.label_fone.place(x=900, y=230, anchor="w")
        self.entry_fone = ctk.CTkEntry(self.frame_resp, placeholder_text="(xx) 0000-0000", validate="key",
                                       validatecommand=(self.main_app.validate_cmd_numeric, "%P", 10))
        self.entry_fone.place(x=900, y=260, anchor="w")

        self.label_celular = ctk.CTkLabel(self.frame_resp, text='Celular:', font=(None, 12, "bold"))
        self.label_celular.place(x=50, y=320, anchor="w")
        self.entry_celular = ctk.CTkEntry(self.frame_resp, placeholder_text="(xx)9 0000-0000", validate="key",
                                          validatecommand=(self.main_app.validate_cmd_numeric, "%P", 11))
        self.entry_celular.place(x=50, y=360, anchor="w")

        self.label_questionario = ctk.CTkLabel(self.frame_resp, text='Como conheceu a empresa:',
                                               font=(None, 12, "bold"))
        self.label_questionario.place(x=250, y=320, anchor="w")
        self.menu_questionario = ctk.CTkOptionMenu(self.frame_resp,
                                                   values=['', 'INSTAGRAM', 'FACEBOOK', 'SITE', 'TIKTOK', 'INDICAcÃO',
                                                           'OUTRO'])
        self.menu_questionario.place(x=250, y=360, anchor="w")

        self.label_observacoes = ctk.CTkLabel(self.frame_resp, text='Observacões:', font=(None, 12, "bold"))
        self.label_observacoes.place(x=50, y=420, anchor="w")
        self.entry_observacoes = ctk.CTkTextbox(self.frame_resp, width=self.main_app.screen_wedth - 310, height=100)
        self.entry_observacoes.place(x=50, y=450)

        self.Bt_Voltar = ctk.CTkButton(self.frame_resp, text="Voltar", image=VoltarIcon, text_color=("black", "white"),
                                       width=100, anchor="w", command=lambda: self.voltar('ocultar'))

        self.Bt_Voltar.place(relx=0.3, rely=0.85, anchor="w")

        self.Bt_Novo_Cliente = ctk.CTkButton(self.frame_resp, text="SALVAR", image=SalvarIcon,
                                             text_color=("black", "white"),
                                             width=100, command=lambda: self.salvar_cliente(tipo))
        self.Bt_Novo_Cliente.place(relx=0.4, rely=0.85, anchor="w")

        self.definir_cliente(resposta="PESSOA FISICA")

    def salvar_cliente(self, tipo):
        resp = self.main_app.msgbox("SALVAR", "Deseja salvar todas as informacões passadas?", 4)
        if resp == 6:

            "id, tipo_de_cliente, cpf, cnpj, email, razao_social, nome, cep, endereco, numero, complemento, bairro, cidade, uf, telefone, celular, questionario, observacoes"

            tipo_cliente = self.menu_tipocliente.get()
            entry_cpf_cnpj = self.entry_cpf_cnpj.get()
            entry_email = self.entry_email.get()
            entry_razao_social = self.entry_razao_social.get()
            entry_nome = self.entry_nome.get()
            entry_cep = self.entry_cep.get()
            entry_endereco = self.entry_endereco.get()
            entry_numero = self.entry_numero.get()
            entry_complemento = self.entry_complemento.get()
            entry_bairro = self.entry_bairro.get()
            entry_cidade = self.entry_cidade.get()
            entry_uf = self.entry_uf.get()
            entry_fone = self.entry_fone.get()
            entry_celular = self.entry_celular.get()
            menu_questionario = self.menu_questionario.get()
            entry_observacoes = self.entry_observacoes.get("0.0", "end")

            # Verifica se os campos obrigatórios estão preenchidos
            if not entry_nome or not entry_cep or not entry_endereco or not entry_numero or not entry_bairro or not entry_cidade or not entry_uf or not entry_cpf_cnpj:
                self.entry_nome.configure(border_color="red")
                self.entry_cep.configure(border_color="red")
                self.entry_endereco.configure(border_color="red")
                self.entry_numero.configure(border_color="red")
                self.entry_bairro.configure(border_color="red")
                self.entry_cidade.configure(border_color="red")
                self.entry_uf.configure(border_color="red")
                self.entry_cpf_cnpj.configure(border_color="red")

                self.main_app.msgbox("Campos obrigatórios não preenchidos",
                                     "Por favor, preencha todos os campos obrigatórios antes de salvar.", 0)
                return

            if tipo == 'CREATE' or tipo == 'UPDATE':
                cnpj = None
                cpf = None

                query = ()
                values = ()

                if tipo_cliente == 'PESSOA FISICA':
                    cpf = entry_cpf_cnpj
                    cnpj = None
                elif tipo_cliente == 'PESSOA JURIDICA':
                    cnpj = entry_cpf_cnpj
                    cpf = None

                if tipo == 'CREATE':
                    query = """INSERT INTO Clientes (tipo_de_cliente, cpf, cnpj, email, razao_social, nome, cep, endereco, numero, complemento, bairro, cidade, uf, telefone, celular, questionario, observacoes)
                            VALUES (?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?, ?) """
                    values = (
                        tipo_cliente, cpf, cnpj, entry_email, entry_razao_social, entry_nome, entry_cep, entry_endereco,
                        entry_numero, entry_complemento, entry_bairro, entry_cidade, entry_uf, entry_fone,
                        entry_celular,
                        menu_questionario, entry_observacoes)

                elif tipo == 'UPDATE':

                    lista = self.valor_unico_selecionado
                    id_cliente = lista[0]
                    # You need to implement this method to get the selected client's ID
                    query = """UPDATE Clientes SET tipo_de_cliente = ?, cpf = ?, cnpj = ?, email = ?, razao_social = ?, nome = ?, cep = ?, endereco = ?, numero = ?, complemento = ?, bairro = ?, cidade = ?, uf = ?, telefone = ?, celular = ?, questionario = ?, observacoes = ?
                            WHERE id = ?"""
                    values = (
                        tipo_cliente, cpf, cnpj, entry_email, entry_razao_social, entry_nome, entry_cep, entry_endereco,
                        entry_numero, entry_complemento, entry_bairro, entry_cidade, entry_uf, entry_fone,
                        entry_celular,
                        menu_questionario, entry_observacoes, id_cliente)

                self.cursor.execute(query, values)
                # Commit the changes to the database
                self.main_app.ConexaoPrincipal.commit()

                self.entry_nome.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_cep.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_endereco.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_numero.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_bairro.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_cidade.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_uf.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_cpf_cnpj.configure(border_color=("#979DA2", "#565B5E"))

                if tipo == 'CREATE':
                    self.main_app.msgbox("NOVO CLIENTE", "Novo cliente adicionado com sucesso!", 0)
                elif tipo == 'UPDATE':
                    self.main_app.msgbox("ATUALIZAR", "Informacões do cliente atualizadas com sucesso!", 0)

                self.menu_tipocliente.set(f'{tipo_cliente}')
                self.entry_cpf_cnpj.delete(0, ctk.END)
                self.entry_email.delete(0, ctk.END)
                self.entry_razao_social.delete(0, ctk.END)
                self.entry_nome.delete(0, ctk.END)
                self.entry_cep.delete(0, ctk.END)
                self.entry_endereco.delete(0, ctk.END)
                self.entry_numero.delete(0, ctk.END)
                self.entry_complemento.delete(0, ctk.END)
                self.entry_bairro.delete(0, ctk.END)
                self.entry_cidade.delete(0, ctk.END)
                self.entry_uf.delete(0, ctk.END)
                self.entry_fone.delete(0, ctk.END)
                self.entry_celular.delete(0, ctk.END)
                self.menu_questionario.set(f'')
                self.entry_observacoes.delete("0.0", "end")

            else:
                pass

    def definir_cliente(self, resposta):

        if resposta == 'PESSOA FISICA':

            self.entry_cpf_cnpj.configure(validate="key",
                                          validatecommand=(self.main_app.validate_cmd_numeric, "%P", 11))

        elif resposta == "PESSOA JURIDICA":
            self.entry_cpf_cnpj.configure(validate="key",
                                          validatecommand=(self.main_app.validate_cmd_numeric, "%P", 14))


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

        self.cor_destaque = self.main_app.chave_customjson("CTkFrame", "fg_color")
        self.listaBTS = []

        self.interface()

    def interface(self):

        self.LabelTitulo = ctk.CTkLabel(self.frame_resp, text=f"NOVO USUARIO", fg_color="transparent",
                                        text_color=("black", "white"), font=(ctk.CTkFont(size=14, weight="bold")),
                                        corner_radius=6)
        self.LabelTitulo.place(x=1, y=1)

        painel_novo_usuario = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270,
                                            height=90, border_width=3,
                                            fg_color="transparent", hover=False)
        painel_novo_usuario.place(relx=0.02, rely=0.1, anchor="w")

        titulo_usuario = ctk.CTkLabel(painel_novo_usuario, text="USUARIO")
        titulo_usuario.place(x=63, y=15)

        titulo_senha = ctk.CTkLabel(painel_novo_usuario, text="SENHA")
        titulo_senha.place(x=265, y=15)

        titulo_acesso = ctk.CTkLabel(painel_novo_usuario, text="ACESSO")
        titulo_acesso.place(x=465, y=15)

        titulo_status = ctk.CTkLabel(painel_novo_usuario, text="STATUS")
        titulo_status.place(x=663, y=15)

        self.EntryUsuario = ctk.CTkEntry(painel_novo_usuario, placeholder_text="Digite aqui:", width=150)
        self.EntryUsuario.place(x=10, y=45)

        self.EntrySenha = ctk.CTkEntry(painel_novo_usuario, placeholder_text="Senha temporaria:", width=150)
        self.EntrySenha.place(x=210, y=45)

        self.MenuAcesso = ctk.CTkOptionMenu(painel_novo_usuario, values=["USUARIO", "ADM"], width=150)
        self.MenuAcesso.place(x=410, y=45)

        self.MenuStatus = ctk.CTkOptionMenu(painel_novo_usuario, values=["ATIVO", "DESATIVADO"], width=150)
        self.MenuStatus.place(x=610, y=45)

        self.Bt_SalvarModulos = ctk.CTkButton(painel_novo_usuario, image=SalvarIcon, text_color=("black", "white"),
                                              text="Salvar Alteracões",
                                              width=80,
                                              command=self.salvar_getswitch)
        self.Bt_SalvarModulos.place(x=900, y=25)

        painel_botoes = ctk.CTkFrame(self.frame_resp, width=self.main_app.screen_wedth - 270, height=50,
                                     corner_radius=0, fg_color="transparent")
        painel_botoes.place(relx=0.02, rely=0.19)

        hovercolor = self.cor_destaque

        self.BT_ModuloEstoque = ctk.CTkButton(painel_botoes, image=EstoqueIcon, text="Estoque",
                                              text_color=("black", "white"), fg_color="transparent",
                                              hover_color=hovercolor, corner_radius=0, height=40, width=100,
                                              anchor="w",
                                              command=lambda: self.modulo_estoque(frame_resp=self.frame_resp))
        self.BT_ModuloEstoque.place(relx=0.0, rely=0.5, anchor="w", )

        self.BT_ModuloCadastro = ctk.CTkButton(painel_botoes, image=CadastroIcon, text="Cadastro",
                                               text_color=("black", "white"), fg_color="transparent",
                                               hover_color=hovercolor, corner_radius=0, height=40, width=100,
                                               anchor="w",
                                               command=lambda: self.modulo_cadastro(frame_resp=self.frame_resp))
        self.BT_ModuloCadastro.place(relx=0.1, rely=0.5, anchor="w", )

        self.BT_ModuloAgenda = ctk.CTkButton(painel_botoes, image=AgendaIcon, text="Agenda",
                                             text_color=("black", "white"), fg_color="transparent",
                                             hover_color=hovercolor, corner_radius=0, height=40, width=100,
                                             anchor="w", command=lambda: self.modulo_agenda(frame_resp=self.frame_resp))
        self.BT_ModuloAgenda.place(relx=0.2, rely=0.5, anchor="w", )

        self.BT_ModuloCarteira = ctk.CTkButton(painel_botoes, image=carteiraIcon, text="Carteira",
                                               text_color=("black", "white"), fg_color="transparent",
                                               hover_color=hovercolor, corner_radius=0, height=40, width=100,
                                               anchor="w",
                                               command=lambda: self.modulo_carteira(frame_resp=self.frame_resp))
        self.BT_ModuloCarteira.place(relx=0.3, rely=0.5, anchor="w", )

        self.BT_ModuloFinancas = ctk.CTkButton(painel_botoes, image=FinancasIcon, text="Financas",
                                               text_color=("black", "white"), fg_color="transparent",
                                               hover_color=hovercolor, corner_radius=0, height=40, width=100,
                                               anchor="w",
                                               command=lambda: self.modulo_financas(frame_resp=self.frame_resp))
        self.BT_ModuloFinancas.place(relx=0.4, rely=0.5, anchor="w", )

        self.BT_ModuloUsuarios = ctk.CTkButton(painel_botoes, image=UsuarioIcon, text="Usuarios",
                                               text_color=("black", "white"), fg_color="transparent",
                                               hover_color=hovercolor, corner_radius=0, height=40, width=100,
                                               anchor="w",
                                               command=lambda: self.modulo_usuario(frame_resp=self.frame_resp))
        self.BT_ModuloUsuarios.place(relx=0.5, rely=0.5, anchor="w", )

        self.BT_ModuloConfiguracoes = ctk.CTkButton(painel_botoes, image=ConfiguracoesIcon, text="Configuracões",
                                                    text_color=("black", "white"), fg_color="transparent",
                                                    hover_color=hovercolor, corner_radius=0, height=40,
                                                    width=100, anchor="w",
                                                    command=lambda: self.modulo_configuracoes(
                                                        frame_resp=self.frame_resp))
        self.BT_ModuloConfiguracoes.place(relx=0.6, rely=0.5, anchor="w", )

        self.listaBTS = [self.BT_ModuloEstoque, self.BT_ModuloCadastro, self.BT_ModuloAgenda, self.BT_ModuloCarteira,
                         self.BT_ModuloFinancas,
                         self.BT_ModuloUsuarios, self.BT_ModuloConfiguracoes]

        self.FrameModuloResp = ctk.CTkFrame(self.frame_resp, width=self.main_app.screen_wedth - 270, height=900,
                                            corner_radius=0)
        self.FrameModuloResp.place(relx=0.02, rely=0.24)

    @staticmethod
    def ativar_switch(principal, visualizar, novo, editar, remover):
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

    def salvar_getswitch(self):
        resp = self.main_app.msgbox("SALVAR", "Deseja salvar as alteracões nos módulos?", 4)
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

                    cursor = self.main_app.ConexaoPrincipal.cursor()
                    cursor.execute(f"SELECT usuario FROM Usuarios where usuario = '{login_digitado}'")
                    resp = cursor.fetchall()
                    if resp:
                        self.main_app.msgbox("USUARIO", "Ja existe um usuario com este nome, por favor escolha outro",
                                             0)
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
                            "Financas": {
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
                            "Configuracões": {
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

                        cursor = self.main_app.ConexaoPrincipal.cursor()

                        cursor.execute("""INSERT INTO Usuarios(usuario, senha, acesso, status)
                                        VALUES(?, ?, ?, ? )""", (login_digitado, senha_digitada, acesso, status))

                        cursor.execute(f"SELECT id FROM Usuarios WHERE usuario ='{login_digitado}'")
                        id_criado = cursor.fetchone()[0]
                        print(id_criado)

                        self.main_app.ConexaoPrincipal.commit()

                        # Itera sobre os dados do dicionário e insere no banco de dados
                        for modulo, submodulos in modules.items():
                            for submodulo, permissoes in submodulos.items():
                                visualizar = permissoes['visualizar']
                                novo = permissoes['novo']
                                editar = permissoes['editar']
                                remover = permissoes['remover']
                                cursor.execute("""
                                    INSERT INTO Modulos (usuario, modulo, submodulo, visualizar, novo, editar, remover, id_usuario)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                                """, (login_digitado, modulo, submodulo, visualizar, novo, editar, remover, id_criado))

                        # Efetua o commit da transacão
                        self.main_app.ConexaoPrincipal.commit()

                        InterfaceNovoUsuario(main_app=self.main_app, frame_resp=self.frame_resp)
                        self.main_app.msgbox("SALVAR", "Usuario criado com sucesso!!!", 0)
        except Exception as erro:
            print(erro)

    def modulo_estoque(self, frame_resp):

        if self.FrameModuloEstoqueResp is None:

            self.FrameModuloEstoqueResp = ctk.CTkFrame(frame_resp, width=self.main_app.screen_wedth - 270,
                                                       height=900, corner_radius=0)
            self.FrameModuloEstoqueResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloEstoque, cor=self.cor_destaque)

            titulo_entrada = ctk.CTkLabel(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="ENTRADA",
                                          text_color=("black", "white"), height=38, width=200,
                                          fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_entrada.place(relx=0.1, rely=0.03, anchor="center")

            entrada_switch = ctk.CTkSwitch(titulo_entrada, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                           offvalue="bloqueado",
                                           switch_height=25, switch_width=45, progress_color="#3DED9D",
                                           command=lambda: self.ativar_switch(entrada_switch, self.Entrada_visualizar,
                                                                              self.Entrada_novo, self.Entrada_editar,
                                                                              self.Entrada_remover))

            entrada_switch.place(relx=0.94, rely=0.5, anchor="center")

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
                                         command=lambda: self.ativar_switch(saida_switch, self.saida_visualizar,
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
                                              command=lambda: self.ativar_switch(inventario_switch,
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
            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloEstoque, cor=self.cor_destaque)

    def modulo_cadastro(self, frame_resp):

        if self.FrameModuloCadastroResp is None:

            self.FrameModuloCadastroResp = ctk.CTkFrame(frame_resp, width=self.main_app.screen_wedth - 270,
                                                        height=900, corner_radius=0)
            self.FrameModuloCadastroResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloCadastro, cor=self.cor_destaque)

            titulo_item = ctk.CTkLabel(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="CAD ITENS",
                                       text_color=("black", "white"), height=38, width=200,
                                       fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_item.place(relx=0.1, rely=0.03, anchor="center")

            item_switch = ctk.CTkSwitch(titulo_item, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                        offvalue="bloqueado",
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.ativar_switch(item_switch, self.item_visualizar,
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
                                           command=lambda: self.ativar_switch(cliente_switch, self.cliente_visualizar,
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
                                                command=lambda: self.ativar_switch(criarusuario_switch,
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

            titulo_gerenciar_user = ctk.CTkLabel(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"),
                                                 text="GERENCIAR USER", text_color=("black", "white"), height=38,
                                                 width=200,
                                                 fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_gerenciar_user.place(relx=0.1, rely=0.26, anchor="center")

            gerenciar_switch = ctk.CTkSwitch(titulo_gerenciar_user, font=ctk.CTkFont(weight="bold"), text="",
                                             onvalue="liberado", offvalue="bloqueado",
                                             switch_height=25, switch_width=45, progress_color="#3DED9D",
                                             command=lambda: self.ativar_switch(gerenciar_switch,
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
            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloCadastro, cor=self.cor_destaque)

    def modulo_agenda(self, frame_resp):

        if self.FrameModuloAgendaResp is None:

            self.FrameModuloAgendaResp = ctk.CTkFrame(frame_resp, width=self.main_app.screen_wedth - 270,
                                                      height=900, corner_radius=0)
            self.FrameModuloAgendaResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloAgenda, cor=self.cor_destaque)

            titulo_agenda = ctk.CTkLabel(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"), text="AGENDA",
                                         text_color=("black", "white"), height=38, width=200,
                                         fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_agenda.place(relx=0.1, rely=0.03, anchor="center")

            agenda_switch = ctk.CTkSwitch(titulo_agenda, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                          offvalue="bloqueado",
                                          switch_height=25, switch_width=45, progress_color="#3DED9D",
                                          command=lambda: self.ativar_switch(agenda_switch, self.agenda_visualizar,
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
            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloAgenda, cor=self.cor_destaque)

    def modulo_carteira(self, frame_resp):

        if self.FrameModuloCarteiraResp is None:

            self.FrameModuloCarteiraResp = ctk.CTkFrame(frame_resp, width=self.main_app.screen_wedth - 270,
                                                        height=900, corner_radius=0)
            self.FrameModuloCarteiraResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloCarteira, cor=self.cor_destaque)

            titulo_vendas = ctk.CTkLabel(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="VENDAS",
                                         text_color=("black", "white"), height=38, width=200,
                                         fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_vendas.place(relx=0.1, rely=0.03, anchor="center")

            vendas_switch = ctk.CTkSwitch(titulo_vendas, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                          offvalue="bloqueado",
                                          switch_height=25, switch_width=45, progress_color="#3DED9D",
                                          command=lambda: self.ativar_switch(vendas_switch, self.vendas_visualizar,
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
                                               command=lambda: self.ativar_switch(faturamento_switch,
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
            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloCarteira, cor=self.cor_destaque)

    def modulo_financas(self, frame_resp):

        if self.FrameModuloFinancasResp is None:

            self.FrameModuloFinancasResp = ctk.CTkFrame(frame_resp, width=self.main_app.screen_wedth - 270,
                                                        height=900, corner_radius=0)
            self.FrameModuloFinancasResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloFinancas, cor=self.cor_destaque)

            titulo_despesas = ctk.CTkLabel(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"),
                                           text="DESPESAS", text_color=("black", "white"), height=38, width=200,
                                           fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_despesas.place(relx=0.1, rely=0.03, anchor="center")

            despesas_switch = ctk.CTkSwitch(titulo_despesas, font=ctk.CTkFont(weight="bold"), text="",
                                            onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=45, progress_color="#3DED9D",
                                            command=lambda: self.ativar_switch(despesas_switch,
                                                                               self.despesas_visualizar,
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
                                          command=lambda: self.ativar_switch(rendas_switch, self.rendas_visualizar,
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
            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloFinancas, cor=self.cor_destaque)

    def modulo_usuario(self, frame_resp):

        if self.FrameModuloUsuarioResp is None:
            self.FrameModuloUsuarioResp = ctk.CTkFrame(frame_resp, width=self.main_app.screen_wedth - 270,
                                                       height=900, corner_radius=0)
            self.FrameModuloUsuarioResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloUsuarios, cor=self.cor_destaque)

            titulo_usuario = ctk.CTkLabel(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"), text="USUARIO",
                                          text_color=("black", "white"), height=38, width=200,
                                          fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_usuario.place(relx=0.1, rely=0.03, anchor="center")

            usuario_switch = ctk.CTkSwitch(titulo_usuario, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                           offvalue="bloqueado",
                                           switch_height=25, switch_width=45, progress_color="#3DED9D",
                                           command=lambda: self.ativar_switch(usuario_switch, self.usuario_visualizar,
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
            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloUsuarios, cor=self.cor_destaque)

    def modulo_configuracoes(self, frame_resp):

        if self.FrameModuloConfiguracoesResp is None:

            self.FrameModuloConfiguracoesResp = ctk.CTkFrame(frame_resp, width=self.main_app.screen_wedth - 270,
                                                             height=900, corner_radius=0)
            self.FrameModuloConfiguracoesResp.place(relx=0.02, rely=0.24)

            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloConfiguracoes, cor=self.cor_destaque)

            titulo_configuracoes = ctk.CTkLabel(self.FrameModuloConfiguracoesResp, font=ctk.CTkFont(weight="bold"),
                                                text="CONFIGURAcÕES", text_color=("black", "white"), height=38,
                                                width=200,
                                                fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_configuracoes.place(relx=0.1, rely=0.03, anchor="center")

            configuracoes_switch = ctk.CTkSwitch(titulo_configuracoes, font=ctk.CTkFont(weight="bold"), text="",
                                                 onvalue="liberado", offvalue="bloqueado",
                                                 switch_height=25, switch_width=45, progress_color="#3DED9D",
                                                 command=lambda: self.ativar_switch(configuracoes_switch,
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
            self.main_app.destacar(self.listaBTS, botao=self.BT_ModuloConfiguracoes, cor=self.cor_destaque)


class InterfaceUsuario:

    def __init__(self, main_app, frame_resp, bt_perfil):

        self.main_app = main_app
        self.frame_resp = frame_resp
        self.bt_perfil = bt_perfil
        self.conexao = self.main_app.ConexaoPrincipal

        self.interface()

    def interface(self):

        self.frame_resp.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
        self.frame_resp.grid_columnconfigure(0, weight=1)

        label_titulo = ctk.CTkLabel(self.frame_resp, text=f"USUARIO", fg_color="transparent",
                                    text_color=("black", "white"),
                                    font=self.main_app.SubTitle, corner_radius=6, anchor="w")
        label_titulo.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        painel_ft_perfil = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                         border_width=1,
                                         fg_color="transparent", hover=False)

        painel_ft_perfil.grid(row=1, column=0, padx=10, pady=(45, 5), sticky="nsew")

        painel_usuario = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                       border_width=1,
                                       fg_color="transparent", hover=False)
        painel_usuario.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        painel_senha = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                     border_width=1, fg_color="transparent",
                                     hover=False)
        painel_senha.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

        painel_excluir = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                       border_width=1,
                                       fg_color="transparent", hover=False)
        painel_excluir.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")

        label_ft_perfil = ctk.CTkLabel(painel_ft_perfil, text="Foto de perfil", font=self.main_app.FontTitle,
                                       fg_color="transparent")
        label_ft_perfil.place(x=10, y=5)

        bt = ctk.CTkButton(painel_ft_perfil, image=ImagemIcon, text="Alterar", command=self.trocar_img,
                           text_color=("black", "white"),
                           width=80, )
        bt.place(x=10, y=50)

        titulo_usuario = ctk.CTkLabel(painel_usuario, text="Usuario", font=self.main_app.FontTitle,
                                      fg_color="transparent")
        titulo_usuario.place(x=10, y=5)

        self.LabelUsuario = ctk.CTkLabel(painel_usuario, text=f"{self.main_app.usuario_logado}",
                                         font=self.main_app.FontBody, fg_color="transparent")
        self.LabelUsuario.place(x=10, y=50)

        titulo_acesso = ctk.CTkLabel(painel_usuario, text="Acesso", font=self.main_app.FontTitle,
                                     fg_color="transparent")
        titulo_acesso.place(x=100, y=5)

        label_acesso = ctk.CTkLabel(painel_usuario, text=f"{self.main_app.acesso_usuario.upper()}",
                                    font=self.main_app.FontBody,
                                    fg_color="transparent")
        label_acesso.place(x=100, y=50)

        bt_editar_user = ctk.CTkButton(painel_usuario, image=EditarIcon2, text="Editar", text_color=("black", "white"),
                                       width=80,
                                       command=self.editar_usuario)
        bt_editar_user.place(x=165, y=28)

        label_senha = ctk.CTkLabel(painel_senha, text="Senha", font=self.main_app.FontTitle, fg_color="transparent")
        label_senha.place(x=10, y=5)

        bt_trocar_senha = ctk.CTkButton(painel_senha, image=SenhaIcon, text="Alterar", text_color=("black", "white"),
                                        width=80,
                                        command=self.trocar_senha)
        bt_trocar_senha.place(x=10, y=50)

        label_excluir = ctk.CTkLabel(painel_excluir, text="Conta", font=self.main_app.FontTitle, fg_color="transparent")
        label_excluir.place(x=10, y=5)

        bt_excluir = ctk.CTkButton(painel_excluir, image=DeletarIcon2, text="Excluir Conta",
                                   text_color=("black", "white"),
                                   width=80,
                                   command=self.excluir_conta)
        bt_excluir.place(x=10, y=50)

    def trocar_img(self):
        imagem = self.bt_perfil

        CarregarIMG(main_app=self.main_app).select_image(imagem, usuario=self.main_app.usuario_logado)

    def editar_usuario(self):
        dialog = ctk.CTkInputDialog(text="DIGITE SEU NOVO NOME DE USUARIO:", title="Editar")
        usuario_digitado = dialog.get_input()

        if usuario_digitado is not None:

            if len(usuario_digitado) >= 3:

                cursor = self.main_app.ConexaoPrincipal.cursor()
                cursor.execute(f"SELECT usuario FROM Usuarios where usuario = '{usuario_digitado}'")
                resposta_bd = cursor.fetchall()
                if not resposta_bd:
                    cursor.execute(
                        f"UPDATE Usuarios SET usuario = '{usuario_digitado}' WHERE usuario = '{self.main_app.usuario_logado}'")
                    self.main_app.usuario_logado = str(usuario_digitado)
                    self.main_app.ConexaoPrincipal.commit()
                    self.LabelUsuario.configure(text=usuario_digitado)

                elif usuario_digitado == self.main_app.usuario_logado:
                    self.main_app.msgbox("USUARIO", "Este ja é o seu nome de usuario\n Informe um nome diferente.", 0)

                else:
                    self.main_app.msgbox("USUARIO", "Ja existe um usuario com este nome!!!", 0)

            elif 1 <= len(usuario_digitado) <= 2:
                self.main_app.msgbox("USUARIO", "Seu novo nome de usuario deve conter pelo menos 3 caracteres", 0)

    def trocar_senha(self):

        dialog = ctk.CTkToplevel()
        dialog.title("SENHA")
        dialog.geometry("340x250")
        dialog.resizable(0, 0)
        dialog.grab_set()

        def requisitos_atual(event):
            msg_atual = ctk.CTkLabel(dialog, text="Senha atual", height=3)
            msg_atual.place(relx=0.15, rely=0.2, anchor="center")

        def requisitos_senha1(event):
            nova = str(nova_senha.get())
            if len(nova) <= 5:
                msg_nova = ctk.CTkLabel(dialog, text="Nova senha", height=3)
                msg_nova.place(relx=0.15, rely=0.4, anchor="center")
                resposta.configure(text="Sua senha deve ter no minimo 6 caracteres.", text_color="red")
                botao_salvar_registro.configure(state="disabled")
            else:
                resposta.configure(text="", text_color="green")

                if len(str(confirmacao_senha.get())) > 5:
                    botao_salvar_registro.configure(state="normal")

        def requisitos_senha2(event):
            nova_senha_digitada = str(confirmacao_senha.get())
            nova_senha_confirmada = str(confirmacao_senha.get())

            msg_confirmacao = ctk.CTkLabel(dialog, text="Redigite a nova senha", height=3)
            msg_confirmacao.place(relx=0.23, rely=0.6, anchor="center")

            if nova_senha_confirmada == nova_senha_digitada and len(nova_senha_confirmada) > 5:
                resposta.configure(text="", text_color="Green")
                botao_salvar_registro.configure(state="normal")
                if len(nova_senha_digitada) > 5:
                    botao_salvar_registro.configure(state="normal")

            else:
                resposta.configure(text="A nova senha não é igual à redigitada.", text_color="red")
                botao_salvar_registro.configure(state="disabled")

        def salvar():
            atual = str(senha_atual.get())
            nova = str(nova_senha.get())

            cursor = self.main_app.ConexaoPrincipal.cursor()
            cursor.execute(
                f"SELECT senha FROM Usuarios WHERE usuario = '{self.main_app.usuario_logado}' AND senha = '{atual}'")
            resultado_bd = cursor.fetchall()

            if resultado_bd:
                cursor.execute(f"UPDATE Usuarios SET senha = '{nova}' WHERE usuario = '{self.main_app.usuario_logado}'")
                self.main_app.ConexaoPrincipal.commit()
                resposta.configure(text="Senha atualizada com sucesso!", text_color="green")
                botao_salvar_registro.configure(state="disabled")
            else:
                resposta.configure(text="Senha atual esta incorreta", text_color="red")

        def fechar():
            dialog.destroy()

        msg = ctk.CTkLabel(dialog, text="TROCAR SENHA", font=self.main_app.FontTitle)
        msg.place(relx=0.5, rely=0.1, anchor="center")

        senha_atual = ctk.CTkEntry(dialog, placeholder_text="Digite sua senha atual", width=320)
        senha_atual.place(relx=0.5, rely=0.3, anchor="center")
        senha_atual.bind('<KeyRelease>', requisitos_atual)

        nova_senha = ctk.CTkEntry(dialog, placeholder_text="Digite sua nova senha", width=320, show="*")
        nova_senha.place(relx=0.5, rely=0.5, anchor="center")
        nova_senha.bind('<KeyRelease>', requisitos_senha1)

        confirmacao_senha = ctk.CTkEntry(dialog, placeholder_text="Confirmar nova senha", width=320, show="*")
        confirmacao_senha.place(relx=0.5, rely=0.7, anchor="center"),
        confirmacao_senha.bind('<KeyRelease>', requisitos_senha2)

        resposta = ctk.CTkLabel(dialog, text="", height=2)
        resposta.place(relx=0.5, rely=0.81, anchor="center")

        botao_salvar_registro = ctk.CTkButton(dialog, text="SALVAR", command=salvar,
                                              state='disabled')
        botao_salvar_registro.place(relx=0.25, rely=0.92, anchor="center")

        botao_cancelar_registro = ctk.CTkButton(dialog, text="Fechar",
                                                command=fechar)
        botao_cancelar_registro.place(relx=0.75, rely=0.92, anchor="center")

    def excluir_conta(self):

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

        botao_excluir = ctk.CTkButton(dialog, text="EXCLUIR",
                                      command=conta_delete)
        botao_excluir.place(relx=0.25, rely=0.79, anchor="center")

        botao_fechar = ctk.CTkButton(dialog, text="Fechar",
                                     command=fechar)
        botao_fechar.place(relx=0.75, rely=0.79, anchor="center")


class InterfaceConfiguracoes:

    def __init__(self, main_app, frame_resp):
        self.main_app = main_app
        self.frame_resp = frame_resp
        self.conexao = self.main_app.ConexaoPrincipal

        self.interface()

    def interface(self):
        self.frame_resp.grid_rowconfigure((0, 1), weight=0)
        self.frame_resp.grid_columnconfigure(0, weight=1)

        label_titulo = ctk.CTkLabel(self.frame_resp, text=f"CONFIGURAcÕES", fg_color="transparent",
                                    text_color=("black", "white"),
                                    font=self.main_app.SubTitle, corner_radius=6, anchor="w")
        label_titulo.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        painel_theme = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                     border_width=1,
                                     fg_color="transparent", hover=False)
        painel_theme.grid(row=1, column=0, sticky="nsew", padx=10, pady=(45, 5))

        label_theme = ctk.CTkLabel(painel_theme, text="Alterar tema", font=self.main_app.FontTitle,
                                   fg_color="transparent")
        label_theme.place(x=10, y=5)

        opcoes = ["blue", "green", "dark-blue", "personalizado"]
        valor_escolhido = self.main_app.themeAtual

        # Encontra a posicão do valor escolhido na lista
        indice_valor_escolhido = opcoes.index(valor_escolhido)

        # Reorganiza a lista colocando o valor escolhido no início
        opcoes = [valor_escolhido] + opcoes[:indice_valor_escolhido] + opcoes[indice_valor_escolhido + 1:]

        mudar_theme = ctk.CTkOptionMenu(painel_theme, font=self.main_app.FontBody, width=100,
                                        values=opcoes, command=self.main_app.theme)
        mudar_theme.place(x=10, y=50)


class CarregarIMG:

    def __init__(self, main_app):

        self.main_app = main_app
        self.conexao = self.main_app.ConexaoPrincipal

    def verificar_foto(self, label_img, usuario):

        cursor = self.conexao.cursor()
        # Buscar a imagem no banco de dados
        cursor.execute(f"SELECT imagem FROM Usuarios where usuario = '{usuario}'")
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
                photo = ctk.CTkImage(image_circular, size=(100, 100))
                # Atualizar o widget Label com a nova imagem
                label_img.configure(image=photo, text="")
                label_img.image = photo
            except Exception as erro:
                print(erro)

        else:
            print("não existe nenhuma img no banco de dados")

    def select_image(self, label_img, usuario):  # Funcão para selecionar a imagem
        # Abrir o diálogo de selecão de arquivo
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

    @staticmethod
    def load_image(file_path, label_img):  # Funcão para carregar a imagem
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
        photo = ctk.CTkImage(image_circular, size=(100, 100))

        # Atualizar o widget Label com a nova imagem
        label_img.configure(image=photo, text="")
        label_img.image = photo

    def insert_image(self, image_base64, usuario):  # Funcão para inserir ou atualizar a img no BD

        cursor = self.conexao.cursor()

        # Converter a imagem base64 para dados binários
        image_binary = binascii.a2b_base64(image_base64)

        # Verificar se já existe uma imagem com o ID 1
        cursor.execute(f"SELECT COUNT(*) FROM Usuarios WHERE usuario = '{usuario}'")
        count = cursor.fetchone()[0]

        if count > 0:
            # Atualizar a imagem existente
            cursor.execute("UPDATE Usuarios SET imagem = ? WHERE usuario = ?", (image_binary, usuario))
        else:
            self.main_app.msgbox("ERRO", "NAO ENCONTRADO USUARIO NO BD PARA INSERIR A NOVA IMAGEM", 0)

        # Salvar as alteracões e fechar a conexão
        self.conexao.commit()


class MenuOpcoes:

    def __init__(self, root_opcoes, main_app):
        self.rootHome = root_opcoes
        self.main_app = main_app

        self.conexao = self.main_app.ConexaoPrincipal

        self.rootHome.title("SYS COMERCIAL")
        self.rootHome.state('zoomed')

        self.screen_height = self.rootHome.winfo_screenheight()
        self.screen_wedth = self.rootHome.winfo_screenwidth()

        self.listaBTS = []

        self.cor_destaque = self.main_app.chave_customjson("CTkButton", "hover_color")

        # Configure a expansão horizontal (caso necessário)
        self.rootHome.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.rootHome.grid_columnconfigure(1, weight=0)  # Coluna 1 não se expandirá
        self.rootHome.grid_columnconfigure(2, weight=1)  # Coluna 2 se expandirá

        self.rootHome.grid_rowconfigure((0, 1, 2), weight=1)

        self.frame_MenuLateralEsq = ctk.CTkFrame(self.rootHome, width=176, corner_radius=0)
        self.frame_MenuLateralEsq.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.frame_MenuLateralEsq.grid_rowconfigure(10, weight=1)

        self.frame_MenuLateralDir = ctk.CTkFrame(self.rootHome, width=37, corner_radius=0, fg_color=self.cor_destaque)
        self.frame_MenuLateralDir.grid(row=0, column=1, rowspan=4, sticky="nsew")

        self.frame_resposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", corner_radius=0)
        self.frame_resposta.grid(row=0, column=2, rowspan=4, sticky="nsew")

        # Configure a expansão vertical

        self.BtOcultar = ctk.CTkButton(self.frame_MenuLateralDir, text="", image=MenuIcon, anchor="w", width=23,
                                       height=23,
                                       fg_color="transparent", text_color=("black", "white"),
                                       command=lambda: self.main_app.esconder_Janela(self.frame_MenuLateralEsq))
        self.bt_opcoes()
        self.scaling_optionemenu.set("100%")

    def limpar_frames(self, laterial_direito, resposta, pos=0, excluir=False):

        # Esconder os widgets em vez de destruí-los
        for widget in laterial_direito.winfo_children():
            widget.place_forget()
            widget.grid_remove()

        if excluir:
            for widget in resposta.winfo_children():
                try:
                    widget.place_forget()
                    widget.grid_remove()
                except Exception as e:
                    print(f"Ocorreu uma exceção ao tentar esconder o widget: {e}")

        self.frame_MenuLateralDir.configure(width=37)
        self.BtOcultar.place(x=pos, y=1)

    def bt_opcoes(self):

        self.Btfoto_perfil = ctk.CTkButton(self.frame_MenuLateralEsq, text="", image=perfilIcon, fg_color="transparent",
                                           command=self.frame_usuario)
        self.Btfoto_perfil.grid(row=0, column=0, pady=5)

        self.BtHome = ctk.CTkButton(self.frame_MenuLateralEsq, text="Home", image=HomeIcon, anchor="w",
                                    width=176, corner_radius=0, fg_color="transparent", text_color=("black", "white"),
                                    command=self.frame_home)
        self.BtHome.grid(row=1, column=0, padx=0, pady=5)

        self.BtEstoque = ctk.CTkButton(self.frame_MenuLateralEsq, text="Estoque ", image=EstoqueIcon, anchor="w",
                                       width=176, corner_radius=0, fg_color="transparent",
                                       text_color=("black", "white"), command=self.frame_estoque)
        self.BtEstoque.grid(row=2, column=0, pady=5)

        self.BtCadastros = ctk.CTkButton(self.frame_MenuLateralEsq, text="Cadastro", image=CadastroIcon, anchor="w",
                                         width=176, corner_radius=0, fg_color="transparent",
                                         text_color=("black", "white"), command=self.frame_cadastro)
        self.BtCadastros.grid(row=3, column=0, pady=5)

        self.BtAgenda = ctk.CTkButton(self.frame_MenuLateralEsq, text="Agenda", image=AgendaIcon, anchor="w",
                                      width=176, corner_radius=0, fg_color="transparent", text_color=("black", "white"),
                                      command=self.frame_agenda)
        self.BtAgenda.grid(row=4, column=0, pady=5)

        self.Btcarteira = ctk.CTkButton(self.frame_MenuLateralEsq, text="Carteira", image=carteiraIcon, anchor="w",
                                        width=176, corner_radius=0, fg_color="transparent",
                                        text_color=("black", "white"), command=self.frame_carteira)
        self.Btcarteira.grid(row=5, column=0, pady=5)

        self.BtFinancas = ctk.CTkButton(self.frame_MenuLateralEsq, text="Financas", image=FinancasIcon, anchor="w",
                                        width=176, corner_radius=0, fg_color="transparent",
                                        text_color=("black", "white"), command=self.frame_financas)
        self.BtFinancas.grid(row=6, column=0, pady=5)

        self.BtUsuario = ctk.CTkButton(self.frame_MenuLateralEsq, text="Usuario", image=UsuarioIcon, anchor="w",
                                       width=176, corner_radius=0, fg_color="transparent",
                                       text_color=("black", "white"), command=self.frame_usuario)
        self.BtUsuario.grid(row=7, column=0, pady=5)

        self.BtConfiguracoes = ctk.CTkButton(self.frame_MenuLateralEsq, text="Configuracoes", image=ConfiguracoesIcon,
                                             anchor="w",
                                             width=176, corner_radius=0, text_color=("black", "white"),
                                             fg_color="transparent", command=self.frame_configuracoes)
        self.BtConfiguracoes.grid(row=8, column=0, pady=5)

        self.listaBTS = [self.BtHome, self.BtEstoque, self.BtCadastros, self.BtAgenda, self.Btcarteira,
                         self.BtFinancas, self.BtUsuario, self.BtConfiguracoes]

        self.LabelLogo = ctk.CTkLabel(self.frame_MenuLateralEsq, text="", image=SeuLogo2, anchor="w")
        self.LabelLogo.grid(row=9, column=0, pady=5)

        self.scaling_optionemenu = ctk.CTkOptionMenu(self.frame_MenuLateralEsq, font=self.main_app.FontBody, width=150,
                                                     values=["80%", "90%", "100%", "110%", "120%"],
                                                     command=self.main_app.change_scaling_event)
        self.scaling_optionemenu.grid(row=11, column=0, pady=5)

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.frame_MenuLateralEsq, font=self.main_app.FontBody,
                                                             width=150,
                                                             values=["system", "light", "Dark"],
                                                             command=self.main_app.aparencia)
        self.appearance_mode_optionemenu.grid(row=12, column=0, pady=5)

        self.desativar_modulos()
        CarregarIMG(main_app=self.main_app).verificar_foto(self.Btfoto_perfil, self.main_app.usuario_logado)
        self.frame_home()

    def frame_home(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtHome, cor=self.cor_destaque)

    def frame_estoque(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=138)
        self.frame_MenuLateralDir.configure(width=176)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtEstoque, cor=self.cor_destaque)

        self.BTEntrada = ctk.CTkButton(self.frame_MenuLateralDir, text="Entrada", image=EntradaIcon, anchor="w",
                                       width=155,
                                       text_color=("black", "white"),
                                       hover_color=self.main_app.chave_customjson("CTkOptionMenu", "button_color"),
                                       )
        self.BTEntrada.place(x=10, y=120)

        self.BTSaida = ctk.CTkButton(self.frame_MenuLateralDir, text="Saida", image=SaidaIcon, anchor="w", width=155,
                                     text_color=("black", "white"),
                                     hover_color=self.main_app.chave_customjson("CTkOptionMenu", "button_color"),
                                     )
        self.BTSaida.place(x=10, y=160)

        self.BTInventario = ctk.CTkButton(self.frame_MenuLateralDir, text="Inventario", image=InventarioIcon,
                                          anchor="w",
                                          width=155, text_color=("black", "white"),
                                          hover_color=self.main_app.chave_customjson("CTkOptionMenu", "button_color"),
                                          )
        self.BTInventario.place(x=10, y=200)

        self.desativar_submodulos(modulo='Estoque')

    def frame_cadastro(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=138)
        self.frame_MenuLateralDir.configure(width=176)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtCadastros, cor=self.cor_destaque)

        self.BTCadastrarItens = ctk.CTkButton(self.frame_MenuLateralDir, text="Cadastrar Itens", image=EstoqueIcon,
                                              anchor="w", width=155,
                                              text_color=("black", "white"),
                                              hover_color=self.main_app.chave_customjson("CTkOptionMenu",
                                                                                         "button_color"),
                                              command=lambda: self.frame_novoitem())
        self.BTCadastrarItens.place(x=10, y=160)

        self.BTCadastrarClientes = ctk.CTkButton(self.frame_MenuLateralDir, text="Cadastrar Clientes",
                                                 image=CadastroIcon,
                                                 anchor="w", width=155,
                                                 text_color=("black", "white"),
                                                 hover_color=self.main_app.chave_customjson("CTkOptionMenu",
                                                                                            "button_color"),

                                                 command=lambda: self.frame_novocliente())
        self.BTCadastrarClientes.place(x=10, y=200)

        self.BTCriarNovoUsuario = ctk.CTkButton(self.frame_MenuLateralDir, text="Novo Usuario", image=UsuarioIcon,
                                                anchor="w", width=155,
                                                text_color=("black", "white"),
                                                hover_color=self.main_app.chave_customjson("CTkOptionMenu",
                                                                                           "button_color"),
                                                command=lambda: self.frame_novo_user())
        self.BTCriarNovoUsuario.place(x=10, y=240)

        self.BTGerenciarUsuario = ctk.CTkButton(self.frame_MenuLateralDir, text="Gerenciar Usuarios",
                                                image=GerenciarUserIcon, anchor="w", width=155,
                                                hover_color=self.main_app.chave_customjson("CTkOptionMenu",
                                                                                           "button_color"),
                                                text_color=("black", "white"),

                                                command=lambda: self.frame_gerenciar_user())

        self.desativar_submodulos(modulo='Cadastro')

        self.BTGerenciarUsuario.place(x=10, y=280)

    def frame_novoitem(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=0, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtCadastros, cor=self.cor_destaque)

        self.main_app.exibir_novoitem(self.frame_resposta)

    def frame_novocliente(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=0, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtCadastros, cor=self.cor_destaque)

        self.main_app.exibir_novocliente(self.frame_resposta)

    def frame_novo_user(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=0, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtCadastros, cor=self.cor_destaque)

        # LabelTitulo = ctk.CTkLabel(self.frame_resposta, text=f"NOVO USUARIO",fg_color="transparent", text_color=("black", "white"), 
        #                            font=self.main_app.SubTitle, corner_radius=6)
        # LabelTitulo.place(relx=0.001, rely=0.02, anchor="w")

        self.main_app.exibir_novousuario(self.frame_resposta)

    def frame_gerenciar_user(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=0, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtCadastros, cor=self.cor_destaque)

        label_titulo = ctk.CTkLabel(self.frame_resposta, text=f"GERENCIAR USUARIOS", fg_color="transparent",
                                    text_color=("black", "white"),
                                    font=self.main_app.SubTitle, corner_radius=6)
        label_titulo.place(relx=0.001, rely=0.02, anchor="w")
        self.main_app.exibir_gerenciarusuarios(self.frame_resposta)

    def frame_agenda(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtAgenda, cor=self.cor_destaque)

        label_titulo = ctk.CTkLabel(self.frame_resposta, text=f"AGENDA", fg_color="transparent",
                                    text_color=("black", "white"),
                                    font=self.main_app.SubTitle, corner_radius=6)
        label_titulo.place(relx=0.001, rely=0.02, anchor="w")

    def frame_carteira(self):

        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=138)
        self.frame_MenuLateralDir.configure(width=176)

        self.main_app.destacar(lista=self.listaBTS, botao=self.Btcarteira, cor=self.cor_destaque)

        self.BTRegistrarVenda = ctk.CTkButton(self.frame_MenuLateralDir, text="Registrar Venda", image=VendasIcon,
                                              anchor="w", width=155,
                                              text_color=("black", "white"),
                                              hover_color=self.main_app.chave_customjson("CTkOptionMenu",
                                                                                         "button_color"),
                                              )
        self.BTRegistrarVenda.place(x=10, y=280)

        self.BTFaturamento = ctk.CTkButton(self.frame_MenuLateralDir, text="Faturamento", image=FaturamentoIcon,
                                           anchor="w", width=155,
                                           text_color=("black", "white"),
                                           hover_color=self.main_app.chave_customjson("CTkOptionMenu", "button_color"),
                                           )
        self.BTFaturamento.place(x=10, y=320)

        self.desativar_submodulos(modulo='carteira')

    def frame_financas(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, pos=138)
        self.frame_MenuLateralDir.configure(width=176)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtFinancas, cor=self.cor_destaque)

        self.BTRegistrarDespesas = ctk.CTkButton(self.frame_MenuLateralDir, text="Registrar Despesas",
                                                 image=DespesaIcon,
                                                 anchor="w", width=155,
                                                 text_color=("black", "white"),
                                                 hover_color=self.main_app.chave_customjson("CTkOptionMenu",
                                                                                            "button_color"),
                                                 )
        self.BTRegistrarDespesas.place(x=10, y=320)

        self.BTOutrasRendas = ctk.CTkButton(self.frame_MenuLateralDir, text="Outras Rendas +", image=ReceitaIcon,
                                            anchor="w", width=155,
                                            text_color=("black", "white"),
                                            hover_color=self.main_app.chave_customjson("CTkOptionMenu", "button_color"),
                                            )
        self.BTOutrasRendas.place(x=10, y=360)
        self.desativar_submodulos(modulo='Financas')

    def frame_usuario(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtUsuario, cor=self.cor_destaque)

        self.main_app.exibir_usuario(self.frame_resposta, self.Btfoto_perfil)

    def frame_configuracoes(self):
        self.limpar_frames(self.frame_MenuLateralDir, self.frame_resposta, excluir=True)

        self.main_app.destacar(lista=self.listaBTS, botao=self.BtConfiguracoes, cor=self.cor_destaque)

        self.main_app.exibir_configuracoes(self.frame_resposta)

    def desativar_modulos(self):
        estoque = 0
        cadastro = 0
        carteira = 0
        financas = 0

        resultado = self.main_app.ModulosDoUsuario
        for tupla in resultado:

            if tupla[2] == 'Agenda' and tupla[3] == 'AGENDA':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    self.BtAgenda.configure(state="disabled")

            elif tupla[2] == 'Usuario' and tupla[3] == 'USUARIO':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    self.BtUsuario.configure(state="disabled")

            elif tupla[2] == 'Configuracões' and tupla[3] == 'CONFIGURACOES':
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

            elif tupla[2] == 'Financas' and tupla[3] == 'DESPESAS':
                if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                    financas += 1

            elif tupla[2] == 'Financas' and tupla[3] == 'OUTRAS RENDAS':
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
        resultado = self.main_app.ModulosDoUsuario
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

            elif modulo == 'Financas':
                for tupla in resultado:

                    if tupla[2] == 'Financas' and tupla[3] == 'DESPESAS':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTRegistrarDespesas.configure(state="disabled")

                    elif tupla[2] == 'Financas' and tupla[3] == 'OUTRAS RENDAS':
                        if tupla[4] == 'bloqueado' and tupla[5] == 'bloqueado' and tupla[6] == 'bloqueado':
                            self.BTOutrasRendas.configure(state="disabled")

        except Exception as erro:
            print(erro)


class TelaLogin:
    def __init__(self, root_login, main_app):
        self.Root_login = root_login
        self.main_app = main_app
        self.Root_login.title("Login")
        self.Root_login.geometry(f"400x430")
        # self.Root_login.resizable(False, False)

        self.conexao = self.main_app.ConexaoPrincipal
        background_login = ctk.CTkLabel(self.Root_login, text="", image=fundoLogin, width=400, height=450)
        background_login.place(relx=0.5, rely=0.5, anchor="center")

        def mostrar_senha():
            if self.MostrarSenha.get():
                self.SenhaDigitado.configure(show="")
            else:
                self.SenhaDigitado.configure(show="*")

        def ativar_enter(Event):
            self.fazer_login()

        painel = ctk.CTkButton(self.Root_login, width=320, height=370, corner_radius=2, fg_color="#242A5F",
                               bg_color="#242A5F", hover=False)
        painel.place(relx=0.5, rely=0.5, anchor="center")

        label_txt = ctk.CTkLabel(painel, text="", image=UsuarioIcon2, font=self.main_app.FontTitle,
                                 fg_color="transparent", bg_color="transparent")
        label_txt.place(relx=0.5, rely=0.1, anchor="center")

        label_txt = ctk.CTkLabel(painel, text="Bem Vindo", font=self.main_app.FontTitle, fg_color="transparent",
                                 bg_color="transparent", text_color="white")
        label_txt.place(relx=0.5, rely=0.17, anchor="center")

        self.LoginDigitado = ctk.CTkEntry(painel, placeholder_text="Digite seu login", text_color="black",
                                          fg_color="white", width=200, border_color="white")
        self.LoginDigitado.place(relx=0.5, rely=0.3, anchor='center')

        self.SenhaDigitado = ctk.CTkEntry(painel, placeholder_text="Digite sua senha", text_color="black",
                                          fg_color="white", width=200, show="*", border_color="white")
        self.SenhaDigitado.place(relx=0.5, rely=0.4, anchor='center')

        self.MostrarSenha = ctk.CTkCheckBox(painel, text="Mostrar senha", font=self.main_app.FontBody,
                                            command=mostrar_senha, text_color="white", border_color="white")
        self.MostrarSenha.place(relx=0.5, rely=0.5, anchor="center")

        self.BtEntrar = ctk.CTkButton(painel, text="Entrar", command=self.fazer_login, text_color="black",
                                      fg_color="white", hover_color="gray90")
        self.BtEntrar.place(relx=0.5, rely=0.6, anchor="center")
        self.BtEntrar.bind("<Return>", ativar_enter)

    def fazer_login(self):
        self.usuario_logado = self.LoginDigitado.get()
        self.senha_logado = self.SenhaDigitado.get()

        if len(self.usuario_logado) == 0 or len(self.senha_logado) == 0:
            self.main_app.msgbox("Login", "Preencha todos os campos", 0)
        else:
            cursor = self.conexao.cursor()
            # Utilize placeholders (?) para evitar injecão de SQL
            cursor.execute(
                "SELECT * FROM Usuarios WHERE usuario = ? AND senha = ? AND status = 'ATIVO'",
                (self.usuario_logado, self.senha_logado)
            )
            resultado = cursor.fetchall()

            if resultado:
                cursor.execute("SELECT acesso FROM Usuarios WHERE  usuario = ?", (self.usuario_logado,))
                self.acesso_usuario = cursor.fetchone()[0]

                cursor.execute("SELECT * FROM Modulos WHERE usuario = ?", (self.usuario_logado,))
                self.main_app.ModulosDoUsuario = cursor.fetchall()
                self.main_app.usuario_logado = self.usuario_logado
                self.main_app.acesso_usuario = self.acesso_usuario
                self.main_app.login_sucesso()
            else:
                self.main_app.msgbox("Login", "Login ou senha incorretos, Tente novamente", 0)


class MainApp:

    @staticmethod
    def _conecta_bd(local_bd):

        try:
            # Conectar ao banco de dados
            conexao = sqlite3.connect(local_bd)
            print("Conexão bem-sucedida ao banco de dados")
            return conexao

        except sqlite3.Error as erro:
            print("Erro ao conectar-se ao banco de dados:", erro)
            return None

    def __init__(self, root_main):
        self.root = root_main
        self.root.title("SYS Comercial")
        self.root.geometry(f"400x430")
        self.root.protocol("WM_DELETE_WINDOW", self.sair)

        self.FontTitle = ctk.CTkFont(size=20, weight="bold")
        self.SubTitle = ctk.CTkFont(size=14, weight="bold")
        self.FontBody = ctk.CTkFont(size=12)

        self.validate_cmd_numeric = root_main.register(self.validate_numeric_input)
        self.validade_cmd_text = root_main.register(self.validate_text_input)

        self.screen_height = self.root.winfo_screenheight()
        self.screen_wedth = self.root.winfo_screenwidth()

        self.themeAtual = load_config(False, localfile=False)
        self.escala_atual = 1.0

        self.ModulosDoUsuario = None

        self.usuario_logado = None

        self.acesso_usuario = None

        self.paste_file = "Banco de dados\db_sys.db"

        self.caminho_banco_de_dados = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.paste_file)

        self.ConexaoPrincipal = MainApp._conecta_bd(self.caminho_banco_de_dados)

        self.login()

    def login(self):
        self.clear_screen()
        self.tela_login = TelaLogin(self.root, self)

    def login_sucesso(self):
        self.clear_screen()

        self.root.configure(fg_color=self.chave_customjson("CTk", "fg_color"))

        self.menu_lateral = MenuOpcoes(self.root, self)
        # self.root.resizable(True, True)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    @staticmethod
    def destacar(lista, botao, cor, fg2="transparent"):
        for valor in lista:
            if valor == botao:
                if cor == "white":
                    botao.configure(fg_color=cor)
                else:
                    botao.configure(fg_color=cor)
            else:
                valor.configure(fg_color=fg2)

    @staticmethod
    def esconder_Janela(menu_lateral):

        largura_janela_atual = menu_lateral.winfo_width()

        if largura_janela_atual > 35:
            menu_lateral.configure(width=28)

        else:
            menu_lateral.configure(width=176)

    def exibir_gerenciarusuarios(self, frame_resposta):
        if self.acesso_usuario == "ADM":
            self.gerenciarusuarios = InterfaceGerenciarUsuarios(self, frame_resp=frame_resposta)
        ctk.set_widget_scaling(self.escala_atual)

    def exibir_novoitem(self, frame_resposta):
        self.interface_Novoitem = InterfaceNovoItem(self, frame_resp=frame_resposta)

    # ctk.set_widget_scaling(self.escala_atual)

    def exibir_novocliente(self, frame_resposta):
        self.interface_NovoUsuario = InterfaceNovoCliente(self, frame_resp=frame_resposta)

    # ctk.set_widget_scaling(self.escala_atual)

    def exibir_novousuario(self, frame_resposta):
        self.interface_NovoUsuario = InterfaceNovoUsuario(self, frame_resp=frame_resposta)
        # ctk.set_widget_scaling(self.escala_atual)

    def exibir_usuario(self, frame_resposta, bt_perfil):
        self.Interface_Usuario = InterfaceUsuario(self, frame_resposta, bt_perfil)
        # ctk.set_widget_scaling(self.escala_atual)

    def exibir_configuracoes(self, frame_resposta):
        self.Interface_Configuracoes = InterfaceConfiguracoes(self, frame_resposta)

    # ctk.set_widget_scaling(self.escala_atual)

    def chave_customjson(self, chave, valor):

        nome_do_pacote = "customtkinter"
        caminho_relativo = f"assets/themes/{self.themeAtual}.json"

        caminho_custom = pkg_resources.resource_filename(nome_do_pacote, caminho_relativo)

        caminho_temas = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/personalizado.JSON")

        try:
            with open(caminho_custom) as arquivo_json:
                data = json.load(arquivo_json)  # Carregue o conteúdo do arquivo JSON
        except Exception as erro:
            print(f"trocando para outro tema, erro json {erro}")
            with open(caminho_temas) as arquivo_json:
                data = json.load(arquivo_json)

        info = data[f"{chave}"][f"{valor}"]
        return info

    @staticmethod
    def msgbox(title, text, style):
        #  Styles:
        #  0 : OK
        #  1 : OK | Cancel
        #  2 : Abort | Retry | Ignore
        #  3 : Yes | No | Cancel 6, 7, 2
        #  4 : Yes | No
        #  5 : Retry | Cancel
        #  6 : Cancel | Try Again | Continue
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    @staticmethod
    def aparencia(new_appearance_mode: str):
        # funcão que altera o modo de aparencia da janela entre light e dark
        ctk.set_appearance_mode(new_appearance_mode)

    def theme(self, new_appearance_mode: str):
        # funcão que altera o modo de aparencia da janela entre light e dark
        if new_appearance_mode.lower() == "personalizado":
            ctk.set_default_color_theme(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/personalizado.JSON"))
        else:
            ctk.set_default_color_theme(new_appearance_mode)

        self.themeAtual = str(new_appearance_mode)
        change_and_save_theme(new_appearance_mode)
        self.login_sucesso()

    def change_scaling_event(self, new_scaling: str):
        try:
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            ctk.set_widget_scaling(new_scaling_float)
            self.escala_atual = new_scaling_float

            if new_scaling in ["110%"]:
                SeuLogo2.configure(size=(100, 100))
            elif new_scaling in ["120%"]:
                SeuLogo2.configure(size=(80, 80))
            else:
                SeuLogo2.configure(size=(130, 130))
        except ExcelIcon as erro:
            print(f"houve um erro ao mudar a escala {erro}")
            pass

    def sair(self):
        resp = self.msgbox("SAIR", "Deseja realmente encerrar o sistema?", 4)
        if resp == 6:
            self.ConexaoPrincipal.close()
            self.root.destroy()

    @staticmethod
    def validate_numeric_input(P, max_length):
        # Verifica se P é vazio ou um número decimal válido
        return P == "" or P.replace(".", "", 1).isdigit() and len(P) <= int(max_length)

    @staticmethod
    def validate_text_input(P, max_length, allow_spaces=True):
        if allow_spaces:
            return P == "" or (isinstance(P, str) and P.replace(" ", "").isalpha() and len(P) <= int(max_length))
        else:
            return P == "" or (isinstance(P, str) and P.isalpha() and len(P) <= int(max_length))


if __name__ == "__main__":
    try:
        ctk.set_default_color_theme(load_config(False, localfile=False))
    except FileNotFoundError:
        ctk.set_default_color_theme(load_config(False, True))

    root = ctk.CTk()
    # root.grid_columnconfigure(1, weight=1)
    # root.grid_columnconfigure((2, 3), weight=0)
    # root.grid_rowconfigure((0, 1), weight=1)

    app = MainApp(root)

    root.mainloop()
