import customtkinter as ctk
from src.views.icones import *
from src.views.appearance_manager import AppearanceManager
import webbrowser

class MainView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.appearance_manager = AppearanceManager()

        self.linkedin_url = "https://linkedin.com/in/luis-henrique-281b97186"
        self.github_url = "https://github.com/Luis-lhgdf"
        self.site_url = "https://luis-lhgdf.github.io/portfolio/"


        self.title("Login")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.configure(fg_color="#558FAD")   

        
       # Configuração das colunas principais
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # widgets referentes ao frame 1
        self.frame = ctk.CTkFrame(self, width=410, height=600, corner_radius=0, fg_color="#558FAD")
        self.frame.grid(column=0, row=0, pady=1, sticky="nsew")

        # Configuração das colunas e linhas do frame 1
        self.frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame.grid_rowconfigure((0, 1, 6), weight=1)

        self.title_label = ctk.CTkLabel(self.frame, text="COMMERCIAL SYS", font=self.appearance_manager.get_font_title(), text_color="white")
        self.title_label.grid(column=0, row=0, pady=(15, 30), sticky="nsew", columnspan=3)

        self.github_icon = ctk.CTkButton(self.frame,image=github_icon, text="", fg_color="transparent",width=0, hover_color="#D9B46E", command=lambda:self.open_website(self.github_url))
        self.github_icon.grid(column=0, row=1, padx=(0,0), sticky="e")

        
        self.linkedin_icon = ctk.CTkButton(self.frame,image=linkedin_icon, text="", fg_color="transparent",width=0, hover_color="#D9B46E",command=lambda:self.open_website(self.linkedin_url))
        self.linkedin_icon.grid(column=1, row=1,padx=(0,0))

        self.site_icon = ctk.CTkButton(self.frame,image=website_icon, text="", fg_color="transparent", width=0, hover_color="#D9B46E",command=lambda:self.open_website(self.site_url))
        self.site_icon.grid(column=2, row=1, padx=(0,0),sticky="w")

        self.illustration_label = ctk.CTkLabel(self.frame, image=illustration_image, text="", fg_color="transparent")
        self.illustration_label.grid(column=0, row=6, pady=(60, 0), sticky="nsew", columnspan=3)

        # widgets referentes ao frame 2
        self.frame2 = ctk.CTkFrame(self, width=410, height=450, corner_radius=20, fg_color="white")
        self.frame2.grid(column=1, row=0, pady=(10, 1), padx=(0, 10), sticky="nsew")

        # Configuração das colunas e linhas do frame 2
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure((1, 10), weight=1)

        self.sign_up_text = ctk.CTkLabel(self.frame2, text="Você não tem uma conta?", width=5, font=self.appearance_manager.get_font_body())
        self.sign_up_text.grid(column=0, row=0, padx=(10, 10), pady=(5, 0), sticky="e")

        self.sign_up = ctk.CTkButton(self.frame2, text="CADASTRE-SE", font=self.appearance_manager.get_font_body(True),text_color="white", fg_color="#558FAD", hover_color="#D9B46E")
        self.sign_up.grid(column=1, row=0, padx=(10, 10), pady=(5, 0), sticky="w")

  

        self.welcome_label = ctk.CTkLabel(self.frame2, text="BEM-VINDO DE VOLTA", font=self.appearance_manager.get_font_title())
        self.welcome_label.grid(column=0, row=2, padx=(60,0), pady=(0, 0), sticky="w")

        self.welcome2_label = ctk.CTkLabel(self.frame2, text="Acesse sua conta", font=self.appearance_manager.get_font_subtitle())
        self.welcome2_label.grid(column=0, row=3,padx=(60,0),pady=(0, 40), sticky="w")

        self.login_text = ctk.CTkLabel(self.frame2, text="Login", font=self.appearance_manager.get_font_subtitle())
        self.login_text.grid(column=0, row=4, padx=(65,0),pady=(5, 3), sticky="w")

        self.login_entry = ctk.CTkEntry(self.frame2, placeholder_text="Digite seu login", height=43, width=300, border_color="gray80", font=self.appearance_manager.get_font_body())
        self.login_entry.grid(column=0, row=5, padx=(60,0),pady=(0, 5), sticky="w")

        self.password_text = ctk.CTkLabel(self.frame2, text="Senha", font=self.appearance_manager.get_font_subtitle())
        self.password_text.grid(column=0, row=6, padx=(65,0),pady=(5, 3), sticky="w")

        self.password_entry = ctk.CTkEntry(self.frame2, placeholder_text="Digite sua senha",height=43, width=300, border_color="gray80", show="*", font=self.appearance_manager.get_font_body())
        self.password_entry.grid(column=0, row=7, padx=(60,0), pady=(0, 3), sticky="w")

        self.show_password_check = ctk.CTkCheckBox(self.frame2, text="", command=self.show_password, height=43, fg_color="#D9B46E", hover_color="#D9B46E")
        self.show_password_check.grid(column=0, row=7, padx=(370, 0), pady=(5, 5), sticky="w")

        self.forget_password = ctk.CTkButton(self.frame2, text="Esqueceu sua senha?", text_color="black", font=self.appearance_manager.get_font_body(), fg_color="transparent", hover_color="#D9B46E")
        self.forget_password.grid(column=0, row=8,padx=(60,0),pady=(0, 5), sticky="w")

        self.login_button = ctk.CTkButton(self.frame2, text="Entrar",height=43, width=140,  font=self.appearance_manager.get_font_subtitle(True),text_color="white", fg_color="#558FAD", hover_color="#D9B46E", command=self.login)
        self.login_button.grid(column=0, row=9, padx=(60,0), pady=(5, 5), sticky="w")
        

        self.database_status = ctk.CTkButton(self.frame2, image=alert_icon, anchor="w", text="", text_color="blue", fg_color="transparent", hover_color="#D9B46E", font=self.appearance_manager.get_font_body())
        self.database_status.grid(column=0, row=10, pady=(50, 5), columnspan=3, sticky="s")

    def open_website(self, url):
        # URL do site que deseja abrir
        website_url = url
        # Abrir o site no navegador padrão
        webbrowser.open(website_url)
        


    def start_interface(self):
        self.mainloop()
    
    def show_password(self):
        if self.show_password_check.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def enter_key (self, Event):
        self.login()

    def update_status(self, status):
        self.database_status.configure(text=status)

        # Desativando o botão de login se a conexão com o banco de dados falhar
        if "Erro" in status:
    
            self.login_button.configure(state="disabled")
            self.database_status.configure(text_color="red")
        else:
            self.login_button.configure(state="normal")
            self.database_status.configure(state="disabled")

    def login(self):
        pass


