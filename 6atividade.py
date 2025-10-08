# import os 
# os.system("cls") 

# numeros=[]
# quantidades_impares=0
# quantidades_pares=0

# def lista_numeros(numeros,quantidades_impares,quantidade_pares):

#     print(f"os numeros sao {numeros}") 
#     print(f"os numeros impares sao {quantidades_impares}") 
#     print(f"os numeros pares sao {quantidade_pares}") 

# for i in range(4):
#     numero=int(input("Digite o numero"))  
#     numeros.append(numero)
#     if numero % 2 ==0:
#         quantidades_pares+=1

#     else:
#         quantidades_impares+=1

# lista_numeros(numeros,quantidades_impares,quantidades_pares)


import os 
os.system("cls")
numeros=[]
quantidades_impares=0
quantidades_pares=0

def lista_numeros_corrigida(numeros, quantidades_impares, quantidade_pares):
        
    return {
            "numeros": numeros,
            "impares": quantidades_impares,
            "pares": quantidade_pares
        }
    for i in range(4):
        numero=int(input("digite seu numero"))
        numeros.append(numero)
        if numero % 2 ==0:
            quantidades_pares+=1
        else:
            quantidades_impares+=1
    # Chamando e armazenando o resultado
    dados = lista_numeros_corrigida(numeros,quantidades_impares,quantidades_pares)
    # def lista_numeros_corrigida(numeros, quantidade_pares, quantidades_impares):
    #     # Agora a chamada: lista_numeros_corrigida(numeros, quantidade_pares, quantidades_impares)
    #     # estaria correta.

    # Agora a variável 'dados' armazena o dicionário, não 'None'.
    print(f"\nLista de Números: {dados['numeros']}")
    print(f"Quantidade de Pares: {dados['pares']}")
    print(f"Quantidade de IMPares: {dados['impares']}")


    # def saudar(nome):
    #   """Esta função recebe um nome e retorna uma saudação."""
    #   return f"Olá, {nome}!"

    # # Chamando a função
    # mensagem = saudar("Maria")
    # print(mensagem) # Saída: Olá, Maria!



#  def saudar(nome):
#   """Esta função recebe um nome e retorna uma saudação."""
#   return f"Olá, {nome}!"

# # Chamando a função
# mensagem = saudar("Maria")
# print(mensagem) # Saída: Olá, Maria!




