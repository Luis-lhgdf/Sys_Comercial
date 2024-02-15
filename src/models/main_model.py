import sqlite3
import os
from src.utils.utils import Utilities

class MainModel:
    def __init__(self):

        self.file_name_db = os.path.join(os.path.dirname(os.path.realpath(__file__)), "src/data/database_location.txt")

        
        self.db_path = ''
        self.full_database_path = None
        self.db_connect = None
        self.db_cursor = None
        self.utils = Utilities()

    def find_database_path(self):
        try:
            with open(self.file_name_db, 'r') as file:
                database_path = file.read().strip()
                return database_path
        except FileNotFoundError:
            return ""

    def save_database_path(self, database_path):
        with open(self.file_name_db, 'w') as file:
            file.write(database_path)

    def db_connection(self):
        self.db_path = self.find_database_path()

        if not self.db_path:
            return (False, "Erro, Banco de dados não encontrado. Por favor, crie um novo ou atualize o local do arquivo.")

        self.full_database_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), self.db_path)

        try:
            self.db_connect = sqlite3.connect(database=self.full_database_path)
            self.db_cursor = self.db_connect.cursor()
            
            print("Conexão bem-sucedida ao banco de dados")
            return (True, "Conexão bem-sucedida ao banco de dados!")
        except sqlite3.Error as erro:
            return (False, str(erro) + ": Erro de conexão com o banco de dados")
                 
    def validate_login_db(self, login, password):

        if not self.db_connection():
            # Se a conexão não puder ser estabelecida, retorne False
            return False

        self.db_cursor.execute(
            "SELECT * FROM Usuarios WHERE usuario = ? AND senha = ? AND status = 'ATIVO'",
            (login, password)
        )
        resultado = self.db_cursor.fetchall()

        self.close_connection()

        # Verifique se há algum resultado retornado pela consulta SQL
        return bool(resultado)

    def close_connection(self):
        self.db_cursor.close()
        self.db_connect.close()
        print("Fechando conexão com o banco de dados")
    
    def get_user_info_list(self):

        self.db_cursor.execute("SELECT acesso FROM Usuarios WHERE usuario = ?", (self.usuario_logado,))
        self.acesso_usuario = self.db_cursor.fetchone()[0]

        self.db_cursor.execute("SELECT * FROM Modulos WHERE usuario = ?", (self.usuario_logado,))
        self.main_app.ModulosDoUsuario = self.db_cursor.fetchall()

        self.main_app.usuario_logado = self.usuario_logado
        self.main_app.acesso_usuario = self.acesso_usuario

    def on_login_success(self):
        print("bem vindo")