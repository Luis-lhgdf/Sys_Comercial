import ctypes
import webbrowser
import customtkinter as ctk

class Utilities:

    def __init__(self) -> None:
        pass
        

    @staticmethod
    def msgbox(title, text, style):
        #  Styles:
        #  0 : OK
        #  1 : OK | Cancel
        #  2 : Abort | Retry | Ignore
        #  3 : Yes | No | Cancel 6, 7, 2
        #  4 : Yes | No
        #  5 : Retry | Cancel
        #  6 : Cancel | Try Again | Continue

        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    @staticmethod
    def open_website(url):
        # URL do site que deseja abrir
        website_url = url
        # Abrir o site no navegador padrão
        webbrowser.open(website_url)

    @staticmethod
    def restart_interface(frame):
        # Destruir todos os widgets existentes
        for widget in frame.winfo_children():
            widget.destroy()


    def validate_password_strength(self, password):
            if len(password) >= 6 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password) and any(char in "!$@%#" for char in password):
                return True
            else:
                return False

    def format_password_label(self, label, text, is_valid):
        if is_valid:
            label.configure(text=text[0], text_color="green")
        else:
            label.configure(text=text[1], text_color="red")
   
   
    def validate_password_match(self, password, confirmation):
        if password == confirmation and password!= '' and confirmation != '':
            return bool


        