import sqlite3
import os

class MainModel:
    def __init__(self, db_path):
        self.db_path = db_path
        self.full_database_path = None
        self.db_connect = None

    def db_connection(self):
        self.full_database_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                                                   self.db_path)
        try:
            self.db_connect = sqlite3.connect(database=self.full_database_path)
            return (True, "Conexão bem-sucedida ao banco de dados!")
        except sqlite3.Error as erro:
            return (False, str(erro) + "\nErro de conexão com o banco banco de dados")


        