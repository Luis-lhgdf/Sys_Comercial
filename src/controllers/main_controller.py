from src.models.main_model import MainModel
from src.views.main_view import MainView
from src.utils.utils import Utilities


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

    def validate_create_db(self):
        password_get = self.view.password_bd_entry.get()
        password_confirmation_get = self.view.password_bd_confirmation_entry.get()

        if not password_get or not password_confirmation_get:
            self.utils.msgbox("Criar Banco de dados", "Preencha todos os campos", 0)
            

        

    def validate_password_db(self, event):
        password_entry = self.view.password_bd_entry.get()
        password_confirmation = self.view.password_bd_confirmation_entry.get()

        is_valid_password = self.utils.validate_password_strength(password_entry)
        is_valid_confirmation = self.utils.validate_password_match(password_entry, password_confirmation)

        self.utils.format_password_label(self.view.password_bd_text,["Senha válida", "Senha válida"], is_valid_password)
        self.utils.format_password_label(self.view.password_bd_confirmation_text,["Senhas Iguais", "Senhas Diferentes"], is_valid_confirmation)

        if is_valid_confirmation and is_valid_password:
            self.view.create_db_button.configure(state="normal")
        else:
            self.view.create_db_button.configure(state="disabled")
        



