def criar_perfil_usuario(nome, idade, cidade):
    # Cria um dicionário com os dados
    usuario = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "ativo": True
    }
    return usuario # Retorna o dicionário inteiro

# Uso:
perfil = criar_perfil_usuario("Ana", 29, "Salvador")
print(f"Nome do usuário: {perfil['nome']}")   # Saída: Nome do usuário: Ana
print(f"Cidade: {perfil['cidade']}")         # Saída: Cidade: Salvador