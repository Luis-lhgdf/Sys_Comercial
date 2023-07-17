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

import mysql.connector
database = 'railway'
host = 'containers-us-west-1.railway.app'
port = 5474
user = 'root'
password = 'JThLpvacyDNwzFLPyLhX'

# Crie a conexão
conexaoBD = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)

root = ctk.CTk()
root.geometry("1000x1000")
root.title("Editar Usuários")
titulo = ctk.CTkFont(family='Open Sans', size=14, weight="bold")
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

        self.EntryUsuario  = ctk.CTkEntry(Painel_NovoUsuario, placeholder_text="Digite aqui:",width=150)
        self.EntryUsuario.place(x=10, y=45)



        TituloSenha = ctk.CTkLabel(Painel_NovoUsuario, text="SENHA")
        TituloSenha.place(x=265, y=15)

        self.EntrySenha  = ctk.CTkEntry(Painel_NovoUsuario, placeholder_text="Digite aqui:",width=150)
        self.EntrySenha.place(x=210, y=45)


        TituloAcesso = ctk.CTkLabel(Painel_NovoUsuario, text="ACESSO")
        TituloAcesso.place(x=465, y=15)
        self.MenuAcesso = ctk.CTkOptionMenu(Painel_NovoUsuario, values=("Usuario", "Adm"),width=150)
        self.MenuAcesso.place(x=410, y=45)




        TituloStatus = ctk.CTkLabel(Painel_NovoUsuario, text="STATUS")
        TituloStatus.place(x=663, y=15)
        self.MenuStatus = ctk.CTkOptionMenu(Painel_NovoUsuario, values=("Ativo", "Desativado"),width=150)
        self.MenuStatus.place(x=610, y=45)


        self.Bt_SalvarModulos = ctk.CTkButton(Painel_NovoUsuario, image=self.SalvarIcon, text_color=("black","white"), text="Salvar Alterações",
                                        width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=self.SalvarGetSwitch)
        self.Bt_SalvarModulos.place(x=900, y=25)




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


        self.FrameModuloEstoqueResp = None
        self.FrameModuloCadastroResp = None
        self.FrameModuloAgendaResp = None
        self.FrameModuloCarteiraResp = None
        self.FrameModuloFinancasResp = None
        self.FrameModuloUsuarioResp = None
        self.FrameModuloConfiguracoesResp = None
    
    def Destaque_Button(self, bt):
        lista_bt = [self.BT_ModuloEstoque, self.BT_ModuloCadastro,  self.BT_ModuloAgenda,  
                    self.BT_ModuloCarteira,  self.BT_ModuloFinancas, self.BT_ModuloUsuarios, self.BT_ModuloConfiguracoes]
        
        for botao in lista_bt:
            if botao == bt:
                bt.configure(fg_color=("#FFD6D6", "gray17"))
            else:
                botao.configure(fg_color="transparent")

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
                print(valor)
        except Exception as erro:
            print(erro)

            pass    

    def SalvarGetSwitch(self):
        resp = msgbox("SALVAR", "Deseja salvar as alterações nos módulos?", 4)
        try:
            if resp == 6:
                login_digitado = self.EntryUsuario.get()
                senha_digitada = self.EntrySenha.get()
                acesso = self.MenuAcesso.get()
                status = self.MenuStatus.get()


    

                if len(login_digitado) <=2:
                    msgbox("USUARIO", "Nome de usuario deve conter pelo menos 3 caracteres", 0)
                elif len(senha_digitada) <=5:
                    msgbox("SENHA", "Sua senha deve ter no minimo 6 caracteres", 0)
                else:
                        
                    cursor = conexaoBD.cursor()
                    cursor.execute(f"SELECT usuario FROM Usuarios where binary usuario = '{login_digitado}'")
                    resp = cursor.fetchall()
                    if resp:
                        msgbox("USUARIO", "Ja existe um usuario com este nome, por favor escolha outro", 0)
                    else:

                        modules = {
                            "Estoque": {
                                "ENTRADA": {
                                    "visualizar": "bloqueado" if not hasattr(self, "Entrada_visualizar") else self.Entrada_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "Entrada_novo") else self.Entrada_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "Entrada_editar") else self.Entrada_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "Entrada_remover") else self.Entrada_remover.get()
                                },
                                "SAIDA": {
                                    "visualizar": "bloqueado" if not hasattr(self, "saida_visualizar") else self.saida_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "saida_novo") else self.saida_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "saida_editar") else self.saida_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "saida_remover") else self.saida_remover.get()
                                },
                                "INVENTARIO": {
                                    "visualizar": "bloqueado" if not hasattr(self, "inventario_visualizar") else self.inventario_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "inventario_novo") else self.inventario_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "inventario_editar") else self.inventario_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "inventario_remover") else self.inventario_remover.get()
                                }
                            },
                            "Cadastro": {
                                "CAD ITEM": {
                                    "visualizar": "bloqueado" if not hasattr(self, "item_visualizar") else self.item_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "item_novo") else self.item_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "item_editar") else self.item_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "item_remover") else self.item_remover.get()
                                },
                                "CAD CLIENTE": {
                                    "visualizar": "bloqueado" if not hasattr(self, "cliente_visualizar") else self.cliente_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "cliente_novo") else self.cliente_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "cliente_editar") else self.cliente_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "cliente_remover") else self.cliente_remover.get()
                                },
                                "CAD USUARIO": {
                                    "visualizar": "bloqueado" if not hasattr(self, "criarusuario_visualizar") else self.criarusuario_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "criarusuario_novo") else self.criarusuario_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "criarusuario_editar") else self.criarusuario_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "criarusuario_remover") else self.criarusuario_remover.get()
                                },
                                "GERENCIAR USER": {
                                    "visualizar": "bloqueado" if not hasattr(self, "gerenciar_visualizar") else self.gerenciar_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "gerenciar_novo") else self.gerenciar_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "gerenciar_editar") else self.gerenciar_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "gerenciar_remover") else self.gerenciar_remover.get()
                                },

                                
                            },
                            "Agenda": {
                                "AGENDA": {
                                    "visualizar": "bloqueado" if not hasattr(self, "agenda_visualizar") else self.agenda_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "agenda_novo") else self.agenda_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "agenda_editar") else self.agenda_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "agenda_remover") else self.agenda_remover.get()
                                }
                            },
                            "Carteira": {
                                "VENDAS": {
                                    "visualizar": "bloqueado" if not hasattr(self, "vendas_visualizar") else self.vendas_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "vendas_novo") else self.vendas_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "vendas_editar") else self.vendas_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "vendas_remover") else self.vendas_remover.get()
                                },
                                "FATURAMENTO": {
                                    "visualizar": "bloqueado" if not hasattr(self, "faturamento_visualizar") else self.faturamento_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "faturamento_novo") else self.faturamento_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "faturamento_editar") else self.faturamento_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "faturamento_remover") else self.faturamento_remover.get()
                                }
                            },
                            "Finanças": {
                                "DESPESAS": {
                                    "visualizar": "bloqueado" if not hasattr(self, "despesas_visualizar") else self.despesas_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "despesas_novo") else self.despesas_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "despesas_editar") else self.despesas_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "despesas_remover") else self.despesas_remover.get()
                                },
                                "OUTRAS RENDAS": {
                                    "visualizar": "bloqueado" if not hasattr(self, "rendas_visualizar") else self.rendas_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "rendas_novo") else self.rendas_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "rendas_editar") else self.rendas_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "rendas_remover") else self.rendas_remover.get()
                                }
                            },
                            "Usuario": {
                                "USUARIO": {
                                    "visualizar": "bloqueado" if not hasattr(self, "usuario_visualizar") else self.usuario_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "usuario_novo") else self.usuario_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "usuario_editar") else self.usuario_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "usuario_remover") else self.usuario_remover.get()
                                }
                            },
                            "Configurações": {
                                "CONFIGURACOES": {
                                    "visualizar": "bloqueado" if not hasattr(self, "configuracoes_visualizar") else self.configuracoes_visualizar.get(),
                                    "novo": "bloqueado" if not hasattr(self, "configuracoes_novo") else self.configuracoes_novo.get(),
                                    "editar": "bloqueado" if not hasattr(self, "configuracoes_editar") else self.configuracoes_editar.get(),
                                    "remover": "bloqueado" if not hasattr(self, "configuracoes_remover") else self.configuracoes_remover.get()
                                }
                            }
                        }

                        cursor = conexaoBD.cursor()

                        cursor.execute("""INSERT INTO Usuarios(usuario, senha, acesso, status)
                                       VALUES(%s, %s, %s, %s )""", (login_digitado, senha_digitada, acesso, status))
                        conexaoBD.commit()
                        
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
                        conexaoBD.commit()
                        

                        # Fecha a conexão
                        conexaoBD.close()
                        self.inicio()
                        msgbox("SALVAR", "Usuario criado com sucesso!!!", 0)
        except Exception as erro:
            print(erro)
            
    def Modulo_Estoque(self):
       
        if self.FrameModuloEstoqueResp is None:

            self.FrameModuloEstoqueResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloEstoqueResp.place(relx=0.02, rely=0.24)
            

            self.Destaque_Button(self.BT_ModuloEstoque)

    

            titulo_entrada = ctk.CTkLabel(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="ENTRADA",text_color=("black","white"), height=38, width=200,
                                        fg_color=("white", "gray10"),corner_radius=10, anchor="w")
            titulo_entrada.place(relx=0.1, rely=0.03, anchor="center")

            Entrada_switch = ctk.CTkSwitch(titulo_entrada, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(Entrada_switch, self.Entrada_visualizar, self.Entrada_novo, self.Entrada_editar, self.Entrada_remover))
            Entrada_switch.place(relx=0.94, rely=0.5, anchor="center")




            self.Entrada_visualizar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.Entrada_visualizar.place(x=10, y=50)



            self.Entrada_novo = ctk.CTkSwitch(self.FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.Entrada_novo.place(x=10, y=80)


            self.Entrada_editar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.Entrada_editar.place(x=10, y=110)


            self.Entrada_remover = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.Entrada_remover.place(x=10, y=140)


            #____________________________________________________________________________________________________________________________________________________________________________________


            titulo_saida = ctk.CTkLabel(self.FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="SAIDA",  text_color=("black","white"),height=38, width=200, 
                                        fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_saida.place(relx=0.36, rely=0.03, anchor="center")

            saida_switch = ctk.CTkSwitch(titulo_saida,  font=ctk.CTkFont(weight="bold"),text="",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(saida_switch, self.saida_visualizar, self.saida_novo, self.saida_editar, self.saida_remover))
            saida_switch.place(relx=0.94, rely=0.5, anchor="center")


            self.saida_visualizar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.saida_visualizar.place(x=300, y=50)


            self.saida_novo = ctk.CTkSwitch(self.FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado",
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.saida_novo.place(x=300, y=80)


            self.saida_editar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.saida_editar.place(x=300, y=110)


            self.saida_remover = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado",
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.saida_remover.place(x=300, y=140)


            #________________________________________________________________________________________________________________________________________-

            
            titulo_inventario = ctk.CTkLabel(self.FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="INVENTARIO",  text_color=("black","white"),height=38, width=200, 
                                            fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_inventario.place(relx=0.632, rely=0.03, anchor="center")
            
            inventario_switch = ctk.CTkSwitch(titulo_inventario,  font=ctk.CTkFont(weight="bold"),text="",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=45, progress_color="#3DED9D", 
                                            command=lambda: self.AtivarSwitch(inventario_switch, self.inventario_visualizar, self.inventario_novo, self.inventario_editar, self.inventario_remover))
            inventario_switch.place(relx=0.94, rely=0.5, anchor="center")


            self.inventario_visualizar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.inventario_visualizar.place(x=600, y=50)


            self.inventario_novo = ctk.CTkSwitch(self.FrameModuloEstoqueResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.inventario_novo.place(x=600, y=80)


            self.inventario_editar = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.inventario_editar.place(x=600, y=110)


            self.inventario_remover = ctk.CTkSwitch(self.FrameModuloEstoqueResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.inventario_remover.place(x=600, y=140)
        else:
            self.FrameModuloEstoqueResp.tkraise()
            self.Destaque_Button(self.BT_ModuloEstoque)

    def Modulo_Cadastro(self):
       
        if self.FrameModuloCadastroResp is None:

            self.FrameModuloCadastroResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloCadastroResp.place(relx=0.02, rely=0.24)
            
            self.Destaque_Button(self.BT_ModuloCadastro)

            
            titulo_item = ctk.CTkLabel(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="CAD ITENS",text_color=("black","white"), height=38, width=200,
                                        fg_color=("white", "gray10"),corner_radius=10, anchor="w")
            titulo_item.place(relx=0.1, rely=0.03, anchor="center")

            item_switch = ctk.CTkSwitch(titulo_item, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(item_switch, self.item_visualizar, self.item_novo, self.item_editar, self.item_remover))
            item_switch.place(relx=0.94, rely=0.5, anchor="center")




            self.item_visualizar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.item_visualizar.place(x=10, y=50)



            self.item_novo = ctk.CTkSwitch(self.FrameModuloCadastroResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.item_novo.place(x=10, y=80)


            self.item_editar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.item_editar.place(x=10, y=110)


            self.item_remover = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.item_remover.place(x=10, y=140)


            #____________________________________________________________________________________________________________________________________________________________________________________


            titulo_cliente = ctk.CTkLabel(self.FrameModuloCadastroResp,  font=ctk.CTkFont(weight="bold"),text="CAD CLIENTES",  text_color=("black","white"),height=38, width=200, 
                                        fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_cliente.place(relx=0.36, rely=0.03, anchor="center")

            cliente_switch = ctk.CTkSwitch(titulo_cliente,  font=ctk.CTkFont(weight="bold"),text="",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(cliente_switch, self.cliente_visualizar, self.cliente_novo, self.cliente_editar, self.cliente_remover))
            cliente_switch.place(relx=0.94, rely=0.5, anchor="center")


            self.cliente_visualizar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.cliente_visualizar.place(x=300, y=50)


            self.cliente_novo = ctk.CTkSwitch(self.FrameModuloCadastroResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado",
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.cliente_novo.place(x=300, y=80)


            self.cliente_editar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.cliente_editar.place(x=300, y=110)


            self.cliente_remover = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado",
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.cliente_remover.place(x=300, y=140)


            #________________________________________________________________________________________________________________________________________-

            
            titulo_criarusuario = ctk.CTkLabel(self.FrameModuloCadastroResp,  font=ctk.CTkFont(weight="bold"),text="CAD USUARIO",  text_color=("black","white"),height=38, width=200, 
                                            fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_criarusuario.place(relx=0.632, rely=0.03, anchor="center")
            
            criarusuario_switch = ctk.CTkSwitch(titulo_criarusuario,  font=ctk.CTkFont(weight="bold"),text="",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=45, progress_color="#3DED9D", 
                                            command=lambda: self.AtivarSwitch(criarusuario_switch, self.criarusuario_visualizar, self.criarusuario_novo, self.criarusuario_editar, self.criarusuario_remover))
            criarusuario_switch.place(relx=0.94, rely=0.5, anchor="center")


            self.criarusuario_visualizar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.criarusuario_visualizar.place(x=600, y=50)


            self.criarusuario_novo = ctk.CTkSwitch(self.FrameModuloCadastroResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.criarusuario_novo.place(x=600, y=80)


            self.criarusuario_editar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.criarusuario_editar.place(x=600, y=110)


            self.criarusuario_remover = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.criarusuario_remover.place(x=600, y=140)


            #________________________________________________________________________________________________________________________________________-

            
            titulo_gerenciarUser = ctk.CTkLabel(self.FrameModuloCadastroResp,  font=ctk.CTkFont(weight="bold"),text="GERENCIAR USER",  text_color=("black","white"),height=38, width=200, 
                                            fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_gerenciarUser.place(relx=0.1, rely=0.26, anchor="center")
            
            gerenciar_switch = ctk.CTkSwitch(titulo_gerenciarUser,  font=ctk.CTkFont(weight="bold"),text="",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=45, progress_color="#3DED9D", 
                                            command=lambda: self.AtivarSwitch(gerenciar_switch, self.gerenciar_visualizar, self.gerenciar_novo, self.gerenciar_editar, self.gerenciar_remover))
            gerenciar_switch.place(relx=0.94, rely=0.5, anchor="center")


            self.gerenciar_visualizar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.gerenciar_visualizar.place(x=10, y=260)


            self.gerenciar_novo = ctk.CTkSwitch(self.FrameModuloCadastroResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.gerenciar_novo.place(x=10, y=290)


            self.gerenciar_editar = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.gerenciar_editar.place(x=10, y=320)


            self.gerenciar_remover = ctk.CTkSwitch(self.FrameModuloCadastroResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.gerenciar_remover.place(x=10, y=350)
        else:
             self.FrameModuloCadastroResp.tkraise()
             self.Destaque_Button(self.BT_ModuloCadastro)
    
    def Modulo_Agenda(self):
       
        if self.FrameModuloAgendaResp is None:

            self.FrameModuloAgendaResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloAgendaResp.place(relx=0.02, rely=0.24)
           
            self.Destaque_Button(self.BT_ModuloAgenda)



            titulo_agenda = ctk.CTkLabel(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"), text="AGENDA",text_color=("black","white"), height=38, width=200,
                                        fg_color=("white", "gray10"),corner_radius=10, anchor="w")
            titulo_agenda.place(relx=0.1, rely=0.03, anchor="center")

            agenda_switch = ctk.CTkSwitch(titulo_agenda, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(agenda_switch, self.agenda_visualizar, self.agenda_novo, self.agenda_editar, self.agenda_remover))
            agenda_switch.place(relx=0.94, rely=0.5, anchor="center")



            self.agenda_visualizar = ctk.CTkSwitch(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.agenda_visualizar.place(x=10, y=50)



            self.agenda_novo = ctk.CTkSwitch(self.FrameModuloAgendaResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.agenda_novo.place(x=10, y=80)


            self.agenda_editar = ctk.CTkSwitch(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.agenda_editar.place(x=10, y=110)


            self.agenda_remover = ctk.CTkSwitch(self.FrameModuloAgendaResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.agenda_remover.place(x=10, y=140)
        else:
            self.FrameModuloAgendaResp.tkraise()
            self.Destaque_Button(self.BT_ModuloAgenda)

    def Modulo_Carteira(self):
       
       
        if self.FrameModuloCarteiraResp is None:

            self.FrameModuloCarteiraResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloCarteiraResp.place(relx=0.02, rely=0.24)
        
            self.Destaque_Button(self.BT_ModuloCarteira)



            titulo_vendas = ctk.CTkLabel(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="VENDAS",text_color=("black","white"), height=38, width=200,
                                        fg_color=("white", "gray10"),corner_radius=10, anchor="w")
            titulo_vendas.place(relx=0.1, rely=0.03, anchor="center")

            vendas_switch = ctk.CTkSwitch(titulo_vendas, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(vendas_switch, self.vendas_visualizar, self.vendas_novo, self.vendas_editar, self.vendas_remover))
            vendas_switch.place(relx=0.94, rely=0.5, anchor="center")




            self.vendas_visualizar = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.vendas_visualizar.place(x=10, y=50)



            self.vendas_novo = ctk.CTkSwitch(self.FrameModuloCarteiraResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.vendas_novo.place(x=10, y=80)


            self.vendas_editar = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.vendas_editar.place(x=10, y=110)


            self.vendas_remover = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.vendas_remover.place(x=10, y=140)


            #____________________________________________________________________________________________________________________________________________________________________________________


            titulo_faturamento = ctk.CTkLabel(self.FrameModuloCarteiraResp,  font=ctk.CTkFont(weight="bold"),text="FATURAMENTO",  text_color=("black","white"),height=38, width=200, 
                                        fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_faturamento.place(relx=0.36, rely=0.03, anchor="center")

            faturamento_switch = ctk.CTkSwitch(titulo_faturamento,  font=ctk.CTkFont(weight="bold"),text="",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(faturamento_switch, self.faturamento_visualizar, self.faturamento_novo, self.faturamento_editar, self.faturamento_remover))
            faturamento_switch.place(relx=0.94, rely=0.5, anchor="center")


            self.faturamento_visualizar = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.faturamento_visualizar.place(x=300, y=50)


            self.faturamento_novo = ctk.CTkSwitch(self.FrameModuloCarteiraResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado",
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.faturamento_novo.place(x=300, y=80)


            self.faturamento_editar = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.faturamento_editar.place(x=300, y=110)


            self.faturamento_remover = ctk.CTkSwitch(self.FrameModuloCarteiraResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado",
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.faturamento_remover.place(x=300, y=140)
        else:
            self.FrameModuloCarteiraResp.tkraise()
            self.Destaque_Button(self.BT_ModuloCarteira)

    def Modulo_Financas(self):

        if self.FrameModuloFinancasResp is None:
            
            self.FrameModuloFinancasResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloFinancasResp.place(relx=0.02, rely=0.24)

            self.Destaque_Button(self.BT_ModuloFinancas)


            titulo_despesas = ctk.CTkLabel(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"), text="DESPESAS",text_color=("black","white"), height=38, width=200,
                                        fg_color=("white", "gray10"),corner_radius=10, anchor="w")
            titulo_despesas.place(relx=0.1, rely=0.03, anchor="center")

            despesas_switch = ctk.CTkSwitch(titulo_despesas, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(despesas_switch, self.despesas_visualizar, self.despesas_novo, self.despesas_editar, self.despesas_remover))
            despesas_switch.place(relx=0.94, rely=0.5, anchor="center")




            self.despesas_visualizar = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.despesas_visualizar.place(x=10, y=50)



            self.despesas_novo = ctk.CTkSwitch(self.FrameModuloFinancasResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.despesas_novo.place(x=10, y=80)


            self.despesas_editar = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.despesas_editar.place(x=10, y=110)


            self.despesas_remover = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.despesas_remover.place(x=10, y=140)


            #____________________________________________________________________________________________________________________________________________________________________________________


            titulo_rendas = ctk.CTkLabel(self.FrameModuloFinancasResp,  font=ctk.CTkFont(weight="bold"),text="OUTRAS RENDAS",  text_color=("black","white"),height=38, width=200, 
                                        fg_color=("white", "gray10"), corner_radius=6, anchor="w")
            titulo_rendas.place(relx=0.36, rely=0.03, anchor="center")

            rendas_switch = ctk.CTkSwitch(titulo_rendas,  font=ctk.CTkFont(weight="bold"),text="",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(rendas_switch, self.rendas_visualizar, self.rendas_novo, self.rendas_editar, self.rendas_remover))
            rendas_switch.place(relx=0.94, rely=0.5, anchor="center")


            self.rendas_visualizar = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.rendas_visualizar.place(x=300, y=50)


            self.rendas_novo = ctk.CTkSwitch(self.FrameModuloFinancasResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado",
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.rendas_novo.place(x=300, y=80)


            self.rendas_editar = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.rendas_editar.place(x=300, y=110)


            self.rendas_remover = ctk.CTkSwitch(self.FrameModuloFinancasResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado",
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.rendas_remover.place(x=300, y=140)

        else:
            self.FrameModuloFinancasResp.tkraise()
            self.Destaque_Button(self.BT_ModuloFinancas)

    def Modulo_Usuario(self):
       
        if self.FrameModuloUsuarioResp is None:
            self.FrameModuloUsuarioResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloUsuarioResp.place(relx=0.02, rely=0.24)

            
            self.Destaque_Button(self.BT_ModuloUsuarios)





            titulo_usuario = ctk.CTkLabel(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"), text="USUARIO",text_color=("black","white"), height=38, width=200,
                                        fg_color=("white", "gray10"),corner_radius=10, anchor="w")
            titulo_usuario.place(relx=0.1, rely=0.03, anchor="center")

            usuario_switch = ctk.CTkSwitch(titulo_usuario, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(usuario_switch, self.usuario_visualizar, self.usuario_novo, self.usuario_editar, self.usuario_remover))
            usuario_switch.place(relx=0.94, rely=0.5, anchor="center")




            self.usuario_visualizar = ctk.CTkSwitch(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.usuario_visualizar.place(x=10, y=50)



            self.usuario_novo = ctk.CTkSwitch(self.FrameModuloUsuarioResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.usuario_novo.place(x=10, y=80)


            self.usuario_editar = ctk.CTkSwitch(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.usuario_editar.place(x=10, y=110)


            self.usuario_remover = ctk.CTkSwitch(self.FrameModuloUsuarioResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.usuario_remover.place(x=10, y=140)
        else:
            self.FrameModuloUsuarioResp.tkraise()
            self.Destaque_Button(self.BT_ModuloUsuarios)

    def Modulo_Configuracoes(self):
       
        if self.FrameModuloConfiguracoesResp is None:

            self.FrameModuloConfiguracoesResp = ctk.CTkFrame(self.FrameCadUsergResposta, width=1100, height=900, corner_radius=0)
            self.FrameModuloConfiguracoesResp.place(relx=0.02, rely=0.24)

        
            self.Destaque_Button(self.BT_ModuloConfiguracoes)




            titulo_configuracoes = ctk.CTkLabel(self.FrameModuloConfiguracoesResp, font=ctk.CTkFont(weight="bold"), text="CONFIGURAÇÕES",text_color=("black","white"), height=38, width=200,
                                        fg_color=("white", "gray10"),corner_radius=10, anchor="w")
            titulo_configuracoes.place(relx=0.1, rely=0.03, anchor="center")

            configuracoes_switch = ctk.CTkSwitch(titulo_configuracoes, font=ctk.CTkFont(weight="bold"), text="", onvalue="liberado",offvalue="bloqueado", 
                                        switch_height=25, switch_width=45, progress_color="#3DED9D",
                                        command=lambda: self.AtivarSwitch(configuracoes_switch, self.configuracoes_visualizar, self.configuracoes_novo, self.configuracoes_editar, self.configuracoes_remover))
            configuracoes_switch.place(relx=0.94, rely=0.5, anchor="center")




            self.configuracoes_visualizar = ctk.CTkSwitch(self.FrameModuloConfiguracoesResp, font=ctk.CTkFont(weight="bold"), text="Visualizar",onvalue="liberado", offvalue="bloqueado",
                                                switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.configuracoes_visualizar.place(x=10, y=50)



            self.configuracoes_novo = ctk.CTkSwitch(self.FrameModuloConfiguracoesResp,  font=ctk.CTkFont(weight="bold"),text="Novo",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.configuracoes_novo.place(x=10, y=80)


            self.configuracoes_editar = ctk.CTkSwitch(self.FrameModuloConfiguracoesResp, font=ctk.CTkFont(weight="bold"), text="Editar",onvalue="liberado", offvalue="bloqueado", 
                                        switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.configuracoes_editar.place(x=10, y=110)


            self.configuracoes_remover = ctk.CTkSwitch(self.FrameModuloConfiguracoesResp, font=ctk.CTkFont(weight="bold"), text="Remover",onvalue="liberado", offvalue="bloqueado", 
                                            switch_height=25, switch_width=50, progress_color="#3DED9D", state="disabled")
            self.configuracoes_remover.place(x=10, y=140)

        else:
            self.FrameModuloConfiguracoesResp.tkraise()
            self.Destaque_Button(self.BT_ModuloConfiguracoes)

app()
root.protocol("WM_DELETE_WINDOW", closesys)
root.mainloop()
