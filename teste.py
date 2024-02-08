import sqlite3

conexao =  sqlite3.connect('banco de dados\db_sys.db')
cursor = conexao.cursor()

cursor.execute("DELETE FROM Clientes")
conexao.commit()
resultado = cursor.fetchall()
print(resultado)
               
