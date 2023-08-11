import customtkinter as ctk
from PIL import Image
import os

root = ctk.CTk()

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")  


MenuIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "menu_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "menu_light.png")), size=(20, 20))



menu_logo = ctk.CTkLabel(root, text="", image=MenuIcon)
menu_logo.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()