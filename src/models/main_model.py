import sqlite3
import os
from src.utils.utils import Utilities


class MainModel:
    def __init__(self):

        self.file_name_db = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
            "data/database_location.txt",
        )
        self.db_path = ""
        self.full_database_path = None
        self.db_connect = None
        self.db_cursor = None
        self.utils = Utilities()

        self.modules_database = {
            "Estoque": {
                "ENTRADA": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
                "SAIDA": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
                "INVENTARIO": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
            },
            "Cadastro": {
                "CAD ITEM": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
                "CAD CLIENTE": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
                "CAD USUARIO": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
                "GERENCIAR USER": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
            },
            "Agenda": {
                "AGENDA": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                }
            },
            "Carteira": {
                "VENDAS": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
                "FATURAMENTO": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
            },
            "Financas": {
                "DESPESAS": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
                "OUTRAS RENDAS": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                },
            },
            "Usuario": {
                "USUARIO": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                }
            },
            "Configuracoes": {
                "CONFIGURACOES": {
                    "visualizar": "bloqueado",
                    "novo": "bloqueado",
                    "editar": "bloqueado",
                    "remover": "bloqueado",
                }
            },
        }

    def find_database_path(self):
        try:
            with open(self.file_name_db, "r") as file:
                database_path = file.read().strip()
                return database_path
        except FileNotFoundError:
            return ""

    def save_database_path(self, database_path):
        with open(self.file_name_db, "w") as file:
            file.write(database_path)

    def db_connection(self):
        self.db_path = self.find_database_path()

        if not self.db_path or not os.path.exists(self.db_path):
            return (
                False,
                "Erro, Banco de dados não encontrado. Por favor, crie um novo ou atualize o local do arquivo.",
            )

        self.full_database_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))), self.db_path
        )

        try:
            self.db_connect = sqlite3.connect(database=self.full_database_path)
            self.db_cursor = self.db_connect.cursor()

            return True, "Conexão bem-sucedida ao banco de dados!"
        except sqlite3.Error as erro:
            return False, str(erro) + ": Erro de conexão com o banco de dados"

    def crate_database(self, database_path):

        conexao = sqlite3.connect(database_path)
        cursor = conexao.cursor()

        # Cria tabela Usuários
        cursor.execute(
            """CREATE TABLE Usuarios (
                            id INTEGER PRIMARY KEY,
                            usuario TEXT,
                            email TEXT,
                            senha TEXT,
                            acesso TEXT,
                            imagem BLOB,
                            status TEXT
                        )"""
        )

        # Cria tabela Produtos
        cursor.execute(
            """CREATE TABLE Produtos (
                            id INTEGER PRIMARY KEY,
                            descricao_produto TEXT,
                            unidade_medida TEXT,
                            valor_unitario REAL,
                            marca TEXT,
                            categoria TEXT,
                            peso REAL,
                            fornecedor TEXT,
                            info_adicionais TEXT
                        )"""
        )

        # Cria tabela Módulos
        cursor.execute(
            """CREATE TABLE Modulos (
                            id INTEGER PRIMARY KEY,
                            usuario TEXT,
                            modulo TEXT,
                            submodulo TEXT,
                            visualizar INTEGER,
                            novo INTEGER,
                            editar INTEGER,
                            remover INTEGER,
                            id_usuario INTEGER
                        )"""
        )

        # Cria tabela Clientes
        cursor.execute(
            """CREATE TABLE Clientes (
                            id INTEGER PRIMARY KEY,
                            tipo_de_cliente TEXT,
                            cpf TEXT,
                            cnpj TEXT,
                            email TEXT,
                            razao_social TEXT,
                            nome TEXT,
                            cep TEXT,
                            endereco TEXT,
                            numero TEXT,
                            complemento TEXT,
                            bairro TEXT,
                            cidade TEXT,
                            uf TEXT,
                            telefone TEXT,
                            celular TEXT,
                            questionario TEXT,
                            observacoes TEXT
                        )"""
        )

        # Comita as alterações e fecha a conexão
        conexao.commit()
        conexao.close()
        print(database_path)

        self.save_database_path(database_path=database_path)

    def validate_login_db(self, login, password):

        if not self.db_connection():
            # Se a conexão não puder ser estabelecida, retorne False
            return False

        self.db_cursor.execute(
            "SELECT * FROM Usuarios WHERE usuario = ? AND senha = ? AND status = 'ATIVO'",
            (login, password),
        )
        query_result = self.db_cursor.fetchall()

        self.close_connection()

        # Verifique se há algum resultado retornado pela consulta SQL
        return bool(query_result)

    def close_connection(self):
        try:
            self.db_cursor.close()
            self.db_connect.close()
            print("Fechando conexão com o banco de dados")
        except AttributeError:
            print("nao houve conexão com banco de dados, fechando aplicação")

    def get_user_info_list(self, usuario, list_user):
        self.db_connection()
        self.db_cursor.execute(
            "SELECT acesso FROM Usuarios WHERE usuario = ?", (usuario,)
        )
        list_user.append(usuario)
        list_user.append(self.db_cursor.fetchone()[0])

        self.db_cursor.execute("SELECT * FROM Modulos WHERE usuario = ?", (usuario,))
        list_user.append(self.db_cursor.fetchall())

    def on_login_success(self, login, list_user):
        self.get_user_info_list(usuario=login, list_user=list_user)

    def create_newuser(
        self, login, password, email=None, acesso="USUARIO", image=None, status="ATIVO"
    ):

        self.db_connection()
        self.db_cursor.execute(
            """INSERT INTO Usuarios (usuario, email, senha, acesso, imagem, status)
                VALUES (?, ?, ?, ?, ?, ?)""",
            (login, email, password, acesso, image, status),
        )
        self.db_connect.commit()

        # Obter o ID do usuário recém-inserido
        self.db_cursor.execute("SELECT last_insert_rowid()")
        id_usuario = self.db_cursor.fetchone()[0]

        # Iterar sobre os módulos e submódulos e inserir os registros na tabela Modulos
        for modulo, submodulos in self.modules_database.items():
            for submodulo, permissoes in submodulos.items():
                if acesso == "ADM":
                    visualizar = novo = editar = remover = "liberado"
                else:  # Se o usuário não for ADM, assume-se que é USUARIO
                    visualizar = novo = editar = remover = "bloqueado"
                    # No caso de módulo 'Usuario', liberamos as permissões
                    if modulo == "Usuario" and submodulo == "USUARIO":
                        visualizar = novo = editar = remover = "liberado"
                self.db_cursor.execute(
                    """
                    INSERT INTO Modulos (usuario, modulo, submodulo, visualizar, novo, editar, remover, id_usuario)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        login,
                        modulo,
                        submodulo,
                        visualizar,
                        novo,
                        editar,
                        remover,
                        id_usuario,
                    ),
                )
        self.db_connect.commit()
        self.close_connection()

    def user_count(self):
        self.db_connection()
        self.db_cursor.execute("SELECT * FROM Usuarios")
        query_result = self.db_cursor.fetchall()
        self.close_connection()
        return len(query_result)
