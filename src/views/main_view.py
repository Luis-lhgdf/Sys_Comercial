from src.views.icones import *
from src.utils.utils import Utilities
from src.views.appearance_manager import AppearanceManager


class MainView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.appearance_manager = AppearanceManager()
        self.utils = Utilities()
        self.db_status = None

        self.linkedin_url = "https://linkedin.com/in/luis-henrique-281b97186"
        self.github_url = "https://github.com/Luis-lhgdf"
        self.site_url = "https://luis-lhgdf.github.io/portfolio/"
        self.login_view()

        self.protocol("WM_DELETE_WINDOW", self.controller.exit)

    def login_view(self):
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

        self.title_label = ctk.CTkLabel(self.frame, text="COMMERCIAL SYS",
                                        font=self.appearance_manager.get_font_title(), text_color="white")
        self.title_label.grid(column=0, row=0, pady=(15, 30), sticky="nsew", columnspan=3)

        self.github_icon = ctk.CTkButton(self.frame, image=github_icon, text="", fg_color="transparent", width=0,
                                         hover_color="#D9B46E",
                                         command=lambda: self.utils.open_website(self.github_url))
        self.github_icon.grid(column=0, row=1, padx=(0, 0), sticky="e")

        self.linkedin_icon = ctk.CTkButton(self.frame, image=linkedin_icon, text="", fg_color="transparent", width=0,
                                           hover_color="#D9B46E",
                                           command=lambda: self.utils.open_website(self.linkedin_url))
        self.linkedin_icon.grid(column=1, row=1, padx=(0, 0))

        self.site_icon = ctk.CTkButton(self.frame, image=website_icon, text="", fg_color="transparent", width=0,
                                       hover_color="#D9B46E", command=lambda: self.utils.open_website(self.site_url))
        self.site_icon.grid(column=2, row=1, padx=(0, 0), sticky="w")

        self.illustration_label = ctk.CTkLabel(self.frame, image=illustration_image, text="", fg_color="transparent")
        self.illustration_label.grid(column=0, row=6, pady=(60, 0), sticky="nsew", columnspan=3)

        # widgets referentes ao frame 2
        self.frame2 = ctk.CTkFrame(self, width=410, height=450, corner_radius=20, fg_color="white")
        self.frame2.grid(column=1, row=0, pady=(10, 1), padx=(0, 10), sticky="nsew")

        # Configuração das colunas e linhas do frame 2
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure((1, 10), weight=1)

        self.sign_up_text = ctk.CTkLabel(self.frame2, text="Você não tem uma conta?", text_color="black", width=5,
                                         font=self.appearance_manager.get_font_body())
        self.sign_up_text.grid(column=0, row=0, padx=(10, 10), pady=(5, 0), sticky="e")

        self.sign_up = ctk.CTkButton(self.frame2, text="CADASTRE-SE", font=self.appearance_manager.get_font_body(True),
                                     text_color="white", fg_color="#558FAD", hover_color="#D9B46E")
        self.sign_up.grid(column=1, row=0, padx=(10, 10), pady=(5, 0), sticky="w")

        self.welcome_label = ctk.CTkLabel(self.frame2, text="BEM-VINDO DE VOLTA",
                                          font=self.appearance_manager.get_font_title(), text_color="black")
        self.welcome_label.grid(column=0, row=2, padx=(60, 0), pady=(0, 0), sticky="w")

        self.welcome2_label = ctk.CTkLabel(self.frame2, text="Acesse sua conta",
                                           font=self.appearance_manager.get_font_subtitle(), text_color="black")
        self.welcome2_label.grid(column=0, row=3, padx=(60, 0), pady=(0, 40), sticky="w")

        self.login_text = ctk.CTkLabel(self.frame2, text="Login", font=self.appearance_manager.get_font_subtitle(),
                                       text_color="black")
        self.login_text.grid(column=0, row=4, padx=(65, 0), pady=(5, 3), sticky="w")

        self.login_entry = ctk.CTkEntry(self.frame2, placeholder_text="Digite seu login", fg_color="white",
                                        text_color="black", placeholder_text_color="gray", height=43, width=300,
                                        border_color="gray80", font=self.appearance_manager.get_font_body())
        self.login_entry.grid(column=0, row=5, padx=(60, 0), pady=(0, 5), sticky="w")

        self.password_text = ctk.CTkLabel(self.frame2, text="Senha", text_color="black",
                                          font=self.appearance_manager.get_font_subtitle())
        self.password_text.grid(column=0, row=6, padx=(65, 0), pady=(5, 3), sticky="w")

        self.password_entry = ctk.CTkEntry(self.frame2, placeholder_text="Digite sua senha", fg_color="white",
                                           text_color="black", placeholder_text_color="gray", height=43, width=300,
                                           border_color="gray80", show="*",
                                           font=self.appearance_manager.get_font_body())
        self.password_entry.grid(column=0, row=7, padx=(60, 0), pady=(0, 3), sticky="w")

        self.show_password_check = ctk.CTkCheckBox(self.frame2, text="",
                                                   command=lambda: self.show_password(self.password_entry), height=43,
                                                   fg_color="#D9B46E", hover_color="#D9B46E")
        self.show_password_check.grid(column=0, row=7, padx=(370, 0), pady=(5, 5), sticky="w")

        self.forget_password = ctk.CTkButton(self.frame2, text="Esqueceu sua senha?", text_color="black",
                                             font=self.appearance_manager.get_font_body(), fg_color="transparent",
                                             hover_color="#D9B46E")
        self.forget_password.grid(column=0, row=8, padx=(60, 0), pady=(0, 5), sticky="w")

        self.login_button = ctk.CTkButton(self.frame2, text="Entrar", height=43, width=140,
                                          font=self.appearance_manager.get_font_subtitle(True), text_color="white",
                                          fg_color="#558FAD", hover_color="#D9B46E", command=self.login)
        self.login_button.grid(column=0, row=9, padx=(60, 0), pady=(5, 5), sticky="w")
        self.login_button.bind("<Return>", self.login_enter_key)

        self.database_status = ctk.CTkButton(self.frame2, image=alert_icon, anchor="w", text="", text_color="blue",
                                             fg_color="transparent",
                                             hover_color="#D9B46E", font=self.appearance_manager.get_font_body(),
                                             command=self.create_database_view)
        self.database_status.grid(column=0, row=10, pady=(50, 5), columnspan=3, sticky="s")

    def create_database_view(self):
        self.utils.restart_interface(self.frame2)

        # Configuração das colunas e linhas do frame 2
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure((1, 10), weight=1)

        self.back_button = ctk.CTkButton(self.frame2, text="", width=0, image=back_icon, fg_color="#558FAD",
                                         hover_color="#D9B46E", command=self.back)
        self.back_button.grid(column=0, row=0, padx=(10, 10), pady=(5, 0), sticky="w")

        self.create_db_label = ctk.CTkLabel(self.frame2, text="CRIAR NOVO BANCO DE DADOS",
                                            font=self.appearance_manager.get_font_title(), text_color="black")
        self.create_db_label.grid(column=0, row=2, padx=(60, 0), pady=(0, 0), sticky="w")

        warning_text = """Por favor, defina uma senha para criar um novo banco\nde dados sqlite. A senha precisa ter pelo menos\n6 caracteres e incluir uma combinação de números\nletras e caracteres especiais (!$@%#)."""


        self.warning_text_label = ctk.CTkLabel(self.frame2, text=warning_text, text_color="black", justify="left",
                                               anchor="w", fg_color="transparent",
                                               font=self.appearance_manager.get_font_subtitle())
        self.warning_text_label.grid(column=0, row=3, padx=(60, 0), pady=(0, 40), )

        self.password_bd_text = ctk.CTkLabel(self.frame2, text="Senha", text_color="black",
                                             font=self.appearance_manager.get_font_subtitle())
        self.password_bd_text.grid(column=0, row=4, padx=(65, 0), pady=(5, 3), sticky="w")

        self.password_bd_entry = ctk.CTkEntry(self.frame2, placeholder_text="Digite sua senha", fg_color="white",
                                              show="*", text_color="black", placeholder_text_color="gray", height=43,
                                              width=300, border_color="gray80",
                                              font=self.appearance_manager.get_font_body())
        self.password_bd_entry.grid(column=0, row=5, padx=(60, 0), pady=(0, 5), sticky="w")
        self.password_bd_entry.bind('<KeyRelease>', self.controller.validate_password_db)

        self.password_bd_confirmation_text = ctk.CTkLabel(self.frame2, text="Redigite sua senha", text_color="black",
                                                          font=self.appearance_manager.get_font_subtitle())
        self.password_bd_confirmation_text.grid(column=0, row=6, padx=(65, 0), pady=(5, 3), sticky="w")

        self.password_bd_confirmation_entry = ctk.CTkEntry(self.frame2, placeholder_text="Redigite sua senha",
                                                     fg_color="white", text_color="black",
                                                     placeholder_text_color="gray", height=43, width=300,
                                                     border_color="gray80", show="*",
                                                     font=self.appearance_manager.get_font_body())
        self.password_bd_confirmation_entry.grid(column=0, row=7, padx=(60, 0), pady=(0, 3), sticky="w")
        self.password_bd_confirmation_entry.bind('<KeyRelease>', self.controller.validate_password_db)

        self.show_password_check = ctk.CTkCheckBox(self.frame2, text="",
                                                   command=lambda: self.show_password(self.password_bd_confirmation_entry),
                                                   height=43, fg_color="#D9B46E", hover_color="#D9B46E")
        self.show_password_check.grid(column=0, row=7, padx=(370, 0), pady=(5, 5), sticky="w")

        self.create_db_button = ctk.CTkButton(self.frame2, text="Criar", height=43, width=140,
                                       font=self.appearance_manager.get_font_subtitle(True), text_color="white",
                                       fg_color="#558FAD", hover_color="#D9B46E", state="disabled", command=self.create_database)
        self.create_db_button.grid(column=0, row=9, padx=(60, 0), pady=(5, 5), sticky="w")

        self.database_status = ctk.CTkLabel(self.frame2, anchor="w", text="Atualizar local do seu banco de dados",
                                            text_color="black", fg_color="transparent",
                                            font=self.appearance_manager.get_font_subtitle())

        self.database_status.grid(column=0, row=10, padx=(60, 0), pady=(50, 5), columnspan=3, sticky="w")

        self.select_database = ctk.CTkButton(self.frame2, image=view_icon, width=0, anchor="w", text="Procurar",
                                             height=43, font=self.appearance_manager.get_font_subtitle(True),
                                             text_color="white", fg_color="#558FAD", hover_color="#D9B46E")
        self.select_database.grid(column=0, row=10, padx=(0, 20), pady=(50, 5), columnspan=3, sticky="e")

    def start_interface(self):
        self.mainloop()

    def show_password(self, widget):

        if self.show_password_check.get():
            widget.configure(show="")
        else:
            widget.configure(show="*")

    def login_enter_key(self, Event):
        self.login()

    def update_status(self, status):
        self.database_status.configure(text=status[1])
        self.db_status = status

        # Desativando o botão de login se a conexão com o banco de dados falhar
        if "Erro" in status[1]:
            self.forget_password.configure(state="disabled")
            self.sign_up.configure(state="disabled")
            self.login_button.configure(state="disabled")
            self.database_status.configure(text_color="red")
        else:
            self.login_button.configure(state="normal")
            self.database_status.configure(state="disabled")

    def login(self):
        self.controller.validate_login()

    def create_database(self):
        print("criando")

    def back(self):
        self.utils.restart_interface(self)
        self.login_view()
        self.update_status(self.db_status)
