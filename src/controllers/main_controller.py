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
        print("chamado função")
        pass  # Implemente a lógica de saída aqui

    def validate_login(self):
        login = self.view.login_entry.get()
        password = self.view.password_entry.get()

        if not login or not password:
            self.utils.msgbox("Login", "Preencha todos os campos", 0)
            return

        if self.model.validate_login_db(login, password):
            self.model.on_login_success()
        else:
            self.utils.msgbox("Login", "Login ou senha incorretos, Tente novamente", 0)

    