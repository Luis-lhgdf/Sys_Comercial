import os

opcao = "tests"  # Substitua "minha_opcao" pela opção desejada
print("O diretório pai com a opção é:", os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), opcao))