from src.views.icones import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import filedialog
import pandas as pd


class ModeloCadastro:
    def __init__(self, main_app, frame_resp, tabela_bd: str, titulo_janela: str, placeholder_text_pesquisar: str,
                 colunas_consulta: list,
                 func_interface, func_editar, func_create_update):

        self.main_app = main_app
        self.frame_resp = frame_resp
        self.tabela_bd = tabela_bd
        self.titulo_janela = titulo_janela
        self.colunas_consulta = colunas_consulta
        self.placeholder_text_pesquisar = placeholder_text_pesquisar
        self.func_interface = func_interface
        self.func_editar = func_editar
        self.func_create_update = func_create_update

        self.cursor = self.main_app.ConexaoPrincipal.cursor()
        self.limite_view = 10

        self.column_names = None
        self.lista_valores = None
        self.total_valores = 0

        self.valor_unico_selecionado = None
        self.valor_lista_selecionado = None

        self.LabelTitulo = ctk.CTkLabel(self.frame_resp, text=f"{str(titulo_janela).upper()}", fg_color="transparent",
                                        text_color=("black", "white"), font=(ctk.CTkFont(size=14, weight="bold")),
                                        corner_radius=6)
        self.LabelTitulo.place(x=1, y=1)

        self.interface_tabela()

    def acao_widget(self, acao):
        if acao == 'ocultar':
            for widget in self.frame_resp.winfo_children():
                if widget != self.LabelTitulo:
                    widget.place_forget()
        if acao == 'reexibir':
            for widget in self.frame_resp.winfo_children():
                if widget != self.LabelTitulo:
                    widget.place(x=widget.winfo_x(), y=widget.winfo_y())

    def interface_tabela(self):
        frame_treeview = tk.Frame(self.frame_resp)
        frame_treeview.place(x=25, y=400, width=self.main_app.screen_wedth, height=305)

        self.tree = ttk.Treeview(frame_treeview, show="headings")
        self.tree.place(x=0, y=0, height=305)
        self.tree.bind("<<TreeviewSelect>>", self.click_select)

        self.scroll_x = ttk.Scrollbar(frame_treeview, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.scroll_y = ttk.Scrollbar(frame_treeview, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.LabelPesquisar = ctk.CTkLabel(self.frame_resp, text="Busca rapida", fg_color="transparent",
                                           font=(ctk.CTkFont(size=14, weight="bold")))
        self.LabelPesquisar.place(relx=0.36, rely=0.13, anchor="w")

        self.Label_Select = ctk.CTkLabel(self.frame_resp, text=f"SELECIONADO: ", height=37, width=250, fg_color="white",
                                         text_color="black",
                                         font=(ctk.CTkFont(size=12, weight="bold")), corner_radius=6, anchor="w")
        self.Label_Select.place(x=50, y=250)

        self.Label_LimiteView = ctk.CTkLabel(self.frame_resp, height=37,
                                             text=f"01 A {self.limite_view} DE {self.total_valores}",
                                             font=(ctk.CTkFont(size=12, weight="bold")), anchor="w")
        self.Label_LimiteView.place(x=820, y=255)

        self.Entry_Pesquisar = ctk.CTkEntry(self.frame_resp, placeholder_text=f"{self.placeholder_text_pesquisar}",
                                            width=550, height=40)
        self.Entry_Pesquisar.place(relx=0.2, rely=0.18, anchor="w")

        self.Bt_Todos = ctk.CTkButton(self.frame_resp, text="TODOS", image=EntradaIcon, text_color=("black", "white"),
                                      width=80, command=self.todos)
        self.Bt_Todos.place(relx=0.7, rely=0.18, anchor="w")

        self.Bt_Pesquisar = ctk.CTkButton(self.frame_resp, image=VisualizarIcon, text_color=("black", "white"),
                                          text="PESQUISAR",
                                          width=80,
                                          command=lambda: self.pesquisar(self.colunas_consulta, self.tabela_bd))
        self.Bt_Pesquisar.place(relx=0.612, rely=0.18, anchor="w")

        self.Bt_Editar = ctk.CTkButton(self.frame_resp, text="Editar", text_color=("black", "white"), image=EditarIcon,
                                       width=40, fg_color="transparent", state="disabled", command=self.func_editar)
        self.Bt_Editar.place(x=320, y=250)

        self.Bt_Excluir = ctk.CTkButton(self.frame_resp, text="Excluir", text_color=("black", "white"),
                                        image=DeletarIcon,
                                        width=40, fg_color="transparent", state="disabled", command=self.excluir)
        self.Bt_Excluir.place(x=420, y=250)

        self.Bt_Excel = ctk.CTkButton(self.frame_resp, text="Excel", text_color=("black", "white"), image=ExcelIcon,
                                      width=40, fg_color="transparent", command=self.excel)
        self.Bt_Excel.place(x=1020, y=250)

        self.Bt_Novo = ctk.CTkButton(self.frame_resp, text="NOVO", image=AdicionarIcon, text_color=("black", "white"),
                                     width=100, command=self.func_create_update)
        self.Bt_Novo.place(relx=0.36, rely=0.85, anchor="w")

        self.Bt_Sincronizar = ctk.CTkButton(self.frame_resp, text="", image=sincronizar, text_color=("black", "white"),
                                            fg_color='transparent',
                                            command=self.sincronizar_tabela)
        self.Bt_Sincronizar.place(x=575, y=250)

        self.Menu_LimiteView = ctk.CTkOptionMenu(self.frame_resp, height=37, width=80,
                                                 font=(ctk.CTkFont(size=11, weight="bold")),
                                                 values=['10', '100', '1000', '10000'],
                                                 command=self.atualizar_limiteview)
        self.Menu_LimiteView.place(x=920, y=250)

        style = ttk.Style()
        style.configure('Treeview.Heading', background="white")
        style.configure("Treeview.Heading", font=('Roboto', 11, "bold"))
        style.configure('Treeview', font=('Roboto', 11))
        style.map("Treeview", background=[('selected', 'gray90')], foreground=[('selected', 'black')])

    def sincronizar_tabela(self, attlimite=True):
        self.Bt_Sincronizar.destroy()

        self.cursor.execute(f"SELECT * FROM {self.tabela_bd} limit 10")

        self.lista_valores = self.cursor.fetchall()

        self.column_names = [description[0] for description in self.cursor.description]

        self.cursor.execute(f"SELECT COUNT(*) AS total_linhas FROM {self.tabela_bd} ")

        self.total_valores = int((self.cursor.fetchone()[0]))

        self.tree.configure(columns=([f'coluna{c}' for c in range(1, len(self.column_names) + 1)]))

        if attlimite:
            self.atualizar_limiteview(10)

    def atualizar_limiteview(self, novo_limite):
        try:
            self.tree.delete(*self.tree.get_children())  # exclui todos os itens de uma treeview
        except tk.TclError:
            pass
        self.cursor.execute(f"SELECT * FROM {self.tabela_bd} limit {int(novo_limite)}")
        self.lista_valores = self.cursor.fetchall()

        self.Label_LimiteView.configure(
            text=f"""01 A {novo_limite if int(novo_limite) < self.total_valores
            else self.total_valores} "f"DE {self.total_valores}""")

        self.limite_view = int(novo_limite)

        self.reexibir_treeview(self.lista_valores)

    def reexibir_treeview(self, lista):
        try:
            self.tree.column("coluna1", width=50)
            self.tree.column("coluna10", width=50)
            self.tree.column("coluna14", width=50)
        except tk.TclError:
            pass

        for valor in lista:
            self.tree.insert("", "end", values=valor)
            # self.tree.tag_configure("center", anchor="center")

        for i, coluna in enumerate(self.tree['columns']):
            nome = str(self.column_names[i]).capitalize()

            self.tree.heading(coluna, text=f"{nome}")

            self.tree.column(coluna, stretch=False)

    def click_select(self, event):
        selected_item = self.tree.selection()
        lista = []
        if selected_item:
            if len(selected_item) == 1:
                unico = self.tree.item(selected_item, "values")
                self.valor_unico_selecionado = unico
                self.Label_Select.configure(text=f"SELECIONADO: {unico[6][0:20]}")
                self.Bt_Editar.configure(state="normal")
                self.Bt_Excluir.configure(state="normal")

            else:
                self.Bt_Editar.configure(state="disabled")
                self.Bt_Excluir.configure(state="normal")

                for item_id in selected_item:
                    valor = self.tree.item(item_id, "values")
                    lista.append(valor)

                    self.Label_Select.configure(text=f"SELECIONADO: {len(selected_item)}")

                self.valor_lista_selecionado = lista

    def todos(self):
        info_digitada = str(self.Entry_Pesquisar.get())
        if info_digitada:
            try:
                self.tree.delete(*self.tree.get_children())
            except tk.TclError:
                pass
            self.reexibir_treeview(self.lista_valores)

    def pesquisar(self, colunas_consulta, tabela_name):

        # TODO corrigir futuramente para o modulo de pqsquisar os clientes

        info_digitada = self.Entry_Pesquisar.get()
        if info_digitada:
            print(f"Tentou pesquisar por {info_digitada} nas colunas {colunas_consulta}")

            # Construir a consulta SQL de forma segura usando placeholders '?' para os parâmetros
            query = f"SELECT {', '.join(colunas_consulta)} FROM {tabela_name} WHERE {' OR '.join([f'{col} LIKE ?' for col in colunas_consulta])}"

            # Criar os parâmetros para substituir os placeholders na consulta
            parametros = ['%' + info_digitada + '%' for _ in colunas_consulta]

            try:
                # Executar a consulta SQL
                self.cursor.execute(query, parametros)
                lista = self.cursor.fetchall()
                # Atualizar a visualização
                self.tree.delete(*self.tree.get_children())
                self.reexibir_treeview(lista=lista)
            except sqlite3.Error as e:
                # Lidar com erros de SQLite
                print("Erro ao executar a consulta SQL:", e)

    def voltar(self, opcao):

        self.acao_widget(acao=opcao)
        self.interface_tabela()
        self.LabelTitulo.configure(text=f'{self.titulo_janela}')

    def excel(self):
        resp = self.main_app.msgbox("Excel", "Deseja exportar todos os registros?", 4)

        def destino(dataframe):
            folder_path = filedialog.asksaveasfilename(defaultextension='.xlsx')

            if folder_path:
                # Definir o nome do arquivo
                file_path = folder_path

                # Verificar se a extensão .xlsx foi adicionada
                if not file_path.endswith('.xlsx'):
                    file_path += '.xlsx'

                dataframe.to_excel(file_path, index=False)
                self.main_app.msgbox("Excel", "Arquivo salvo com sucesso", 0)

        if resp == 6:
            print("esta vazio, puxando valores no banco de dados")
            if self.lista_valores is None:
                self.cursor.execute("SELECT * FROM Clientes")
                self.lista_valores = self.cursor.fetchall()
                self.column_names = self.column_names = [description[0] for description in self.cursor.description]
                df = pd.DataFrame(self.lista_valores, columns=self.column_names)
                destino(dataframe=df)

            else:
                print("NAO ESTA VAZIA")
                df = pd.DataFrame(self.lista_valores, columns=self.column_names)
                destino(dataframe=df)

    def excluir(self):
        resp = self.main_app.msgbox("EXCLUIR", "Tem certeza que deseja excluir este cliente?", 4)
        if resp == 6:
            lista = self.lista_valores
            for valor in lista:
                id_valor = int(valor[0])

                query = f"DELETE FROM {self.tabela_bd} WHERE id = {id_valor}"
                self.cursor.execute(query)
                self.main_app.ConexaoPrincipal.commit()
            self.main_app.msgbox("EXCLUIR", "Valor excluído com sucesso!", 0)
            self.sincronizar_tabela(attlimite=False)
            self.atualizar_limiteview(self.limite_view)
