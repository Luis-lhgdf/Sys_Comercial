import pandas as pd
import random

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

columns = ["Módulo", "Seção", "Visualizar", "Novo", "Editar", "Remover"]
df = pd.DataFrame(data, columns=columns)
print(df)
