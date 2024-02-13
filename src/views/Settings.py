from src.views.icones import *

class InterfaceConfiguracoes:

    def __init__(self, main_app, frame_resp):
        self.main_app = main_app
        self.frame_resp = frame_resp
        self.conexao = self.main_app.ConexaoPrincipal

        self.interface()

    def interface(self):
        self.frame_resp.grid_rowconfigure((0, 1), weight=0)
        self.frame_resp.grid_columnconfigure(0, weight=1)

        label_titulo = ctk.CTkLabel(self.frame_resp, text=f"CONFIGURAcÕES", fg_color="transparent",
                                    text_color=("black", "white"),
                                    font=self.main_app.SubTitle, corner_radius=6, anchor="w")
        label_titulo.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        painel_theme = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                     border_width=1,
                                     fg_color="transparent", hover=False)
        painel_theme.grid(row=1, column=0, sticky="nsew", padx=10, pady=(45, 5))

        label_theme = ctk.CTkLabel(painel_theme, text="Alterar tema", font=self.main_app.FontTitle,
                                   fg_color="transparent")
        label_theme.place(x=10, y=5)

        opcoes = ["blue", "green", "dark-blue", "personalizado"]
        valor_escolhido = self.main_app.themeAtual

        # Encontra a posicão do valor escolhido na lista
        indice_valor_escolhido = opcoes.index(valor_escolhido)

        # Reorganiza a lista colocando o valor escolhido no início
        opcoes = [valor_escolhido] + opcoes[:indice_valor_escolhido] + opcoes[indice_valor_escolhido + 1:]

        mudar_theme = ctk.CTkOptionMenu(painel_theme, font=self.main_app.FontBody, width=100,
                                        values=opcoes, command=self.main_app.theme)
        mudar_theme.place(x=10, y=50)
