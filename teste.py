import tkinter as tk
from tkinter import ttk
from faker import Faker



def generate_fake_data():
    fake = Faker()
    data = []
    for _ in range(500):
        data.append((fake.name(), fake.city(), fake.phone_number()))
    return data

def on_edit(event):
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, "values")

        entry_nome.delete(0, "end")
        entry_nome.insert(0, values[0])

        entry_cidade.delete(0, "end")
        entry_cidade.insert(0, values[1])

        entry_telefone.delete(0, "end")
        entry_telefone.insert(0, values[2])
   
    


def main():

    
    global tree, entry_nome, entry_cidade, entry_telefone

    root = tk.Tk()
    root.title("Exemplo de Treeview com 5000 Dados Fakes")

    # Criando o widget Treeview
    tree = ttk.Treeview(root, columns=("coluna1", "coluna2", "coluna3"), show="headings")

    # Definindo os cabeçalhos das colunas
    tree.heading("coluna1", text="Nome")
    tree.heading("coluna2", text="Cidade")
    tree.heading("coluna3", text="Telefone")

    # Definindo a largura das colunas
    tree.column("coluna1", width=200)
    tree.column("coluna2", width=200)
    tree.column("coluna3", width=150)

    # Gerando dados fake
    fake_data = generate_fake_data()

    # Inserindo os dados no Treeview
    for item in fake_data:
        tree.insert("", "end", values=item)

    # Adicionando uma barra de rolagem ao Treeview
    scroll_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll_y.set)
    scroll_y.pack(side="right", fill="y")

    # Criando as entradas
    entry_nome = tk.Entry(root, width=30)
    entry_cidade = tk.Entry(root, width=30)
    entry_telefone = tk.Entry(root, width=30)

    # Exibindo as entradas na janela
    entry_nome.pack(pady=5)
    entry_cidade.pack(pady=5)
    entry_telefone.pack(pady=5)

    # Exibindo o widget Treeview na janela
    tree.pack(fill="both", expand=True)

    # Vinculando o evento de seleção do Treeview à função on_edit()
    tree.bind("<<TreeviewSelect>>", on_edit)

    root.mainloop()

if __name__ == "__main__":
    main()

