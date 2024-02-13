from src.views.icones import *


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
