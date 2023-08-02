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


        self.ExcelIcon = ctk.CTkImage(light_image=Image.open(os.path.join(self.image_path, "excel.png")),
                    dark_image=Image.open(os.path.join(self.image_path, "excel.png")), size=(30, 30))
        

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

        # Definindo os cabeçalhos das colunas
        database = 'railway'
        host = 'containers-us-west-1.railway.app'
        port = 5474
        user = 'root'
        password = 'JThLpvacyDNwzFLPyLhX'
        # Crie a conexão
        conexao = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
        cursor = conexao.cursor()


        limite_view = 10
        cursor.execute(F"SELECT * FROM Clientes limit  {limite_view}")
        ListaClientes = cursor.fetchall()
        textcoluna = cursor.column_names
        cursor.execute("SELECT count(id) from Clientes")
        totalClientes = cursor.fetchone()[0]


        def Reexibir_treeview(lista):
            cursor = conexao.cursor()
            for cliente in lista:
                tree.insert("", "end", values=cliente)
                tree.tag_configure("center", anchor="center")


                
            for i, coluna in enumerate(tree['columns']):
 
                cursor.execute(f"select max(length(`{textcoluna[i]}`)) from Clientes limit {limite_view}")
                largura = int(cursor.fetchone()[0])
                tree.column(coluna, width=largura*9)
                tree.heading(coluna, text=f"{textcoluna[i]}")
                tree.column(coluna, stretch=False)

        def Atualizar_limiteView(novo_limite):
            global limite_view
            tree.delete(*tree.get_children())
            print("novo limente é", novo_limite)

            cursor = conexao.cursor()
            
            cursor.execute(F"SELECT * FROM Clientes limit  {int(novo_limite)}")
            ListaClientes = cursor.fetchall()

            Label_LimiteView.configure(text=f"01 A {novo_limite if int(novo_limite) < totalClientes else totalClientes} DE {totalClientes}")
            limite_view = int(novo_limite)
            Reexibir_treeview(ListaClientes)
        
        def click_select(event):
            selected_item = tree.selection()
            if selected_item:
                if len(selected_item) ==1:
                    unico = tree.item(selected_item, "values") 
                    Label_Select.configure(text=f"SELECIONADO: {unico[5][0:20]}")
                    Bt_EditarCliente.configure(state="normal")
                    Bt_ExcluirCliente.configure(state="normal")

                                          
                else:
                    Bt_EditarCliente.configure(state="disabled")
                    Bt_ExcluirCliente.configure(state="normal")
                    for item_id in selected_item:
                        valor = tree.item(item_id, "values")
        
                        Label_Select.configure(text=f"SELECIONADO: {len(selected_item)}")

        def PesquisarCliente():
            cliente_digitado = str(Entry_Pesquisar.get())
            if cliente_digitado:
                cursor = conexao.cursor()
                cursor.execute(f"select * from Clientes WHERE razao_social LIKE'%{cliente_digitado}%' OR cpf LIKE'%{cliente_digitado}%' OR cnpj LIKE'%{cliente_digitado}%' OR id LIKE'%{cliente_digitado}%'")
                lista = cursor.fetchall()
                print(lista)
                tree.delete(*tree.get_children())
                Reexibir_treeview(lista=lista)



        frame_resp = ctk.CTkFrame(self.root, fg_color="transparent", width=(self.screen_wedth), height=self.screen_height, corner_radius=0)
        frame_resp.grid(row=0,column=2)


        LabelTitulo =ctk.CTkLabel(frame_resp, text=f"CLIENTES",fg_color="transparent", text_color=("black", "white"),  font=(ctk.CTkFont(size=14, weight="bold")), corner_radius=6)
        LabelTitulo.place(relx=0.001, rely=0.02, anchor="w")

        
        LabelPesquisar = ctk.CTkLabel(frame_resp, text="Busca rapida", fg_color="transparent",font=(ctk.CTkFont(size=14, weight="bold")) )
        LabelPesquisar.place(relx=0.36, rely=0.13, anchor="w")

        Entry_Pesquisar = ctk.CTkEntry(frame_resp, placeholder_text="Digite o nome do cliente aqui:", width=550, height=40)
        Entry_Pesquisar.place(relx=0.2, rely=0.18, anchor="w")



        Bt_Todos = ctk.CTkButton(frame_resp, text="TODOS", image=self.EntradaIcon, text_color=("black","white"), 
                                    width=80,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'))
        Bt_Todos.place(relx=0.7, rely=0.18, anchor="w")



        Bt_Pesquisar = ctk.CTkButton(frame_resp, image=self.VisualizarIcon, text_color=("black","white"), text="PESQUISAR",
                                        width=80, fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'), command=PesquisarCliente)
        Bt_Pesquisar.place(relx=0.612, rely=0.18, anchor="w")       

     
    
        Label_Select = ctk.CTkLabel(frame_resp, text=f"SELECIONADO: ", height=37, width=250, fg_color="white", text_color="black", 
                                   font=(ctk.CTkFont(size=12, weight="bold")), corner_radius=6, anchor="w")
        Label_Select.place(relx=0.13, rely=0.35, anchor="center")


        Bt_EditarCliente = ctk.CTkButton(frame_resp, text="Editar", text_color=("black","white"), image=self.EditarIcon,  
                                         width=40, fg_color=("transparent"), hover_color=("white", '#191919'), state="disabled")
        Bt_EditarCliente.place(relx=0.26, rely=0.35, anchor="center")


        Bt_ExcluirCliente = ctk.CTkButton(frame_resp, text="Excluir", text_color=("black","white"), image=self.DeletarIcon,  
                                         width=40, fg_color=("transparent"), hover_color=("white", '#191919'), state="disabled")
        Bt_ExcluirCliente.place(relx=0.34, rely=0.35, anchor="center")


        Label_LimiteView = ctk.CTkLabel(frame_resp,  height=37, text=f"01 A {limite_view} DE {totalClientes}", 
                                        font=(ctk.CTkFont(size=12, weight="bold")), anchor="w")
        Label_LimiteView.place(relx=0.59, rely=0.35, anchor="w")



        Bt_Excel = ctk.CTkButton(frame_resp, text="Excel", text_color=("black","white"), image=self.ExcelIcon,  
                                 width=40, fg_color=("transparent"), hover_color=("white", '#191919'))
        Bt_Excel.place(relx=0.77, rely=0.35, anchor="center")



        Bt_NovoCLiente = ctk.CTkButton(frame_resp, text="NOVO CLIENTE",  image=self.AdicionarIcon, text_color=("black","white"), 
                                    width=100,fg_color=("white", "gray10"), hover_color=("gray80", 'gray40'))
        
        Bt_NovoCLiente.place(relx=0.35, rely=0.85, anchor="w")


        Menu_LimiteView = ctk.CTkOptionMenu(frame_resp,  height=37, width=80, font=(ctk.CTkFont(size=11, weight="bold")), values=['10','100','1000','10000'], command=Atualizar_limiteView)
        Menu_LimiteView.place(relx=0.70, rely=0.35, anchor="center")
     
        # Criando o widget Treeview
        tree = ttk.Treeview(frame_resp, columns=([f'coluna{c}' for c in range(1,len(textcoluna)+1)]), show="headings")
        tree.place(x=50,y=300, width=1050, height=300)  


        # Adicionando uma barra de rolagem ao Treeview
        scroll_y = ttk.Scrollbar(frame_resp, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll_y.set)
        scroll_y.place(x=1100, y=300, height=300)  # Ajuste a posição x para 850


        # Adicionando uma barra de rolagem horizontal ao Treeview
        scroll_x = ttk.Scrollbar(frame_resp, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.place(x=50, y=600, width=1050) 


   
        style = ttk.Style()
        # style.theme_use("clam")
        style.configure('Treeview.Heading', background="white")
        style.configure("Treeview.Heading", font=("calibri", 11, "bold"))
        style.map("Treeview", background=[('selected', 'gray90')], foreground=[('selected', 'black')])  
        tree.bind("<<TreeviewSelect>>", click_select)


        Reexibir_treeview(ListaClientes)

                





                        








Menu()