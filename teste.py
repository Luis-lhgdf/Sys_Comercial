valor_str = "R$60,58"

# Remover o símbolo de moeda e vírgulas
valor_str = valor_str.replace("R$", "").replace(",", ".") 

# Converter a string para float
valor_float = float(valor_str)

print(valor_float)
