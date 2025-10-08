import os 
os.system("cls") 

numeros=[]
# n1=0
# n2=0



def calculos(n1, n2):
    calcular = {
        "soma": n1 + n2,               #forma de dicionario
        "subtracao": n1 - n2,
        "multiplicacao": n1 * n2,
        "divisao": n1 / n2 if n2 != 0 else "Divisão por zero"
    }
    return calcular


def mostrar_resultado(resultados):
    print(f"os numeros foram{numeros}")
    print("resultado dos calculos")
    for operacao,resultado in resultados.items():
        print(f"{operacao}: {resultado}")


for i in range(2):
    numero=int(input("Digite os numeros"))
    numeros.append(numero)
    #primeiro é o numero da lista depois o nome da variavel


resultado=calculos(numeros[0],numeros[1])
mostrar_resultado(resultado)