import customtkinter as ctk


root = ctk.CTk()
root.geometry("500x500")



print(root._fg_color)
frame = ctk.CTkFrame(root, fg_color="blue")
frame.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()

