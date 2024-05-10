from src.views.icones import *
from ..models.carregar_img import CarregarIMG
from src.views.icones import *
from src.models.main_model import MainModel
from src.utils.utils import Utilities
from src.views.Settings_view import InterfaceSettings
from src.views.appearance_manager import AppearanceManager


class InterfaceMenu:
    def __init__(self, root):
        self.root = root
        self.model = MainModel()
        self.appearance_manager = AppearanceManager()
        self.info_list_user = self.root.info_list_user
        self.utils = Utilities()

        # Configuração inicial da janela principal
        self.root.title("SYS COMERCIAL")  # Define o título da janela
        self.root.state("zoomed")  # Maximiza a janela ao abrir
        self.root.resizable(True, True)

        # redefinindo as cores do fg_color para as cores que esta no arquivo de temas json
        self.root.configure(
            fg_color=self.appearance_manager.json_fgcolor(
                self.appearance_manager.current_theme, "CTk", "fg_color"
            )
        )

        # Obtém as dimensões da tela
        self.screen_height = self.root.winfo_screenheight()
        self.screen_width = self.root.winfo_screenwidth()

        # Lista para armazenar os botões de navegação finalizados
        self.buttons_list = []

        self.buttons_list_text = (
            []
        )  # armazena apenas os texts dos botoes do menu lateral

        self.button_info = (
            {}
        )  # armazena um dicionario com os atributos e valores para criar os botoes ctk

        # Configura a expansão horizontal da janela principal
        self.root.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.root.grid_columnconfigure(1, weight=1)  # Coluna 1 se expandirá

        # Configura a expansão vertical da janela principal
        self.root.grid_rowconfigure(0, weight=1)

        # Frame para os botões de navegação à esquerda
        self.menu_navigation_frame = ctk.CTkFrame(self.root, width=176, corner_radius=0)
        self.menu_navigation_frame.grid(row=0, column=0, sticky="nsew")

        # Frame principal para exibição de conteúdo
        self.main_content = ctk.CTkFrame(
            self.root, fg_color="transparent", corner_radius=0
        )
        self.main_content.grid(row=0, column=1, sticky="nsew")

        self.load_module_buttons()

    def load_module_buttons(self):

        # Botão para ocultar o menu lateral direito
        self.hide_button = ctk.CTkButton(
            self.menu_navigation_frame,
            text="",
            image=menu_icon,
            anchor="w",
            width=23,
            height=23,
            fg_color="transparent",
            text_color=("black", "white"),
            command=self.hide_menu_navigation,
        )

        self.hide_button.grid(row=0, column=0, pady=10, sticky="w")

        self.profile_photo = ctk.CTkButton(
            self.menu_navigation_frame,
            text="",
            image=profiledefault_icon,
            anchor="center",
            fg_color="transparent",
            width=0,
            corner_radius=10,
        )
        self.profile_photo.grid(row=1, column=0, pady=10)

        self.button_info = {
            "Home": [
                {
                    "text": "Home",
                    "image": home_icon,
                    "anchor": "w",
                    "width": 176,
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ("black", "white"),
                    "command": self.home,
                }
            ],
            "Estoque": [
                {
                    "text": "Estoque",
                    "image": stock_icon,
                    "anchor": "w",
                    "width": 176,
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ("black", "white"),
                    "command": lambda: self.show_submenus("Estoque"),
                    "submodules": [
                        {
                            "Entrada": [
                                entry_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Estoque", "ENTRADA"
                                ),
                            ],
                            "Saida": [
                                exit_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Estoque", "SAIDA"
                                ),
                            ],
                            "Inventario": [
                                inventory_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Estoque", "INVENTARIO"
                                ),
                            ],
                        }
                    ],
                }
            ],
            "Cadastro": [
                {
                    "text": "Cadastro",
                    "image": register_icon,
                    "anchor": "w",
                    "width": 176,
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ("black", "white"),
                    "command": lambda: self.show_submenus("Cadastro"),
                    "submodules": [
                        {
                            "Cadastrar Itens": [
                                item_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Cadastro", "CAD ITEM"
                                ),
                            ],
                            "Cadastrar Clientes": [
                                register_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Cadastro", "CAD CLIENTE"
                                ),
                            ],
                            "Cadastrar Usuario": [
                                user_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Cadastro", "CAD USUARIO"
                                ),
                            ],
                            "Gerenciar Usuarios": [
                                manage_user_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Cadastro", "GERENCIAR USER"
                                ),
                            ],
                        }
                    ],
                }
            ],
            "Agenda": [
                {
                    "text": "Agenda",
                    "image": agenda_icon,
                    "anchor": "w",
                    "width": 176,
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ("black", "white"),
                    "command": lambda: self.check_permission_and_redirect(
                        self.info_list_user, "Agenda"
                    ),
                }
            ],
            "Carteira": [
                {
                    "text": "Carteira",
                    "image": wallet_icon,
                    "anchor": "w",
                    "width": 176,
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ("black", "white"),
                    "command": lambda: self.show_submenus("Carteira"),
                    "submodules": [
                        {
                            "Registrar Vendas": [
                                sales_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Carteira", "VENDAS"
                                ),
                            ],
                            "Faturamento": [
                                income_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Carteira", "FATURAMENTO"
                                ),
                            ],
                        }
                    ],
                }
            ],
            "Financas": [
                {
                    "text": "Financas",
                    "image": finance_icon,
                    "anchor": "w",
                    "width": 176,
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ("black", "white"),
                    "command": lambda: self.show_submenus("Financas"),
                    "submodules": [
                        {
                            "Registrar Despesas": [
                                expense_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Financas", "DESPESAS"
                                ),
                            ],
                            "Outras Rendas +": [
                                revenue_icon,
                                lambda: self.check_permission_and_redirect(
                                    self.info_list_user, "Financas", "OUTRAS RENDAS"
                                ),
                            ],
                        }
                    ],
                }
            ],
            "Usuario": [
                {
                    "text": "Usuario",
                    "image": user_icon,
                    "anchor": "w",
                    "width": 176,
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ("black", "white"),
                    "command": lambda: self.check_permission_and_redirect(
                        self.info_list_user, "Usuario"
                    ),
                }
            ],
            "Configuracoes": [
                {
                    "text": "Configuracoes",
                    "image": settings_icon,
                    "anchor": "w",
                    "width": 176,
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ("black", "white"),
                    "command": lambda: self.check_permission_and_redirect(
                        self.info_list_user, "Configuracoes"
                    ),
                }
            ],
        }

        for module, buttons_info in self.button_info.items():
            for info in buttons_info:
                button = ctk.CTkButton(
                    self.menu_navigation_frame,
                    text=info["text"],
                    image=info["image"],
                    anchor=info["anchor"],
                    width=info["width"],
                    corner_radius=info["corner_radius"],
                    fg_color=info["fg_color"],
                    text_color=info["text_color"],
                    command=info["command"],
                )

                self.buttons_list.append(button)
                self.buttons_list_text.append(button._text)
                button.grid(row=len(self.buttons_list) + 2, column=0, pady=5)

                if "submodules" in info:
                    for submodulo in [info["submodules"][0]]:
                        for key, value in submodulo.items():
                            icon = value[0]
                            command = value[1]
                            button = ctk.CTkButton(
                                self.menu_navigation_frame,
                                text=key,
                                anchor="w",
                                width=info["width"],
                                image=icon,
                                corner_radius=info["corner_radius"],
                                fg_color=["#FFF5DE", "#175776"],
                                text_color=info["text_color"],
                                command=command,
                            )

                            self.buttons_list.append(button)
                            self.buttons_list_text.append(button._text)
                            button.grid(
                                row=len(self.buttons_list) + 2, column=0, pady=0
                            )
                            button.grid_remove()

        self.your_logo = ctk.CTkLabel(
            self.menu_navigation_frame, text="", image=your_logo2, anchor="center"
        )
        self.your_logo.grid(
            row=len(self.buttons_list) + 3, column=0, pady=0, sticky="s"
        )

        self.scaling_optionemenu = ctk.CTkOptionMenu(
            self.menu_navigation_frame,
            font=self.root.appearance_manager.get_font_body(),
            width=150,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.root.appearance_manager.change_scaling_event,
        )

        self.scaling_optionemenu.grid(
            row=len(self.buttons_list) + 4,
            column=0,
            pady=(0, 50),
            sticky="s",
            rowspan=2,
        )

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(
            self.menu_navigation_frame,
            font=self.root.appearance_manager.get_font_body(),
            width=150,
            values=["system", "light", "Dark"],
            command=self.root.appearance_manager.appearance_theme,
        )

        self.appearance_mode_optionemenu.grid(
            row=len(self.buttons_list) + 5, column=0, pady=0, sticky="s"
        )

        self.menu_navigation_frame.grid_rowconfigure(
            (len(self.buttons_list) + 4, len(self.buttons_list) + 5), weight=1
        )

    def show_submenus(self, module):

        for info in self.button_info.get(module, []):
            if "submodules" in info:
                for submodulo in info["submodules"]:
                    for key in submodulo.keys():
                        for button in self.buttons_list:
                            if button._text == key:
                                if button.grid_info():
                                    button.grid_remove()
                                else:
                                    button.grid()

    def hide_menu_navigation(self):
        # Verifica a largura atual do menu_navigation_frame

        current_width = self.menu_navigation_frame.winfo_width()

        if current_width in [141, 158, 176, 194, 211]:

            # Encolhe o menu
            new_width = 1

            for button in self.buttons_list:
                button.configure(width=new_width, text="")

            self.hide_button.configure(width=new_width)

            self.profile_photo.grid_remove()
            self.your_logo.grid_remove()
            self.scaling_optionemenu.grid_remove()
            self.appearance_mode_optionemenu.grid_remove()

        else:
            # Expande o menu
            new_width = current_width

            for i, button in enumerate(self.buttons_list):
                button.configure(width=176, text=self.buttons_list_text[i])

            self.hide_button.configure(width=1)
            self.profile_photo.grid()
            self.your_logo.grid()
            self.scaling_optionemenu.grid()
            self.appearance_mode_optionemenu.grid()

        # Atualiza a largura do menu_navigation_frame
        self.menu_navigation_frame.configure(width=new_width)

    def check_permission_and_redirect(
        self, user, selected_module, selected_submodulo=None
    ):

        tem_acesso, permissions = self.has_permission(
            user, selected_module, selected_submodulo
        )

        if tem_acesso:
            self.redirect_to_module(permissions)
        else:
            self.utils.msgbox(
                "Permissão", "Você nao tem acesso liberado para este modulo", 0
            )

    def has_permission(self, user_info, module_name, selected_submodulo=None):
        for module_data in user_info[2]:
            if selected_submodulo is None:
                if module_data[2] == module_name:
                    permissions = module_data[4:8]
                    if all(perm == "bloqueado" for perm in permissions):
                        return False, []
                    else:
                        return True, module_data
            else:
                if (
                    module_data[2] == module_name
                    and module_data[3] == selected_submodulo
                ):
                    permissions = module_data[4:8]
                    if all(perm == "bloqueado" for perm in permissions):
                        return False, []
                    else:
                        return True, module_data
        return False, []

    def redirect_to_module(self, permissions):

        user, module, submodule, visualizar, novo, editar, remover, id_user = (
            permissions[1:]
        )

        self.utils.restart_interface(self.main_content)
        # Implemente a lógica para redirecionar o usuário para o módulo selecionado
        if module == "Configuracoes":
            InterfaceSettings(
                self,
                user,
                module,
                submodule,
                visualizar,
                novo,
                editar,
                remover,
                id_user,
            )

    def home(self):
        self.utils.restart_interface(self.main_content)
        text = ctk.CTkLabel(self.main_content, text="Bem vindo")
        text.grid(row=0, column=0, sticky="nsew")

    def update_window_menu(self):
        self.root.restart_menu()
