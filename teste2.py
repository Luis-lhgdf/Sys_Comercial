import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x500")


def switch_event():
    print("Ativar Modulo de vendas:", switch.get())



switch = ctk.CTkSwitch(root, text="Ativar Modulo de venda", onvalue="on", offvalue="off", command=switch_event,width=500, height=500,)
switch.place(x=10, y=50)

# switch.toggle()


root.mainloop()

