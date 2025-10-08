import os
import time

def limpa_tela():
    time.sleep(3)
    os.system("cls")  # ou "clear" se estiver no Linux/Mac

def preco_produto(valor):
    return valor

def calcular_desconto(valor):
    if valor < 100:
        return 0.10
    else:
        return 0.20

def mostrar_resultado(valor_produto, desconto_aplicado):
    valor_com_desconto = valor_produto * (1 - desconto_aplicado)
    
    print(f"O produto custava: R${valor_produto:.2f}")
    print(f"Desconto aplicado: {desconto_aplicado * 100:.0f}%")
    print(f"Preço com desconto: R${valor_com_desconto:.2f}")

# ---- Execução do programa ----

limpa_tela()

# Entrada e conversão
try:
    preco = float(input("Digite o preço do produto: "))
except ValueError:
    print("Erro: digite um valor numérico válido.")
    exit()

# Processamento
resultado = preco_produto(produtos)
desconto = calcular_desconto(resultado)

# Saída
mostrar_resultado(resultado, desconto)
