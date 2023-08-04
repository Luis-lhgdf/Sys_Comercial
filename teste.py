import tkinter as tk

class MeuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exemplo de Botões")
        self.geometry("300x100")

        self.criar_widgets()

    def criar_widgets(self):
        # Botão 1
        self.botao1.pack(side=tk.LEFT)

        # Botão 2
        botao2 = tk.Button(self, text="Botão 2", command=self.funcao_botao2)
        botao2.pack(side=tk.LEFT)

        # Botão 3
        botao3 = tk.Button(self, text="Botão 3", command=self.funcao_botao3)
        botao3.pack(side=tk.LEFT)

    def funcao_botao1(self):
        print("Botão 1 foi clicado!")

    def funcao_botao2(self):
        print("Botão 2 foi clicado!")

    def funcao_botao3(self):
        print("Botão 3 foi clicado!")

    def outra_funcao(self):
        # Acessando o botao1 em outra função
        self.botao1.configure(text="Botão 1 Clicado")

if __name__ == "__main__":
    app = MeuApp()
    app.mainloop()

