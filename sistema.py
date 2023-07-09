import customtkinter as ctk
from tkinter import filedialog
import mysql.connector
from PIL import Image, ImageTk
import base64
import binascii
import io
import os
import ctypes
import sys


# Criar a janela





local  = r'liftam.JSON'
ctk.set_default_color_theme(local)


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

def fecharSistemaa():
    resp = msgbox("Confirmação",
                "Deseja Encerrar O Programa?", 4)
    if resp==6:
        
        sys.exit()

class mysql_bd:
    def conecta_bd(self):
        # Defina as informações de conexão
        database = 'railway'
        host = 'containers-us-west-1.railway.app'
        port = 5474
        user = 'root'
        password = 'JThLpvacyDNwzFLPyLhX'

        # Crie a conexão
        self.conexao = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
        # Verifique se a conexão foi estabelecida
        if self.conexao.is_connected():
            print('Conexão bem-sucedida ao banco de dados')
            return self.conexao

    def desconeta_bd(self):
        self.conexao.close()
        print('Conexãoao banco de dados foi encerrada')

class validar_acesso():
    def validar(self):
        usuario = self.LoginDigitado.get()
        print(login)

    

class icone_empresa(mysql_bd):

    def verificar_foto(self, label_img, usuario):
        

        conexao = self.conecta_bd()
        cursor = conexao.cursor()

        # Buscar a imagem no banco de dados
        cursor.execute(f"SELECT * FROM foto_perfil WHERE usuario = '{usuario}'")
        result = cursor.fetchone()

        if result:
            
            print(f"encontrado {usuario}")
            # Converter o valor binário para imagem
            image_binary = result[2]  # A coluna 'img' é o índice 2 no resultado
            image = Image.open(io.BytesIO(image_binary))

            # Redimensionar a imagem se necessário
            image = image.resize((100, 100))

            # Converter a imagem para o formato suportado pelo Tkinter
            photo = ImageTk.PhotoImage(image)
            # Atualizar o widget Label com a nova imagem
            label_img.configure(image=photo, text="")
            label_img.image = photo
            
        else:
            print("não existe nenhuma img no banco de dados")

        # Fechar a conexão com o banco de dados
        self.desconeta_bd()
    
    def select_image(self, label_img, usuario): # Função para selecionar a imagem
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
    
    def load_image(self,file_path, label_img): # Função para carregar a imagem
        # Carregar a imagem
        image = Image.open(file_path)

        # Redimensionar a imagem se necessário
        image = image.resize((100, 100))

        # Converter a imagem para o formato suportado pelo Tkinter
        photo = ImageTk.PhotoImage(image)

        # Atualizar o widget Label com a nova imagem
        label_img.configure(image=photo, text="")
        label_img.image = photo
   
    def insert_image(self,image_base64, usuario):  # Função para inserir ou atualizar a img no BD

        conexao = self.conecta_bd()
        cursor = conexao.cursor()

        # Converter a imagem base64 para dados binários
        image_binary = binascii.a2b_base64(image_base64)

        # Verificar se já existe uma imagem com o ID 1
        cursor.execute(f"SELECT COUNT(*) FROM foto_perfil WHERE usuario = '{usuario}'")
        count = cursor.fetchone()[0]

        if count > 0:
            # Atualizar a imagem existente
            cursor.execute("UPDATE foto_perfil SET img = %s WHERE usuario = %s", (image_binary, usuario))
        else:
            # Inserir uma nova imagem
            cursor.execute("INSERT INTO foto_perfil (id, usuario, img) VALUES (%s, %s, %s)", (count+1, usuario, image_binary))

        # Salvar as alterações e fechar a conexão
        conexao.commit()
        conexao.close()

class usuario_conf(icone_empresa):
    def iniciar_img_perfil(self, labelIMG):
        imagem = labelIMG
        self.verificar_foto(imagem, usuario="anubis")
    def trocar_img_perfil(self, frame_resp, labelIMG):
        imagem = labelIMG
        def button_click():
            self.select_image(imagem, usuario="anubis")

        bt = ctk.CTkButton(frame_resp, text="alterar img", command=button_click)
        bt.place(x=50, y=50)

class Menu(usuario_conf, validar_acesso):  
    def __init__(self):
        super().__init__()
        # tela de login
        self.Root_login = ctk.CTk()
        self.Root_login.geometry(f"400x430")
        self.Root_login.title("SYS LIFTAM")

        # _______definindo as fontes principais que serão usadas ao longo do codigo_______
        self.FontTitle =ctk.CTkFont(family='inria serif', size=20, weight="bold")
        self.FontBody =ctk.CTkFont(family='inria serif', size=12)

        # _________________Criando as img_icones com as opções LIGHT E DARK e definindo o tamanho com SIZE______________
            
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
                            dark_image=Image.open(os.path.join(self.image_path, "adicionar_light.png")), size=(17, 17))


        self.EditarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "editar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "editar_light.png")), size=(17, 17))


        self.ItemIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "item_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "item_light.png")), size=(17, 17))



        self.VisualizarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "visualizar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "visualizar_light.png")), size=(17, 17))


        self.VoltarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "voltar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "voltar_light.png")), size=(17, 17))


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


        # __________________________________________________________________________________

        LabelTxt = ctk.CTkLabel(self.Root_login, text="Bem Vindo", font=self.FontTitle)
        LabelTxt.place(relx=0.5, rely=0.2, anchor="center")


        self.LoginDigitado = ctk.CTkEntry(self.Root_login, placeholder_text="Digite seu login", width=200)
        self.LoginDigitado.place(relx=0.5,rely=0.3, anchor='center')

        self.SenhaDigitado = ctk.CTkEntry(self.Root_login, placeholder_text="Digite sua senha", width=200)
        self.SenhaDigitado.place(relx=0.5,rely=0.4, anchor='center')

        self.MostrarSenha = ctk.CTkCheckBox(self.Root_login, text="Mostrar senha", font=self.FontBody)
        self.MostrarSenha.place(relx=0.5, rely=0.5, anchor="center")

        self.BtEntrar = ctk.CTkButton(self.Root_login, text="Entrar",command=self.validar, hover_color= ("#880016", "#880016"),
                                      text_color = ("white", "white"))
        self.BtEntrar.place(relx=0.5, rely=0.6, anchor="center")


        LabelLogo = ctk.CTkLabel(self.Root_login, text="", image=self.SeuLogo)
        LabelLogo.place(relx=0.5, rely=0.8, anchor="center")
        
        LabelTxt2 = ctk.CTkLabel(self.Root_login, text="Modo")
        LabelTxt2.place(relx=0.15, rely=0.90, anchor="center")

        appearance_mode_optionemenu = ctk.CTkOptionMenu(self.Root_login, font=self.FontBody, width=100, height=20, values=["Dark","light"], command=self.aparencia)
        appearance_mode_optionemenu.place(relx=0.15, rely=0.95, anchor="center")

        # Executar o loop principal da janela
        self.Root_login.mainloop()

    def frame_Inicial(self):
        self.Root_login.withdraw()
        self.rootHome = ctk.CTkToplevel()
        self.rootHome.state('zoomed')
        self.screen_height = self.rootHome.winfo_screenheight()
        self.screen_wedth = self.rootHome.winfo_screenwidth()


        
        self.frame_MenuLateralEsq = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, corner_radius=0)
        self.frame_MenuLateralEsq.grid(row=0,column=0)

        self.frame_OcultarMenu = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=37, height=self.screen_height, corner_radius=0)
        self.frame_OcultarMenu.grid(row=0,column=1)

        self.frame_temp = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.frame_temp.grid(row=0,column=2)

        self.BtOcultar = ctk.CTkButton(self.frame_OcultarMenu,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", text_color=("black","white"), command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)


        self.BtHome = ctk.CTkButton(self.frame_MenuLateralEsq, text="Home", image=self.HomeIcon, anchor="w", 
                                    width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Home)
        self.BtHome.place(x=0, y=120)


        self.BtEstoque = ctk.CTkButton(self.frame_MenuLateralEsq, text="Estoque ", image=self.EstoqueIcon, anchor="w", 
                                       width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Estoque)
        self.BtEstoque.place(x=0, y=160)
        

        self.BtCadastros = ctk.CTkButton(self.frame_MenuLateralEsq, text="Cadastro", image=self.CadastroIcon, anchor="w", 
                                         width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Cadastro)
        self.BtCadastros.place(x=0, y=200)        


        self.BtAgenda = ctk.CTkButton(self.frame_MenuLateralEsq, text="Agenda", image=self.AgendaIcon, anchor="w", 
                                      width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Agenda)
        self.BtAgenda.place(x=0, y=240)


        self.Btcarteira = ctk.CTkButton(self.frame_MenuLateralEsq, text="Carteira", image=self.carteiraIcon, anchor="w", 
                                       width=176, corner_radius=0, fg_color="transparent",  text_color=("black","white"), command=self.Frame_carteira)
        self.Btcarteira.place(x=0, y=280)
        


        self.BtFinancas = ctk.CTkButton(self.frame_MenuLateralEsq, text="Finanças", image=self.FinancasIcon, anchor="w", 
                                       width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_financas)
        self.BtFinancas.place(x=0, y=320)  


        self.BtUsuario = ctk.CTkButton(self.frame_MenuLateralEsq, text="Usuario", image=self.UsuarioIcon, anchor="w", 
                                       width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Usuario)
        self.BtUsuario.place(x=0, y=360)  




        self.BtConfiguracoes = ctk.CTkButton(self.frame_MenuLateralEsq, text="Configuracoes", image=self.ConfiguracoesIcon, anchor="w",
                                             width=176, corner_radius=0,  text_color=("black","white"), fg_color="transparent", command=self.Frame_Configuracoes)
        self.BtConfiguracoes.place(x=0, y=400)    



        self.foto_perfil = ctk.CTkLabel(self.frame_MenuLateralEsq, text="Carregando", width=80, height=80, fg_color='gray')
        self.foto_perfil.place(relx=0.5, rely=0.07, anchor="center")


        LabelLogo = ctk.CTkLabel(self.frame_MenuLateralEsq, text="", image=self.SeuLogo2)
        LabelLogo.place(x=-10, y=(self.screen_height-300))


        appearance_mode_optionemenu = ctk.CTkOptionMenu(self.frame_MenuLateralEsq, font=self.FontBody, width=150, height=30, values=["Dark","light"], command=self.aparencia)
        appearance_mode_optionemenu.place(x=10, y=(self.screen_height-100))

        self.FrameLateralAtual = self.frame_OcultarMenu   
        self.frameRespostaAtual = self.frame_temp
        self.iniciar_img_perfil(self.foto_perfil)

        self.Frame_Home()
        self.rootHome.protocol("WM_DELETE_WINDOW", fecharSistemaa)
        self.rootHome.mainloop()

    def aparencia(self, new_appearance_mode: str):
        # função que altera o modo de aparencia da janela entre ligth e dark
        ctk.set_appearance_mode(new_appearance_mode) 

    def ocultarJanela(self):
        larguraJanelaAtual = self.frame_MenuLateralEsq.winfo_width()
       
        
        if larguraJanelaAtual > 35:
            self.frame_MenuLateralEsq.configure(width=28)

        else:
            self.frame_MenuLateralEsq.configure(width=176)

    def Frame_Home(self):
        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
        
        self.frame_OcultarMenu = ctk.CTkFrame(self.rootHome, width=37, height=self.screen_height, corner_radius=0, fg_color=("white", "#880016"))
        self.frame_OcultarMenu.grid(row=0,column=1)
        self.FrameLateralAtual = self.frame_OcultarMenu

        self.FrameHomegResposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.FrameHomegResposta.grid(row=0,column=2)
        self.frameRespostaAtual = self.FrameHomegResposta

        


        self.BtHome.configure(fg_color=("white", "#880016"))
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")





        self.BtOcultar = ctk.CTkButton(self.frame_OcultarMenu,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", text_color=("black","white"), command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)

    def Frame_Estoque(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color=("white", "#880016"))
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
                
                
        self.FrameEstoqueLateral = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameEstoqueLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameEstoqueLateral


        

        
        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=138,y=1)

        self.op1 = ctk.CTkButton(self.FrameLateralAtual, text="Entrada", image=self.EntradaIcon,anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op1.place(x=10, y=120)
        
        self.op2 = ctk.CTkButton(self.FrameLateralAtual, text="Saida", image=self.SaidaIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op2.place(x=10, y=160)  

        self.op3 = ctk.CTkButton(self.FrameLateralAtual, text="Inventario", image=self.InventarioIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op3.place(x=10, y=200)  

    def Frame_Cadastro(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color=("white", "#880016"))
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
                
                
        self.FrameCadastroLateral = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameCadastroLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameCadastroLateral


        
        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=138,y=1)

        self.op1 = ctk.CTkButton(self.FrameLateralAtual, text="Cadastrar Itens", image=self.EstoqueIcon,anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op1.place(x=10, y=160)
        
        self.op2 = ctk.CTkButton(self.FrameLateralAtual, text="Cadastrar Clientes", image=self.CadastroIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op2.place(x=10, y=200)  

        self.op3 = ctk.CTkButton(self.FrameLateralAtual, text="Novo Usuario", image=self.UsuarioIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op3.place(x=10, y=240)  

    def Frame_Agenda(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color=("white", "#880016"))
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")



        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                

        self.FrameAgendaLateral = ctk.CTkFrame(self.rootHome, width=37, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameAgendaLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameAgendaLateral

        self.FrameAgendaResposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.FrameAgendaResposta.grid(row=0,column=2)
        self.frameRespostaAtual = self.FrameAgendaResposta

        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)
          
    def Frame_carteira(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color=("white", "#880016"))
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
                
                
        self.FramecarteiraLateral = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FramecarteiraLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FramecarteiraLateral


        

        
        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=138,y=1)

        self.op1 = ctk.CTkButton(self.FrameLateralAtual, text="Registrar Venda", image=self.VendasIcon,anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                    hover_color= ("#ff9ea2", "black"))
        self.op1.place(x=10, y=280)
        
        self.op2 = ctk.CTkButton(self.FrameLateralAtual, text="Faturamento", image=self.FaturamentoIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                    hover_color= ("#ff9ea2", "black"))
        self.op2.place(x=10, y=320)   
    
    def Frame_financas(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color=("white", "#880016"))
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
                
                
        self.FramefinancasLateral = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FramefinancasLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FramefinancasLateral


        

        
        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=138,y=1)

        self.op1 = ctk.CTkButton(self.FrameLateralAtual, text="Registrar Despesas", image=self.DespesaIcon,anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                    hover_color= ("#ff9ea2", "black"))
        self.op1.place(x=10, y=320)
        
        self.op2 = ctk.CTkButton(self.FrameLateralAtual, text="Outras Rendas +", image=self.ReceitaIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                    hover_color= ("#ff9ea2", "black"))
        self.op2.place(x=10, y=360)      
   
    def Frame_Usuario(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color=("white", "#880016"))
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                

        self.FrameUsuarioLateral = ctk.CTkFrame(self.rootHome, width=37, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameUsuarioLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameUsuarioLateral

        self.FrameUsuarioresposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.FrameUsuarioresposta.grid(row=0,column=2)
        self.frameRespostaAtual = self.FrameUsuarioresposta

        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)   

        self.trocar_img_perfil(self.FrameUsuarioresposta, self.foto_perfil)
    
    def Frame_Configuracoes(self):
        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color=("white", "#880016"))


        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                

        self.FrameConfigLateral = ctk.CTkFrame(self.rootHome, width=37, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameConfigLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameConfigLateral

        self.FrameConfigResposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.FrameConfigResposta.grid(row=0,column=2)
        self.frameRespostaAtual = self.FrameConfigResposta

        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)

        
        


Menu()


