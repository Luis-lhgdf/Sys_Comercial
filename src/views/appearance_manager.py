class AppearanceManager:
    def __init__(self):
        self.font_title = ("Helvetica", 20, "bold")
        self.font_subtitle = ("Helvetica", 14, "bold")
        self.font_body = ("Helvetica", 12)
        # Adicione mais atributos conforme necessário

    def get_font_title(self):
        return self.font_title

    def get_font_subtitle(self):
        return self.font_subtitle

    def get_font_body(self):
        return self.font_body