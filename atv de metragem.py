import os 
import time

def limpa_tela():
    time.sleep(3)
    os.system("cls") 


def converter_centimetro(numero):
    return numero *100


numeros=int(input("digite o numero"))

resultado=converter_centimetro(1)
print(f"resultado: {resultado} centimetros ")