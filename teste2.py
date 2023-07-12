import tkinter as tk
import tkinter.ttk as ttk
import re

# Lista de nomes aleatórios
nomes = ["Ana", "Carlos", "João", "Maria", "Pedro", "Lucas", "Lúcia", "Rafaela", "Ricardo", "Sandra"]

# Função para autocompletar o input do usuário
def autocomplete(text):
    return [nome for nome in nomes if re.match(f'^{text}', nome, re.IGNORECASE)]

# Função chamada ao selecionar um nome na lista
def selecionar_nome(event):
    selected_item = listbox.get(listbox.curselection())
    entry_var.set(selected_item)

# Função para filtrar a lista de nomes conforme o input do usuário
def atualizar_autocompletar(*args):
    listbox.delete(0, tk.END)
    if entry_var.get():
        suggestions = autocomplete(entry_var.get())
        for item in suggestions:
            listbox.insert(tk.END, item)

# Criação da janela principal
window = tk.Tk()
window.title("Autocompletar Nomes")
window.geometry("300x200")

# Variável de controle para o Entry
entry_var = tk.StringVar()

# Entry para o input do usuário
entry = ttk.Entry(window, textvariable=entry_var)
entry.pack(pady=10)
entry.bind("<KeyRelease>", atualizar_autocompletar)

# Listbox para mostrar as sugestões
listbox = tk.Listbox(window)
listbox.pack()

# Scrollbar para a Listbox

window.mainloop()