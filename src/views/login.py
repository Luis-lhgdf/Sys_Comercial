from src.views.icones import *


class InterfaceLogin:
    def __init__(self, root_login, main_app):
        self.Root_login = root_login
        self.main_app = main_app
        self.Root_login.title("Login")
        self.Root_login.geometry(f"400x430")
        # self.Root_login.resizable(False, False)

        self.conexao = self.main_app.ConexaoPrincipal
        background_login = ctk.CTkLabel(self.Root_login, text="", image=fundoLogin, width=400, height=450)
        background_login.place(relx=0.5, rely=0.5, anchor="center")

        def mostrar_senha():
            if self.MostrarSenha.get():
                self.SenhaDigitado.configure(show="")
            else:
                self.SenhaDigitado.configure(show="*")

        def ativar_enter(Event):
            self.fazer_login()

        painel = ctk.CTkButton(self.Root_login, width=320, height=370, corner_radius=2, fg_color="#242A5F",
                               bg_color="#242A5F", hover=False)
        painel.place(relx=0.5, rely=0.5, anchor="center")

        label_txt = ctk.CTkLabel(painel, text="", image=UsuarioIcon2, font=self.main_app.FontTitle,
                                 fg_color="transparent", bg_color="transparent")
        label_txt.place(relx=0.5, rely=0.1, anchor="center")

        label_txt = ctk.CTkLabel(painel, text="Bem Vindo", font=self.main_app.FontTitle, fg_color="transparent",
                                 bg_color="transparent", text_color="white")
        label_txt.place(relx=0.5, rely=0.17, anchor="center")

        self.LoginDigitado = ctk.CTkEntry(painel, placeholder_text="Digite seu login", text_color="black",
                                          fg_color="white", width=200, border_color="white")
        self.LoginDigitado.place(relx=0.5, rely=0.3, anchor='center')

        self.SenhaDigitado = ctk.CTkEntry(painel, placeholder_text="Digite sua senha", text_color="black",
                                          fg_color="white", width=200, show="*", border_color="white")
        self.SenhaDigitado.place(relx=0.5, rely=0.4, anchor='center')

        self.MostrarSenha = ctk.CTkCheckBox(painel, text="Mostrar senha", font=self.main_app.FontBody,
                                            command=mostrar_senha, text_color="white", border_color="white")
        self.MostrarSenha.place(relx=0.5, rely=0.5, anchor="center")

        self.BtEntrar = ctk.CTkButton(painel, text="Entrar", command=self.fazer_login, text_color="black",
                                      fg_color="white", hover_color="gray90")
        self.BtEntrar.place(relx=0.5, rely=0.6, anchor="center")
        self.BtEntrar.bind("<Return>", ativar_enter)

    def fazer_login(self):
        self.usuario_logado = self.LoginDigitado.get()
        self.senha_logado = self.SenhaDigitado.get()

        if len(self.usuario_logado) == 0 or len(self.senha_logado) == 0:
            self.main_app.msgbox("Login", "Preencha todos os campos", 0)
        else:
            cursor = self.conexao.cursor()
            # Utilize placeholders (?) para evitar injecão de SQL
            cursor.execute(
                "SELECT * FROM Usuarios WHERE usuario = ? AND senha = ? AND status = 'ATIVO'",
                (self.usuario_logado, self.senha_logado)
            )
            resultado = cursor.fetchall()

            if resultado:
                cursor.execute("SELECT acesso FROM Usuarios WHERE  usuario = ?", (self.usuario_logado,))
                self.acesso_usuario = cursor.fetchone()[0]

                cursor.execute("SELECT * FROM Modulos WHERE usuario = ?", (self.usuario_logado,))
                self.main_app.ModulosDoUsuario = cursor.fetchall()
                self.main_app.usuario_logado = self.usuario_logado
                self.main_app.acesso_usuario = self.acesso_usuario
                self.main_app.login_sucesso()
            else:
                self.main_app.msgbox("Login", "Login ou senha incorretos, Tente novamente", 0)
