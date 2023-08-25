import tkinter as tk
from tkinter import messagebox

def formatar_valor(valor_str):
    valor_str = valor_str.replace(".", "").replace(",", "")
    if valor_str.isdigit():
        valor_float = float(valor_str) / 100
        return f"R$ {valor_float:.2f}"
    return "Valor inválido"

def validar_caracteres(char):
    if char.isdigit() or char in [".", ","]:
        return True
    return False

def calcular(*args):
    valor_digitado = entry.get()
    valor_formatado = formatar_valor(valor_digitado)
    resultado_label.config(text=f"Valor digitado: {valor_formatado}")

# Criando a janela
janela = tk.Tk()
janela.title("Digite um Valor em Reais")

# Criando widgets
instrucao_label = tk.Label(janela, text="Digite um valor em Reais:")
entry = tk.Entry(janela, validate="key")
resultado_label = tk.Label(janela, text="")

# Definindo a validação de caracteres permitidos
entry['validatecommand'] = (entry.register(validar_caracteres), '%S')

# Posicionando widgets na janela
instrucao_label.pack(pady=10)
entry.pack(pady=5)

resultado_label.pack()

# Adicionando um trace para monitorar a digitação e ajustar automaticamente a formatação
var = tk.StringVar()
entry.config(textvariable=var)
var.trace("w", lambda name, index, mode, var=var: calcular())

# Iniciando o loop principal da interface
janela.mainloop()
