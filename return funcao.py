import os
os.system("cls")

# Lista para armazenar todos os salários digitados
valor_salario = []

def calcular_desconto(salario):
    """
    Calcula o desconto com base no salário.
    Retorna True se o cálculo for bem-sucedido.
    Retorna False se houver erro (ex: salário inválido).
    """

    # Validação
    if salario <= 0:
        print("❌ Erro: salário inválido. Deve ser maior que zero.\n")
        return False  # Falha → não faz cálculo

    # Cálculo do desconto
    if salario > 100:
        desconto = 0.30
    elif salario < 100:
        desconto = 0.20
    else:
        desconto = 0.25  # exemplo de caso neutro

    salario_liquido = salario - (salario * desconto)

    # Mostra o resultado
    print(f"💰 Salário bruto: R${salario:.2f}")
    print(f"📉 Desconto aplicado: {desconto * 100:.0f}%")
    print(f"✅ Salário líquido: R${salario_liquido:.2f}\n")

    # Guarda os resultados em uma lista (como histórico)
    valor_salario.append({
        "salário_bruto": salario,
        "desconto_%": desconto * 100,
        "salário_liquido": salario_liquido
    })

    return True  # sucesso

# --------- PROGRAMA PRINCIPAL ---------
while True:
    try:
        salario = float(input("Digite seu salário (ou 0 para sair): "))

        if salario == 0:
            print("\nEncerrando o programa...")
            break

        # Chama a função e verifica se deu certo
        if calcular_desconto(salario):
            print("✅ Cálculo realizado com sucesso!\n")
        else:
            print("⚠️ Não foi possível calcular o desconto.\n")

    except ValueError:
        print("❗ Digite apenas números válidos.\n")

# --------- EXIBIÇÃO FINAL ---------
print("📊 HISTÓRICO DE SALÁRIOS CALCULADOS:")
for item in valor_salario:
    print(f"→ Bruto: R${item['salário_bruto']:.2f}")
    (f"Desconto: {item['desconto_%']:.0f}")
    (f"Líquido: R${item['salário_liquido']:.2f}")





# import os
# os.system("cls")
# valor_salario=[]

# def calcular_desconto(salario):
#     # """
#     # Função que calcula o desconto baseado no salário.
#     # Retorna:
#     #   - True → se o cálculo deu certo
#     #   - False → se houve erro
#     # """
#     if salario <= 0:
#         print("Erro: salário inválido. Deve ser maior que zero.")
#         return False  # ❌ erro → salário negativo ou zero

#     elif salario > 100:
#         desconto = 0.30
#     elif salario < 100:
#         desconto = 0.20
#     else:
#         desconto = 0  # caso neutro, não deve ocorrer

#     salario_liquido = salario - (salario * desconto)
    
    
#     print(f"Salário bruto: R${salario:.2f}")
#     print(f"Desconto aplicado: {desconto * 100:.0f}%")
#     print(f"Salário líquido: R${salario_liquido:.2f}")

    
#     return True  # ✅ sucesso → tudo certo

# # --- Programa principal ---
# salario = float(input("Digite seu salário: "))
# valor_salario.append(salario)

# # Aqui, verificamos se o retorno foi True ou False
# if calcular_desconto(salario):
#     print("\nCálculo realizado com sucesso!")
# else:
#     print("\nNão foi possível calcular o desconto.")
