# Importando a classe MainController do módulo main_controller no pacote src.controllers.
from src.controllers.main_controller import MainController

# Definindo a função principal do programa.
def main():
    # Instanciando a classe MainController e armazenando-a na variável controller.
    controller = MainController()
    
    # Estabelecendo uma conexão com o banco de dados através do método db_connection() do objeto controller.
    db_connection = controller.model.db_connection()
    
    # Iniciando o processo de login, passando a conexão do banco de dados como argumento.
    controller.login(db_connection)

# Verificando se este arquivo está sendo executado diretamente como um script.
if __name__ == "__main__":
    # Chamando a função main se este arquivo estiver sendo executado diretamente.
    main()




