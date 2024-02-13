from src.models.main_model import MainModel
from src.views.main_view import MainView

class MainController:
    def __init__(self, db_path):
        self.model = MainModel(db_path)
        self.view = MainView(self)

    def login(self, db_status):
        self.view.update_status(db_status[1])
        self.view.start_interface()


    def exit(self):
        pass  # Implemente a lógica de saída aqui
