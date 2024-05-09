from src.views.icones import *
from src.utils.utils import Utilities
from src.views.appearance_manager import AppearanceManager
from src.models.main_model import MainModel
from src.views.menu_view import InterfaceMenu


class MainView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.appearance_manager = AppearanceManager()
        self.utils = Utilities()
        self.model = MainModel()
        self.db_status = None
        self.linkedin_url = "https://linkedin.com/in/luis-henrique-281b97186"
        self.github_url = "https://github.com/Luis-lhgdf"
        self.site_url = "https://luis-lhgdf.github.io/portfolio/"
        self.login_view()
        self.info_list_user = []
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
        self.frame = ctk.CTkFrame(
            self, width=410, height=600, corner_radius=0, fg_color="#558FAD"
        )
        self.frame.grid(column=0, row=0, pady=1, sticky="nsew")

        # Configuração das colunas e linhas do frame 1
        self.frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame.grid_rowconfigure((0, 1, 6), weight=1)

        self.title_label = ctk.CTkLabel(
            self.frame,
            text="COMMERCIAL SYS",
            font=self.appearance_manager.get_font_title(),
            text_color="white",
        )
        self.title_label.grid(
            column=0, row=0, pady=(15, 30), sticky="nsew", columnspan=3
        )

        self.github_icon = ctk.CTkButton(
            self.frame,
            image=github_icon,
            text="",
            fg_color="transparent",
            width=0,
            hover_color="#D9B46E",
            command=lambda: self.utils.open_website(self.github_url),
        )
        self.github_icon.grid(column=0, row=1, padx=(0, 0), sticky="e")

        self.linkedin_icon = ctk.CTkButton(
            self.frame,
            image=linkedin_icon,
            text="",
            fg_color="transparent",
            width=0,
            hover_color="#D9B46E",
            command=lambda: self.utils.open_website(self.linkedin_url),
        )
        self.linkedin_icon.grid(column=1, row=1, padx=(0, 0))

        self.site_icon = ctk.CTkButton(
            self.frame,
            image=website_icon,
            text="",
            fg_color="transparent",
            width=0,
            hover_color="#D9B46E",
            command=lambda: self.utils.open_website(self.site_url),
        )
        self.site_icon.grid(column=2, row=1, padx=(0, 0), sticky="w")

        self.illustration_label = ctk.CTkLabel(
            self.frame, image=illustration_image, text="", fg_color="transparent"
        )
        self.illustration_label.grid(
            column=0, row=6, pady=(60, 0), sticky="nsew", columnspan=3
        )

        # widgets referentes ao frame 2
        self.frame2 = ctk.CTkFrame(
            self, width=410, height=450, corner_radius=20, fg_color="white"
        )
        self.frame2.grid(column=1, row=0, pady=(10, 1), padx=(0, 10), sticky="nsew")

        # Configuração das colunas e linhas do frame 2
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure((1, 10), weight=1)

        self.sign_up_text = ctk.CTkLabel(
            self.frame2,
            text="Você não tem uma conta?",
            text_color="black",
            width=5,
            font=self.appearance_manager.get_font_body(),
        )
        self.sign_up_text.grid(column=0, row=0, padx=(10, 10), pady=(5, 0), sticky="e")

        self.sign_up = ctk.CTkButton(
            self.frame2,
            text="CADASTRE-SE",
            font=self.appearance_manager.get_font_body(True),
            text_color="white",
            fg_color="#558FAD",
            hover_color="#D9B46E",
            command=self.create_user_view,
        )
        self.sign_up.grid(column=1, row=0, padx=(10, 10), pady=(5, 0), sticky="w")

        self.welcome_label = ctk.CTkLabel(
            self.frame2,
            text="BEM-VINDO DE VOLTA",
            font=self.appearance_manager.get_font_title(),
            text_color="black",
        )
        self.welcome_label.grid(column=0, row=2, padx=(60, 0), pady=(0, 0), sticky="w")

        self.welcome2_label = ctk.CTkLabel(
            self.frame2,
            text="Acesse sua conta",
            font=self.appearance_manager.get_font_subtitle(),
            text_color="black",
        )
        self.welcome2_label.grid(
            column=0, row=3, padx=(60, 0), pady=(0, 40), sticky="w"
        )

        self.login_text = ctk.CTkLabel(
            self.frame2,
            text="Login",
            font=self.appearance_manager.get_font_subtitle(),
            text_color="black",
        )
        self.login_text.grid(column=0, row=4, padx=(65, 0), pady=(5, 3), sticky="w")

        self.login_entry = ctk.CTkEntry(
            self.frame2,
            placeholder_text="Digite seu login",
            fg_color="white",
            text_color="black",
            placeholder_text_color="gray",
            height=43,
            width=300,
            border_color="gray80",
            font=self.appearance_manager.get_font_body(),
        )
        self.login_entry.grid(column=0, row=5, padx=(60, 0), pady=(0, 5), sticky="w")

        self.password_text = ctk.CTkLabel(
            self.frame2,
            text="Senha",
            text_color="black",
            font=self.appearance_manager.get_font_subtitle(),
        )
        self.password_text.grid(column=0, row=6, padx=(65, 0), pady=(5, 3), sticky="w")

        self.password_entry = ctk.CTkEntry(
            self.frame2,
            placeholder_text="Digite sua senha",
            fg_color="white",
            text_color="black",
            placeholder_text_color="gray",
            height=43,
            width=300,
            border_color="gray80",
            show="*",
            font=self.appearance_manager.get_font_body(),
        )
        self.password_entry.grid(column=0, row=7, padx=(60, 0), pady=(0, 3), sticky="w")

        self.show_password_check = ctk.CTkCheckBox(
            self.frame2,
            text="",
            command=lambda: self.show_password(self.password_entry),
            height=43,
            fg_color="#D9B46E",
            hover_color="#D9B46E",
        )
        self.show_password_check.grid(
            column=0, row=7, padx=(370, 0), pady=(5, 5), sticky="w"
        )

        # self.forget_password = ctk.CTkButton(self.frame2, text="Esqueceu sua senha?", text_color="black",
        #                                      font=self.appearance_manager.get_font_body(), fg_color="transparent",
        #                                      hover_color="#D9B46E")
        # self.forget_password.grid(column=0, row=8, padx=(60, 0), pady=(0, 5), sticky="w")

        self.login_button = ctk.CTkButton(
            self.frame2,
            text="Entrar",
            height=43,
            width=140,
            font=self.appearance_manager.get_font_subtitle(True),
            text_color="white",
            fg_color="#558FAD",
            hover_color="#D9B46E",
            command=self.login,
        )
        self.login_button.grid(column=0, row=9, padx=(60, 0), pady=(5, 5), sticky="w")
        self.login_button.bind("<Return>", self.login_enter_key)

        self.database_status = ctk.CTkButton(
            self.frame2,
            image=alert_icon,
            anchor="w",
            text="",
            text_color="blue",
            fg_color="transparent",
            hover_color="#D9B46E",
            font=self.appearance_manager.get_font_body(),
            command=self.create_database_view,
        )
        self.database_status.grid(
            column=0, row=10, pady=(50, 5), columnspan=3, sticky="s"
        )

    def create_database_view(self):
        self.utils.restart_interface(self.frame2)

        # Configuração das colunas e linhas do frame 2
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure((1, 5), weight=1)

        self.back_button = ctk.CTkButton(
            self.frame2,
            text="",
            width=0,
            image=back_icon,
            fg_color="#558FAD",
            hover_color="#D9B46E",
            command=self.back,
        )
        self.back_button.grid(column=0, row=0, padx=(10, 10), pady=(5, 0), sticky="w")

        self.create_db_label = ctk.CTkLabel(
            self.frame2,
            text="CRIAR NOVO BANCO DE DADOS",
            font=self.appearance_manager.get_font_title(),
            text_color="black",
        )
        self.create_db_label.grid(
            column=0, row=2, padx=(60, 0), pady=(0, 0), sticky="w"
        )
        warning_text = """
        Propósito do Banco de Dados:
        Este banco de dados foi criado para armazenar informações importantes para o funcionamento do sistema, como dados de usuários, produtos, módulos e clientes. Ele permite que o sistema gerencie eficientemente essas informações, garantindo uma melhor experiência de uso.

        Segurança dos Dados:
        É crucial manter os dados seguros e protegidos contra acessos não autorizados. Por isso, recomendamos utilizar senhas fortes, criptografia e realizar backups regulares dos dados para evitar perdas.

        Estrutura do Banco de Dados:
        O banco de dados possui diversas tabelas, incluindo Usuarios, Produtos, Modulos e Clientes. Cada tabela tem seus próprios campos que armazenam informações específicas. Por exemplo, a tabela Usuarios armazena informações como usuário, email e senha.

        Backup e Recuperação:
        Realizar backups regulares do banco de dados é fundamental para garantir a integridade dos dados. Em caso de falha ou perda de dados, os backups podem ser utilizados para realizar a recuperação das informações perdidas.

        Manutenção e Atualizações:
        Manter o banco de dados atualizado e realizar manutenções regulares são práticas essenciais para garantir seu bom funcionamento. Isso inclui otimizações de desempenho e aplicação de atualizações de segurança.

        Escalabilidade:
        É importante considerar a capacidade do banco de dados de lidar com um aumento no volume de dados e usuários ao longo do tempo. Certifique-se de planejar para escalabilidade futura, adotando práticas que facilitem a expansão do sistema conforme necessário.

        Ferramentas e Recursos Disponíveis:
        Existem diversas ferramentas e recursos disponíveis para gerenciar e administrar o banco de dados, como interfaces gráficas e frameworks de desenvolvimento. Além disso, a documentação oficial pode ser uma fonte valiosa de informações e suporte.

        Compatibilidade:
        Este banco de dados foi desenvolvido para ser compatível com diferentes sistemas operacionais e tecnologias. Certifique-se de verificar os requisitos de compatibilidade específicos para garantir uma integração adequada com o seu ambiente de trabalho.

        Suporte e Comunidade:
        Caso precise de suporte adicional ou queira interagir com outros usuários, existem fóruns de discussão, documentação oficial e recursos de treinamento disponíveis para ajudá-lo. Não hesite em buscar ajuda sempre que necessário.
        """
        self.warning_text_box = ctk.CTkTextbox(
            self.frame2,
            fg_color="transparent",
            font=self.appearance_manager.get_font_body(bold=True),
            width=500,
            height=310,
        )
        self.warning_text_box.grid(column=0, row=3, padx=(10, 0), pady=(0, 40))

        self.warning_text_box.insert("0.0", warning_text)
        self.warning_text_box.configure(
            state="disabled",
            text_color="black",
            border_color="black",
            corner_radius=5,
            wrap="word",
            fg_color="#D9B46E",
        )

        self.create_db_button = ctk.CTkButton(
            self.frame2,
            text="Criar",
            height=43,
            width=140,
            font=self.appearance_manager.get_font_subtitle(True),
            text_color="white",
            fg_color="#558FAD",
            hover_color="#D9B46E",
            command=self.create_database_dialog,
        )
        self.create_db_button.grid(
            column=0, row=4, padx=(60, 0), pady=(5, 5), sticky="w"
        )

        self.database_status = ctk.CTkLabel(
            self.frame2,
            anchor="w",
            text="Atualizar local do seu banco de dados",
            text_color="black",
            fg_color="transparent",
            font=self.appearance_manager.get_font_subtitle(),
        )

        self.database_status.grid(
            column=0, row=5, padx=(60, 0), pady=(50, 5), columnspan=3, sticky="w"
        )

        self.search_database = ctk.CTkButton(
            self.frame2,
            image=view_icon,
            width=0,
            anchor="w",
            text="Procurar",
            height=43,
            font=self.appearance_manager.get_font_subtitle(True),
            text_color="white",
            fg_color="#558FAD",
            hover_color="#D9B46E",
            command=self.search_database_dialog,
        )
        self.search_database.grid(
            column=0, row=5, padx=(0, 20), pady=(50, 5), columnspan=3, sticky="e"
        )

    def create_user_view(self):
        self.utils.restart_interface(self.frame2)

        # Configuração das colunas e linhas do frame 2
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure((1, 10), weight=1)

        self.back_button = ctk.CTkButton(
            self.frame2,
            text="",
            width=0,
            image=back_icon,
            fg_color="#558FAD",
            hover_color="#D9B46E",
            command=self.back,
        )
        self.back_button.grid(column=0, row=0, padx=(10, 10), pady=(5, 0), sticky="w")

        self.create_user_label = ctk.CTkLabel(
            self.frame2,
            text="CRIE SUA CONTA",
            font=self.appearance_manager.get_font_title(),
            text_color="black",
        )
        self.create_user_label.grid(
            column=0, row=2, padx=(60, 0), pady=(0, 0), sticky="w"
        )

        self.create_user_label2 = ctk.CTkLabel(
            self.frame2,
            text="O nome de usuário deve conter apenas letras e números.\nSua senha deve conter 6 digitos e com caracteres\nespeciais (!$@%#)",
            font=self.appearance_manager.get_font_subtitle(),
            text_color="black",
            justify="left",
        )
        self.create_user_label2.grid(
            column=0, row=3, padx=(60, 0), pady=(0, 40), sticky="w"
        )

        self.login_text = ctk.CTkLabel(
            self.frame2,
            text="Usuario",
            font=self.appearance_manager.get_font_subtitle(),
            text_color="black",
        )
        self.login_text.grid(column=0, row=4, padx=(65, 0), pady=(5, 3), sticky="w")

        self.login_entry = ctk.CTkEntry(
            self.frame2,
            placeholder_text="Digite seu nome de usuario",
            fg_color="white",
            text_color="black",
            placeholder_text_color="gray",
            height=43,
            width=300,
            border_color="gray80",
            font=self.appearance_manager.get_font_body(),
        )
        self.login_entry.grid(column=0, row=5, padx=(60, 0), pady=(0, 5), sticky="w")

        self.password_text = ctk.CTkLabel(
            self.frame2,
            text="Senha",
            text_color="black",
            font=self.appearance_manager.get_font_subtitle(),
        )
        self.password_text.grid(column=0, row=6, padx=(65, 0), pady=(5, 3), sticky="w")

        self.password_entry = ctk.CTkEntry(
            self.frame2,
            placeholder_text="Digite sua senha",
            fg_color="white",
            text_color="black",
            placeholder_text_color="gray",
            height=43,
            width=300,
            border_color="gray80",
            show="*",
            font=self.appearance_manager.get_font_body(),
        )
        self.password_entry.grid(column=0, row=7, padx=(60, 0), pady=(0, 3), sticky="w")

        self.password_confirmation_text = ctk.CTkLabel(
            self.frame2,
            text="Redigite sua senha",
            text_color="black",
            font=self.appearance_manager.get_font_subtitle(),
        )
        self.password_confirmation_text.grid(
            column=0, row=8, padx=(65, 0), pady=(5, 3), sticky="w"
        )

        self.password_confirmation_entry = ctk.CTkEntry(
            self.frame2,
            placeholder_text="Digite sua senha",
            fg_color="white",
            text_color="black",
            placeholder_text_color="gray",
            height=43,
            width=300,
            border_color="gray80",
            show="*",
            font=self.appearance_manager.get_font_body(),
        )
        self.password_confirmation_entry.grid(
            column=0, row=9, padx=(60, 0), pady=(0, 3), sticky="w"
        )

        self.show_password_check = ctk.CTkCheckBox(
            self.frame2,
            text="",
            command=lambda: self.show_password(self.password_confirmation_entry),
            height=43,
            fg_color="#D9B46E",
            hover_color="#D9B46E",
        )
        self.show_password_check.grid(
            column=0, row=9, padx=(370, 0), pady=(5, 5), sticky="w"
        )

        self.create_user_button = ctk.CTkButton(
            self.frame2,
            text="Criar",
            height=43,
            width=140,
            font=self.appearance_manager.get_font_subtitle(True),
            text_color="white",
            fg_color="#558FAD",
            hover_color="#D9B46E",
            command=self.create_newuser,
        )
        self.create_user_button.grid(
            column=0, row=10, padx=(60, 0), pady=(5, 5), sticky="w"
        )
        self.create_user_button.bind("<Return>", self.login_enter_key)

        self.password_entry.bind(
            "<KeyRelease>",
            lambda event: self.utils.validate_password(
                self.password_entry.get(),
                self.password_confirmation_entry.get(),
                self.password_text,
                self.password_confirmation_text,
                event,
            ),
        )
        self.password_confirmation_entry.bind(
            "<KeyRelease>",
            lambda event: self.utils.validate_password(
                self.password_entry.get(),
                self.password_confirmation_entry.get(),
                self.password_text,
                self.password_confirmation_text,
                event,
            ),
        )
        self.login_entry.bind(
            "<KeyRelease>",
            lambda event: self.utils.validate_username(
                self.login_entry.get(), self.login_text, event
            ),
        )

    def create_newuser(self):
        password_confirmation = self.utils.validate_password(
            self.password_entry.get(),
            self.password_confirmation_entry.get(),
            self.password_text,
            self.password_confirmation_text,
        )
        username_confirmation = self.utils.validate_username(
            self.login_entry.get(), self.login_text
        )

        if password_confirmation and username_confirmation:
            is_valid = self.controller.validade_create_newuser(self.login_entry.get())
            usercount = self.model.user_count()
            acesso = "ADM" if usercount == 0 else "USUARIO"
            if is_valid:
                password = self.utils.encrypt_password(
                    self.password_confirmation_entry.get()
                )
                self.model.create_newuser(
                    self.login_entry.get(), password, acesso=acesso
                )
                self.utils.msgbox(
                    "Criar usuario",
                    f"Usuario {self.login_entry.get()} criado com sucesso!!!",
                    0,
                )
                self.login_entry.delete(0, "end")
                self.password_entry.delete(0, "end")
                self.password_confirmation_entry.delete(0, "end")

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

        try:
            # Desativando o botão de login se a conexão com o banco de dados falhar
            if status[0] == False:
                print(status)
                # self.forget_password.configure(state="disabled")
                self.sign_up.configure(state="disabled")
                self.login_button.configure(state="disabled")
                self.database_status.configure(text_color="red")
            else:
                self.login_button.configure(state="normal")
                self.database_status.configure(state="disabled")
        except:
            pass

    def login(self):
        if self.controller.validate_login():
            self.utils.restart_interface(self)
            InterfaceMenu(self)

    def create_database_dialog(self):
        self.controller.create_database_and_set_path()

    def search_database_dialog(self):
        self.controller.search_database()

    def back(self):
        self.utils.restart_interface(self)
        self.login_view()
        self.update_status(self.db_status)
