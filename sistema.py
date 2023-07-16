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

def fecharSistemaa():
    resp = msgbox("Confirmação",
                "Deseja encerrar o sistema?", 4)
    if resp==6:
        sys.exit()

class mysql_bd:
    def conecta_bd(self):
        # Defina as informações de conexão
        database = 'railway'
        host = 'containers-us-west-1.railway.app'
        port = 5474
        user = 'root'
        password = 'JThLpvacyDNwzFLPyLhX'

        # Crie a conexão
        self.conexao = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
        # Verifique se a conexão foi estabelecida
        if self.conexao.is_connected():
            print('Conexão bem-sucedida ao banco de dados')
            return self.conexao

    def desconeta_bd(self):
        self.conexao.close()
        print('Conexãoao banco de dados foi encerrada')

class validar_acesso(mysql_bd):
    def validar(self):
        self.usuario_logado = self.LoginDigitado.get()
        self.senha_logado = self.SenhaDigitado.get()

        if len(self.usuario_logado) ==0 or len(self.senha_logado) ==0:
            msgbox("Login", "Preencha todos os campos", 0)
        else:
            self.conexaoBD = self.conecta_bd()
            cursor = self.conexaoBD.cursor()
            cursor.execute(f"SELECT * FROM Usuarios WHERE BINARY usuario = '{self.usuario_logado}' AND senha = '{self.senha_logado}' AND status = '{'ativo'}'")
            resultado = cursor.fetchall()
            if resultado:
                cursor.execute(f"SELECT acesso FROM Usuarios  WHERE BINARY  usuario = '{self.usuario_logado}' ")

                self.acesso_usuario = str(cursor.fetchall()[0][0])
                self.frame_Inicial()
                
            else:
                msgbox("Login", "Login ou senha incorretos, Tente novamente",0)
                self.desconeta_bd()

    def Novo_Usuario(self):
        print("em construção")

class trocar_imgORlogo(mysql_bd):

    def verificar_foto(self, label_img, usuario):
        

        
        cursor = self.conexaoBD.cursor()
        # Buscar a imagem no banco de dados
        cursor.execute(f"SELECT img FROM Usuarios WHERE BINARY usuario = '{usuario}'")
        result = cursor.fetchone()

        if result[0] != None:

            # Converter o valor binário para imagem
            image_binary = result[0]  # A coluna 'img' é o índice 2 no resultado
            image = Image.open(io.BytesIO(image_binary))

            # Redimensionar a imagem se necessário
            image = image.resize((100, 100))
            # Crie uma nova imagem circular de fundo transparente
            image_circular = Image.new("RGBA", image.size, (0, 0, 0, 0))

            # Crie um objeto de desenho
            draw = ImageDraw.Draw(image_circular)

            # Calcule as coordenadas do círculo
            center_x = image_circular.width // 2
            center_y = image_circular.height // 2
            radius = min(center_x, center_y)

            # Desenhe o círculo
            draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill="white")

            # Recorte a imagem usando o círculo como máscara
            image_circular.paste(image, (0, 0), mask=image_circular)

            # Converter a imagem circular para o formato suportado pelo Tkinter
            photo = ImageTk.PhotoImage(image_circular)
            # Atualizar o widget Label com a nova imagem
            label_img.configure(image=photo, text="")
            label_img.image = photo
            
        else:
            print("não existe nenhuma img no banco de dados")


    
    def select_image(self, label_img, usuario): # Função para selecionar a imagem
        # Abrir o diálogo de seleção de arquivo
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])

        # Verificar se um arquivo foi selecionado
        if file_path:
            # Carregar a imagem selecionada
            self.load_image(file_path, label_img)
            
            # Converter a imagem para bytes
            with open(file_path, "rb") as f:
                image_bytes = f.read()

            # Converter os bytes para base64
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            # Inserir ou atualizar a imagem no banco de dados
            self.insert_image(image_base64, usuario)
    
    def load_image(self,file_path, label_img): # Função para carregar a imagem
        # Carregar a imagem
        image = Image.open(file_path)

        # Redimensionar a imagem se necessário
        image = image.resize((100, 100))
        # Crie uma nova imagem circular de fundo transparente
        image_circular = Image.new("RGBA", image.size, (0, 0, 0, 0))

        # Crie um objeto de desenho
        draw = ImageDraw.Draw(image_circular)

        # Calcule as coordenadas do círculo
        center_x = image_circular.width // 2
        center_y = image_circular.height // 2
        radius = min(center_x, center_y)

        # Desenhe o círculo
        draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill="white")

        # Recorte a imagem usando o círculo como máscara
        image_circular.paste(image, (0, 0), mask=image_circular)

        # Converter a imagem circular para o formato suportado pelo Tkinter
        photo = ImageTk.PhotoImage(image_circular)

        # Atualizar o widget Label com a nova imagem
        label_img.configure(image=photo, text="")
        label_img.image = photo
   
    def insert_image(self,image_base64, usuario):  # Função para inserir ou atualizar a img no BD

        
        cursor = self.conexaoBD.cursor()

        # Converter a imagem base64 para dados binários
        image_binary = binascii.a2b_base64(image_base64)

        # Verificar se já existe uma imagem com o ID 1
        cursor.execute(f"SELECT COUNT(*) FROM Usuarios WHERE usuario = '{usuario}'")
        count = cursor.fetchone()[0]

        if count > 0:
            # Atualizar a imagem existente
            cursor.execute("UPDATE Usuarios SET img = %s WHERE usuario = %s", (image_binary, usuario))
        else:
            msgbox("ERRO", "NAO ENCONTRADO USUARIO NO BD PARA INSERIR A NOVA IMAGEM",0)

        # Salvar as alterações e fechar a conexão
        self.conexaoBD.commit()

class cadastro_conf():
   
    def gerenciar_user(self, frame_resp):
        if self.acesso_usuario == "adm":
            titulo = ctk.CTkFont(size=14, weight="bold")
            
            cursor = self.conexaoBD.cursor()
            cursor.execute("SELECT usuario, acesso, status FROM Usuarios")
            resultado = cursor.fetchall()

            usuarios = []
            acesso = []
            status = []
           
            for user in resultado:
                usuarios.append(user[0])
                acesso.append(user[1])
                status.append(user[2])

                

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
                        if v == 'adm':
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
                        if v == 'adm':
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

                Menu1 = ("usuario", "adm")
                Menu2 = ("adm", "usuario")

                Status1 = ("ativo", "desativado")
                Status2 = ("desativado", "ativo")


                acesso_menu =  ctk.CTkOptionMenu(scrol, values=(Menu1 if acesso[i] == "usuario" else Menu2), width=100, height=26)
                acesso_menu.grid(padx=2, pady=5,row=i, column=1)
                
                
                status_menu = ctk.CTkOptionMenu(scrol, values=(Status1 if status[i] == "ativo" else Status2), width=100, height=26)
                status_menu.grid(padx=2, pady=5,row=i, column=2)
                


                
                # Cria os botões Salvar e Cancelar
                salvar_button[i] = ctk.CTkButton(scrol, text="Salvar", text_color=("black","white"), image=self.SalvarIcon, width=60,  fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda: salvar_usuario(i, usuario_entry, status_menu, acesso_menu))
                salvar_button[i].grid(row=i, column=4)
                
                cancelar_button[i] =ctk.CTkButton(scrol, text="Cancelar", text_color=("black","white"), image=self.VoltarIcon, width=60,  fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda: cancelar_usuario(i, usuario_entry, status_menu, acesso_menu))
                cancelar_button[i].grid(padx=5, row=i, column=5)

                Editar_Modulos[i] =ctk.CTkButton(scrol, text="Modulos", text_color=("black","white"),image=self.EditarIcon, width=60,  fg_color=("transparent"), hover_color=("white", '#191919'))
                Editar_Modulos[i].grid(padx=5, row=i, column=6)

                excluir_button[i] =ctk.CTkButton(scrol, text="Deletar", text_color=("black","white"),image=self.DeletarIcon, width=60, fg_color=("transparent"), hover_color=("white", '#191919'), command=lambda: excluir_usuario(i, usuario_entry, status_menu, acesso_menu))
                excluir_button[i].grid(padx=5, row=i, column=7)
                
                # Esconde os rótulos e o botão Editar
                usuario_label[i].grid_remove()
                status_label[i].grid_remove()
                acesso_label[i].grid_remove()
                
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

class usuario_conf(trocar_imgORlogo):
    def iniciar_img_perfil(self, labelIMG):

        imagem = labelIMG

        self.verificar_foto(imagem, usuario=self.usuario_logado)

    def usuario_funcs(self, frame_resp, labelIMG):
        
        titulo = ctk.CTkFont(family='Open Sans', size=14, weight="bold")
        corpo = ctk.CTkFont(family='Open Sans', size=14)
        
        def Trocar_img():
            imagem = labelIMG
            self.select_image(imagem, usuario=self.usuario_logado)

        Painel_FtPerfil = ctk.CTkButton(frame_resp, text="", width=1100, height=90, border_width=1, fg_color="transparent", hover_color=("#FBECEC", "gray14"))
        Painel_FtPerfil.place(relx=0.02, rely=0.1, anchor="w")

        Label_FtPerfil = ctk.CTkLabel(Painel_FtPerfil, text="Foto de perfil", font=titulo, fg_color="transparent")
        Label_FtPerfil.place(x=10,y=5)
        bt = ctk.CTkButton(Painel_FtPerfil,image=self.ImagemIcon, text="Alterar", command=Trocar_img, text_color=("black","white"), 
                                        width=80,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'))
        bt.place(x=10,y=50)


        def Editar_Usuario():
            dialog = ctk.CTkInputDialog(text="DIGITE SEU NOVO NOME DE USUARIO:", title="Editar",button_fg_color=("#323232"), button_hover_color='#191919')
            resp = dialog.get_input()
            if len(resp) >=3:
                cursor = self.conexaoBD.cursor()
                cursor.execute(f"SELECT usuario FROM Usuarios WHERE BINARY usuario = '{resp}'")
                resp = cursor.fetchall()
                if not resp:
                    cursor.execute(f"UPDATE Usuarios SET usuario = '{resp}' WHERE usuario = '{self.usuario_logado}'")
                    self.usuario_logado = str(resp)
                    self.conexaoBD.commit()
                    LabelUsuario.configure(text=resp)

                elif  resp == self.usuario_logado:
                    msgbox("USUARIO", "Este ja é o seu nome de usuario\n Informe um nome diferente.", 0)

                else:
                    msgbox("USUARIO", "Ja existe um usuario com este nome!!!", 0)




            else:
                msgbox("USUARIO", "Seu novo nome de usuario deve conter pelo menos 3 caracteres", 0)

        Painel_Usuario = ctk.CTkButton(frame_resp, text="", width=1100, height=90, border_width=1, fg_color="transparent", hover_color=("#FBECEC", "gray14"))
        Painel_Usuario.place(relx=0.02, rely=0.25, anchor="w")


        TituloUsuario = ctk.CTkLabel(Painel_Usuario, text="Usuario", font=titulo, fg_color="transparent")
        TituloUsuario.place(x=10,y=5)
        LabelUsuario = ctk.CTkLabel(Painel_Usuario, text=f"{self.usuario_logado}", font=corpo, fg_color="transparent")
        LabelUsuario.place(x=10,y=50)

        TituloAcesso = ctk.CTkLabel(Painel_Usuario, text="Acesso", font=titulo, fg_color="transparent")
        TituloAcesso.place(x=100,y=5)
       
        LabelAcesso = ctk.CTkLabel(Painel_Usuario, text=f"{self.acesso_usuario.upper()}", font=corpo, fg_color="transparent")
        LabelAcesso.place(x=100,y=50) 


        BtEditarUser = ctk.CTkButton(Painel_Usuario, image=self.EditarIcon2, text="Editar", text_color=("black","white"), 
                                        width=80,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=Editar_Usuario)
        BtEditarUser.place(x=165,y=28)


        def Trocar_senha():
         
            dialog = ctk.CTkToplevel()
            dialog.geometry("340x250")
            dialog.resizable(0, 0)
            dialog.grab_set()

            def requisitos_atual(event):
                msgatual = ctk.CTkLabel(dialog, text="Senha atual", height=3)
                msgatual.place(relx=0.15, rely=0.2, anchor="center")


            def requisitos_senha1(event):
                nova = str(NovaSenha.get())
                if len(nova) <=5:
                    msgnova = ctk.CTkLabel(dialog, text="Nova senha", height=3)
                    msgnova.place(relx=0.15, rely=0.4, anchor="center")
                    resposta.configure(text="Sua senha deve ter no minimo 6 caracteres.", text_color="red")
                    Okbt.configure(state="disabled")
                else:
                    resposta.configure(text="", text_color="green")
                    
                    if len(str(ConfirmaçãoSenha.get())) >5:
                        Okbt.configure(state="normal")
                    

            def requisitos_senha2(event):
                nova = str(NovaSenha.get())
                confir = str(ConfirmaçãoSenha.get())

                msgconfir = ctk.CTkLabel(dialog, text="Redigite a nova senha", height=3)
                msgconfir.place(relx=0.23, rely=0.6, anchor="center")

                if confir == nova and len(confir) >5:
                    resposta.configure(text="", text_color="Green")
                    Okbt.configure(state="normal")
                    if len(nova) >5:
                        Okbt.configure(state="normal")
                    
                else:
                    resposta.configure(text="A nova senha não é igual à redigitada.", text_color="red")
                    Okbt.configure(state="disabled")




            def salvar():
                atual = str(SenhaAtual.get())
                nova = str(NovaSenha.get())
    
                cursor = self.conexaoBD.cursor()
                cursor.execute(f"SELECT senha FROM Usuarios WHERE usuario = '{self.usuario_logado}' AND senha = '{atual}'")
                resultado_bd = cursor.fetchall()
                

                if resultado_bd:
                    cursor.execute(f"UPDATE Usuarios SET senha = '{nova}' WHERE usuario = '{self.usuario_logado}'")
                    self.conexaoBD.commit()
                    resposta.configure(text="Senha atualizada com sucesso!", text_color="green")
                    Okbt.configure(state="disabled")
                else:   
                    resposta.configure(text="Senha atual esta incorreta", text_color="red")


                    
            def fechar():
               
                dialog.destroy()


            msg = ctk.CTkLabel(dialog, text="TROCAR SENHA", font=titulo)
            msg.place(relx=0.5, rely=0.1, anchor="center")

            SenhaAtual = ctk.CTkEntry(dialog, placeholder_text="Digite sua senha atual", width=320)
            SenhaAtual.place(relx=0.5, rely=0.3, anchor="center")
            SenhaAtual.bind('<KeyRelease>', requisitos_atual)

            NovaSenha = ctk.CTkEntry(dialog, placeholder_text="Digite sua nova senha", width=320, show="*")
            NovaSenha.place(relx=0.5, rely=0.5, anchor="center")
            NovaSenha.bind('<KeyRelease>', requisitos_senha1)

            ConfirmaçãoSenha = ctk.CTkEntry(dialog, placeholder_text="Confirmar nova senha", width=320, show="*")
            ConfirmaçãoSenha.place(relx=0.5, rely=0.7, anchor="center"),
            ConfirmaçãoSenha.bind('<KeyRelease>', requisitos_senha2)

            resposta = ctk.CTkLabel(dialog, text="", height=2)
            resposta.place(relx=0.5, rely=0.81, anchor="center")

            Okbt = ctk.CTkButton(dialog, text="SALVAR", fg_color=("#323232"), hover_color='#191919', command=salvar, state='disabled')
            Okbt.place(relx=0.25, rely=0.92, anchor="center")

            CancelarBT = ctk.CTkButton(dialog, text="Fechar", fg_color=("#323232"), hover_color='#191919', command=fechar)
            CancelarBT.place(relx=0.75, rely=0.92, anchor="center")
     
        Painel_Senha = ctk.CTkButton(frame_resp, text="", width=1100, height=90, border_width=1, fg_color="transparent", hover_color=("#FBECEC", "gray14"))
        Painel_Senha.place(relx=0.02, rely=0.4, anchor="w")

        LabelSenha = ctk.CTkLabel(Painel_Senha, text="Senha", font=titulo, fg_color="transparent")
        LabelSenha.place(x=10,y=5)

        BtTrocarSenha = ctk.CTkButton(Painel_Senha, image=self.SenhaIcon, text="Alterar", text_color=("black","white"), 
                                        width=80,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=Trocar_senha)
        BtTrocarSenha.place(x=10,y=50)

        def Excluir_conta():
            
            dialog = ctk.CTkToplevel()
            dialog.geometry("340x120")
            dialog.resizable(0, 0)
            dialog.grab_set()

        
            def fechar():
                dialog.destroy()

            def conta_delete():
                cursor = self.conexao.cursor()
                cursor.execute(f"DELETE FROM Usuarios where usuario = '{self.usuario_logado}'")
                self.conexaoBD.commit()
                dialog.destroy()
                self.rootHome.destroy()
                self.Root_login.deiconify()
  

                
                 
                 

            msg = ctk.CTkLabel(dialog, text="DESEJA REALMENTE EXCLUIR SUA CONTA?", font=titulo)
            msg.place(relx=0.5, rely=0.1, anchor="center")

            Okbt = ctk.CTkButton(dialog, text="EXCLUIR", fg_color=("#323232"), hover_color='#191919', command=conta_delete)
            Okbt.place(relx=0.25, rely=0.79, anchor="center")

            CancelarBT = ctk.CTkButton(dialog, text="Fechar", fg_color=("#323232"), hover_color='#191919', command=fechar)
            CancelarBT.place(relx=0.75, rely=0.79, anchor="center")
    


        Painel_Excluir = ctk.CTkButton(frame_resp, text="", width=1100, height=90, border_width=1, fg_color="transparent", hover_color=("#FBECEC", "gray14"))
        Painel_Excluir.place(relx=0.02, rely=0.55, anchor="w")

        LabelExcluir = ctk.CTkLabel(Painel_Excluir, text="Conta", font=titulo, fg_color="transparent")
        LabelExcluir.place(x=10,y=5)

        BtExcluir = ctk.CTkButton(Painel_Excluir,image=self.DeletarIcon2, text="Excluir Conta", text_color=("black","white"), 
                                        width=80,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=Excluir_conta)
        BtExcluir.place(x=10,y=50)

class Menu(usuario_conf, validar_acesso, cadastro_conf):  
    def __init__(self):
        super().__init__()
        # tela de login
        self.Root_login = ctk.CTk()
        self.Root_login.geometry(f"400x430")
        self.Root_login.title("SYS LIFTAM")

        # _______definindo as fontes principais que serão usadas ao longo do codigo_______
        self.FontTitle =ctk.CTkFont(family='inria serif', size=20, weight="bold")
        self.FontBody =ctk.CTkFont(family='inria serif', size=12)

        # _________________Criando as img_icones com as opções LIGHT E DARK e definindo o tamanho com SIZE______________
            
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


        # __________________________________________________________________________________

        LabelTxt = ctk.CTkLabel(self.Root_login, text="Bem Vindo", font=self.FontTitle)
        LabelTxt.place(relx=0.5, rely=0.2, anchor="center")

        def mostrar_senha():
            if self.MostrarSenha.get():
                self.SenhaDigitado.configure(show="")
            else:
                self.SenhaDigitado.configure(show="*")

        
        def ativar_enter(event):
            self.validar()
            
            # Aqui você pode adicionar a lógica que deseja executar quando a tecla Enter for pressionada
            # Por exemplo, você pode chamar uma função de verificação de login ou qualquer outra ação desejada
            print("Tecla Enter pressionada!")

        self.LoginDigitado = ctk.CTkEntry(self.Root_login, placeholder_text="Digite seu login", width=200)
        self.LoginDigitado.place(relx=0.5,rely=0.3, anchor='center')

        self.SenhaDigitado = ctk.CTkEntry(self.Root_login, placeholder_text="Digite sua senha", width=200, show="*")
        self.SenhaDigitado.place(relx=0.5,rely=0.4, anchor='center')

        self.MostrarSenha = ctk.CTkCheckBox(self.Root_login, text="Mostrar senha", font=self.FontBody, command=mostrar_senha)
        self.MostrarSenha.place(relx=0.5, rely=0.5, anchor="center") 

        self.BtEntrar = ctk.CTkButton(self.Root_login, text="Entrar",command=self.validar, hover_color= ("#880016", "#880016"),
                                      text_color = ("white", "white"))
        self.BtEntrar.place(relx=0.5, rely=0.6, anchor="center")
        self.BtEntrar.bind("<Return>", ativar_enter)
        
        # Crie um estilo para o botão com a borda alterada quando estiver com foco




# Vincule o evento de pressionar a tecla Enter ao botão BtEntrar



        LabelLogo = ctk.CTkLabel(self.Root_login, text="", image=self.SeuLogo)
        LabelLogo.place(relx=0.5, rely=0.8, anchor="center")
        
        LabelTxt2 = ctk.CTkLabel(self.Root_login, text="Modo")
        LabelTxt2.place(relx=0.15, rely=0.90, anchor="center")

        appearance_mode_optionemenu = ctk.CTkOptionMenu(self.Root_login, font=self.FontBody, width=100, height=20, values=["Dark","light"], command=self.aparencia)
        appearance_mode_optionemenu.place(relx=0.15, rely=0.95, anchor="center")

        # Executar o loop principal da janela
        self.Root_login.mainloop()

    def frame_Inicial(self):
        self.Root_login.withdraw()
        self.rootHome = ctk.CTkToplevel()
        self.rootHome.state('zoomed')
        self.screen_height = self.rootHome.winfo_screenheight()
        self.screen_wedth = self.rootHome.winfo_screenwidth()


        
        self.frame_MenuLateralEsq = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, corner_radius=0)
        self.frame_MenuLateralEsq.grid(row=0,column=0)

        self.frame_OcultarMenu = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=37, height=self.screen_height, corner_radius=0)
        self.frame_OcultarMenu.grid(row=0,column=1)

        self.frame_temp = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.frame_temp.grid(row=0,column=2)

        self.BtOcultar = ctk.CTkButton(self.frame_OcultarMenu,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", text_color=("black","white"), command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)


        self.BtHome = ctk.CTkButton(self.frame_MenuLateralEsq, text="Home", image=self.HomeIcon, anchor="w", 
                                    width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Home)
        self.BtHome.place(x=0, y=120)


        self.BtEstoque = ctk.CTkButton(self.frame_MenuLateralEsq, text="Estoque ", image=self.EstoqueIcon, anchor="w", 
                                       width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Estoque)
        self.BtEstoque.place(x=0, y=160)
        

        self.BtCadastros = ctk.CTkButton(self.frame_MenuLateralEsq, text="Cadastro", image=self.CadastroIcon, anchor="w", 
                                         width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Cadastro)
        self.BtCadastros.place(x=0, y=200)        


        self.BtAgenda = ctk.CTkButton(self.frame_MenuLateralEsq, text="Agenda", image=self.AgendaIcon, anchor="w", 
                                      width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Agenda)
        self.BtAgenda.place(x=0, y=240)


        self.Btcarteira = ctk.CTkButton(self.frame_MenuLateralEsq, text="Carteira", image=self.carteiraIcon, anchor="w", 
                                       width=176, corner_radius=0, fg_color="transparent",  text_color=("black","white"), command=self.Frame_carteira)
        self.Btcarteira.place(x=0, y=280)
        


        self.BtFinancas = ctk.CTkButton(self.frame_MenuLateralEsq, text="Finanças", image=self.FinancasIcon, anchor="w", 
                                       width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_financas)
        self.BtFinancas.place(x=0, y=320)  


        self.BtUsuario = ctk.CTkButton(self.frame_MenuLateralEsq, text="Usuario", image=self.UsuarioIcon, anchor="w", 
                                       width=176, corner_radius=0, fg_color="transparent", text_color=("black","white"), command=self.Frame_Usuario)
        self.BtUsuario.place(x=0, y=360)  




        self.BtConfiguracoes = ctk.CTkButton(self.frame_MenuLateralEsq, text="Configuracoes", image=self.ConfiguracoesIcon, anchor="w",
                                             width=176, corner_radius=0,  text_color=("black","white"), fg_color="transparent", command=self.Frame_Configuracoes)
        self.BtConfiguracoes.place(x=0, y=400)    



        self.foto_perfil = ctk.CTkButton(self.frame_MenuLateralEsq, text="", image=self.perfilIcon, command=self.Frame_Usuario, fg_color="transparent")
        self.foto_perfil.place(relx=0.5, rely=0.07, anchor="center")


        LabelLogo = ctk.CTkLabel(self.frame_MenuLateralEsq, text="", image=self.SeuLogo2)
        LabelLogo.place(x=-10, y=(self.screen_height-300))


        appearance_mode_optionemenu = ctk.CTkOptionMenu(self.frame_MenuLateralEsq, font=self.FontBody, width=150, height=30, values=["Dark","light"], command=self.aparencia)
        appearance_mode_optionemenu.place(x=10, y=(self.screen_height-100))

        self.FrameLateralAtual = self.frame_OcultarMenu   
        self.frameRespostaAtual = self.frame_temp
       
        self.iniciar_img_perfil(self.foto_perfil)
        self.Frame_Home()

        def closesys():
            self.desconeta_bd()
            fecharSistemaa()
        self.rootHome.protocol("WM_DELETE_WINDOW", closesys)
        self.rootHome.mainloop()

    def aparencia(self, new_appearance_mode: str):
        # função que altera o modo de aparencia da janela entre ligth e dark
        ctk.set_appearance_mode(new_appearance_mode) 

    def ocultarJanela(self):
        larguraJanelaAtual = self.frame_MenuLateralEsq.winfo_width()
       
        
        if larguraJanelaAtual > 35:
            self.frame_MenuLateralEsq.configure(width=28)

        else:
            self.frame_MenuLateralEsq.configure(width=176)

    def Frame_Home(self):
        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
        
        
        self.frame_OcultarMenu = ctk.CTkFrame(self.rootHome, width=37, height=self.screen_height, corner_radius=0, fg_color=("white", "#880016"))
        self.frame_OcultarMenu.grid(row=0,column=1)
        self.FrameLateralAtual = self.frame_OcultarMenu

        self.FrameHomegResposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.FrameHomegResposta.grid(row=0,column=2)
        self.frameRespostaAtual = self.FrameHomegResposta

        


        self.BtHome.configure(fg_color=("white", "#880016"))
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")





        self.BtOcultar = ctk.CTkButton(self.frame_OcultarMenu,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", text_color=("black","white"), command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)

    def Frame_Estoque(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color=("white", "#880016"))
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                
                
        self.FrameEstoqueLateral = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameEstoqueLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameEstoqueLateral


        

        
        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=138,y=1)

        self.op1 = ctk.CTkButton(self.FrameLateralAtual, text="Entrada", image=self.EntradaIcon,anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op1.place(x=10, y=120)
        
        self.op2 = ctk.CTkButton(self.FrameLateralAtual, text="Saida", image=self.SaidaIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op2.place(x=10, y=160)  

        self.op3 = ctk.CTkButton(self.FrameLateralAtual, text="Inventario", image=self.InventarioIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op3.place(x=10, y=200)  

    def Frame_Cadastro(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color=("white", "#880016"))
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                
                
        self.FrameCadastroLateral = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameCadastroLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameCadastroLateral


        
        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=138,y=1)

        self.op1 = ctk.CTkButton(self.FrameLateralAtual, text="Cadastrar Itens", image=self.EstoqueIcon,anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op1.place(x=10, y=160)
        
        self.op2 = ctk.CTkButton(self.FrameLateralAtual, text="Cadastrar Clientes", image=self.CadastroIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op2.place(x=10, y=200)  

        self.op3 = ctk.CTkButton(self.FrameLateralAtual, text="Novo Usuario", image=self.UsuarioIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"))
        self.op3.place(x=10, y=240)  

        self.op4 = ctk.CTkButton(self.FrameLateralAtual, text="Gerenciar Usuarios", image=self.GerenciarUserIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                 hover_color= ("#ff9ea2", "black"), command=self.Frame_GerenciarUser)
        self.op4.place(x=10, y=280)  

    def Frame_GerenciarUser(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color=("white", "#880016"))
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                

        self.FrameGerenciarUserLateral = ctk.CTkFrame(self.rootHome, width=37, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameGerenciarUserLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameGerenciarUserLateral

        self.FrameGerenciarUserResposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.FrameGerenciarUserResposta.grid(row=0,column=2)
        self.frameRespostaAtual = self.FrameGerenciarUserResposta

        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)   

        
        self.gerenciar_user(self.FrameGerenciarUserResposta)

    def Frame_Agenda(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color=("white", "#880016"))
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")



        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                

        self.FrameAgendaLateral = ctk.CTkFrame(self.rootHome, width=37, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameAgendaLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameAgendaLateral

        self.FrameAgendaResposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.FrameAgendaResposta.grid(row=0,column=2)
        self.frameRespostaAtual = self.FrameAgendaResposta

        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)
          
    def Frame_carteira(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color=("white", "#880016"))
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                
                
        self.FramecarteiraLateral = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FramecarteiraLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FramecarteiraLateral


        

        
        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=138,y=1)

        self.op1 = ctk.CTkButton(self.FrameLateralAtual, text="Registrar Venda", image=self.VendasIcon,anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                    hover_color= ("#ff9ea2", "black"))
        self.op1.place(x=10, y=280)
        
        self.op2 = ctk.CTkButton(self.FrameLateralAtual, text="Faturamento", image=self.FaturamentoIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                    hover_color= ("#ff9ea2", "black"))
        self.op2.place(x=10, y=320)   
    
    def Frame_financas(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color=("white", "#880016"))
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                
        self.FramefinancasLateral = ctk.CTkFrame(self.rootHome, width=176, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FramefinancasLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FramefinancasLateral


        

        
        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=138,y=1)

        self.op1 = ctk.CTkButton(self.FrameLateralAtual, text="Registrar Despesas", image=self.DespesaIcon,anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                    hover_color= ("#ff9ea2", "black"))
        self.op1.place(x=10, y=320)
        
        self.op2 = ctk.CTkButton(self.FrameLateralAtual, text="Outras Rendas +", image=self.ReceitaIcon, anchor="w", width=155, fg_color=("#FFD6D6","gray17"), text_color=("black", "white"),
                                    hover_color= ("#ff9ea2", "black"))
        self.op2.place(x=10, y=360)      
   
    def Frame_Usuario(self):

        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color=("white", "#880016"))
        self.BtConfiguracoes.configure(fg_color="transparent")

        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                

        self.FrameUsuarioLateral = ctk.CTkFrame(self.rootHome, width=37, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameUsuarioLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameUsuarioLateral

        self.FrameUsuarioresposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.FrameUsuarioresposta.grid(row=0,column=2)
        self.frameRespostaAtual = self.FrameUsuarioresposta

        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)   

        self.usuario_funcs(self.FrameUsuarioresposta, self.foto_perfil)
    
    def Frame_Configuracoes(self):
        self.BtHome.configure(fg_color="transparent")
        self.BtEstoque.configure(fg_color="transparent")
        self.BtCadastros.configure(fg_color="transparent")
        self.BtAgenda.configure(fg_color="transparent")
        self.Btcarteira.configure(fg_color="transparent")
        self.BtFinancas.configure(fg_color="transparent")
        self.BtUsuario.configure(fg_color="transparent")
        self.BtConfiguracoes.configure(fg_color=("white", "#880016"))


        self.FrameLateralAtual.destroy()
        self.frameRespostaAtual.destroy()
                

        self.FrameConfigLateral = ctk.CTkFrame(self.rootHome, width=37, height=self.screen_height, fg_color=("white", "#880016"), corner_radius=0)
        self.FrameConfigLateral.grid(row=0,column=1)
        self.FrameLateralAtual = self.FrameConfigLateral

        self.FrameConfigResposta = ctk.CTkFrame(self.rootHome, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        self.FrameConfigResposta.grid(row=0,column=2)
        self.frameRespostaAtual = self.FrameConfigResposta

        self.BtOcultar = ctk.CTkButton(self.FrameLateralAtual,text="", image=self.MenuIcon, anchor="w", width=23, height=23,  fg_color="transparent", command=self.ocultarJanela)
        self.BtOcultar.place(x=0,y=1)

        
        


Menu()


