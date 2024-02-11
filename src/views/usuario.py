from src.views.icones import *
from ..models.carregar_img import CarregarIMG


class InterfaceUsuario:

    def __init__(self, main_app, frame_resp, bt_perfil):

        self.main_app = main_app
        self.frame_resp = frame_resp
        self.bt_perfil = bt_perfil
        self.conexao = self.main_app.ConexaoPrincipal

        self.interface()

    def interface(self):

        self.frame_resp.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
        self.frame_resp.grid_columnconfigure(0, weight=1)

        label_titulo = ctk.CTkLabel(self.frame_resp, text=f"USUARIO", fg_color="transparent",
                                    text_color=("black", "white"),
                                    font=self.main_app.SubTitle, corner_radius=6, anchor="w")
        label_titulo.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        painel_ft_perfil = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                         border_width=1,
                                         fg_color="transparent", hover=False)

        painel_ft_perfil.grid(row=1, column=0, padx=10, pady=(45, 5), sticky="nsew")

        painel_usuario = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                       border_width=1,
                                       fg_color="transparent", hover=False)
        painel_usuario.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        painel_senha = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                     border_width=1, fg_color="transparent",
                                     hover=False)
        painel_senha.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

        painel_excluir = ctk.CTkButton(self.frame_resp, text="", width=self.main_app.screen_wedth - 270, height=90,
                                       border_width=1,
                                       fg_color="transparent", hover=False)
        painel_excluir.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")

        label_ft_perfil = ctk.CTkLabel(painel_ft_perfil, text="Foto de perfil", font=self.main_app.FontTitle,
                                       fg_color="transparent")
        label_ft_perfil.place(x=10, y=5)

        bt = ctk.CTkButton(painel_ft_perfil, image=ImagemIcon, text="Alterar", command=self.trocar_img,
                           text_color=("black", "white"),
                           width=80, )
        bt.place(x=10, y=50)

        titulo_usuario = ctk.CTkLabel(painel_usuario, text="Usuario", font=self.main_app.FontTitle,
                                      fg_color="transparent")
        titulo_usuario.place(x=10, y=5)

        self.LabelUsuario = ctk.CTkLabel(painel_usuario, text=f"{self.main_app.usuario_logado}",
                                         font=self.main_app.FontBody, fg_color="transparent")
        self.LabelUsuario.place(x=10, y=50)

        titulo_acesso = ctk.CTkLabel(painel_usuario, text="Acesso", font=self.main_app.FontTitle,
                                     fg_color="transparent")
        titulo_acesso.place(x=100, y=5)

        label_acesso = ctk.CTkLabel(painel_usuario, text=f"{self.main_app.acesso_usuario.upper()}",
                                    font=self.main_app.FontBody,
                                    fg_color="transparent")
        label_acesso.place(x=100, y=50)

        bt_editar_user = ctk.CTkButton(painel_usuario, image=EditarIcon2, text="Editar", text_color=("black", "white"),
                                       width=80,
                                       command=self.editar_usuario)
        bt_editar_user.place(x=165, y=28)

        label_senha = ctk.CTkLabel(painel_senha, text="Senha", font=self.main_app.FontTitle, fg_color="transparent")
        label_senha.place(x=10, y=5)

        bt_trocar_senha = ctk.CTkButton(painel_senha, image=SenhaIcon, text="Alterar", text_color=("black", "white"),
                                        width=80,
                                        command=self.trocar_senha)
        bt_trocar_senha.place(x=10, y=50)

        label_excluir = ctk.CTkLabel(painel_excluir, text="Conta", font=self.main_app.FontTitle, fg_color="transparent")
        label_excluir.place(x=10, y=5)

        bt_excluir = ctk.CTkButton(painel_excluir, image=DeletarIcon2, text="Excluir Conta",
                                   text_color=("black", "white"),
                                   width=80,
                                   command=self.excluir_conta)
        bt_excluir.place(x=10, y=50)

    def trocar_img(self):
        imagem = self.bt_perfil

        CarregarIMG(main_app=self.main_app).select_image(imagem, usuario=self.main_app.usuario_logado)

    def editar_usuario(self):
        dialog = ctk.CTkInputDialog(text="DIGITE SEU NOVO NOME DE USUARIO:", title="Editar")
        usuario_digitado = dialog.get_input()

        if usuario_digitado is not None:

            if len(usuario_digitado) >= 3:

                cursor = self.main_app.ConexaoPrincipal.cursor()
                cursor.execute(f"SELECT usuario FROM Usuarios where usuario = '{usuario_digitado}'")
                resposta_bd = cursor.fetchall()
                if not resposta_bd:
                    cursor.execute(
                        f"UPDATE Usuarios SET usuario = '{usuario_digitado}' WHERE usuario = '{self.main_app.usuario_logado}'")
                    self.main_app.usuario_logado = str(usuario_digitado)
                    self.main_app.ConexaoPrincipal.commit()
                    self.LabelUsuario.configure(text=usuario_digitado)

                elif usuario_digitado == self.main_app.usuario_logado:
                    self.main_app.msgbox("USUARIO", "Este ja é o seu nome de usuario\n Informe um nome diferente.", 0)

                else:
                    self.main_app.msgbox("USUARIO", "Ja existe um usuario com este nome!!!", 0)

            elif 1 <= len(usuario_digitado) <= 2:
                self.main_app.msgbox("USUARIO", "Seu novo nome de usuario deve conter pelo menos 3 caracteres", 0)

    def trocar_senha(self):

        dialog = ctk.CTkToplevel()
        dialog.title("SENHA")
        dialog.geometry("340x250")
        dialog.resizable(0, 0)
        dialog.grab_set()

        def requisitos_atual(event):
            msg_atual = ctk.CTkLabel(dialog, text="Senha atual", height=3)
            msg_atual.place(relx=0.15, rely=0.2, anchor="center")

        def requisitos_senha1(event):
            nova = str(nova_senha.get())
            if len(nova) <= 5:
                msg_nova = ctk.CTkLabel(dialog, text="Nova senha", height=3)
                msg_nova.place(relx=0.15, rely=0.4, anchor="center")
                resposta.configure(text="Sua senha deve ter no minimo 6 caracteres.", text_color="red")
                botao_salvar_registro.configure(state="disabled")
            else:
                resposta.configure(text="", text_color="green")

                if len(str(confirmacao_senha.get())) > 5:
                    botao_salvar_registro.configure(state="normal")

        def requisitos_senha2(event):
            nova_senha_digitada = str(confirmacao_senha.get())
            nova_senha_confirmada = str(confirmacao_senha.get())

            msg_confirmacao = ctk.CTkLabel(dialog, text="Redigite a nova senha", height=3)
            msg_confirmacao.place(relx=0.23, rely=0.6, anchor="center")

            if nova_senha_confirmada == nova_senha_digitada and len(nova_senha_confirmada) > 5:
                resposta.configure(text="", text_color="Green")
                botao_salvar_registro.configure(state="normal")
                if len(nova_senha_digitada) > 5:
                    botao_salvar_registro.configure(state="normal")

            else:
                resposta.configure(text="A nova senha não é igual à redigitada.", text_color="red")
                botao_salvar_registro.configure(state="disabled")

        def salvar():
            atual = str(senha_atual.get())
            nova = str(nova_senha.get())

            cursor = self.main_app.ConexaoPrincipal.cursor()
            cursor.execute(
                f"SELECT senha FROM Usuarios WHERE usuario = '{self.main_app.usuario_logado}' AND senha = '{atual}'")
            resultado_bd = cursor.fetchall()

            if resultado_bd:
                cursor.execute(f"UPDATE Usuarios SET senha = '{nova}' WHERE usuario = '{self.main_app.usuario_logado}'")
                self.main_app.ConexaoPrincipal.commit()
                resposta.configure(text="Senha atualizada com sucesso!", text_color="green")
                botao_salvar_registro.configure(state="disabled")
            else:
                resposta.configure(text="Senha atual esta incorreta", text_color="red")

        def fechar():
            dialog.destroy()

        msg = ctk.CTkLabel(dialog, text="TROCAR SENHA", font=self.main_app.FontTitle)
        msg.place(relx=0.5, rely=0.1, anchor="center")

        senha_atual = ctk.CTkEntry(dialog, placeholder_text="Digite sua senha atual", width=320)
        senha_atual.place(relx=0.5, rely=0.3, anchor="center")
        senha_atual.bind('<KeyRelease>', requisitos_atual)

        nova_senha = ctk.CTkEntry(dialog, placeholder_text="Digite sua nova senha", width=320, show="*")
        nova_senha.place(relx=0.5, rely=0.5, anchor="center")
        nova_senha.bind('<KeyRelease>', requisitos_senha1)

        confirmacao_senha = ctk.CTkEntry(dialog, placeholder_text="Confirmar nova senha", width=320, show="*")
        confirmacao_senha.place(relx=0.5, rely=0.7, anchor="center"),
        confirmacao_senha.bind('<KeyRelease>', requisitos_senha2)

        resposta = ctk.CTkLabel(dialog, text="", height=2)
        resposta.place(relx=0.5, rely=0.81, anchor="center")

        botao_salvar_registro = ctk.CTkButton(dialog, text="SALVAR", command=salvar,
                                              state='disabled')
        botao_salvar_registro.place(relx=0.25, rely=0.92, anchor="center")

        botao_cancelar_registro = ctk.CTkButton(dialog, text="Fechar",
                                                command=fechar)
        botao_cancelar_registro.place(relx=0.75, rely=0.92, anchor="center")

    def excluir_conta(self):

        dialog = ctk.CTkToplevel()
        dialog.title("EXCLUIR")
        dialog.geometry("340x120")
        dialog.resizable(0, 0)
        dialog.grab_set()

        def fechar():
            dialog.destroy()

        def conta_delete():
            cursor = self.main_app.ConexaoPrincipal.cursor()
            cursor.execute(f"DELETE FROM Usuarios where usuario = '{self.main_app.usuario_logado}'")
            self.main_app.ConexaoPrincipal.commit()
            dialog.destroy()

            self.main_app.root.geometry(f"400x430")
            self.main_app.login()

        msg = ctk.CTkLabel(dialog, text="DESEJA REALMENTE EXCLUIR SUA CONTA?", font=self.main_app.SubTitle)
        msg.place(relx=0.5, rely=0.1, anchor="center")

        botao_excluir = ctk.CTkButton(dialog, text="EXCLUIR",
                                      command=conta_delete)
        botao_excluir.place(relx=0.25, rely=0.79, anchor="center")

        botao_fechar = ctk.CTkButton(dialog, text="Fechar",
                                     command=fechar)
        botao_fechar.place(relx=0.75, rely=0.79, anchor="center")
