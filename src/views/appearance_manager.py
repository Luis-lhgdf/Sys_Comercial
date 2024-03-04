from deep_translator import GoogleTranslator
import customtkinter as ctk
import os
import json
import pkg_resources

class AppearanceManager:
    def __init__(self):

        self.font_title = ("Open Sans", 30, "bold", "italic")
        self.font_subtitle = ("Open Sans", 20)
        self.font_body = ("Open Sans", 12)


        self.default_libtheme_location = pkg_resources.resource_filename('customtkinter', 'assets/themes/')

        self.custom_theme_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), "themes/custom_colors.json")

        self.current_theme_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), "themes/current_theme.json")

        # funções para carregar o thema atual e definir aos hovercolors dos botoes direto dos arquivos json
        self.current_theme = self.load_config()

        self.highlight_color = self.json_fgcolor(self.current_theme, "CTkButton","hover_color")


    def get_font_title(self):
        return self.font_title
    

    def get_font_subtitle(self, bold=False):
        if bold:
            return ("Open Sans", 20, "bold")
        else:
            return self.font_subtitle


    def get_font_body(self, bold=False):  # Adicionando um parâmetro opcional para negrito
        if bold:
            return ("Open Sans", 12, "bold")
        else:
            return self.font_body
        

    def appearance_theme(self, new_appearance_mode: str):
    # funcão que altera o modo de aparencia da janela entre light e dark
        ctk.set_appearance_mode(new_appearance_mode)


    def change_scaling_event(self, new_scaling: str):
    
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)


    def json_fgcolor(self, theme, widget_name, key):
            
        if theme.lower() == 'personalizado':

            with open(self.custom_theme_location) as file_json:

                dict_theme = json.load(file_json)
                color_hex = dict_theme[widget_name][key]

                return color_hex
        else:
            
            local = self.default_libtheme_location + theme +'.json'
            with open(local) as file_json:

                dict_theme = json.load(file_json)  # Carregue o conteúdo do arquivo JSON
                color_hex = dict_theme[widget_name][key]

                return color_hex


    def load_config(self):
        
        with open(self.current_theme_location, "r") as config_file:
            theme = json.load(config_file)
            theme = str(theme["theme"]["default_theme"][0])

            if theme == 'personalizado':
                ctk.set_default_color_theme(self.custom_theme_location)
            else:

                local = self.default_libtheme_location + theme +'.json'
                ctk.set_default_color_theme(local)
            
            return theme

