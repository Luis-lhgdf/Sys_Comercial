import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageDraw
import base64
import binascii
import io
from PIL import Image


class CarregarIMG:

    def __init__(self, main_app):

        self.main_app = main_app
        self.conexao = self.main_app.ConexaoPrincipal

    def verificar_foto(self, label_img, usuario):

        cursor = self.conexao.cursor()
        # Buscar a imagem no banco de dados
        cursor.execute(f"SELECT imagem FROM Usuarios where usuario = '{usuario}'")
        result = cursor.fetchone()

        if result[0] is not None:
            try:
                # Converter o valor binário para imagem
                image_binary = result[0]  # A coluna 'img' é o índice 2 no resultado
                image = Image.open(io.BytesIO(image_binary))

                # Redimensionar a imagem se necessário
                image = image.resize((100, 100))
                # Crie uma nova imagem circular de fundo transparente
                image_circular = Image.new("RGBA", image.size, (0, 0, 0, 0))

                # Crie um objeto de desenho
                draw = ImageDraw.Draw(image_circular)

                # Calcule as coordenadas do círculo
                center_x = image_circular.width // 2
                center_y = image_circular.height // 2
                radius = min(center_x, center_y)

                # Desenhe o círculo
                draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill="white")

                # Recorte a imagem usando o círculo como máscara
                image_circular.paste(image, (0, 0), mask=image_circular)

                # Converter a imagem circular para o formato suportado pelo Tkinter
                photo = ctk.CTkImage(image_circular, size=(100, 100))
                # Atualizar o widget Label com a nova imagem
                label_img.configure(image=photo, text="")
                label_img.image = photo
            except Exception as erro:
                print(erro)

        else:
            print("não existe nenhuma img no banco de dados")

    def select_image(self, label_img, usuario):  # Funcão para selecionar a imagem
        # Abrir o diálogo de selecão de arquivo
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])

        # Verificar se um arquivo foi selecionado
        if file_path:
            # Carregar a imagem selecionada
            self.load_image(file_path, label_img)

            # Converter a imagem para bytes
            with open(file_path, "rb") as f:
                image_bytes = f.read()

            # Converter os bytes para base64
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            # Inserir ou atualizar a imagem no banco de dados
            self.insert_image(image_base64, usuario)

    @staticmethod
    def load_image(file_path, label_img):  # Funcão para carregar a imagem
        # Carregar a imagem
        image = Image.open(file_path)

        # Redimensionar a imagem se necessário
        image = image.resize((100, 100))
        # Crie uma nova imagem circular de fundo transparente
        image_circular = Image.new("RGBA", image.size, (0, 0, 0, 0))

        # Crie um objeto de desenho
        draw = ImageDraw.Draw(image_circular)

        # Calcule as coordenadas do círculo
        center_x = image_circular.width // 2
        center_y = image_circular.height // 2
        radius = min(center_x, center_y)

        # Desenhe o círculo
        draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill="white")

        # Recorte a imagem usando o círculo como máscara
        image_circular.paste(image, (0, 0), mask=image_circular)

        # Converter a imagem circular para o formato suportado pelo Tkinter
        photo = ctk.CTkImage(image_circular, size=(100, 100))

        # Atualizar o widget Label com a nova imagem
        label_img.configure(image=photo, text="")
        label_img.image = photo

    def insert_image(self, image_base64, usuario):  # Funcão para inserir ou atualizar a img no BD

        cursor = self.conexao.cursor()

        # Converter a imagem base64 para dados binários
        image_binary = binascii.a2b_base64(image_base64)

        # Verificar se já existe uma imagem com o ID 1
        cursor.execute(f"SELECT COUNT(*) FROM Usuarios WHERE usuario = '{usuario}'")
        count = cursor.fetchone()[0]

        if count > 0:
            # Atualizar a imagem existente
            cursor.execute("UPDATE Usuarios SET imagem = ? WHERE usuario = ?", (image_binary, usuario))
        else:
            self.main_app.msgbox("ERRO", "NAO ENCONTRADO USUARIO NO BD PARA INSERIR A NOVA IMAGEM", 0)

        # Salvar as alteracões e fechar a conexão
        self.conexao.commit()
