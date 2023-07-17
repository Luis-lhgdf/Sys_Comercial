import mysql.connector
database = 'railway'
host = 'containers-us-west-1.railway.app'
port = 5474
user = 'root'
password = 'JThLpvacyDNwzFLPyLhX'

# Crie a conexão
conexaoBD = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)

cursor = conexaoBD.cursor()

cursor.execute("select * from modulos where usuario = 'anubis' ")
resultado = cursor.fetchall()

conexaoBD.close()

print(resultado)