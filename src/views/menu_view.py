from src.views.icones import *
from ..models.carregar_img import CarregarIMG


class InterfaceMenu:

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
