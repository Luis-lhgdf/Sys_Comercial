# from src.views.main_app import MainApp, load_config
# import customtkinter as ctk

# if __name__ == "__main__":
#     try:
#         ctk.set_default_color_theme(load_config(False, localfile=False))
#     except FileNotFoundError:
#         ctk.set_default_color_theme(load_config(False, True))

#     root = ctk.CTk()
#     app = MainApp(root)
#     root.mainloop()


import customtkinter as ctk
from deep_translator import GoogleTranslator

# Defina a variável global para o idioma de tradução padrão
idioma_padrao = "en"

# Inicialize o tradutor com o idioma padrão
tradutor = GoogleTranslator(source="pt", target=idioma_padrao)

# Texto a ser traduzido
texto = "Boa noite, galera!"

root = ctk.CTk()

print(tradutor.translate(texto))




