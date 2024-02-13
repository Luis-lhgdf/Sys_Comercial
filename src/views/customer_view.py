from src.views.icones import *
from src.views.modelo_cadastro import ModeloCadastro


class InterfaceNovoCliente(ModeloCadastro):

    def __init__(self, main_app, frame_resp):
        self.main_app = main_app
        self.frame_resp = frame_resp
        self.cursor = self.main_app.ConexaoPrincipal.cursor()
        self.placehold = 'Pesquise por ID, CNPJ, CPF, nome ou razão social'
        self.colunas_bd = ['razao_social', 'cpf', 'cnpj', 'id', 'nome']

        super().__init__(main_app=self.main_app, frame_resp=self.frame_resp, tabela_bd="Clientes",
                         titulo_janela="CLIENTES", placeholder_text_pesquisar=self.placehold,
                         colunas_consulta=self.colunas_bd,
                         func_interface=self.interface_create, func_editar=self.editar_cliente,
                         func_create_update=lambda: self.interface_create('CREATE'))

        self.Bt_Novo = ctk.CTkButton(self.frame_resp, text="NOVO", image=AdicionarIcon, text_color=("black", "white"),
                                     width=100, command=lambda: self.interface_create('CREATE'))

    def editar_cliente(self):
        lista = self.valor_unico_selecionado
        tipo_cliente = str(lista[1])

        # ('id', 'tipo_de_cliente', 'cpf', 'cnpj', 'email',
        #  'razao_social', 'nome', 'cep', 'endereco', 'numero',
        #  'complemento', 'bairro', 'cidade', 'uf', 'fone',
        #  'celular', 'questionario', 'observacoes')

        # ('143', 'Pessoa Jurídica', 'None', '12.345.678/0001-99', 'empresa1@example.com',
        #  'Empresa XYZ Ltda.', 'Empresa XYZ', '54321-876', 'Avenida dos Negócios', '456',
        #  'None', 'Bairro Comercial', 'Rio de Janeiro', 'RJ', '(21) 2222-2222',
        #  '(21) 98888-8888', 'Respondeu parcialmente ao questionário.', 'Informacões adicionais importantes.')

        self.interface_create('UPDATE')

        self.menu_tipocliente.set(f'{str(lista[1]).upper()}')
        self.entry_nome.insert(0, f'{lista[6]}')

        if tipo_cliente == 'PESSOA FISICA':
            cpf = int(str(lista[2]).replace(".", "").replace("-", ""))
            self.entry_cpf_cnpj.insert(0, f'{cpf}')

        elif tipo_cliente == 'PESSOA JURIDICA':
            cnpj = int(str(lista[3]).replace(".", "").replace("-", "").replace("/", ""))

            self.entry_cpf_cnpj.insert(0, f'{cnpj}')
            self.entry_razao_social.insert(0, f'{str(lista[5])}')

        self.entry_email.insert(0, f'{str(lista[4])}')
        self.entry_cep.insert(0, f"{int(str(lista[7]).replace('-', ''))}")
        self.entry_endereco.insert(0, f"{str(lista[8])}")
        self.entry_numero.insert(0, f"{int(lista[9])}")
        self.entry_complemento.insert(0, f"{str(lista[10])}")
        self.entry_bairro.insert(0, f"{str(lista[11])}")
        self.entry_cidade.insert(0, f"{str(lista[12])}")
        self.entry_uf.insert(0, f"{str(lista[13])}")
        self.entry_fone.insert(0,
                               f"{int(str(lista[14]).replace('(', '').replace(')', '').replace(' ', '').replace('-', ''))}")

        self.entry_celular.insert(0,
                                  f"{int(str(lista[15]).replace('(', '').replace(')', '').replace(' ', '').replace('-', ''))}")

        self.menu_questionario.set(f'{str(lista[16])}')
        self.entry_observacoes.insert('1.0', f"{str(lista[17])}")

    def interface_create(self, tipo: str):
        # Esconder os widgets em vez de destruí-los
        self.acao_widget('ocultar')

        self.LabelTitulo.configure(text=('CADASTRAR CLIENTE' if tipo.upper() == "CREATE"
                                         else 'EDITAR CLIENTE' if tipo.upper() == "UPDATE" else ''))
        # Crie o widget para a opcão 'tipo_de_cliente'

        self.label_tipo_cliente = ctk.CTkLabel(self.frame_resp, text='Tipo de Cliente:', font=(None, 12, "bold"))
        self.label_tipo_cliente.place(x=50, y=50, anchor="w")

        self.menu_tipocliente = ctk.CTkOptionMenu(self.frame_resp, values=['PESSOA FISICA', 'PESSOA JURIDICA'],
                                                  command=self.definir_cliente)
        self.menu_tipocliente.place(x=50, y=80, anchor="w")

        self.label_cpf_cnpj = ctk.CTkLabel(self.frame_resp, text='CPF/CNPJ:*', font=(None, 12, "bold"))
        self.label_cpf_cnpj.place(x=250, y=50, anchor="w")

        self.entry_cpf_cnpj = ctk.CTkEntry(self.frame_resp, width=150)
        self.entry_cpf_cnpj.place(x=250, y=80, anchor="w")

        self.label_email = ctk.CTkLabel(self.frame_resp, text='Email:', font=(None, 12, "bold"))
        self.label_email.place(x=450, y=50, anchor="w")
        self.entry_email = ctk.CTkEntry(self.frame_resp, width=300)
        self.entry_email.place(x=450, y=80, anchor="w")

        self.label_razao_social = ctk.CTkLabel(self.frame_resp, text='Razão Social:', font=(None, 12, "bold"))
        self.label_razao_social.place(x=800, y=50, anchor="w")
        self.entry_razao_social = ctk.CTkEntry(self.frame_resp, width=300, validate="key",
                                               validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_razao_social.place(x=800, y=80, anchor="w")

        self.label_nome = ctk.CTkLabel(self.frame_resp, text='Nome:*', font=(None, 12, "bold"))
        self.label_nome.place(x=50, y=140, anchor="w")
        self.entry_nome = ctk.CTkEntry(self.frame_resp, width=300, validate="key",
                                       validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_nome.place(x=50, y=170, anchor="w")

        self.label_cep = ctk.CTkLabel(self.frame_resp, text='CEP:*', font=(None, 12, "bold"))
        self.label_cep.place(x=400, y=140, anchor="w")

        self.entry_cep = ctk.CTkEntry(self.frame_resp, validate="key",
                                      validatecommand=(self.main_app.validate_cmd_numeric, "%P", 8))
        self.entry_cep.place(x=400, y=170, anchor="w")

        self.label_endereco = ctk.CTkLabel(self.frame_resp, text='Endereco:*', font=(None, 12, "bold"))
        self.label_endereco.place(x=600, y=140, anchor="w")
        self.entry_endereco = ctk.CTkEntry(self.frame_resp, width=300, validate="key",
                                           validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_endereco.place(x=600, y=170, anchor="w")

        self.label_numero = ctk.CTkLabel(self.frame_resp, text='N°:*', font=(None, 12, "bold"))
        self.label_numero.place(x=950, y=140, anchor="w")
        self.entry_numero = ctk.CTkEntry(self.frame_resp, width=50, validate="key",
                                         validatecommand=(self.main_app.validate_cmd_numeric, "%P", 5))
        self.entry_numero.place(x=950, y=170, anchor="w")

        self.label_complemento = ctk.CTkLabel(self.frame_resp, text='Complemento:', font=(None, 12, "bold"))
        self.label_complemento.place(x=50, y=230, anchor="w")

        self.entry_complemento = ctk.CTkEntry(self.frame_resp, width=300, validate="key",
                                              validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_complemento.place(x=50, y=260, anchor="w")

        self.label_bairro = ctk.CTkLabel(self.frame_resp, text='Bairro:*', font=(None, 12, "bold"))
        self.label_bairro.place(x=400, y=230, anchor="w")
        self.entry_bairro = ctk.CTkEntry(self.frame_resp, validate="key",
                                         validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_bairro.place(x=400, y=260, anchor="w")

        self.label_cidade = ctk.CTkLabel(self.frame_resp, text='Cidade:*', font=(None, 12, "bold"))
        self.label_cidade.place(x=600, y=230, anchor="w")

        self.entry_cidade = ctk.CTkEntry(self.frame_resp, validate="key",
                                         validatecommand=(self.main_app.validade_cmd_text, "%P", 500))
        self.entry_cidade.place(x=600, y=260, anchor="w")

        self.label_uf = ctk.CTkLabel(self.frame_resp, text='UF:*', font=(None, 12, "bold"))
        self.label_uf.place(x=800, y=230, anchor="w")
        self.entry_uf = ctk.CTkEntry(self.frame_resp, width=50, validate="key",
                                     validatecommand=(self.main_app.validade_cmd_text, "%P", 2, False))
        self.entry_uf.place(x=800, y=260, anchor="w")

        self.label_fone = ctk.CTkLabel(self.frame_resp, text='Telefone:', font=(None, 12, "bold"))
        self.label_fone.place(x=900, y=230, anchor="w")
        self.entry_fone = ctk.CTkEntry(self.frame_resp, placeholder_text="(xx) 0000-0000", validate="key",
                                       validatecommand=(self.main_app.validate_cmd_numeric, "%P", 10))
        self.entry_fone.place(x=900, y=260, anchor="w")

        self.label_celular = ctk.CTkLabel(self.frame_resp, text='Celular:', font=(None, 12, "bold"))
        self.label_celular.place(x=50, y=320, anchor="w")
        self.entry_celular = ctk.CTkEntry(self.frame_resp, placeholder_text="(xx)9 0000-0000", validate="key",
                                          validatecommand=(self.main_app.validate_cmd_numeric, "%P", 11))
        self.entry_celular.place(x=50, y=360, anchor="w")

        self.label_questionario = ctk.CTkLabel(self.frame_resp, text='Como conheceu a empresa:',
                                               font=(None, 12, "bold"))
        self.label_questionario.place(x=250, y=320, anchor="w")
        self.menu_questionario = ctk.CTkOptionMenu(self.frame_resp,
                                                   values=['', 'INSTAGRAM', 'FACEBOOK', 'SITE', 'TIKTOK', 'INDICAcÃO',
                                                           'OUTRO'])
        self.menu_questionario.place(x=250, y=360, anchor="w")

        self.label_observacoes = ctk.CTkLabel(self.frame_resp, text='Observacões:', font=(None, 12, "bold"))
        self.label_observacoes.place(x=50, y=420, anchor="w")
        self.entry_observacoes = ctk.CTkTextbox(self.frame_resp, width=self.main_app.screen_wedth - 310, height=100)
        self.entry_observacoes.place(x=50, y=450)

        self.Bt_Voltar = ctk.CTkButton(self.frame_resp, text="Voltar", image=VoltarIcon, text_color=("black", "white"),
                                       width=100, anchor="w", command=lambda: self.voltar('ocultar'))

        self.Bt_Voltar.place(relx=0.3, rely=0.85, anchor="w")

        self.Bt_Novo_Cliente = ctk.CTkButton(self.frame_resp, text="SALVAR", image=SalvarIcon,
                                             text_color=("black", "white"),
                                             width=100, command=lambda: self.salvar_cliente(tipo))
        self.Bt_Novo_Cliente.place(relx=0.4, rely=0.85, anchor="w")

        self.definir_cliente(resposta="PESSOA FISICA")

    def salvar_cliente(self, tipo):
        resp = self.main_app.msgbox("SALVAR", "Deseja salvar todas as informacões passadas?", 4)
        if resp == 6:

            "id, tipo_de_cliente, cpf, cnpj, email, razao_social, nome, cep, endereco, numero, complemento, bairro, cidade, uf, telefone, celular, questionario, observacoes"

            tipo_cliente = self.menu_tipocliente.get()
            entry_cpf_cnpj = self.entry_cpf_cnpj.get()
            entry_email = self.entry_email.get()
            entry_razao_social = self.entry_razao_social.get()
            entry_nome = self.entry_nome.get()
            entry_cep = self.entry_cep.get()
            entry_endereco = self.entry_endereco.get()
            entry_numero = self.entry_numero.get()
            entry_complemento = self.entry_complemento.get()
            entry_bairro = self.entry_bairro.get()
            entry_cidade = self.entry_cidade.get()
            entry_uf = self.entry_uf.get()
            entry_fone = self.entry_fone.get()
            entry_celular = self.entry_celular.get()
            menu_questionario = self.menu_questionario.get()
            entry_observacoes = self.entry_observacoes.get("0.0", "end")

            # Verifica se os campos obrigatórios estão preenchidos
            if not entry_nome or not entry_cep or not entry_endereco or not entry_numero or not entry_bairro or not entry_cidade or not entry_uf or not entry_cpf_cnpj:
                self.entry_nome.configure(border_color="red")
                self.entry_cep.configure(border_color="red")
                self.entry_endereco.configure(border_color="red")
                self.entry_numero.configure(border_color="red")
                self.entry_bairro.configure(border_color="red")
                self.entry_cidade.configure(border_color="red")
                self.entry_uf.configure(border_color="red")
                self.entry_cpf_cnpj.configure(border_color="red")

                self.main_app.msgbox("Campos obrigatórios não preenchidos",
                                     "Por favor, preencha todos os campos obrigatórios antes de salvar.", 0)
                return

            if tipo == 'CREATE' or tipo == 'UPDATE':
                cnpj = None
                cpf = None

                query = ()
                values = ()

                if tipo_cliente == 'PESSOA FISICA':
                    cpf = entry_cpf_cnpj
                    cnpj = None
                elif tipo_cliente == 'PESSOA JURIDICA':
                    cnpj = entry_cpf_cnpj
                    cpf = None

                if tipo == 'CREATE':
                    query = """INSERT INTO Clientes (tipo_de_cliente, cpf, cnpj, email, razao_social, nome, cep, endereco, numero, complemento, bairro, cidade, uf, telefone, celular, questionario, observacoes)
                            VALUES (?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?, ?) """
                    values = (
                        tipo_cliente, cpf, cnpj, entry_email, entry_razao_social, entry_nome, entry_cep, entry_endereco,
                        entry_numero, entry_complemento, entry_bairro, entry_cidade, entry_uf, entry_fone,
                        entry_celular,
                        menu_questionario, entry_observacoes)

                elif tipo == 'UPDATE':

                    lista = self.valor_unico_selecionado
                    id_cliente = lista[0]
                    # You need to implement this method to get the selected client's ID
                    query = """UPDATE Clientes SET tipo_de_cliente = ?, cpf = ?, cnpj = ?, email = ?, razao_social = ?, nome = ?, cep = ?, endereco = ?, numero = ?, complemento = ?, bairro = ?, cidade = ?, uf = ?, telefone = ?, celular = ?, questionario = ?, observacoes = ?
                            WHERE id = ?"""
                    values = (
                        tipo_cliente, cpf, cnpj, entry_email, entry_razao_social, entry_nome, entry_cep, entry_endereco,
                        entry_numero, entry_complemento, entry_bairro, entry_cidade, entry_uf, entry_fone,
                        entry_celular,
                        menu_questionario, entry_observacoes, id_cliente)

                self.cursor.execute(query, values)
                # Commit the changes to the database
                self.main_app.ConexaoPrincipal.commit()

                self.entry_nome.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_cep.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_endereco.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_numero.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_bairro.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_cidade.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_uf.configure(border_color=("#979DA2", "#565B5E"))
                self.entry_cpf_cnpj.configure(border_color=("#979DA2", "#565B5E"))

                if tipo == 'CREATE':
                    self.main_app.msgbox("NOVO CLIENTE", "Novo cliente adicionado com sucesso!", 0)
                elif tipo == 'UPDATE':
                    self.main_app.msgbox("ATUALIZAR", "Informacões do cliente atualizadas com sucesso!", 0)

                self.menu_tipocliente.set(f'{tipo_cliente}')
                self.entry_cpf_cnpj.delete(0, ctk.END)
                self.entry_email.delete(0, ctk.END)
                self.entry_razao_social.delete(0, ctk.END)
                self.entry_nome.delete(0, ctk.END)
                self.entry_cep.delete(0, ctk.END)
                self.entry_endereco.delete(0, ctk.END)
                self.entry_numero.delete(0, ctk.END)
                self.entry_complemento.delete(0, ctk.END)
                self.entry_bairro.delete(0, ctk.END)
                self.entry_cidade.delete(0, ctk.END)
                self.entry_uf.delete(0, ctk.END)
                self.entry_fone.delete(0, ctk.END)
                self.entry_celular.delete(0, ctk.END)
                self.menu_questionario.set(f'')
                self.entry_observacoes.delete("0.0", "end")

            else:
                pass

    def definir_cliente(self, resposta):

        if resposta == 'PESSOA FISICA':

            self.entry_cpf_cnpj.configure(validate="key",
                                          validatecommand=(self.main_app.validate_cmd_numeric, "%P", 11))

        elif resposta == "PESSOA JURIDICA":
            self.entry_cpf_cnpj.configure(validate="key",
                                          validatecommand=(self.main_app.validate_cmd_numeric, "%P", 14))
