from src.views.icones import *
from ..models.carregar_img import CarregarIMG
from src.views.icones import *

class InterfaceMenu:
    def __init__(self, root):
        self.root = root
        # Configuração inicial da janela principal
        self.root.title("SYS COMERCIAL")  # Define o título da janela
        self.root.state('zoomed')  # Maximiza a janela ao abrir
        self.root.resizable(True, True)

        # redefinindo as cores do fg_color para as cores que esta no arquivo de temas json
        self.root.configure(fg_color=self.root.appearance_manager.json_fgcolor(self.root.appearance_manager.current_theme,"CTk","fg_color"))


        # Obtém as dimensões da tela
        self.screen_height = self.root.winfo_screenheight()
        self.screen_width = self.root.winfo_screenwidth()

        # Lista para armazenar os botões de navegação
        self.buttons_list = []                  

        # Configura a expansão horizontal da janela principal
        self.root.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.root.grid_columnconfigure(1, weight=0)  # Coluna 1 não se expandirá
        self.root.grid_columnconfigure(2, weight=1)  # Coluna 2 se expandirá

        # Configura a expansão vertical da janela principal
        self.root.grid_rowconfigure(0, weight=1)

        # Frame para os botões de navegação à esquerda
        self.navigation_frame = ctk.CTkFrame(self.root, width=176, corner_radius=0, fg_color="transparent")
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure((9,10,11), weight=1)

        # Frame para opções à direita (como ocultar menu)
        self.options_frame = ctk.CTkFrame(self.root, width=37, corner_radius=0, fg_color=self.root.appearance_manager.highlight_color)
        self.options_frame.grid(row=0, column=1, sticky="nsew")

        # Frame principal para exibição de conteúdo
        self.main_content = ctk.CTkFrame(self.root, fg_color="transparent", corner_radius=0)
        self.main_content.grid(row=0, column=2, sticky="nsew")

        # Botão para ocultar o menu lateral direito
        self.hide_button = ctk.CTkButton(self.options_frame, text="", image=menu_icon, anchor="w", width=23, height=23,
                                    fg_color="transparent", text_color=("black", "white"))

        self.load_module_buttons()
   
    def load_module_buttons(self):

        self.profile_photo = ctk.CTkButton(self.navigation_frame, text="", image=profiledefault_icon, anchor="center", fg_color="transparent", width=0, corner_radius=10)
        self.profile_photo.grid(row=0, column=0, pady=10)


        button_info = [
            {"text": "Home", "image": home_icon, "anchor": "w", "width": 176, "corner_radius": 0,
            "fg_color": "transparent", "text_color": ("black", "white"), "command": None},
            {"text": "Estoque", "image": stock_icon, "anchor": "w", "width": 176, "corner_radius": 0,
            "fg_color": "transparent", "text_color": ("black", "white"), "command": None},
            {"text": "Cadastro", "image": register_icon, "anchor": "w", "width": 176, "corner_radius": 0,
            "fg_color": "transparent", "text_color": ("black", "white"), "command": None},
            {"text": "Agenda", "image": agenda_icon, "anchor": "w", "width": 176, "corner_radius": 0,
            "fg_color": "transparent", "text_color": ("black", "white"), "command": None},
            {"text": "Carteira", "image": wallet_icon, "anchor": "w", "width": 176, "corner_radius": 0,
            "fg_color": "transparent", "text_color": ("black", "white"), "command": None},
            {"text": "Financas", "image": finance_icon, "anchor": "w", "width": 176, "corner_radius": 0,
            "fg_color": "transparent", "text_color": ("black", "white"), "command": None},
            {"text": "Usuario", "image": user_icon, "anchor": "w", "width": 176, "corner_radius": 0,
            "fg_color": "transparent", "text_color": ("black", "white"), "command": None},
            {"text": "Configuracoes", "image": settings_icon, "anchor": "w", "width": 176, "corner_radius": 0,
            "fg_color": "transparent", "text_color": ("black", "white"), "command": None}
        ]

        for index, info in enumerate(button_info):
            button = ctk.CTkButton(self.navigation_frame,
                text=info["text"],
                image=info["image"],
                anchor=info['anchor'],
                width=info['width'],
                corner_radius=info['corner_radius'],
                fg_color=info['fg_color'],
                text_color=info['text_color'],
                command=info["command"])
            
            button.grid(row=index+1, column=0, pady=5)

            self.buttons_list.append(button)
            

        self.your_logo = ctk.CTkLabel(self.navigation_frame, text="", image=your_logo2, anchor="center")
        self.your_logo.grid(row=len(button_info)+1, column=0, pady=0, sticky="s")

        self.scaling_optionemenu = ctk.CTkOptionMenu(self.navigation_frame,
            font=self.root.appearance_manager.get_font_body(),
            width=150,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.root.appearance_manager.change_scaling_event)
        
        self.scaling_optionemenu.grid(row=len(button_info) + 2, column=0, pady=(0,50), sticky="s", rowspan=2)

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.navigation_frame,
            font=self.root.appearance_manager.get_font_body(),
            width=150,
            values=["system", "light", "Dark"],
            command= self.root.appearance_manager.appearance_theme)
        
        self.appearance_mode_optionemenu.grid(row=len(button_info) + 3, column=0, pady=0, sticky="s")

                
