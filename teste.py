import customtkinter as ctk
import ctypes
import mysql.connector 
import customtkinter as ctk
import mysql.connector
from PIL import Image
import os
import ctypes

root = ctk.CTk()
root.geometry("1000x1000")
root.title("Editar Usuários")
titulo = ctk.CTkFont(family='Open Sans', size=14, weight="bold")


screen_height = root.winfo_screenheight()
screen_wedth = root.winfo_screenwidth()

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

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")  


EditarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "editar_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "editar_light.png")), size=(30, 30))

VoltarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "voltar_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "voltar_light.png")), size=(30, 30))

DeletarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "deletar_black.png")),
    dark_image=Image.open(os.path.join(image_path, "deletar_light.png")), size=(30, 30))

SalvarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "salvar_black.png")),
    dark_image=Image.open(os.path.join(image_path, "salvar_light.png")), size=(30, 30))    


for i, user in enumerate(resultado):
    usuarios.append(user[0])
    acesso.append(user[1])

    status.append(user[2])

for v in range(0,50):
    usuarios.append(f"visitante {v}")
    status.append("ativo")
    acesso.append(f"usuario")



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
        
        Tadm = 0
        Tuser = 0

        for v in acesso:
            if v == 'adm':
                Tadm +=1
            else:
                Tuser +=1  
        
        TotalPerfil.configure(text=f"Total de Perfils\n{len(usuarios)}")
                            
        TotalAdm.configure(text=f"Total de Administradores\n{Tadm}")
                          
        TotalUser.configure(text=f"Total de Usuarios\n{Tuser}")
                               
       


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
        Editar_Modulos[i].grid_remove()
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

                
        Tadm = 0
        Tuser = 0

        for v in acesso:
            if v == 'adm':
                Tadm +=1
            else:
                Tuser +=1  
        
        TotalPerfil.configure(text=f"Total de Perfils\n{len(usuarios)}")
                            
        TotalAdm.configure(text=f"Total de Administradores\n{Tadm}")
                          
        TotalUser.configure(text=f"Total de Usuarios\n{Tuser}")

        usuario_label[i].destroy()
        status_label[i].destroy()
        acesso_label[i].destroy()

        usuario_entry.grid_remove()
        status_menu.grid_remove()
        acesso_menu.grid_remove()


        salvar_button[i].destroy()
        cancelar_button[i].destroy()
        excluir_button[i].destroy()
        Editar_Modulos[i].destroy()
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
    Editar_Modulos[i].grid_remove()
    editar_button[i].grid()

def editar_usuario(i):
    # Cria os campos de entrada com as informações atuais do usuário
    editar_button[i].configure(state="disabled")


    usuario_entry = ctk.CTkEntry(scrol,  width=120)
    usuario_entry.insert(0, usuarios[i])
    usuario_entry.grid(padx=2, pady=5,row=i, column=0)
    
    
    status_menu = ctk.CTkOptionMenu(scrol, values=("ativo", "desativado"), width=120, height=26)
    status_menu.grid(padx=2, pady=5,row=i, column=1)
    
    acesso_menu =  ctk.CTkOptionMenu(scrol, values=("usuario", "adm"),width=120, height=26)
    acesso_menu.grid(padx=2, pady=5,row=i, column=2)

    
    # Cria os botões Salvar e Cancelar
    salvar_button[i] = ctk.CTkButton(scrol, text="Salvar",image=SalvarIcon, width=60, text_color="black", fg_color=("white"), hover_color='gray80', command=lambda: salvar_usuario(i, usuario_entry, status_menu, acesso_menu))
    salvar_button[i].grid(row=i, column=4)
    
    cancelar_button[i] =ctk.CTkButton(scrol, text="Cancelar",image=VoltarIcon, width=60,  text_color="black", fg_color=("white"), hover_color='gray80', command=lambda: cancelar_usuario(i, usuario_entry, status_menu, acesso_menu))
    cancelar_button[i].grid(padx=5, row=i, column=5)

    Editar_Modulos[i] =ctk.CTkButton(scrol, text="Modulos",image=EditarIcon, width=60,text_color="black",  fg_color=("white"), hover_color='gray80')
    Editar_Modulos[i].grid(padx=5, row=i, column=6)

    excluir_button[i] =ctk.CTkButton(scrol, text="Deletar",image=DeletarIcon, width=60,text_color="black",  fg_color=("white"), hover_color='gray80', command=lambda: excluir_usuario(i, usuario_entry, status_menu, acesso_menu))
    excluir_button[i].grid(padx=5, row=i, column=7)
    
    # Esconde os rótulos e o botão Editar
    usuario_label[i].grid_remove()
    status_label[i].grid_remove()
    acesso_label[i].grid_remove()




frame_MenuLateralEsq = ctk.CTkFrame(root, width=176, height=screen_height, corner_radius=0, fg_color="gray30")
frame_MenuLateralEsq.grid(row=0,column=0)


FrameGerenciarUserLateral = ctk.CTkFrame(root, width=37, height=screen_height, corner_radius=0)
FrameGerenciarUserLateral.grid(row=0,column=1)
FrameLateralAtual = FrameGerenciarUserLateral

FrameGerenciarUserResposta = ctk.CTkFrame(root, fg_color="transparent", width=(screen_wedth), height=screen_height, corner_radius=0)
FrameGerenciarUserResposta.grid(row=0,column=2)
frameRespostaAtual = FrameGerenciarUserResposta

BtOcultar = ctk.CTkButton(FrameLateralAtual,text="ocultar", anchor="w", width=23, height=23,  fg_color="transparent")
BtOcultar.place(x=0,y=1) 




usuario_label = []
status_label = []
acesso_label = []
editar_button = []
salvar_button = [None] * len(usuarios)
cancelar_button = [None] * len(usuarios)
excluir_button = [None] * len(usuarios)
Editar_Modulos = [None] * len(usuarios)


Tadm = 0
Tuser = 0

for v in acesso:
    if v == 'adm':
        Tadm +=1
    else:
        Tuser +=1






LabelTitulo =ctk.CTkLabel(FrameGerenciarUserResposta, text=f"GERENCIAR USUARIOS",fg_color="transparent", text_color="black", font=titulo, corner_radius=6)
LabelTitulo.place(relx=0.001, rely=0.02, anchor="w")

TotalPerfil = ctk.CTkLabel(FrameGerenciarUserResposta, text=f"Total de Perfils\n{len(usuarios)}", height=50, width=200,
                            fg_color="white", text_color="black", font=titulo, corner_radius=6)
TotalPerfil.place(relx=0.05, rely=0.3, anchor="w")


TotalAdm = ctk.CTkLabel(FrameGerenciarUserResposta, text=f"Total de Administradores\n{Tadm}", height=50, fg_color="white",width=200,
                         text_color="black", font=titulo, corner_radius=6)
TotalAdm.place(relx=0.35, rely=0.3, anchor="w")


TotalUser = ctk.CTkLabel(FrameGerenciarUserResposta, text=f"Total de Usuarios\n{Tuser}",height=50, width=200,
                         fg_color="white", text_color="black", font=titulo, corner_radius=6)
TotalUser.place(relx=0.65, rely=0.3, anchor="w")


# criando scrolframe com label de cabeçalho
cabeçalho = ctk.CTkLabel(FrameGerenciarUserResposta, text="       Usuario                    Acesso                     Status", 
                        width=1123,corner_radius=5, fg_color=("white", "gray10"), text_color=("black", "white"), anchor="w", font=titulo)
cabeçalho.place(relx=0.01, rely=0.443, anchor="w")

scrol = ctk.CTkScrollableFrame(FrameGerenciarUserResposta, width=1100, height=50)
scrol.place(relx=0.01, rely=0.6, anchor="w")

def Reexibir (): 
# adicionado nas lista os botoes com cada usuario cadastrado no banco de dados
    for i in range(len(usuarios)):
        usuario_label.append(ctk.CTkLabel(scrol, text=usuarios[i], fg_color="white", anchor="w", width=120, corner_radius=6))
        usuario_label[i].grid(padx=2, pady=5, row=i, column=0)
        
        status_label.append(ctk.CTkLabel(scrol, text=status[i], fg_color="white", anchor="w", width=120, corner_radius=6))
        status_label[i].grid(padx=2, pady=5, row=i, column=1)
        
        acesso_label.append(ctk.CTkLabel(scrol, text=acesso[i],  fg_color="white", anchor="w", width=120, corner_radius=6))
        acesso_label[i].grid(padx=2,pady=5, row=i, column=2)
        
        editar_button.append(ctk.CTkButton(scrol, text="Editar",image=EditarIcon, text_color="black", width=60, fg_color=("white"), hover_color='gray80', command=lambda i=i: editar_usuario(i)))
        editar_button[i].grid(padx=60,pady=5, row=i, column=3)
Reexibir()


def pesquisarUser():
    try:
        resp = Pesquisar.get()
        if len(resp) >0:  
            Reexibir() 
            for i, v in enumerate(usuario_label):    
                if resp.upper().strip() != v._text.upper():
                    usuario_label[i].grid_remove()
                    status_label[i].grid_remove()
                    acesso_label[i].grid_remove()
                    editar_button[i].grid_remove()
        else:
            Reexibir() 
            


    except Exception as erro:
        print(erro)
        msgbox("Pesquisa", "Usuario nao encontrado", 0)
        

LabelPesquisar = ctk.CTkLabel(FrameGerenciarUserResposta, text="Busca rapida", fg_color="transparent", font=titulo)
LabelPesquisar.place(relx=0.36, rely=0.13, anchor="w")

Pesquisar = ctk.CTkEntry(FrameGerenciarUserResposta, placeholder_text="Digite o nome do usuario aqui:", width=550, height=40)
Pesquisar.place(relx=0.2, rely=0.18, anchor="w")

Bt_Todos = ctk.CTkButton(FrameGerenciarUserResposta, text="TODOS", text_color="black", width=80, fg_color=("white"), hover_color='gray80', command=Reexibir)
Bt_Todos.place(relx=0.7, rely=0.18, anchor="w")

Bt_Pesquisar = ctk.CTkButton(FrameGerenciarUserResposta, text="PESQUISAR", text_color="black", width=80, fg_color=("white"), hover_color='gray80', command=pesquisarUser)
Bt_Pesquisar.place(relx=0.63, rely=0.18, anchor="w")

Bt_NovoUser = ctk.CTkButton(FrameGerenciarUserResposta, text="Novo Usuario", text_color="white", width=60, fg_color=("green"), hover_color='gray80')
Bt_NovoUser.place(relx=0.75, rely=0.8, anchor="w")



def closesys():
    conexaoBD.close()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", closesys)
root.mainloop()
