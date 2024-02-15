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

root = ctk.CTk()

root.geometry("500x500")
def nova_janela():
    dialog = ctk.CTkToplevel()

    dialog.title("SENHA")
    dialog.geometry("340x250")
    dialog.resizable(0, 0)
    dialog.grab_set()



b1 = ctk.CTkButton(root, text="nova janela", command=nova_janela)
b1.pack()

root.mainloop()




