import pandas as pd
import random

import mysql.connector
database = 'railway'
host = 'containers-us-west-1.railway.app'
port = 5474
user = 'root'
password = 'JThLpvacyDNwzFLPyLhX'

# Crie a conexão
conexao = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)





# Exemplo de dados aleatórios
modules = {
    "Estoque": {
        "ENTRADA": {},
        "SAIDA": {},
        "INVENTARIO": {}
    },
    "Cadastro": {
        "CAD ITEM": {},
        "CAD CLIENTE": {},
        "CAD USUARIO": {},
        "GERENCIAR USER": {}
    },
    "Agenda": {
        "AGENDA": {}
    },
    "Carteira": {
        "VENDAS": {},
        "FATURAMENTO": {}
    },
    "Finanças": {
        "DESPESAS": {},
        "OUTRAS RENDAS": {}
    },
    "Usuario": {
        "USUARIO": {}
    },
    "Configurações": {
        "CONFIGURACOES": {}
    }
}

for module_name, module_data in modules.items():
    for section_name in module_data.keys():
        section_data = {
            "Visualizar": random.choice(["liberado", "bloqueado"]),
            "Novo": random.choice(["liberado", "bloqueado"]),
            "Editar": random.choice(["liberado", "bloqueado"]),
            "Remover": random.choice(["liberado", "bloqueado"])
        }
        module_data[section_name] = section_data

# Criar DataFrame
data = []
for module_name, module_data in modules.items():
    for section_name, section_data in module_data.items():
        row = [module_name, section_name] + list(section_data.values())
        data.append(row)

columns = ["modulo", "submodulo", "Visualizar", "Novo", "Editar", "Remover"]
df = pd.DataFrame(data, columns=columns)

df['usuario'] = "luis"

df = df[["usuario", "modulo", "submodulo", "Visualizar", "Novo", "Editar", "Remover"]]
print(df)
for row in df.values:
    
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO modulos (usuario, modulo, submodulo, visualizar, novo, editar, remover)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, list(row))
    conexao.commit()
    print("tudo certo")




conexao.close()