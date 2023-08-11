import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import pandas as pd
import re


# Variáveis globais para armazenar os valores calculados
valor_venda_sucateiro = 0
valor_cobre_novo = 0
quantidade_cobre_reforma = 0
valor_reindustrializacao = 0
diferenca = 0
cenario = 0 
dataconsulta = 0
listamateriais= ['Cobre', 'Alumínio']


def calcular_vantagem():
    global valor_venda_sucateiro, valor_cobre_novo, quantidade_cobre_reforma, valor_reindustrializacao, diferenca, cenario, dataconsulta

    valor_venda_sucateiro = entry_valor_venda_sucateiro.get()
    valor_cobre_novo = entry_valor_cobre_novo.get()
    quantidade_cobre_reforma = entry_quantidade_cobre_reforma.get()
    valor_reindustrializacao = entry_valor_reindustrializacao.get()
    dataconsulta = entry_dataconsulta.get()

    if any(val == "" for val in [valor_venda_sucateiro, valor_cobre_novo, quantidade_cobre_reforma, valor_reindustrializacao, dataconsulta]):
        messagebox.showinfo("Erro", "Há campos em branco")
        return

    valor_venda_sucateiro = float(valor_venda_sucateiro)
    valor_cobre_novo = float(valor_cobre_novo)
    quantidade_cobre_reforma = float(quantidade_cobre_reforma)
    valor_reindustrializacao = float(valor_reindustrializacao)
    dataconsulta = str(entry_dataconsulta.get())

    # Cálculo dos valores
    valor_total_venda_sucateiro = valor_venda_sucateiro * (quantidade_cobre_reforma * 1.33)
    valor_total_reindustrializacao = valor_reindustrializacao * quantidade_cobre_reforma
    valor_compra_fio_novo = quantidade_cobre_reforma * valor_cobre_novo
    diferenca = valor_compra_fio_novo - valor_total_venda_sucateiro


    # Exibição do resultado
    if diferenca < valor_total_reindustrializacao:
        resultado = f"Cenário mais vantajoso: Vender para o sucateiro e comprar cobre novo.\n" \
                    f"Custo total: R$ {diferenca:.2f}\n" \
                    f"Cobre necessário para comprar: {quantidade_cobre_reforma:.2f} kg"
        cenario= 'Vender'
    else:
        resultado = f"Cenário mais vantajoso: Reindustrializar o cobre usado.\n" \
                    f"Custo total: R$ {valor_total_reindustrializacao:.2f}\n" \
                    f"Cobre necessário para comprar: Não é necessário comprar cobre, mas enviar {quantidade_cobre_reforma * 1.33} kg para reindustrializar."
        cenario= 'Reindustrializar'
            
            
    messagebox.showinfo("Resultado", resultado)

def procurar_pasta():
    folder_selected = filedialog.askdirectory()  # Abre o diálogo de seleção de pasta
    entry_path.delete(0, tk.END)  # Limpa o conteúdo da caixa de entrada
    entry_path.insert(0, folder_selected)  # Insere o caminho da pasta selecionada na caixa de entrada
    return folder_selected


def salvar_em_excel(diretorio):
    if not diretorio:
        messagebox.showerror("Erro", "Nenhum diretório selecionado.")
        return

    data = {'Data': [dataconsulta],
            'Venda sucateiro': [valor_venda_sucateiro],
            'Cobre novo': [valor_cobre_novo],
            'Qnt. neces. reforma': [quantidade_cobre_reforma],
            'Valor reind.': [valor_reindustrializacao],
            'Cenário mais vantajoso': [cenario]
            }
    df = pd.DataFrame(data)
    file_path = f'{diretorio}/{entry_nomearquivo.get()}.xlsx'
    df.to_excel(file_path, index=False)
    messagebox.showinfo("Salvo em Excel", "Dados salvos em Excel com sucesso!")


def validate_date_input(P):
    # Verifica se o padrão de data está correto (dd/mm/aaaa)
    return re.match(r"^[0-9/]*$", P) is not None


def validate_numeric_input(P):
    # Verifica se a entrada contém apenas números ou está vazia
    return P == "" or (re.match(r'^\d+(\.\d*)?$', P) is not None)


# Criação da interface gráfica

root= tk.Tk()
root.title("Calculadora de Vantagem - Serviços recuperação de equipamentos SER")
# root.iconbitmap(r'C:\Users\2020283\Desktop\cpfl.ico')
root.geometry("565x460")

# image = tk.PhotoImage(file=(r'C:\Users\2020283\Desktop\servicos.png'))
# background_label = tk.Label(root, image=image)
# background_label.place(x=300, y=450, anchor='s')
# background_label.lower()

root.resizable(False, False)


#ComboBox
labels_combobox = tk.Label(root, text="Selecione o material teórico para compra")
labels_combobox.place(x=10, y=160)
cb_materiais= ttk.Combobox(root,values=listamateriais, state="readonly")
cb_materiais.place(x=260, y=160)
cb_materiais.set('Cobre')


validate_date = root.register(validate_date_input)

# Caixa para data da consulta
label_dataconsulta = tk.Label(root, text="Data da consulta")
label_dataconsulta.place(x=10, y=10)
entry_dataconsulta = tk.Entry(root, width=10, validate="key", validatecommand=(validate_date, "%P"))
entry_dataconsulta.place(x=300, y=10)
label_unidade5 = tk.Label(root, text="dd/mm/aaaa")
label_unidade5.place(x=370, y=10)

validate_numeric = root.register(validate_numeric_input)

# Caixa para valor de venda ao sucateiro
label_valor_venda_sucateiro = tk.Label(root, text="Valor da venda ao sucateiro por quilo")
label_valor_venda_sucateiro.place(x=10, y=40)
entry_valor_venda_sucateiro = tk.Entry(root, width=10, validate="key", validatecommand=(validate_numeric, "%P"))
entry_valor_venda_sucateiro.place(x=300, y=40)
label_unidade1 = tk.Label(root, text="R$")
label_unidade1.place(x=370, y=40)

# Caixa para valor do material (cobre ou aluminio) novo por quilo
label_valor_cobre_novo = tk.Label(root, text="Valor do material (cobre ou aluminio) novo por quilo")
label_valor_cobre_novo.place(x=10, y=70)
entry_valor_cobre_novo = tk.Entry(root, width=10, validate="key", validatecommand=(validate_numeric, "%P"))
entry_valor_cobre_novo.place(x=300, y=70)
label_unidade2 = tk.Label(root, text="R$")
label_unidade2.place(x=370, y=70)

# Caixa para quantidade de cobre necessária para retornar
label_quantidade_cobre_reforma = tk.Label(root, text="Quantidade de cobre necessária para retornar")
label_quantidade_cobre_reforma.place(x=10, y=100)
entry_quantidade_cobre_reforma = tk.Entry(root, width=10, validate="key", validatecommand=(validate_numeric, "%P"))
entry_quantidade_cobre_reforma.place(x=300, y=100)
label_unidade3 = tk.Label(root, text="Kg")
label_unidade3.place(x=370, y=100)

# Caixa para valor da reindustrialização por quilo
label_valor_reindustrializacao = tk.Label(root, text="Valor da reindustrialização por quilo")
label_valor_reindustrializacao.place(x=10, y=130)
entry_valor_reindustrializacao = tk.Entry(root, width=10, validate="key", validatecommand=(validate_numeric, "%P"))
entry_valor_reindustrializacao.place(x=300 ,y=130)
label_unidade4 = tk.Label(root, text="R$")
label_unidade4.place(x=370, y=130)



# Botão calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular_vantagem)
btn_calcular.configure(bg='lightblue', fg='black', font=('Helvetica', 9))
btn_calcular.place(x=305, y=190)

# Caixa para nome do arquivo
label_nomearquivo = tk.Label(root, text="Nome do arquivo a ser salvo")
label_nomearquivo.place(x=10, y=235)
entry_nomearquivo = tk.Entry(root, width=45)
entry_nomearquivo.place(x=220, y=235)

# Caixa para selecionar a pasta
label_salvar = tk.Label(root, text="Selecione a pasta que deseja salvar")
label_salvar.place(x=10, y=265)
entry_path = tk.Entry(root, width=45)
entry_path.place(x=220, y=265)


btn_selecionar_pasta = tk.Button(root, text="Browse", command=procurar_pasta)
btn_selecionar_pasta.configure(bg='lightblue', fg='black', font=('Helvetica', 9))
btn_selecionar_pasta.place(x=500, y=262)


# Botão salvar em Excel
btn_salvar_excel = tk.Button(root, text="Salvar em Excel", command=lambda: salvar_em_excel(entry_path.get()))
btn_salvar_excel.configure(bg='lightblue', fg='black', font=('Helvetica', 9))
btn_selecionar_pasta.configure(bg='lightblue', fg='black', font=('Helvetica', 9))
btn_salvar_excel.place(x=305, y=290)

# Botão fechar
fechar = tk.Button(root, text=" Fechar ", command=root.destroy)
fechar.place(x=500, y=420)
fechar.configure(bg="white", fg='red', font=('Helvetica', 9))

root.mainloop()