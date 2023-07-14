import customtkinter as ctk
import ctypes
import mysql.connector 
import customtkinter as ctk
import mysql.connector
from PIL import Image
import os
import ctypes
local  = r'liftam.JSON'
ctk.set_default_color_theme(local)


root = ctk.CTk()
root.geometry("1000x1000")
root.title("Editar Usuários")
titulo = ctk.CTkFont(family='Open Sans', size=14, weight="bold")

def closesys():
    root.destroy()

class app():

    def __init__(self):

        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")  


        self.MenuIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "menu_black.png")),
                                dark_image=Image.open(os.path.join(self.image_path, "menu_light.png")), size=(20, 20))


        self.HomeIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "home_black.png")),
                                dark_image=Image.open(os.path.join(self.image_path, "home_light.png")),  size=(17, 17))


        self.FotoPerfil = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "perfil.jpg")),
                            dark_image=Image.open(os.path.join(self.image_path, "perfil.jpg")), size=(100, 100))


        self.SeuLogo = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "logo1.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "logo1.png")), size=(100, 100))


        self.SeuLogo2 = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "logo2.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "logo2.png")), size=(200, 200))


        self.EstoqueIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "estoque_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "estoque_light.png")), size=(17, 17))

        self.CadastroIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "cadastro_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "cadastro_light.png")),  size=(17, 17))


        self.AgendaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "agenda_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "agenda_light.png")), size=(17, 17))


        self.carteiraIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "carteira_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "carteira_light.png")),  size=(17, 17))


        self.UsuarioIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "usuario_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "usuario_light.png")), size=(17, 17))


        self.ConfiguracoesIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "configuracoes_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "configuracoes_light.png")), size=(17, 17))


        self.EntradaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "entrada_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "entrada_light.png")), size=(17, 17))


        self.SaidaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "saida_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "saida_light.png")), size=(17, 17))


        self.InventarioIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "inventario_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "inventario_light.png")), size=(17, 17))



        self.AdicionarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "adicionar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "adicionar_light.png")), size=(30, 30))


        self.EditarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "editar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "editar_light.png")), size=(30, 30))
        

        self.EditarIcon2 = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "editar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "editar_light.png")), size=(17, 17))
        




        self.ItemIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "item_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "item_light.png")), size=(17, 17))



        self.VisualizarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "visualizar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "visualizar_light.png")), size=(17, 17))


        self.VoltarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "voltar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "voltar_light.png")), size=(30, 30))


        self.FinancasIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "financas_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "financas_light.png")), size=(17, 17))


        self.VendasIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "vendas_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "vendas_light.png")), size=(17, 17))


        self.DespesaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "despesa_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "despesa_light.png")), size=(17, 17))



        self.ReceitaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "receita_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "receita_light.png")), size=(17, 17))


        self.FaturamentoIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "faturamento_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "faturamento_light.png")), size=(17, 17))

        self.GerenciarUserIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "gerenciarUser_black.png")),
                    dark_image=Image.open(os.path.join(self.image_path, "gerenciarUser_light.png")), size=(17, 17))

        self.DeletarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "deletar_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "deletar_light.png")), size=(30, 30))
        

        self.DeletarIcon2 = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "deletar_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "deletar_light.png")), size=(17, 17))
        
        
        self.SalvarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "salvar_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "salvar_light.png")), size=(30, 30))  
        

                
        self.ImagemIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "imagem_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "imagem_light.png")), size=(17, 17))


                    
        self.SenhaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "senha_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "senha_light.png")), size=(17, 17))

        
            
        

        self.perfilIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "perfil.png")),
                    dark_image=Image.open(os.path.join(self.image_path, "perfil.png")), size=(80, 80))
        
        self.inicio()

    def aparencia(self, new_appearance_mode: str):
        # função que altera o modo de aparencia da janela entre ligth e dark
        ctk.set_appearance_mode(new_appearance_mode) 

    def inicio(self):
        root.state("zoomed")
        screen_height = root.winfo_screenheight()
        screen_wedth = root.winfo_screenwidth()


        frame_MenuLateralEsq = ctk.CTkFrame(root, width=176, height=screen_height, corner_radius=0)
        frame_MenuLateralEsq.grid(row=0,column=0)

        frame_OcultarMenu = ctk.CTkFrame(root, width=37, height=screen_height, corner_radius=0, fg_color=("white", "#880016"))
        frame_OcultarMenu.grid(row=0,column=1)
        FrameLateralAtual = frame_OcultarMenu
        BtOcultar = ctk.CTkButton(FrameLateralAtual,text="ocultar", anchor="w", width=23, height=23,  fg_color="transparent")
        BtOcultar.place(x=0,y=1) 



        appearance_mode_optionemenu = ctk.CTkOptionMenu(frame_MenuLateralEsq, width=150, height=30, values=["Dark","light"], command=self.aparencia)
        appearance_mode_optionemenu.place(x=10, y=(screen_height-100))


        self.FrameCadUsergResposta = ctk.CTkFrame(root, fg_color="transparent", width=(screen_wedth), height=screen_height, corner_radius=0)
        self.FrameCadUsergResposta.grid(row=0,column=2)
        

        Painel_NovoUsuario = ctk.CTkButton(self.FrameCadUsergResposta, text="", width=1100, height=90, border_width=3, fg_color="transparent", hover_color=("#FBECEC", "gray14"))
        Painel_NovoUsuario.place(relx=0.02, rely=0.1, anchor="w")

        TituloUsuario = ctk.CTkLabel(Painel_NovoUsuario, text="USUARIO")
        TituloUsuario.place(x=63, y=15)

        EntryUsuario  = ctk.CTkEntry(Painel_NovoUsuario, placeholder_text="Digite aqui:",width=150)
        EntryUsuario.place(x=10, y=45)



        TituloSenha = ctk.CTkLabel(Painel_NovoUsuario, text="SENHA")
        TituloSenha.place(x=265, y=15)
        EntrySenha  = ctk.CTkEntry(Painel_NovoUsuario, placeholder_text="Digite aqui:",width=150)
        EntryUsuario.place(x=10, y=45)
        EntrySenha.place(x=210, y=45)


        TituloAcesso = ctk.CTkLabel(Painel_NovoUsuario, text="ACESSO")
        TituloAcesso.place(x=465, y=15)
        MenuAcesso = ctk.CTkOptionMenu(self.FrameCadUsergResposta, values=("Usuario", "Adm"),width=150)
        MenuAcesso.place(x=440, y=77)


        TituloStatus = ctk.CTkLabel(Painel_NovoUsuario, text="STATUS")
        TituloStatus.place(x=665, y=15)
        MenuStatus = ctk.CTkOptionMenu(self.FrameCadUsergResposta, values=("Ativo", "Desativado"),width=150)
        MenuStatus.place(x=640, y=77)



        PainelBotoes = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=50, corner_radius=0, fg_color="transparent")
        PainelBotoes.place(relx=0.02, rely=0.19)
       



        self.BT_ModuloEstoque =ctk.CTkButton(PainelBotoes, image=self.EstoqueIcon, text="Estoque",text_color=("black", "white"), fg_color="transparent", 
                                             hover_color=("#FFD6D6", "gray17"),  corner_radius=0, height=40,width=100, anchor="w", command=self.Modulo_Estoque)
        self.BT_ModuloEstoque.place(relx=0.0, rely=0.5, anchor="w", )


        self.BT_ModuloCadastro =ctk.CTkButton(PainelBotoes, image=self.CadastroIcon, text="Cadastro",text_color=("black", "white"), fg_color="transparent", 
                                             hover_color=("#FFD6D6", "gray17"),  corner_radius=0, height=40,width=100, anchor="w", command=self.Modulo_Cadastro)
        self.BT_ModuloCadastro.place(relx=0.1, rely=0.5, anchor="w", )



        self.BT_ModuloAgenda =ctk.CTkButton(PainelBotoes, image=self.AgendaIcon, text="Agenda",text_color=("black", "white"), fg_color="transparent", 
                                             hover_color=("#FFD6D6", "gray17"),  corner_radius=0, height=40,width=100, anchor="w", command=self.Modulo_Agenda)
        self.BT_ModuloAgenda.place(relx=0.2, rely=0.5, anchor="w", )


        self.BT_ModuloCarteira =ctk.CTkButton(PainelBotoes, image=self.carteiraIcon, text="Carteira",text_color=("black", "white"), fg_color="transparent", 
                                             hover_color=("#FFD6D6", "gray17"),  corner_radius=0, height=40,width=100, anchor="w", command=self.Modulo_Carteira)
        self.BT_ModuloCarteira.place(relx=0.3, rely=0.5, anchor="w", )


        self.BT_ModuloFinancas =ctk.CTkButton(PainelBotoes, image=self.FinancasIcon, text="Finanças",text_color=("black", "white"), fg_color="transparent", 
                                             hover_color=("#FFD6D6", "gray17"),  corner_radius=0, height=40,width=100, anchor="w", command=self.Modulo_Financas)
        self.BT_ModuloFinancas.place(relx=0.4, rely=0.5, anchor="w", )


        self.BT_ModuloUsuarios =ctk.CTkButton(PainelBotoes, image=self.UsuarioIcon, text="Usuarios",text_color=("black", "white"), fg_color="transparent", 
                                             hover_color=("#FFD6D6", "gray17"),  corner_radius=0, height=40,width=100, anchor="w", command=self.Modulo_Usuario)
        self.BT_ModuloUsuarios.place(relx=0.5, rely=0.5, anchor="w", )


        self.BT_ModuloConfiguracoes =ctk.CTkButton(PainelBotoes, image=self.ConfiguracoesIcon, text="Configurações",text_color=("black", "white"), fg_color="transparent", 
                                             hover_color=("#FFD6D6", "gray17"),  corner_radius=0, height=40,width=100, anchor="w", command=self.Modulo_Configuracoes)
        self.BT_ModuloConfiguracoes.place(relx=0.6, rely=0.5, anchor="w", )




        FrameModuloResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
        FrameModuloResp.place(relx=0.02, rely=0.24)
        self.FrameModuloAtual = FrameModuloResp
    
    def Destaque_Button(self, bt):
        lista_bt = [self.BT_ModuloEstoque, self.BT_ModuloCadastro,  self.BT_ModuloAgenda,  
                    self.BT_ModuloCarteira,  self.BT_ModuloFinancas, self.BT_ModuloUsuarios, self.BT_ModuloConfiguracoes]
        
        for botao in lista_bt:
            if botao == bt:
                bt.configure(fg_color=("#FFD6D6", "gray17"))
            else:
                botao.configure(fg_color="transparent")

    def Modulo_Estoque(self):
       
        self.FrameModuloAtual.destroy()

        FrameModuloEstoqueResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
        FrameModuloEstoqueResp.place(relx=0.02, rely=0.24)
        self.FrameModuloAtual = FrameModuloEstoqueResp




 

        titulo_entrada = ctk.CTkLabel(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="ENTRADA",
                                    text_color=("black","white"), height=30, width=200, fg_color=("white", "gray10"),
                                    corner_radius=6, anchor="w")
        titulo_entrada.place(relx=0.1, rely=0.03, anchor="center")

        Entrada_switch = ctk.CTkSwitch(titulo_entrada, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",
                                    offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D",state="normal",command=lambda: self.ativarswitchp(Entrada_switch))
        Entrada_switch.place(relx=0.95, rely=0.5, anchor="center")

        Entrada_visualizar = ctk.CTkSwitch(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        Entrada_visualizar.place(x=10, y=50)


        Entrada_novo = ctk.CTkSwitch(FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        Entrada_novo.place(x=10, y=80)


        Entrada_editar = ctk.CTkSwitch(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        Entrada_editar.place(x=10, y=110)


        Entrada_remover = ctk.CTkSwitch(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        Entrada_remover.place(x=10, y=140)





        titulo_saida = ctk.CTkLabel(FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="SAIDA",  text_color=("black","white"),height=30, width=200, fg_color=("white", "gray10"), corner_radius=6, anchor="w")
        titulo_saida.place(relx=0.36, rely=0.03, anchor="center")
        saida_switch = ctk.CTkSwitch(titulo_entrada,  font=ctk.CTkFont(weight="bold"),text="",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D")
        saida_switch.place(relx=0.95, rely=0.5, anchor="center")


        saida_visualizar = ctk.CTkSwitch(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        saida_visualizar.place(x=300, y=50)


        saida_novo = ctk.CTkSwitch(FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        saida_novo.place(x=300, y=80)


        saida_editar = ctk.CTkSwitch(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        saida_editar.place(x=300, y=110)


        saida_remover = ctk.CTkSwitch(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        saida_remover.place(x=300, y=140)



        
        titulo_inventario = ctk.CTkLabel(FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="INVENTARIO",  text_color=("black","white"),height=30, width=200, fg_color=("white", "gray10"), corner_radius=6, anchor="w")
        titulo_inventario.place(relx=0.632, rely=0.03, anchor="center")
        inventario_switch = ctk.CTkSwitch(titulo_entrada,  font=ctk.CTkFont(weight="bold"),text="",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D")
        inventario_switch.place(relx=0.95, rely=0.5, anchor="center")


        inventario_visualizar = ctk.CTkSwitch(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        inventario_visualizar.place(x=600, y=50)


        inventario_novo = ctk.CTkSwitch(FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        inventario_novo.place(x=600, y=80)


        inventario_editar = ctk.CTkSwitch(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        inventario_editar.place(x=600, y=110)


        inventario_remover = ctk.CTkSwitch(FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
        inventario_remover.place(x=600, y=140)







    def ativarswitchp(self):
        print("função chamada")


        



        self.Destaque_Button(self.BT_ModuloEstoque)
     
    def Modulo_Cadastro(self):
       
        self.FrameModuloAtual.destroy()

        FrameModuloCadastroResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
        FrameModuloCadastroResp.place(relx=0.02, rely=0.24)
        self.FrameModuloAtual = FrameModuloCadastroResp


        self.Destaque_Button(self.BT_ModuloCadastro)

    def Modulo_Agenda(self):
       
        self.FrameModuloAtual.destroy()

        FrameModuloAgendaResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
        FrameModuloAgendaResp.place(relx=0.02, rely=0.24)

        self.FrameModuloAtual = FrameModuloAgendaResp


        self.Destaque_Button(self.BT_ModuloAgenda)

    def Modulo_Carteira(self):
       
        self.FrameModuloAtual.destroy()

        FrameModuloCarteiraResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
        FrameModuloCarteiraResp.place(relx=0.02, rely=0.24)

        self.FrameModuloAtual = FrameModuloCarteiraResp


        self.Destaque_Button(self.BT_ModuloCarteira)

    def Modulo_Financas(self):
       
        self.FrameModuloAtual.destroy()

        FrameModuloFinancasResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
        FrameModuloFinancasResp.place(relx=0.02, rely=0.24)

        self.FrameModuloAtual = FrameModuloFinancasResp


        self.Destaque_Button(self.BT_ModuloFinancas)

    def Modulo_Usuario(self):
       
        self.FrameModuloAtual.destroy()

        FrameModuloUsuarioResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
        FrameModuloUsuarioResp.place(relx=0.02, rely=0.24)

        self.FrameModuloAtual = FrameModuloUsuarioResp


        self.Destaque_Button(self.BT_ModuloUsuarios)

    def Modulo_Configuracoes(self):
       
        self.FrameModuloAtual.destroy()

        FrameModuloConfiguracoesResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
        FrameModuloConfiguracoesResp.place(relx=0.02, rely=0.24)


        self.FrameModuloAtual = FrameModuloConfiguracoesResp


        self.Destaque_Button(self.BT_ModuloConfiguracoes)

app()
root.protocol("WM_DELETE_WINDOW", closesys)
root.mainloop()
