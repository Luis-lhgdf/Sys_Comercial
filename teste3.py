import customtkinter as ctk

class App():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.state("zoomed")
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()

        self.FrameCadUsergResposta = ctk.CTkFrame(self.root, fg_color="transparent", width=screen_width, height=screen_height, corner_radius=0)
        self.FrameCadUsergResposta.grid(row=0, column=2)

        Bt_SalvarModulos = ctk.CTkButton(self.FrameCadUsergResposta, text_color=("black", "white"), text="Salvar Alterações",
                                         width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'))
        Bt_SalvarModulos.place(x=900, y=25)

        PainelBotoes = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=50, corner_radius=0, fg_color="transparent")
        PainelBotoes.place(relx=0.02, rely=0.19)

        self.BT_ModuloEstoque = ctk.CTkButton(PainelBotoes, text="Estoque", text_color=("black", "white"), fg_color="transparent",
                                              hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40, width=100, anchor="w",
                                              command=self.Modulo_Estoque)
        self.BT_ModuloEstoque.place(relx=0.0, rely=0.5, anchor="w")

        self.BT_ModuloCadastro = ctk.CTkButton(PainelBotoes, text="Cadastro", text_color=("black", "white"), fg_color="transparent",
                                               hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40, width=100, anchor="w",
                                               command=self.Modulo_Cadastro)
        self.BT_ModuloCadastro.place(relx=0.1, rely=0.5, anchor="w")

        self.BT_ModuloAgenda = ctk.CTkButton(PainelBotoes, text="Agenda", text_color=("black", "white"), fg_color="transparent",
                                             hover_color=("#FFD6D6", "gray17"), corner_radius=0, height=40, width=100, anchor="w",
                                             command=self.Modulo_Agenda)
        self.BT_ModuloAgenda.place(relx=0.2, rely=0.5, anchor="w")

        self.FrameModuloEstoqueResp = None
        self.FrameModuloCadastroResp = None
        self.FrameModuloAgendaResp = None

        self.Destaque_Button(self.BT_ModuloEstoque)
        self.Modulo_Estoque()

        self.root.mainloop()

    def Destaque_Button(self, bt):
        lista_bt = [self.BT_ModuloEstoque, self.BT_ModuloCadastro, self.BT_ModuloAgenda]
        for botao in lista_bt:
            if botao == bt:
                bt.configure(fg_color=("#FFD6D6", "gray17"))
            else:
                botao.configure(fg_color="transparent")

    def Modulo_Estoque(self):
        # Verifica se o frame do módulo Estoque já foi criado
        if self.FrameModuloEstoqueResp is None:
            self.FrameModuloEstoqueResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloEstoqueResp.place(relx=0.02, rely=0.24)

            titulo_entrada = ctk.CTkLabel(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="ENTRADA",
                                          text_color=("black", "white"), height=38, width=200,
                                          fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_entrada.place(relx=0.1, rely=0.03, anchor="center")

            self.Entrada_switch = ctk.CTkSwitch(titulo_entrada, font=ctk.CTkFont(weight="bold"), text="",
                                                onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=45, progress_color="#3DED9D")
            self.Entrada_switch.place(relx=0.94, rely=0.5, anchor="center")
        else:
            # Caso o frame já tenha sido criado, apenas torna-o visível novamente
            self.FrameModuloEstoqueResp.tkraise()

    def Modulo_Cadastro(self):
        # Verifica se o frame do módulo Cadastro já foi criado
        if self.FrameModuloCadastroResp is None:
            self.FrameModuloCadastroResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloCadastroResp.place(relx=0.02, rely=0.24)

            titulo_item = ctk.CTkLabel(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="CAD ITENS",
                                       text_color=("black", "white"), height=38, width=200,
                                       fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_item.place(relx=0.1, rely=0.03, anchor="center")

            self.Item_switch = ctk.CTkSwitch(titulo_item, font=ctk.CTkFont(weight="bold"), text="",
                                             onvalue="liberado", offvalue="bloqueado",
                                             switch_height=25, switch_width=45, progress_color="#3DED9D")
            self.Item_switch.place(relx=0.94, rely=0.5, anchor="center")
        else:
            # Caso o frame já tenha sido criado, apenas torna-o visível novamente
            self.FrameModuloCadastroResp.tkraise()

    def Modulo_Agenda(self):
        # Verifica se o frame do módulo Agenda já foi criado
        if self.FrameModuloAgendaResp is None:
            self.FrameModuloAgendaResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloAgendaResp.place(relx=0.02, rely=0.24)

            titulo_agenda = ctk.CTkLabel(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"), text="AGENDA",
                                         text_color=("black", "white"), height=38, width=200,
                                         fg_color=("white", "gray10"), corner_radius=10, anchor="w")
            titulo_agenda.place(relx=0.1, rely=0.03, anchor="center")

            self.Agenda_switch = ctk.CTkSwitch(titulo_agenda, font=ctk.CTkFont(weight="bold"), text="",
                                               onvalue="liberado", offvalue="bloqueado",
                                               switch_height=25, switch_width=45, progress_color="#3DED9D")
            self.Agenda_switch.place(relx=0.94, rely=0.5, anchor="center")
        else:
            # Caso o frame já tenha sido criado, apenas torna-o visível novamente
            self.FrameModuloAgendaResp.tkraise()

App()
