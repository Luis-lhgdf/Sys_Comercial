from src.views.main_app import MainApp, load_config
import customtkinter as ctk

if __name__ == "__main__":
    try:
        ctk.set_default_color_theme(load_config(False, localfile=False))
    except FileNotFoundError:
        ctk.set_default_color_theme(load_config(False, True))

    root = ctk.CTk()
    app = MainApp(root)
    root.mainloop()
