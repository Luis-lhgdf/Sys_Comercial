import customtkinter as ctk
import ctypes
import mysql.connector 

def msgbox(title, text, style):
    #  Styles:
    #  0 : OK
    #  1 : OK | Cancel
    #  2 : Abort | Retry | Ignore
    #  3 : Yes | No | Cancel 6, 7, 2
    #  4 : Yes | No
    #  5 : Retry | Cancel
    #  6 : Cancel | Try Again | Continue
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# titulo = ctk.CTkFont(family='Open Sans', size=14, weight="bold")
database = 'railway'
host = 'containers-us-west-1.railway.app'
port = 5474
user = 'root'
password = 'JThLpvacyDNwzFLPyLhX'

conexaoBD = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port )
cursor = conexaoBD.cursor()
cursor.execute("SELECT usuario, acesso, status FROM Usuarios")
resultado = cursor.fetchall()

usuarios = []
status = []
acesso = []



for i, user in enumerate(resultado):
    usuarios.append(user[0])
    status.append(user[1])
    acesso.append(user[2])




def salvar_usuario(i, usuario_entry, status_menu, acesso_menu):
    editar_button[i].configure(state="normal")
    # Salva as alterações nas listas

    cursor.execute(f"SELECT usuario FROM Usuarios WHERE BINARY usuario = '{usuario_entry.get()}'")
    resp = cursor.fetchall()
    if not resp:
        cursor.execute(f"UPDATE Usuarios SET usuario = '{usuario_entry.get()}' WHERE BINARY usuario = '{usuarios[i]}'")
        conexaoBD.commit()
        usuarios[i] = usuario_entry.get()
        status[i] = status_menu.get()
        acesso[i] = acesso_menu.get()
        # Atualiza os rótulos com as novas informações
        usuario_label[i].configure(text=usuarios[i])
        status_label[i].configure(text=status[i])
        acesso_label[i].configure(text=acesso[i])
        # Mostra os rótulos e esconde os campos de entrada
        usuario_label[i].grid()
        status_label[i].grid()
        acesso_label[i].grid()
        usuario_entry.grid_remove()
        status_menu.grid_remove()
        acesso_menu.grid_remove()

        salvar_button[i].grid_remove()
        cancelar_button[i].grid_remove()
        excluir_button[i].grid_remove()
        editar_button[i].grid()
    else:
        msgbox("USUARIO", "Ja existe um usuario com este nome!!!", 0)
def excluir_usuario(i, usuario_entry, status_menu, acesso_menu):
    resp = msgbox("EXCLUIR USUARIO", "Deseja realmente excluir este usuario?", 4)


    if resp == 6:
        editar_button[i].configure(state="normal")
        # Salva as alterações nas listas
        print(usuarios[i])

        cursor.execute(f"delete from Usuarios where binary usuario ='{usuarios[i]}' ")

        conexaoBD.commit()
        usuarios.pop(i)
        status.pop(i) 
        acesso.pop(i) 
    
        # Atualiza os rótulos com as novas informações

        usuario_label[i].destroy()
        status_label[i].destroy()
        acesso_label[i].destroy()

        usuario_entry.grid_remove()
        status_menu.grid_remove()
        acesso_menu.grid_remove()


        salvar_button[i].destroy()
        cancelar_button[i].destroy()
        excluir_button[i].destroy()
        editar_button[i].destroy()


def cancelar_usuario(i, usuario_entry, status_menu, acesso_menu):
    editar_button[i].configure(state="normal")

    # Descarta as alterações e esconde os campos de entrada
    usuario_entry.grid_remove()
    status_menu.grid_remove()
    acesso_menu.grid_remove()

    usuario_label[i].grid(row=i, column=0)
    

    status_label[i].grid(row=i, column=1)
    

    acesso_label[i].grid(row=i, column=2)




    salvar_button[i].grid_remove()
    cancelar_button[i].grid_remove()
    excluir_button[i].grid_remove()
    editar_button[i].grid()

def editar_usuario(i):
    # Cria os campos de entrada com as informações atuais do usuário
    editar_button[i].configure(state="disabled")


    usuario_entry = ctk.CTkEntry(scrol,  width=100)
    usuario_entry.insert(0, usuarios[i])
    usuario_entry.grid(padx=2, pady=5,row=i, column=0)
    
    
    status_menu = ctk.CTkOptionMenu(scrol, values=("ativo", "desativado"), width=100, height=26)
    status_menu.grid(padx=2, pady=5,row=i, column=1)
    
    acesso_menu =  ctk.CTkOptionMenu(scrol, values=("usuario", "adm"),width=100, height=26)
    acesso_menu.grid(padx=2, pady=5,row=i, column=2)

    
    # Cria os botões Salvar e Cancelar
    salvar_button[i] = ctk.CTkButton(scrol, text="Salvar",width=60,  fg_color=("#323232"), hover_color='#191919', command=lambda: salvar_usuario(i, usuario_entry, status_menu, acesso_menu))
    salvar_button[i].grid(row=i, column=4)
    
    cancelar_button[i] =ctk.CTkButton(scrol, text="Cancelar", width=60,  fg_color=("#323232"), hover_color='#191919', command=lambda: cancelar_usuario(i, usuario_entry, status_menu, acesso_menu))
    cancelar_button[i].grid(padx=5, row=i, column=5)

    excluir_button[i] =ctk.CTkButton(scrol, text="Excluir", width=60, fg_color=("#323232"), hover_color='#191919', command=lambda: excluir_usuario(i, usuario_entry, status_menu, acesso_menu))
    excluir_button[i].grid(padx=5, row=i, column=6)
    
    # Esconde os rótulos e o botão Editar
    usuario_label[i].grid_remove()
    status_label[i].grid_remove()
    acesso_label[i].grid_remove()
    
root = ctk.CTk()
root.geometry("1000x300")
root.title("Editar Usuários")

usuario_label = []
status_label = []
acesso_label = []
editar_button = []
salvar_button = [None] * len(usuarios)
cancelar_button = [None] * len(usuarios)
excluir_button = [None] * len(usuarios)

titulo = ctk.CTkFont(family='Open Sans', size=14, weight="bold")
# criando scrolframe com label de cabeçalho
cabeçalho = ctk.CTkLabel(root, text="       Usuario             Acesso             Status", font=titulo, width=723,corner_radius=5, fg_color="gray80", text_color="black", anchor="w")
cabeçalho.place(x=1, y=4)
scrol = ctk.CTkScrollableFrame(root, width=700, height=50)
scrol.place(x=1,y=28)



# adicionado nas lista os botoes com cada usuario cadastrado no banco de dados
for i in range(len(usuarios)):
    usuario_label.append(ctk.CTkLabel(scrol, text=usuarios[i], fg_color="white", anchor="w", width=100, corner_radius=6))
    usuario_label[i].grid(padx=2, pady=5, row=i, column=0)
    
    status_label.append(ctk.CTkLabel(scrol, text=status[i], fg_color="white", anchor="w", width=100, corner_radius=6))
    status_label[i].grid(padx=2, pady=5, row=i, column=1)
    
    acesso_label.append(ctk.CTkLabel(scrol, text=acesso[i],  fg_color="white", anchor="w", width=100, corner_radius=6))
    acesso_label[i].grid(padx=2,pady=5, row=i, column=2)
    
    editar_button.append(ctk.CTkButton(scrol, text="Editar", width=60, fg_color=("#323232"), hover_color='#191919', command=lambda i=i: editar_usuario(i)))
    editar_button[i].grid(padx=60,pady=5, row=i, column=3)


def closesys():
    conexaoBD.close()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", closesys)
root.mainloop()
