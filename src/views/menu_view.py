from src.views.icones import *
from ..models.carregar_img import CarregarIMG
from src.views.icones import *

class InterfaceMenu:

    def __init__(self, root):
        self.root = root

        # self.conexao = self.main_app.ConexaoPrincipal

        self.root.title("SYS COMERCIAL")
        self.root.state('zoomed')

        self.screen_height = self.root.winfo_screenheight()
        self.screen_wedth = self.root.winfo_screenwidth()

        self.listaBTS = []

        # self.cor_destaque = self.main_app.chave_customjson("CTkButton", "hover_color")

        # Configure a expansão horizontal (caso necessário)
        self.root.grid_columnconfigure(0, weight=0)  # Coluna 0 não se expandirá
        self.root.grid_columnconfigure(1, weight=0)  # Coluna 1 não se expandirá
        self.root.grid_columnconfigure(2, weight=1)  # Coluna 2 se expandirá

        self.root.grid_rowconfigure((0, 1, 2), weight=1)

        self.frame_MenuLateralEsq = ctk.CTkFrame(self.root, width=176, corner_radius=0)
        self.frame_MenuLateralEsq.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.frame_MenuLateralEsq.grid_rowconfigure(10, weight=1)

        self.frame_MenuLateralDir = ctk.CTkFrame(self.root, width=37, corner_radius=0, fg_color="green")
        self.frame_MenuLateralDir.grid(row=0, column=1, rowspan=4, sticky="nsew")

        self.frame_resposta = ctk.CTkFrame(self.root, fg_color="transparent", corner_radius=0)
        self.frame_resposta.grid(row=0, column=2, rowspan=4, sticky="nsew")


        self.BtOcultar = ctk.CTkButton(self.frame_MenuLateralDir, text="", image=menu_icon, anchor="w", width=23,
                                       height=23,
                                       fg_color="transparent", text_color=("black", "white"))
        # self.bt_opcoes()
        # self.scaling_optionemenu.set("100%")
