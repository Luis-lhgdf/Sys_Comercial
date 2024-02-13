from src.controllers.main_controller import MainController

def main():
    db_path = "dat/db_sys.db"  # Caminho para o banco de dados SQLite
    controller = MainController(db_path)
    db_connection = controller.model.db_connection()
    controller.login(db_connection)


if __name__ == "__main__":
    main()
