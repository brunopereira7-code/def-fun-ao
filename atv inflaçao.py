import os 
import time 



def limpa_tela():
    time.sleep(3)
    os.system("cls") 


def preco_produto(valor):
    return valor 


def calcular_valor(valor):
    if valor <100:
        desconto=0.10

    else:
        desconto=0.20

    


def mostrar_resultado(produto,valor_produto,desconto_aplicado):
    valor_com_desconto=valor_produto*(1- desconto_aplicado)
    print(f"o produto é {produto}")
    print(f"o produto custa {valor_produto:.2f}")
    print(f"desconto aplicado:{desconto_aplicado *100:.0f}%") 
    print(f"preço com desconto {valor_com_desconto:.2f}") 

    


limpa_tela()

try:
    produtos=input("digite o produto:")
    preco=float(input("Digite o preço do produto"))
except ValueError:
    print("erro digite valor numerico.")
    exit() 

resultado=preco_produto(preco)
mostrar_resultado(produtos) 
