from src.models.main_model import MainModel
from src.views.main_view import MainView
from src.utils.utils import Utilities
from customtkinter import filedialog

class MainController:
    def __init__(self):
        self.model = MainModel()
        self.view = MainView(self)
        self.utils = Utilities()

    def login(self, db_status):
        self.view.update_status(db_status)

        self.view.start_interface()

    def exit(self):
        resp = self.utils.msgbox("SAIR", "Deseja realmente encerrar o sistema?", 4)
        if resp == 6:
            self.model.close_connection()
            self.view.destroy()

    def validate_login(self):
        login_get = self.view.login_entry.get()
        password_get = self.view.password_entry.get()

        if not login_get or not password_get:
            self.utils.msgbox("Login", "Preencha todos os campos", 0)
            return

        if self.model.validate_login_db(login_get, password_get):
            self.model.on_login_success()
        else:
            self.utils.msgbox("Login", "Login ou senha incorretos, Tente novamente", 0)

    def create_database_and_set_path(self):
        db_path = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("Banco de Dados SQLite", "*.db")], initialfile="database_syscomercial.db")
        if db_path:
            self.model.crate_database(database_path=db_path)
            self.view.create_db_button.configure(text=f"Banco de dados criado com Sucesso:\n{db_path}", command=None)
            self.login(self.model.db_connection())

        



