def cadastrar(lista_existente_de_usuarios):
    """Cadastra um novo usuário, verificando se o e-mail já existe."""
    usuario = {}
    usuario["nome"] = input("Nome: ").strip()

    while True:
        idade_str = input("Idade: ").strip()
        if idade_str.isdigit():
            usuario["idade"] = int(idade_str)
            break
        else:
            print("Erro: Idade inválida. Digite apenas números.")

    while True:
        email_candidato = input("E-mail: ").strip()
        email_em_uso = False
        # Verifica se o email já existe na lista de usuários
        for u_existente in lista_existente_de_usuarios:
            if u_existente["email"] == email_candidato:
                email_em_uso = True
                break
        
        if email_em_uso:
            print("Erro: Este e-mail já está cadastrado. Tente outro.")
        else:
            usuario["email"] = email_candidato
            break
            
    print("\nUsuário cadastrado com sucesso!\n")
    return usuario


def mostrar_usuarios(lista_de_usuarios):
    """Mostra todos os usuários cadastrados."""
    if not lista_de_usuarios:
        print("\nNenhum usuário cadastrado ainda.\n")
        return

    print("\n--- Usuários Cadastrados ----\n")
    for i, usr in enumerate(lista_de_usuarios, start=1):
        print("-" * 33)
        print(f"Usuário {i}")
        print(f"Nome: {usr['nome']}")
        print(f"Idade: {usr['idade']}")
        print(f"E-mail: {usr['email']}")
        print("-" * 33)
    print()


def menu():
    """Exibe o menu principal e gerencia as operações do sistema."""
    usuarios = []  # Lista para armazenar os dicionários de usuários
    nome_operador = input("Olá! Como te chamas?: ").strip()
    print(f"\nOlá, {nome_operador}! Bem-vindo(a) ao Sistema de Cadastro.\n")

    print("===== MENU PRINCIPAL =====\n")
    while True:
        print("[1] Cadastrar Novo Usuário")
        print("[2] Mostrar Usuários Cadastrados")
        print("[3] Sair")
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            # Passa a lista atual de usuários para a função cadastrar
            # para permitir a verificação de e-mails duplicados
            novo_usuario = cadastrar(usuarios)
            usuarios.append(novo_usuario)
        elif op == "2":
            mostrar_usuarios(usuarios)
        elif op == "3":
            print("\nPrograma Encerrado. Até logo!")
            break
        else:
            print("\nOpção Inválida. Tente novamente.\n")


# Condição correta para iniciar o programa
if __name__ == "__main__":
    menu()