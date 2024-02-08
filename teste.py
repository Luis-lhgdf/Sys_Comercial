import os
import sqlite3

caminho_banco_de_dados = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Banco de dados")

if not os.path.exists(caminho_banco_de_dados + "\db_sys.db"):
    print("banco de dados nao existe!")
    print("criando seu banco de dados db_sys.db, aguarde...")
    conexao = sqlite3.connect(caminho_banco_de_dados + "\db_sys.db")
    cursor = conexao.cursor()

    # Cria tabela Usuários
    cursor.execute('''CREATE TABLE Usuarios (
                        id INTEGER PRIMARY KEY,
                        usuario TEXT,
                        email TEXT,
                        senha TEXT,
                        acesso TEXT,
                        imagem BLOB,
                        status TEXT
                    )''')

    # Cria tabela Produtos
    cursor.execute('''CREATE TABLE Produtos (
                        id INTEGER PRIMARY KEY,
                        descricao_produto TEXT,
                        unidade_medida TEXT,
                        valor_unitario REAL,
                        marca TEXT,
                        categoria TEXT,
                        peso REAL,
                        fornecedor TEXT,
                        info_adicionais TEXT
                    )''')

    # Cria tabela Módulos
    cursor.execute('''CREATE TABLE Modulos (
                        id INTEGER PRIMARY KEY,
                        usuario TEXT,
                        modulo TEXT,
                        submodulo TEXT,
                        visualizar INTEGER,
                        novo INTEGER,
                        editar INTEGER,
                        remover INTEGER,
                        id_usuario INTEGER
                    )''')

    # Cria tabela Clientes
    cursor.execute('''CREATE TABLE Clientes (
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
                    )''')

    # Comita as alterações e fecha a conexão
    conexao.commit()
    conexao.close()

    print("Banco de dados criado com sucesso em", caminho_banco_de_dados)
else:
    print("O banco de dados já existe em", caminho_banco_de_dados)

