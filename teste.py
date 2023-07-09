from PIL import Image, ImageTk
import customtkinter as ctk
import mysql.connector
import io

root = ctk.CTk()
root.geometry('500x500')

label = ctk.CTkLabel(root, text="")
label.pack()

# Defina as informações de conexão
database = 'railway'
host = 'containers-us-west-1.railway.app'
port = 5474
user = 'root'
password = 'JThLpvacyDNwzFLPyLhX'

# Crie a conexão
conexao = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
cursor = conexao.cursor()

# Buscar a imagem no banco de dados
cursor.execute(f"SELECT * FROM foto_perfil WHERE usuario = 'anubis'")
result = cursor.fetchone()

if result:
    # Converter o valor binário para imagem
    image_binary = result[2]  # A coluna 'img' é o índice 2 no resultado
    image = Image.open(io.BytesIO(image_binary))

    # Redimensionar manualmente a imagem para 500x500 pixels
    image = image.resize((500, 500))

    # Criar instância de CTkImage
    ctk_image = ctk.CTkImage(image)

    # Atualizar o widget Label com a nova imagem
    label.configure(image=ctk_image)
    label.image = ctk_image

    conexao.close()
else:
    print("não existe nenhuma img no banco de dados")

root.mainloop()
