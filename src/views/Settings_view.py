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
        self.screen_height = self.root.screen_height
        self.screen_wedth = self.root.screen_wedth
        self.interface()

    def interface(self):
        # Configuração do layout
        self.main_content.grid_rowconfigure(0, weight=0)
        self.main_content.grid_rowconfigure(1, weight=0)
        self.main_content.grid_rowconfigure(2, weight=0)
        self.main_content.grid_rowconfigure(3, weight=0)
        self.main_content.grid_columnconfigure(0, weight=1)

        # Opções de temas
        opcoes = ["blue", "green", "dark-blue", "personalizado"]
        valor_escolhido = self.appearance_manager.current_theme
        indice_valor_escolhido = opcoes.index(valor_escolhido)
        opcoes.insert(0, opcoes.pop(indice_valor_escolhido))

        # Título
        label_titulo = ctk.CTkLabel(
            self.main_content,
            text=f"CONFIGURAÇÕES",
            fg_color="transparent",
            font=self.appearance_manager.get_font_title(),
            corner_radius=6,
            anchor="w",
        )
        label_titulo.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        # Botões para alterar tema, cor do tema e escala
        self.create_panel_button(
            "Alterar tema", opcoes, self.appearance_manager.write_color_to_theme, row=1
        )
        self.create_panel_button(
            "Alterar cor do tema",
            ["system", "light", "dark"],
            self.appearance_manager.appearance_theme,
            row=2,
        )
        self.create_panel_button(
            "Alterar escala (zoom)",
            ["80%", "90%", "100%", "110%", "120%"],
            self.change_scaling_event,
            row=3,
        )

    def create_panel_button(self, text, values, command, row):
        painel_button = ctk.CTkButton(
            self.main_content,
            text=text,
            text_color=("black", "white"),
            font=self.appearance_manager.get_font_title(),
            width=self.screen_wedth - 210,
            height=90,
            border_width=1,
            fg_color="transparent",
            hover=False,
            anchor="nw",
        )
        painel_button.grid(row=row, column=0, sticky="nsew", padx=10, pady=(45, 5))

        option_menu = ctk.CTkOptionMenu(
            painel_button,
            font=self.appearance_manager.get_font_body(),
            width=150,
            values=values,
            command=command,
        )
        option_menu.place(x=10, y=50)

        update_button = ctk.CTkButton(
            painel_button, text="Atualizar", command=self.update_interface
        )
        update_button.place(x=200, y=50)

    def update_interface(self):
        resp = self.utils.msgbox(
            "Confirmação",
            "Para realizar esata ação sera necessario realizar o Login novavemnte, Deseja Continuar?",
            3,
        )
        if resp == 6:
            self.root.update_window_menu()

    def change_scaling_event(self, new_scaling: str):

        try:

            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            ctk.set_widget_scaling(new_scaling_float)

        except:
            pass
