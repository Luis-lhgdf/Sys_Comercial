import mysql.connector
database = 'railway'
host = 'containers-us-west-1.railway.app'
port = 5474
user = 'root'
password = 'JThLpvacyDNwzFLPyLhX'

# Crie a conexão
conexaoBD = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)

cursor = conexaoBD.cursor()

cursor.execute("select * from modulos where usuario = 'anubis'")
resultado = cursor.fetchall()

conexaoBD.close()
modulo = "Estoque"
submodulo = 'ENTRADA'

for tupla in resultado:
   if tupla[2] == modulo and tupla[3] == submodulo:
    if tupla[4] == "liberado" or tupla[5] == "liberado" or tupla[6] == "liberado" or tupla[7] == "liberado":
        print("liberado")
