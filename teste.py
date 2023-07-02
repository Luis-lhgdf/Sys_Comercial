
import customtkinter

root = customtkinter.CTk()
root.title("MENU")
# self.root.minsize(500, 500)
# self.root.maxsize(500, 500)
def aparencia(new_appearance_mode: str):
    # função que altera o modo de aparencia da janela entre ligth e dark
    customtkinter.set_appearance_mode(new_appearance_mode) 



appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root, width=100, height=20, values=["Light","Dark"], command=aparencia)
appearance_mode_optionemenu.pack()


root.geometry('500x500')
root.wm_state('zoomed')
root.grab_set()
root.focus_force()

root.mainloop()