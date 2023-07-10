
import customtkinter as ctk
import time
app = ctk.CTk()
app.geometry("800x800")


def button_click_event():
    dialog = ctk.CTkToplevel()
    dialog.geometry("340x250")
    dialog.resizable(0, 0)
    dialog.focus_force()
    dialog.focus_get()
    dialog.focus_set()
    dialog.grab_set()


    def salvar():
        atual = str(SenhaAtual.get())
        nova = str(NovaSenha.get())
        confir = str(ConfirmaçãoSenha.get())
        if atual == "951357":
            if nova == confir:
                if len(nova) >=4 and len(confir)>=4:
                    resposta.configure(text="Senha atualizada", text_color="green")
                else:
                    resposta.configure(text="Senha curta", text_color="red")
            else:
                resposta.configure(text="As senhas nao conferem", text_color="red")
        else:
            resposta.configure(text="As senhas nao conferem", text_color="red")
            
    def fechar():
        dialog.destroy()


    msg = ctk.CTkLabel(dialog, text="Informe os dados da sua nova senha")
    msg.place(relx=0.5, rely=0.1, anchor="center")

    SenhaAtual = ctk.CTkEntry(dialog, placeholder_text="Digite sua senha atual", width=320)
    SenhaAtual.place(relx=0.5, rely=0.3, anchor="center")

    NovaSenha = ctk.CTkEntry(dialog, placeholder_text="Digite sua nova senha", width=320, show="*")
    NovaSenha.place(relx=0.5, rely=0.5, anchor="center")

    ConfirmaçãoSenha = ctk.CTkEntry(dialog, placeholder_text="Confirmar nova senha", width=320, show="*")
    ConfirmaçãoSenha.place(relx=0.5, rely=0.7, anchor="center")

    resposta = ctk.CTkLabel(dialog, text="", height=2)
    resposta.place(relx=0.5, rely=0.81, anchor="center")

    Okbt = ctk.CTkButton(dialog, text="SALVAR", command=salvar)
    Okbt.place(relx=0.25, rely=0.92, anchor="center")

    CancelarBT = ctk.CTkButton(dialog, text="Fechar", command=fechar)
    CancelarBT.place(relx=0.75, rely=0.92, anchor="center")





button2 = ctk.CTkButton(app, text="Open Dialog 2", command=button_click_event)
button2.pack(padx=20, pady=20)

app.mainloop()

