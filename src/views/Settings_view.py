from src.views.icones import *
from ..models.carregar_img import CarregarIMG
from src.views.icones import *
from src.models.main_model import MainModel
from src.views.appearance_manager import AppearanceManager
from src.utils.utils import Utilities


class InterfaceSettings:

    def __init__(
        self, root, user, module, submodule, visualizar, novo, editar, remover, id_user
    ):
        self.root = root
        self.main_content = self.root.main_content
        self.model = MainModel()
        self.utils = Utilities()
        self.appearance_manager = AppearanceManager()

        self.interface()

    def interface(self):

        self.main_content.grid_rowconfigure((0, 1), weight=0)
        self.main_content.grid_columnconfigure(0, weight=1)

        label_titulo = ctk.CTkLabel(
            self.main_content,
            text=f"CONFIGURACÕES",
            fg_color="transparent",
            text_color=("black", "white"),
            font=self.appearance_manager.get_font_title(),
            corner_radius=6,
            anchor="w",
        )
        label_titulo.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        painel_theme = ctk.CTkButton(
            self.main_content,
            text="Alterar tema",
            font=self.appearance_manager.get_font_title(),
            height=90,
            border_width=1,
            fg_color="transparent",
            hover=False,
            anchor="nw",
        )
        painel_theme.grid(row=1, column=0, sticky="nsew", padx=10, pady=(45, 5))

        opcoes = ["blue", "green", "dark-blue", "personalizado"]

        valor_escolhido = self.appearance_manager.current_theme

        # Encontra a posicão do valor escolhido na lista
        indice_valor_escolhido = opcoes.index(valor_escolhido)

        # Reorganiza a lista colocando o valor escolhido no início
        opcoes = (
            [valor_escolhido]
            + opcoes[:indice_valor_escolhido]
            + opcoes[indice_valor_escolhido + 1 :]
        )

        mudar_theme = ctk.CTkOptionMenu(
            painel_theme,
            font=self.appearance_manager.get_font_body(),
            width=100,
            values=opcoes,
            command=self.appearance_manager.write_color_to_theme,
        )
        mudar_theme.place(x=10, y=50)

        bt = ctk.CTkButton(
            painel_theme, text="Atualizar", command=self.update_interface
        )
        bt.place(x=200, y=50)

    def update_interface(self):
        self.root.update_window_menu()
