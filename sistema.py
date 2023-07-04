import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import pyodbc
import base64
import binascii
import io
import os
from PIL import Image
# Criar a janela

local  = r'liftam.JSON'
ctk.set_default_color_theme(local)


image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")  

# _________________Criando as img_icones com as opções LIGHT E DARK e definindo o tamanho com SIZE______________


MenuIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "menu_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "menu_light.png")), size=(20, 20))


HomeIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))


SeuLogo = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "logo1.png")),
                       dark_image=Image.open(os.path.join(image_path, "logo1.png")), size=(100, 100))


SeuLogo2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "logo2.png")),
                       dark_image=Image.open(os.path.join(image_path, "logo2.png")), size=(200, 200))



EstoqueIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "estoque_black.png")),
                       dark_image=Image.open(os.path.join(image_path, "estoque_light.png")),size=(20, 20))


CadastroIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "cadastro_black.png")),
                       dark_image=Image.open(os.path.join(image_path, "cadastro_light.png")), size=(20, 20))


AgendaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "agenda_black.png")),
                       dark_image=Image.open(os.path.join(image_path, "agenda_light.png")), size=(20, 20))


MedicaoIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "carteira_black.png")),
                       dark_image=Image.open(os.path.join(image_path, "carteira_light.png")), size=(20, 20))

UsuarioIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "usuario_black.png")),
                       dark_image=Image.open(os.path.join(image_path, "usuario_light.png")), size=(20, 20))


ConfiguracoesIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "configuracoes_black.png")),
                       dark_image=Image.open(os.path.join(image_path, "configuracoes_light.png")), size=(20, 20))







class icone_empresa:
    def __init__(self):
        super().__init__()
       # Função para recuperar a imagem do banco de dados
        # servidor = 'localhost'
        # database = "BD_Teste"
        # loginsql = 'sa'
        # senhasql = 'Lhgdfluis45'

        # dados_conexao = ("Driver={ODBC Driver 18 for SQL Server};"
        #                 f"Server={servidor};"
        #                 f"Database={database};"
        #                 f"UID={loginsql};"
        #                 f"PWD={senhasql};"
        #                 "TrustServerCertificate=Yes")

        # conexao = pyodbc.connect(dados_conexao)
        # cursor = conexao.cursor()

        # # Buscar a imagem no banco de dados
        # cursor.execute("SELECT image FROM imagens WHERE id = 1")
        # result = cursor.fetchone()

        # if result:
        #     # Converter o valor binário para imagem
        #     image_binary = result[0]
        #     image = Image.open(io.BytesIO(image_binary))

        #     # Redimensionar a imagem se necessário
        #     image = image.resize((100, 100))

        #     # Converter a imagem para o formato suportado pelo Tkinter
        #     photo = ctk.CTkImage(image)

        #     # Atualizar o widget Label com a nova imagem
        #     # label.configure(image=photo)
        #     # label.image = photo
        #     # root.state('zoomed') 

        # # Fechar a conexão com o banco de dados
        # conexao.close()
    
    def select_image(self): # Função para selecionar a imagem
        # Abrir o diálogo de seleção de arquivo
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])

        # Verificar se um arquivo foi selecionado
        if file_path:
            # Carregar a imagem selecionada
            self.load_image(file_path)
            
            # Converter a imagem para bytes
            with open(file_path, "rb") as f:
                image_bytes = f.read()

            # Converter os bytes para base64
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            # Inserir ou atualizar a imagem no banco de dados
            self.insert_image(image_base64)
    
    def load_image(self,file_path): # Função para carregar a imagem
        # Carregar a imagem
        image = Image.open(file_path)

        # Redimensionar a imagem se necessário
        image = image.resize((100, 100))

        # Converter a imagem para o formato suportado pelo Tkinter
        photo = ctk.CTkImage(image)

        # Atualizar o widget Label com a nova imagem
        # label.configure(image=photo)
        # label.image = photo
   
    def insert_image(self,image_base64):  # Função para inserir ou atualizar a img no BD
        # Conectar ao banco de dados
        servidor = '192.168.15.62'
        database = "BD_Teste"
        loginsql = 'sa'
        senhasql = 'Lhgdfluis45'

        dados_conexao = ("Driver={ODBC Driver 18 for SQL Server};"
                    f"Server={servidor};"
                    f"Database={database};"
                    f"UID={loginsql};"
                    f"PWD={senhasql};"
                    "TrustServerCertificate=Yes")

        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        # Converter a imagem base64 para dados binários
        image_binary = binascii.a2b_base64(image_base64)

        # Verificar se já existe uma imagem com o ID 1
        cursor.execute("SELECT COUNT(*) FROM imagens WHERE id = 1")
        count = cursor.fetchone()[0]

        if count > 0:
            # Atualizar a imagem existente
            cursor.execute("UPDATE imagens SET image = ? WHERE id = 1", (image_binary,))
        else:
            # Inserir uma nova imagem
            cursor.execute("INSERT INTO imagens (id, image) VALUES (1, ?)", (image_binary,))

        # Salvar as alterações e fechar a conexão
        conexao.commit()
        conexao.close()


class Menu(icone_empresa):
    def __init__(self):
        super().__init__()
        # tela de login
        self.Root_login = ctk.CTk()
        self.Root_login.geometry(f"400x430")
        self.Root_login.title("SYS LIFTAM")

        # _______definindo as fontes principais que serão usadas ao longo do codigo_______
        self.FontTitle =ctk.CTkFont(family='inria serif', size=20, weight="bold")
        self.FontBody =ctk.CTkFont(family='inria serif', size=12)


        LabelTxt = ctk.CTkLabel(self.Root_login, text="Bem Vindo", font=self.FontTitle)
        LabelTxt.place(relx=0.5, rely=0.2, anchor="center")


        self.LoginDigitado = ctk.CTkEntry(self.Root_login, placeholder_text="Digite seu login", width=200)
        self.LoginDigitado.place(relx=0.5,rely=0.3, anchor='center')

        self.SenhaDigitado = ctk.CTkEntry(self.Root_login, placeholder_text="Digite sua senha", width=200)
        self.SenhaDigitado.place(relx=0.5,rely=0.4, anchor='center')

        self.MostrarSenha = ctk.CTkCheckBox(self.Root_login, text="Mostrar senha", font=self.FontBody)
        self.MostrarSenha.place(relx=0.5, rely=0.5, anchor="center")

        self.BtEntrar = ctk.CTkButton(self.Root_login, text="Entrar",command=self.frame_Inicial)
        self.BtEntrar.place(relx=0.5, rely=0.6, anchor="center")


        LabelLogo = ctk.CTkLabel(self.Root_login, text="", image=SeuLogo)
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


        
        self.frame_MenuLateralEsq = ctk.CTkFrame(self.rootHome, width=175, height=self.screen_height)
        self.frame_MenuLateralEsq.grid(row=0,column=0)

        self.frame_OcultarMenu = ctk.CTkFrame(self.rootHome, fg_color="transparent", height=self.screen_height)
        self.frame_OcultarMenu.grid(row=0,column=1)

        self.frame_resposta = ctk.CTkFrame(self.rootHome, fg_color="transparent")
        self.frame_resposta.grid(row=0,column=2)

        self.BtOcultar = ctk.CTkButton(self.frame_OcultarMenu,text="", image=MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent")
        self.BtOcultar.place(x=1,y=1)

        self.BtHome = ctk.CTkButton(self.frame_MenuLateralEsq, text="Home", image=HomeIcon, anchor="w", width=155)
        self.BtHome.place(x=10, y=80)

        self.BtEstoque = ctk.CTkButton(self.frame_MenuLateralEsq, text="Estoque ", image=EstoqueIcon, anchor="w", width=155)
        self.BtEstoque.place(x=10, y=120)
        
        self.BtCadastros = ctk.CTkButton(self.frame_MenuLateralEsq, text="Cadastro", image=CadastroIcon, anchor="w", width=155)
        self.BtCadastros.place(x=10, y=160)        

        self.BtAgenda = ctk.CTkButton(self.frame_MenuLateralEsq, text="Agenda", image=AgendaIcon, anchor="w", width=155)
        self.BtAgenda.place(x=10, y=200)

        self.BtMedicao = ctk.CTkButton(self.frame_MenuLateralEsq, text="Medição", image=MedicaoIcon, anchor="w", width=155)
        self.BtMedicao.place(x=10, y=240)
        

        self.BtUsuario = ctk.CTkButton(self.frame_MenuLateralEsq, text="Usuario", image=UsuarioIcon, anchor="w", width=155, command=self.Frame_Usuario)
        self.BtUsuario.place(x=10, y=280)  

        self.BtConfiguracoes = ctk.CTkButton(self.frame_MenuLateralEsq, text="Configuracoes", image=ConfiguracoesIcon, anchor="w", width=155, command=self.Frame_Configuracoes)
        self.BtConfiguracoes.place(x=10, y=320)    


        LabelLogo = ctk.CTkLabel(self.frame_MenuLateralEsq, text="", image=SeuLogo2)
        LabelLogo.place(x=-10, y=(self.screen_height-300))


        appearance_mode_optionemenu = ctk.CTkOptionMenu(self.frame_MenuLateralEsq, font=self.FontBody, width=150, height=30, values=["Dark","light"], command=self.aparencia)
        appearance_mode_optionemenu.place(x=10, y=(self.screen_height-100))

        self.FrameLateralAtual = self.frame_OcultarMenu   



        self.rootHome.mainloop()

    def aparencia(self, new_appearance_mode: str):
        # função que altera o modo de aparencia da janela entre ligth e dark
        ctk.set_appearance_mode(new_appearance_mode) 

    def Frame_Usuario(self):
        self.FrameLateralAtual.destroy()
                
        self.FrameUsuarioLateral = ctk.CTkFrame(self.rootHome, width=175, height=self.screen_height, fg_color="transparent")
        self.FrameUsuarioLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameUsuarioLateral

        self.BtHome.configure(fg_color="#C41616")
        self.BtEstoque.configure(fg_color="#C41616")
        self.BtCadastros.configure(fg_color="#C41616")
        self.BtAgenda.configure(fg_color="#C41616")
        self.BtMedicao.configure(fg_color="#C41616")
        self.BtUsuario.configure(fg_color="#A11919")
        self.BtConfiguracoes.configure(fg_color="#C41616")
        
        
        self.BtOcultar = ctk.CTkButton(self.FrameUsuarioLateral,text="", image=MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent")
        self.BtOcultar.place(x=1,y=1)

        self.op1 = ctk.CTkButton(self.FrameUsuarioLateral, text="opção1", image=MedicaoIcon, anchor="w", width=155)
        self.op1.place(x=5, y=280)
        

        self.op2 = ctk.CTkButton(self.FrameUsuarioLateral, text="opção2", image=UsuarioIcon, anchor="w", width=155)
        self.op2.place(x=5, y=320)  

    def Frame_Configuracoes(self):
        self.FrameLateralAtual.destroy()
                
        self.FrameConfigLateral = ctk.CTkFrame(self.rootHome, width=175, height=self.screen_height, fg_color="transparent")
        self.FrameConfigLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameConfigLateral


        self.BtHome.configure(fg_color="#C41616")
        self.BtEstoque.configure(fg_color="#C41616")
        self.BtCadastros.configure(fg_color="#C41616")
        self.BtAgenda.configure(fg_color="#C41616")
        self.BtMedicao.configure(fg_color="#C41616")
        self.BtUsuario.configure(fg_color="#C41616")
        self.BtConfiguracoes.configure(fg_color="#A11919")

        self.BtOcultar = ctk.CTkButton(self.FrameConfigLateral,text="", image=MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent")
        self.BtOcultar.place(x=1,y=1)

        self.op1 = ctk.CTkButton(self.FrameConfigLateral, text="opção1", image=MedicaoIcon, anchor="w", width=155)
        self.op1.place(x=5, y=320)
        
        self.op2 = ctk.CTkButton(self.FrameConfigLateral, text="opção2", image=UsuarioIcon, anchor="w", width=155)
        self.op2.place(x=5, y=360)  

        self.op3 = ctk.CTkButton(self.FrameConfigLateral, text="opçao3", image=ConfiguracoesIcon, anchor="w", width=155, command=self.Frame_Configuracoes)
        self.op3.place(x=5, y=400)  
Menu()





