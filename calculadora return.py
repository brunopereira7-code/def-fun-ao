

import os
os.system("cls") 

numeros=[]

def calculos(n1,n2):
    calcular=[ n1+n2, n1-n2, n1*n2, n1/n2 ]
    return calcular

def mostrar_resultado(lista_resultados,numeros_listados):
    print(f"os numeros foram: {numeros_listados}")
    print(f"o resultado da soma,subtraçao,multiplicacao,divisao foram: {lista_resultados}")

for i in range(2):
    numero=int(input(f"Digite o {i+1} numero:"))
    numeros.append(numero)

if len(numeros) ==2:

    resultado=calculos(numeros[0],numeros[1])
    mostrar_resultado(resultado,numeros)
else:
    print("erro digite um numero")

