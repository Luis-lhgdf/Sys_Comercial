import customtkinter as ctk
from tkinter import filedialog
import mysql.connector
from PIL import Image, ImageTk,  ImageDraw
import base64
import binascii
import io
import os
import ctypes
import sys

# Criar a janela

local  = r'liftam.JSON'
ctk.set_default_color_theme(local)


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

class Menu():
    def __init__(self):
        self.root = ctk.CTk()

        self.root.geometry('1000x1000')
        self.acesso_usuario = 'ADM'

        self.screen_height = self.root.winfo_screenheight()
        self.screen_wedth = self.root.winfo_screenwidth()
        self.usuario_logado = 'anubis'

        database = 'railway'
        host = 'containers-us-west-1.railway.app'
        port = 5474
        user = 'root'
        password = 'JThLpvacyDNwzFLPyLhX'

        # Crie a conexão
        self.conexaoBD = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)

        


        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")  


        self.MenuIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "menu_black.png")),
                                dark_image=Image.open(os.path.join(self.image_path, "menu_light.png")), size=(20, 20))


        self.HomeIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "home_black.png")),
                                dark_image=Image.open(os.path.join(self.image_path, "home_light.png")),  size=(17, 17))


        self.FotoPerfil = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "perfil.jpg")),
                            dark_image=Image.open(os.path.join(self.image_path, "perfil.jpg")), size=(100, 100))


        self.SeuLogo = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "logo1.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "logo1.png")), size=(100, 100))


        self.SeuLogo2 = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "logo2.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "logo2.png")), size=(200, 200))


        self.EstoqueIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "estoque_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "estoque_light.png")), size=(17, 17))

        self.CadastroIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "cadastro_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "cadastro_light.png")),  size=(17, 17))


        self.AgendaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "agenda_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "agenda_light.png")), size=(17, 17))


        self.carteiraIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "carteira_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "carteira_light.png")),  size=(17, 17))


        self.UsuarioIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "usuario_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "usuario_light.png")), size=(17, 17))


        self.ConfiguracoesIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "configuracoes_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "configuracoes_light.png")), size=(17, 17))


        self.EntradaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "entrada_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "entrada_light.png")), size=(17, 17))


        self.SaidaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "saida_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "saida_light.png")), size=(17, 17))


        self.InventarioIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "inventario_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "inventario_light.png")), size=(17, 17))



        self.AdicionarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "adicionar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "adicionar_light.png")), size=(30, 30))


        self.EditarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "editar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "editar_light.png")), size=(30, 30))
        

        self.EditarIcon2 = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "editar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "editar_light.png")), size=(17, 17))
        




        self.ItemIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "item_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "item_light.png")), size=(17, 17))



        self.VisualizarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "visualizar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "visualizar_light.png")), size=(17, 17))


        self.VoltarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "voltar_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "voltar_light.png")), size=(30, 30))


        self.FinancasIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "financas_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "financas_light.png")), size=(17, 17))


        self.VendasIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "vendas_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "vendas_light.png")), size=(17, 17))


        self.DespesaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "despesa_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "despesa_light.png")), size=(17, 17))



        self.ReceitaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "receita_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "receita_light.png")), size=(17, 17))


        self.FaturamentoIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "faturamento_black.png")),
                            dark_image=Image.open(os.path.join(self.image_path, "faturamento_light.png")), size=(17, 17))

        self.GerenciarUserIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "gerenciarUser_black.png")),
                    dark_image=Image.open(os.path.join(self.image_path, "gerenciarUser_light.png")), size=(17, 17))

        self.DeletarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "deletar_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "deletar_light.png")), size=(30, 30))
        

        self.DeletarIcon2 = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "deletar_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "deletar_light.png")), size=(17, 17))
        
        
        self.SalvarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "salvar_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "salvar_light.png")), size=(30, 30))  
        

                
        self.ImagemIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "imagem_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "imagem_light.png")), size=(17, 17))


                    
        self.SenhaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "senha_black.png")),
            dark_image=Image.open(os.path.join(self.image_path, "senha_light.png")), size=(17, 17))

        
          
        

        self.perfilIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "perfil.png")),
                    dark_image=Image.open(os.path.join(self.image_path, "perfil.png")), size=(80, 80))
        self.iniciar()

        self.root.mainloop()
    def iniciar(self):
        self.Menulateral = ctk.CTkFrame(self.root, width=176, height=self.screen_height, fg_color="gray60")
        self.Menulateral.grid(row=0, column=0)

        self.frame_OcultarMenu = ctk.CTkFrame(self.root, fg_color="white", width=37, height=self.screen_height, corner_radius=0)
        self.frame_OcultarMenu.grid(row=0,column=1)
  
        frame_resp = ctk.CTkFrame(self.root, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        frame_resp.grid(row=0,column=2)


        if self.acesso_usuario == "ADM":
            titulo = ctk.CTkFont(size=14, weight="bold")
            
            cursor = self.conexaoBD.cursor()
            cursor.execute("SELECT usuario, acesso, status FROM Usuarios")
            resultado = cursor.fetchall()

            cursor.execute(f"select * from modulos where usuario = '{self.usuario_logado}'")
            self.ModulosDoUsuario = cursor.fetchall()

            usuarios = []
            acesso = []
            status = []
            
            for user in resultado:
                usuarios.append(user[0])
                acesso.append(user[1])
                status.append(user[2])

                        
            def modulos_usuario(i, usuario_entry, status_menu, acesso_menu):

                usuario_entry.grid_remove()
                acesso_menu.grid_remove()
                status_menu.grid_remove()

                salvar_button[i].grid_remove()
                cancelar_button[i].grid_remove()
                excluir_button[i].grid_remove()
                Editar_Modulos[i].grid_remove()

                
                outros_usuarios = len(usuario_label)-1
                for c in range(0, outros_usuarios+1):
                    usuario_label[c].grid_remove()
                    acesso_label[c].grid_remove()
                    status_label[c].grid_remove()
                    editar_button[c].grid_remove()

                cabeçalho.configure(text='     Usuario             Modulo             Submodulo             visualizar             Novo             Editar             Remover')

                usuario_label_modulo = []
                modulo_label_modulo = []
                submodulo_label_modulo = []
                visualizar_menu_modulo = []
                novo_menu_modulo = []
                editar_menu_modulo = []
                remover_menu_modulo = []
                print(self.ModulosDoUsuario)

                for i, linha in enumerate(self.ModulosDoUsuario):
                    usuario_label_modulo.append(ctk.CTkLabel(scrol, text=linha[1], fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
                    usuario_label_modulo[i].grid(padx=2, pady=5, row=i, column=0)

                    modulo_label_modulo.append(ctk.CTkLabel(scrol, text=linha[2], fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
                    modulo_label_modulo[i].grid(padx=2, pady=5, row=i, column=1)

                    submodulo_label_modulo.append(ctk.CTkLabel(scrol, text=linha[3].capitalize(), fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
                    submodulo_label_modulo[i].grid(padx=2, pady=5, row=i, column=2)

                    visualizar_menu_modulo.append(ctk.CTkOptionMenu(scrol, values=("liberado", "bloquado"), width=100, height=26))
                    visualizar_menu_modulo[i].grid(padx=2, pady=5, row=i, column=3)

                    novo_menu_modulo.append(ctk.CTkOptionMenu(scrol, values=("liberado", "bloquado"), width=100, height=26))
                    novo_menu_modulo[i].grid(padx=2, pady=5, row=i, column=4)

                    editar_menu_modulo.append(ctk.CTkOptionMenu(scrol, values=("liberado", "bloquado"), width=100, height=26))
                    editar_menu_modulo[i].grid(padx=2, pady=5, row=i, column=5)

                    remover_menu_modulo.append(ctk.CTkOptionMenu(scrol, values=("liberado", "bloquado"), width=100, height=26))
                    remover_menu_modulo[i].grid(padx=2, pady=5, row=i, column=6)


                

            def salvar_usuario(i, usuario_entry, status_menu, acesso_menu):
                editar_button[i].configure(state="normal")
                # Salva as alterações nas listas 

                NovoUser = usuario_entry.get()
                NovoAcesso = acesso_menu.get()
                NovoStatus =  status_menu.get()

                if NovoUser != usuarios[i]:
                    cursor.execute(f"SELECT usuario FROM Usuarios WHERE BINARY usuario = '{usuario_entry.get()}'")
                    resp = cursor.fetchall()
                    if not resp:
                        cursor.execute(f"UPDATE Usuarios SET usuario = '{usuario_entry.get()}' WHERE BINARY usuario = '{usuarios[i]}'")
                        self.usuario_logado = usuario_entry.get()
                        usuarios[i] = usuario_entry.get()
                        self.conexaoBD.commit()
                    else:
                        msgbox("USUARIO", "Ja existe um usuario com este nome!!!", 0)

                if NovoAcesso != acesso[i] :
                    cursor.execute(f"UPDATE Usuarios SET acesso = '{acesso_menu.get()}' WHERE BINARY usuario = '{usuarios[i]}'")
                    acesso[i] = acesso_menu.get()
                    self.conexaoBD.commit()

                if NovoStatus != status[i]:
                    cursor.execute(f"UPDATE Usuarios SET status = '{status_menu.get()}' WHERE BINARY usuario = '{usuarios[i]}'")
                    status[i] = status_menu.get()
                    self.conexaoBD.commit()
                    
                # Atualiza os rótulos com as novas informações

                    Tadm = 0
                    Tuser = 0

                    for v in acesso:
                        if v == 'ADM':
                            Tadm +=1
                        else:
                            Tuser +=1  
                    
                    TotalPerfil.configure(text=f"Total de Perfils\n{len(usuarios)}")
                                        
                    TotalAdm.configure(text=f"Total de Administradores\n{Tadm}")
                                    
                    TotalUser.configure(text=f"Total de Usuarios\n{Tuser}")



                usuario_label[i].configure(text=usuarios[i])
                acesso_label[i].configure(text=acesso[i])
                status_label[i].configure(text=status[i])
                
                # Mostra os rótulos e esconde os campos de entrada
                usuario_label[i].grid()
                acesso_label[i].grid()
                status_label[i].grid()
                
                usuario_entry.grid_remove()
                acesso_menu.grid_remove()
                status_menu.grid_remove()
                

                salvar_button[i].grid_remove()
                Editar_Modulos[i].grid_remove()
                cancelar_button[i].grid_remove()
                excluir_button[i].grid_remove()
                editar_button[i].grid()

            def excluir_usuario(i, usuario_entry, status_menu, acesso_menu):
                resp = msgbox("EXCLUIR USUARIO", "Deseja realmente excluir este usuario?", 4)


                if resp == 6:
                    editar_button[i].configure(state="normal")
                    # Salva as alterações nas listas
                    print(usuarios[i])

                    cursor.execute(f"delete from Usuarios where binary usuario ='{usuarios[i]}' ")

                    self.conexaoBD.commit()
                    usuarios.pop(i)
                    acesso.pop(i) 
                    status.pop(i) 
                    
                
                    # Atualiza os rótulos com as novas informações

                    Tadm = 0
                    Tuser = 0

                    for v in acesso:
                        if v == 'ADM':
                            Tadm +=1
                        else:
                            Tuser +=1  
                    
                    TotalPerfil.configure(text=f"Total de Perfils\n{len(usuarios)}")
                                        
                    TotalAdm.configure(text=f"Total de Administradores\n{Tadm}")
                                    
                    TotalUser.configure(text=f"Total de Usuarios\n{Tuser}")

                    usuario_label[i].destroy()
                    acesso_label[i].destroy()
                    status_label[i].destroy()
                    

                    usuario_entry.grid_remove()
                    acesso_menu.grid_remove()
                    status_menu.grid_remove()
                    


                    salvar_button[i].destroy()
                    cancelar_button[i].destroy()
                    Editar_Modulos[i].destroy()
                    excluir_button[i].destroy()
                    editar_button[i].destroy()

            def cancelar_usuario(i, usuario_entry, status_menu,acesso_menu ):
                editar_button[i].configure(state="normal")

                # Descarta as alterações e esconde os campos de entrada
                usuario_entry.grid_remove()
                acesso_menu.grid_remove()
                status_menu.grid_remove()

                usuario_label[i].grid(row=i, column=0)

                acesso_label[i].grid(row=i, column=1)
                
                status_label[i].grid(row=i, column=2)
                

                




                salvar_button[i].grid_remove()
                cancelar_button[i].grid_remove()
                excluir_button[i].grid_remove()
                Editar_Modulos[i].grid_remove()
                editar_button[i].grid()

            def editar_usuario(i):
                # Cria os campos de entrada com as informações atuais do usuário
                editar_button[i].configure(state="disabled")


                usuario_entry = ctk.CTkEntry(scrol,  width=100)
                usuario_entry.insert(0, usuarios[i])
                usuario_entry.grid(padx=2, pady=5,row=i, column=0)

                Menu1 = ("USUARIO", "ADM")
                Menu2 = ("ADM", "USUARIO")

                Status1 = ("ATIVO", "DESATIVADO")
                Status2 = ("DESATIVADO", "ATIVO")


                acesso_menu =  ctk.CTkOptionMenu(scrol, values=(Menu1 if acesso[i] == "USUARIO" else Menu2), width=100, height=26)
                acesso_menu.grid(padx=2, pady=5,row=i, column=1)
                
                
                status_menu = ctk.CTkOptionMenu(scrol, values=(Status1 if status[i] == "ATIVO" else Status2), width=100, height=26)
                status_menu.grid(padx=2, pady=5,row=i, column=2)
                


                
                # Cria os botões Salvar e Cancelar
                salvar_button[i] = ctk.CTkButton(scrol, text="Salvar", text_color=("black","white"), image=self.SalvarIcon, width=60,  fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda: salvar_usuario(i, usuario_entry, status_menu, acesso_menu))
                salvar_button[i].grid(row=i, column=4)
                
                cancelar_button[i] =ctk.CTkButton(scrol, text="Cancelar", text_color=("black","white"), image=self.VoltarIcon, width=60,  fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda: cancelar_usuario(i, usuario_entry, status_menu, acesso_menu))
                cancelar_button[i].grid(padx=5, row=i, column=5)

                Editar_Modulos[i] =ctk.CTkButton(scrol, text="Modulos", text_color=("black","white"),image=self.EditarIcon, width=60,  fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda: modulos_usuario(i, usuario_entry, status_menu, acesso_menu))
                Editar_Modulos[i].grid(padx=5, row=i, column=6)

                excluir_button[i] =ctk.CTkButton(scrol, text="Deletar", text_color=("black","white"),image=self.DeletarIcon, width=60, fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda: excluir_usuario(i, usuario_entry, status_menu, acesso_menu))
                excluir_button[i].grid(padx=5, row=i, column=7)
                
                # Esconde os rótulos e o botão Editar
                usuario_label[i].grid_remove()
                status_label[i].grid_remove()
                acesso_label[i].grid_remove()




                print("a")
         
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
                if v == 'ADM':
                    Tadm +=1
                else:
                    Tuser +=1


            LabelTitulo =ctk.CTkLabel(frame_resp, text=f"GERENCIAR USUARIOS",fg_color="transparent", text_color=("black", "white"), font=titulo, corner_radius=6)
            LabelTitulo.place(relx=0.001, rely=0.02, anchor="w")

            TotalPerfil = ctk.CTkLabel(frame_resp, text=f"Total de Perfils\n{len(usuarios)}", height=50, width=200,
                                        fg_color="white", text_color="black", font=titulo, corner_radius=6)
            TotalPerfil.place(relx=0.05, rely=0.3, anchor="w")


            TotalAdm = ctk.CTkLabel(frame_resp, text=f"Total de Administradores\n{Tadm}", height=50, fg_color="white",width=200,
                                    text_color="black", font=titulo, corner_radius=6)
            TotalAdm.place(relx=0.35, rely=0.3, anchor="w")


            TotalUser = ctk.CTkLabel(frame_resp, text=f"Total de Usuarios\n{Tuser}",height=50, width=200,
                                    fg_color="white", text_color="black", font=titulo, corner_radius=6)
            TotalUser.place(relx=0.65, rely=0.3, anchor="w")


            # criando scrolframe com label de cabeçalho
            cabeçalho = ctk.CTkLabel(frame_resp, text="     Usuario             Acesso             Status", 
                                    width=1123,corner_radius=5, fg_color=("white", "gray10"), text_color=("black", "white"), anchor="w", font=titulo)
            cabeçalho.place(relx=0.01, rely=0.443, anchor="w")

            scrol = ctk.CTkScrollableFrame(frame_resp, width=1100, height=50)
            scrol.place(relx=0.01, rely=0.6, anchor="w")


            def Reexibir():
            # adicionado nas lista os botoes com cada usuario cadastrado no banco de dados
                for i in range(len(usuarios)):
                    usuario_label.append(ctk.CTkLabel(scrol, text=usuarios[i], fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
                    usuario_label[i].grid(padx=2, pady=5, row=i, column=0)
                                    
                    acesso_label.append(ctk.CTkLabel(scrol, text=acesso[i],  fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
                    acesso_label[i].grid(padx=2,pady=5, row=i, column=1)
                    
                    status_label.append(ctk.CTkLabel(scrol, text=status[i], fg_color="white", anchor="w", width=100, corner_radius=6, text_color=("black")))
                    status_label[i].grid(padx=2, pady=5, row=i, column=2)

                    
                    editar_button.append(ctk.CTkButton(scrol, text="Editar", text_color=("black","white"), image=self.EditarIcon, width=60, fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda i=i: editar_usuario(i)))
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
                    

            LabelPesquisar = ctk.CTkLabel(frame_resp, text="Busca rapida", fg_color="transparent", font=titulo)
            LabelPesquisar.place(relx=0.36, rely=0.13, anchor="w")

            Pesquisar = ctk.CTkEntry(frame_resp, placeholder_text="Digite o nome do usuario aqui:", width=550, height=40)
            Pesquisar.place(relx=0.2, rely=0.18, anchor="w")



            Bt_Todos = ctk.CTkButton(frame_resp, text="TODOS", image=self.EntradaIcon, text_color=("black","white"), 
                                        width=80,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=Reexibir)
            Bt_Todos.place(relx=0.7, rely=0.18, anchor="w")



            Bt_Pesquisar = ctk.CTkButton(frame_resp, image=self.VisualizarIcon, text_color=("black","white"), text="PESQUISAR",
                                            width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=pesquisarUser)
            Bt_Pesquisar.place(relx=0.612, rely=0.18, anchor="w")



            Bt_NovoUser = ctk.CTkButton(frame_resp, text="Novo Usuario",  image=self.AdicionarIcon, text_color=("black","white"), 
                                        width=80,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'))
            
            Bt_NovoUser.place(relx=0.74, rely=0.8, anchor="w")






Menu()