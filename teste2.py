import customtkinter as ctk
from tkinter import filedialog
import mysql.connector
from PIL import Image, ImageTk,  ImageDraw
from tkinter import ttk
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


        # Criando o widget Treeview
        tree = ttk.Treeview(frame_resp, columns=([f'coluna{c}' for c in range(1,17)]), show="headings")

        # Definindo os cabeçalhos das colunas
        database = 'railway'
        host = 'containers-us-west-1.railway.app'
        port = 5474
        user = 'root'
        password = 'JThLpvacyDNwzFLPyLhX'

        # Crie a conexão
        conexao = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)

        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM Clientes")
        resultado = cursor.column_names



        for i, coluna in enumerate(tree['columns']):
            tree.column(coluna, width=20 if coluna == 'coluna1' else 200)
            tree.heading(coluna, text=f"{resultado[i]}")
  

        
        def generate_fake_data():
            data = []
            for _ in range(500):
                cliente = [
                    _ + 1,
                    'Pessoa Física' if _ % 2 == 0 else 'Pessoa Jurídica',
                    f'{100 + _}',
                    f'{200 + _}',
                    f'cliente{_}@exemplo.com',
                    f'Empresa {_}',
                    f'Empresa {_} LTDA',
                    f'{80000 + _}',
                    f'Rua {_} de Abril',
                    str(_),
                    f'Sala {_}',
                    'Centro',
                    'Cidade Exemplo',
                    'EX',
                    f'(99) 9999-{1000 + _}',
                    f'(99) 9999-{2000 + _}',
                    'Resposta à pergunta',
                    'Observação sobre o cliente',
                ]
                data.append(cliente)
            return data

        # Gerando dados fake
        fake_data = generate_fake_data()

        # Inserindo os dados no Treeview
        for item in fake_data:
            tree.insert("", "end", values=item)
            
        # Adicionando uma barra de rolagem ao Treeview
        scroll_y = ttk.Scrollbar(frame_resp, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll_y.set)
        scroll_y.place(x=1100, y=300, height=300)  # Ajuste a posição x para 850


        # Adicionando uma barra de rolagem horizontal ao Treeview
        scroll_x = ttk.Scrollbar(frame_resp, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.place(x=50, y=600, width=1050) 


        # Exibindo o widget Treeview na janela
        tree.place(x=50,y=300, width=1050, height=300)

        def on_edit(event):
            selected_item = tree.selection()
            if selected_item:
                values = tree.item(selected_item, "values")
                
                print(values)

        # Vinculando o evento de seleção do Treeview à função on_edit()
        style = ttk.Style()
        style.theme_use("alt")
        style.configure('Treeview.Heading', background="white")
        style.map("Treeview", background=[('selected', 'gray90')], foreground=[('selected', 'black')])
        
        tree.bind("<<TreeviewSelect>>", on_edit)






Menu()