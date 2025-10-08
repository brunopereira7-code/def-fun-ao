import os
os.system("cls") 

# A lista global para armazenar os números digitados
numeros = []

# Função para calcular, agora retornando uma LISTA para manter a ordem
def calculos(n1, n2):
    """Realiza os 4 cálculos básicos e retorna os resultados em uma lista."""
    # Usando lista [] para garantir a ordem e permitir resultados duplicados
    resultados_calculados = [n1 + n2, n1 - n2, n1 * n2, n1 / n2]
    return resultados_calculados

# Função para mostrar, agora recebendo os números originais como parâmetro
def mostrar_resultado(lista_resultados, numeros_originais):
    """Exibe os resultados dos cálculos e os números que foram usados."""
    print(f"\nOs números digitados foram: {numeros_originais}")
    print(f"Os resultados (Soma, Subtração, Multiplicação, Divisão) foram: {lista_resultados}")

# --- Lógica Principal do Programa ---

# 1. Coleta dos dois números
for i in range(2):
    # Usamos uma variável temporária 'numero_digitado'
    numero_digitado = int(input(f"Digite o {i+1}º número: "))
    # Adicionamos o número à lista 'numeros' (forma correta)
    numeros.append(numero_digitado)

# 2. Verifica se temos 2 números antes de calcular
if len(numeros) == 2:
    # 3. Chama a função de cálculo passando os dois números da lista
    # numeros[0] é o primeiro número, numeros[1] é o segundo
    resultado_final = calculos(numeros[0], numeros[1])

    # 4. Chama a função de exibição, passando os resultados E a lista de números original
    mostrar_resultado(resultado_final, numeros)
else:
    print("Erro: Não foram digitados dois números.")