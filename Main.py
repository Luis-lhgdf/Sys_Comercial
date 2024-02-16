from src.controllers.main_controller import MainController


def main():
    controller = MainController()
    db_connection = controller.model.db_connection()
    controller.login(db_connection)


if __name__ == "__main__":
    main()
