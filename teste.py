import customtkinter as ctk

ctk.set_default_color_theme(r'C:\Users\luisg\OneDrive\Documentos\GitHub\Sys_Comercial\temas\personalizado.JSON')

root = ctk.CTk()
root.geometry("500x500")



print(root._fg_color)
frame = ctk.CTkFrame(root, fg_color="blue")
frame.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()

