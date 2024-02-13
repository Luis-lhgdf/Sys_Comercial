import ctypes
import json
import sqlite3

import pkg_resources

from src.views import login
from src.views import cliente
from src.views import configuracoes
from src.views import gerenciar_usuarios
from src.views import item
from src.views import menu
from src.views import novo_usuario
from src.views import usuario
from src.views.icones import *


# Carregar configuracões do arquivo JSON


def load_config(value: bool, localfile=False):
    local = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/config.json")

    try:
        with open(local, "r") as config_file:
            config = json.load(config_file)
            if value:
                return config
            else:
                if localfile:
                    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/personalizado.json")
                else:
                    return str(config["theme"]["default_theme"][0])

    except FileNotFoundError:
        return {
            "theme": {
                "default_theme": ["blue"]
            }
        }


# Salvar configuracões no arquivo JSON
def save_config(config):
    local = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/config.json")
    with open(local, "w") as config_file:
        json.dump(config, config_file, indent=4)

# Funcão para alterar e salvar o tema
def change_and_save_theme(new_theme):
    config = load_config(True)
    config["theme"]["default_theme"][0] = new_theme
    save_config(config)


class MainApp:

    @staticmethod
    def _conecta_bd(local_bd):

        try:
            # Conectar ao banco de dados
            conexao = sqlite3.connect(local_bd)
            print("Conexão bem-sucedida ao banco de dados")
            return conexao

        except sqlite3.Error as erro:
            print("Erro ao conectar-se ao banco de dados:", erro)
            return None

    def __init__(self, root_main):
        self.root = root_main
        self.root.title("SYS Comercial")
        self.root.geometry(f"400x430")
        self.root.protocol("WM_DELETE_WINDOW", self.sair)

        self.FontTitle = ctk.CTkFont(size=20, weight="bold")
        self.SubTitle = ctk.CTkFont(size=14, weight="bold")
        self.FontBody = ctk.CTkFont(size=12)

        self.validate_cmd_numeric = self.root.register(self.validate_numeric_input)
        self.validade_cmd_text = self.root.register(self.validate_text_input)

        self.screen_height = self.root.winfo_screenheight()
        self.screen_wedth = self.root.winfo_screenwidth()

        self.themeAtual = load_config(False, localfile=False)
        self.escala_atual = 1.0

        self.ModulosDoUsuario = None

        self.usuario_logado = None

        self.acesso_usuario = None

        self.paste_file = "data\db_sys.db"

        self.caminho_banco_de_dados = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                                                   self.paste_file)

        print(self.caminho_banco_de_dados)

        self.ConexaoPrincipal = MainApp._conecta_bd(self.caminho_banco_de_dados)

        self.login()

    def login(self):
        self.clear_screen()
        self.tela_login = login.InterfaceLogin(self.root, self)

    def login_sucesso(self):
        self.clear_screen()

        self.root.configure(fg_color=self.chave_customjson("CTk", "fg_color"))

        self.menu_lateral = menu.InterfaceMenu(self.root, self)
        # self.root.resizable(True, True)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    @staticmethod
    def destacar(lista, botao, cor, fg2="transparent"):
        for valor in lista:
            if valor == botao:
                if cor == "white":
                    botao.configure(fg_color=cor)
                else:
                    botao.configure(fg_color=cor)
            else:
                valor.configure(fg_color=fg2)

    @staticmethod
    def esconder_Janela(menu_lateral):

        largura_janela_atual = menu_lateral.winfo_width()

        if largura_janela_atual > 35:
            menu_lateral.configure(width=28)

        else:
            menu_lateral.configure(width=176)

    def exibir_gerenciarusuarios(self, frame_resposta):
        if self.acesso_usuario == "ADM":
            self.gerenciarusuarios = gerenciar_usuarios.InterfaceGerenciarUsuarios(self, frame_resp=frame_resposta)
        ctk.set_widget_scaling(self.escala_atual)

    def exibir_novoitem(self, frame_resposta):
        self.interface_Novoitem = item.InterfaceNovoItem(self, frame_resp=frame_resposta)

    # ctk.set_widget_scaling(self.escala_atual)

    def exibir_novocliente(self, frame_resposta):
        self.interface_NovoUsuario = cliente.InterfaceNovoCliente(self, frame_resp=frame_resposta)

    # ctk.set_widget_scaling(self.escala_atual)

    def exibir_novousuario(self, frame_resposta):
        self.interface_NovoUsuario = novo_usuario.InterfaceNovoUsuario(self, frame_resp=frame_resposta)
        # ctk.set_widget_scaling(self.escala_atual)

    def exibir_usuario(self, frame_resposta, bt_perfil):
        self.Interface_Usuario = usuario.InterfaceUsuario(self, frame_resposta, bt_perfil)
        # ctk.set_widget_scaling(self.escala_atual)

    def exibir_configuracoes(self, frame_resposta):
        self.Interface_Configuracoes = configuracoes.InterfaceConfiguracoes(self, frame_resposta)

    # ctk.set_widget_scaling(self.escala_atual)

    def chave_customjson(self, chave, valor):

        nome_do_pacote = "customtkinter"
        caminho_relativo = f"assets/themes/{self.themeAtual}.json"

        caminho_custom = pkg_resources.resource_filename(nome_do_pacote, caminho_relativo)

        caminho_temas = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/personalizado.JSON")

        try:
            with open(caminho_custom) as arquivo_json:
                data = json.load(arquivo_json)  # Carregue o conteúdo do arquivo JSON
        except FileNotFoundError:
            with open(caminho_temas) as arquivo_json:
                data = json.load(arquivo_json)

        info = data[f"{chave}"][f"{valor}"]
        return info

    @staticmethod
    def msgbox(title, text, style):
        #  Styles:
        #  0 : OK
        #  1 : OK | Cancel
        #  2 : Abort | Retry | Ignore
        #  3 : Yes | No | Cancel 6, 7, 2
        #  4 : Yes | No
        #  5 : Retry | Cancel
        #  6 : Cancel | Try Again | Continue
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    @staticmethod
    def aparencia(new_appearance_mode: str):
        # funcão que altera o modo de aparencia da janela entre light e dark
        ctk.set_appearance_mode(new_appearance_mode)

    def theme(self, new_appearance_mode: str):
        # funcão que altera o modo de aparencia da janela entre light e dark
        print(os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/personalizado.JSON"))
        if new_appearance_mode.lower() == "personalizado":
            ctk.set_default_color_theme(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), "temas/personalizado.JSON"))

        else:
            ctk.set_default_color_theme(new_appearance_mode)

        self.themeAtual = str(new_appearance_mode)
        change_and_save_theme(new_appearance_mode)
        self.login_sucesso()

    def change_scaling_event(self, new_scaling: str):
        try:
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            ctk.set_widget_scaling(new_scaling_float)
            self.escala_atual = new_scaling_float

            if new_scaling in ["110%"]:
                SeuLogo2.configure(size=(100, 100))
            elif new_scaling in ["120%"]:
                SeuLogo2.configure(size=(80, 80))
            else:
                SeuLogo2.configure(size=(130, 130))
        except ExcelIcon as erro:
            print(f"houve um erro ao mudar a escala {erro}")
            pass

    def sair(self):
        resp = self.msgbox("SAIR", "Deseja realmente encerrar o sistema?", 4)
        if resp == 6:
            self.ConexaoPrincipal.close()
            self.root.destroy()

    @staticmethod
    def validate_numeric_input(P, max_length):
        # Verifica se P é vazio ou um número decimal válido
        return P == "" or P.replace(".", "", 1).isdigit() and len(P) <= int(max_length)

    @staticmethod
    def validate_text_input(P, max_length, allow_spaces=True):
        if allow_spaces:
            return P == "" or (isinstance(P, str) and P.replace(" ", "").isalpha() and len(P) <= int(max_length))
        else:
            return P == "" or (isinstance(P, str) and P.isalpha() and len(P) <= int(max_length))
