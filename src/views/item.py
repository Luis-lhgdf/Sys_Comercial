from src.views.icones import *
from src.views.modelo_cadastro import ModeloCadastro


class InterfaceNovoItem(ModeloCadastro):

    def __init__(self, main_app, frame_resp):
        self.main_app = main_app
        self.frame_resp = frame_resp
        self.cursor = self.main_app.ConexaoPrincipal.cursor()
        self.placehold = 'Pesquise por Id, Descrição, Marca, Categoria ou Fornecedor'
        self.colunas_bd = ['Id', 'descricao_produto', 'marca', 'categoria', 'fornecedor']

        super().__init__(main_app=self.main_app, frame_resp=self.frame_resp, tabela_bd="Produtos",
                         titulo_janela="ITENS", placeholder_text_pesquisar=self.placehold,
                         colunas_consulta=self.colunas_bd,
                         func_interface=self.interface_create, func_editar=self.editar_produto,
                         func_create_update=lambda: self.interface_create('CREATE'))

    def editar_produto(self):
        lista = self.valor_unico_selecionado

        self.interface_create('UPDATE')

        # pegue o valor de cada entry
        self.entry_descricao_produto.insert(0, f'{lista[1]}')
        self.entry_unidade_medida.insert(0, f'{lista[2]}')
        self.entry_valor_unitario.insert(0, f'{lista[3]}')
        self.entry_marca.insert(0, f'{lista[4]}')
        self.entry_categoria.insert(0, f'{lista[5]}')
        self.entry_peso.insert(0, f'{lista[6]}')
        self.entry_fornecedor.insert(0, f'{lista[7]}')
        self.entry_info_adicionais.insert("1.0", f"{lista[8]}")

    def interface_create(self, tipo: str):
        # Esconder os widgets em vez de destruí-los

        # descricao_produto, unidade_medida, valor_unitario, marca, categoria, Peso, fornecedor, info_adicionais

        self.acao_widget('ocultar')

        self.LabelTitulo.configure(text=('CADASTRAR ITEM' if tipo.upper() == "CREATE"
                                         else 'EDITAR ITEM' if tipo.upper() == "UPDATE" else ''))

        self.label_descricao_produto = ctk.CTkLabel(self.frame_resp, text='Descricão do Produto:',
                                                    font=(None, 12, "bold"))
        self.label_descricao_produto.place(x=50, y=50, anchor="w")
        self.entry_descricao_produto = ctk.CTkEntry(self.frame_resp, width=300)
        self.entry_descricao_produto.place(x=50, y=80, anchor="w")

        self.label_unidade_medida = ctk.CTkLabel(self.frame_resp, text='Unidade de Medida:', font=(None, 12, "bold"))
        self.label_unidade_medida.place(x=400, y=50, anchor="w")

        self.entry_unidade_medida = ctk.CTkEntry(self.frame_resp, width=150)
        self.entry_unidade_medida.place(x=400, y=80, anchor="w")

        self.label_valor_unitario = ctk.CTkLabel(self.frame_resp, text='Valor Unitário:', font=(None, 12, "bold"))
        self.label_valor_unitario.place(x=600, y=50, anchor="w")
        self.entry_valor_unitario = ctk.CTkEntry(self.frame_resp, width=100)
        self.entry_valor_unitario.place(x=600, y=80, anchor="w")

        self.label_marca = ctk.CTkLabel(self.frame_resp, text='Marca:', font=(None, 12, "bold"))
        self.label_marca.place(x=750, y=50, anchor="w")
        self.entry_marca = ctk.CTkEntry(self.frame_resp, width=150)
        self.entry_marca.place(x=750, y=80, anchor="w")

        self.label_categoria = ctk.CTkLabel(self.frame_resp, text='Categoria:', font=(None, 12, "bold"))
        self.label_categoria.place(x=50, y=120, anchor="w")
        self.entry_categoria = ctk.CTkEntry(self.frame_resp, width=200)
        self.entry_categoria.place(x=50, y=150, anchor="w")

        self.label_peso = ctk.CTkLabel(self.frame_resp, text='Peso:', font=(None, 12, "bold"))
        self.label_peso.place(x=300, y=120, anchor="w")
        self.entry_peso = ctk.CTkEntry(self.frame_resp, width=100)
        self.entry_peso.place(x=300, y=150, anchor="w")

        self.label_fornecedor = ctk.CTkLabel(self.frame_resp, text='Fornecedor:', font=(None, 12, "bold"))
        self.label_fornecedor.place(x=450, y=120, anchor="w")
        self.entry_fornecedor = ctk.CTkEntry(self.frame_resp, width=250, validate="key",
                                             validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_fornecedor.place(x=450, y=150, anchor="w")

        self.label_info_adicionais = ctk.CTkLabel(self.frame_resp, text='Informacões Adicionais:',
                                                  font=(None, 12, "bold"))
        self.label_info_adicionais.place(x=50, y=190, anchor="w")
        self.entry_info_adicionais = ctk.CTkTextbox(self.frame_resp, width=self.main_app.screen_wedth - 310,
                                                    height=100)
        self.entry_info_adicionais.place(x=50, y=220)

        self.Bt_Voltar = ctk.CTkButton(self.frame_resp, text="Voltar", image=VoltarIcon,
                                       text_color=("black", "white"),
                                       width=100, anchor="w", command=lambda: self.voltar('ocultar'))

        self.Bt_Voltar.place(relx=0.3, rely=0.85, anchor="w")

        self.Bt_Novo_Cliente = ctk.CTkButton(self.frame_resp, text="SALVAR", image=SalvarIcon,
                                             text_color=("black", "white"),
                                             width=100, command=lambda: self.salvar_produto(tipo))
        self.Bt_Novo_Cliente.place(relx=0.4, rely=0.85, anchor="w")

    def salvar_produto(self, tipo):
        resp = self.main_app.msgbox("SALVAR", "Deseja salvar todas as informacões passadas?", 4)
        if resp == 6:

            # descricao_produto, unidade_medida, valor_unitario, marca, categoria, Peso, fornecedor, info_adicionais"

            # pegue o valor de cada entry
            descricao_produto = self.entry_descricao_produto.get()
            unidade_medida = self.entry_unidade_medida.get()
            valor_unitario = self.entry_valor_unitario.get()

            valor_unitario = float(valor_unitario) if valor_unitario and valor_unitario.replace(".",
                                                                                                "").isdigit() else None
            marca = self.entry_marca.get()
            categoria = self.entry_categoria.get()
            peso = self.entry_peso.get()
            peso = float(peso) if peso and peso.replace(".", "", 1).isdigit() else None
            fornecedor = self.entry_fornecedor.get()
            info_adicionais = self.entry_info_adicionais.get("0.0", "end")

            query = ()
            values = ()

            # Verifica se os campos obrigatórios estão preenchidos

            if not descricao_produto or not unidade_medida or not valor_unitario:
                # edite a cor para vermelho das entry
                self.entry_descricao_produto.configure(border_color="red")
                self.entry_unidade_medida.configure(border_color="red")
                self.entry_valor_unitario.configure(border_color="red")

                self.main_app.msgbox("Campos obrigatórios não preenchidos",
                                     "Por favor, preencha todos os campos obrigatórios antes de salvar.", 0)

                return

            if tipo == 'CREATE':

                query = """INSERT INTO Produtos (descricao_produto, unidade_medida, valor_unitario, 
                        marca, categoria, peso, fornecedor, info_adicionais)
                        VALUES (?, ?, ?, ?,?, ?, ?, ?) """
                values = (
                    descricao_produto, unidade_medida, valor_unitario, marca, categoria, peso, fornecedor,
                    info_adicionais)

            elif tipo == 'UPDATE':

                lista = self.valor_unico_selecionado
                id_produto = lista[0]

                query = """UPDATE Produtos SET descricao_produto = ?, unidade_medida = ?, valor_unitario = ?, 
                marca = ?, categoria = ?, peso = ?, fornecedor = ?, info_adicionais = ? WHERE id = ?"""

                values = (
                    descricao_produto, unidade_medida, valor_unitario, marca, categoria, peso, fornecedor,
                    info_adicionais,
                    id_produto)

                self.cursor.execute(query, values)

                self.main_app.ConexaoPrincipal.commit()

                self.entry_descricao_produto.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_unidade_medida.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_valor_unitario.configure(border_color=("#979DA2", "#565B5E"))

            self.cursor.execute(query, values)
            # Commit the changes to the database
            self.main_app.ConexaoPrincipal.commit()

            if tipo == 'CREATE':
                self.main_app.msgbox("NOVO PRODUTO", "Novo Produto adicionado com sucesso!", 0)
            elif tipo == 'UPDATE':
                self.main_app.msgbox("ATUALIZAR", "Informacões do Produto atualizadas com sucesso!", 0)

            self.entry_descricao_produto.delete(0, ctk.END)
            self.entry_unidade_medida.delete(0, ctk.END)
            self.entry_valor_unitario.delete(0, ctk.END)
            self.entry_marca.delete(0, ctk.END)
            self.entry_categoria.delete(0, ctk.END)
            self.entry_peso.delete(0, ctk.END)
            self.entry_fornecedor.delete(0, ctk.END)
            self.entry_info_adicionais.delete("0.0", "end")
