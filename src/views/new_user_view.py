from src.views.icones import *


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
