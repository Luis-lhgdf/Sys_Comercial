import customtkinter as ctk
from src.views.icones import *
from src.views.appearance_manager import AppearanceManager

class MainView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.appearance_manager = AppearanceManager()

        self.title("Login")
        self.geometry("1000x600")

        self.resizable(False, False)

        def mostrar_senha():
            if self.MostrarSenha.get():
                self.SenhaDigitado.configure(show="")
            else:
                self.SenhaDigitado.configure(show="*")

        def ativar_enter(Event):
            self.fazer_login()


        self.painel = ctk.CTkFrame(self, width=410, height=600, corner_radius=2, fg_color="#242A5F")
        self.painel.grid(column=0, row=0, padx=(0, 1), pady=1, sticky="nsew")

        self.paine2 = ctk.CTkFrame(self, width=590, height=600, corner_radius=2, fg_color="white")
        self.paine2.grid(column=1, row=0, padx=(1, 0), pady=1, sticky="nsew")


        self.grid_columnconfigure((0,1), weight=1)  # Coluna 2 se expandirá

        self.grid_rowconfigure(0, weight=1)

        self.UsuarioIcon2 = ctk.CTkLabel(self.painel, text="", image=UsuarioIcon2, font=self.appearance_manager.get_font_title(),
                                 fg_color="transparent", bg_color="transparent")
        self.UsuarioIcon2.grid(column=0, row=0, pady=1, sticky="nsew")

        self.txt_welcome = ctk.CTkLabel(self.paine2, text="Bem Vindo", font=self.appearance_manager.get_font_title(), text_color="black")
        self.txt_welcome.grid(column=0, row=0, pady=(150,20), sticky="nsew")

        self.LoginDigitado = ctk.CTkEntry(self.paine2, placeholder_text="Digite seu login", text_color="black",
                                          fg_color="white", width=200, border_color="black")
        self.LoginDigitado.grid(column=0, row=1, pady=(0, 20), sticky="nsew")

        self.SenhaDigitado = ctk.CTkEntry(self.paine2, placeholder_text="Digite sua senha", text_color="black",
                                          fg_color="white", width=200, show="*", border_color="black")
        self.SenhaDigitado.grid(column=0, row=2, pady=(0, 20), sticky="nsew")

        self.MostrarSenha = ctk.CTkCheckBox(self.paine2, text="Mostrar senha", font=self.appearance_manager.get_font_title(),
                                            command=mostrar_senha, text_color="black", border_color="black")
        self.MostrarSenha.grid(column=0, row=3, pady=(0, 20), sticky="nsew")

        self.BtEntrar = ctk.CTkButton(self.paine2, text="Entrar", font=self.appearance_manager.get_font_title(), command=self.fazer_login,
                                       text_color="black", fg_color="white", hover_color="gray90")
        self.BtEntrar.grid(column=0, row=4, pady=(0, 20), sticky="nsew")

        self.status_label = ctk.CTkLabel(self.paine2, text="", font=self.appearance_manager.get_font_title(),
                                 fg_color="transparent", bg_color="transparent", text_color="black")
        self.status_label.grid(column=0, row=5,  pady=(0, 20),sticky="nsew")


    def start_interface(self):
        self.mainloop()

    def update_status(self, status):
        print("oi")
        # self.status_label.configure(text=status)
        
        # # Desativando o botão de login se a conexão com o banco de dados falhar
        # if "Erro" in status[1]:
        #     self.BtEntrar.configure(state="disabled")
       
        # else:
        #     self.BtEntrar.configure(state="normal")

    def fazer_login(self):
        print("luis henrique")


