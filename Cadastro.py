def cadastrar():
    usuario = {}
    usuario["nome"] = input("Nome : ")
    while True:
        idade = input("Idade : ").strip()
        if idade.isdigit():
            usuario["idade"] = int(idade)
            break
        else:
            print("Digite a idade Correta")
    while True:
        email = input("E-mail : ")
        if usuario["email"] != email:
            usuario["email"] = email
            break
        else:
            print("este email já existe!") 
    menu()       

    return usuario


def usuarios_cadastrados(lista):
    
    users = cadastrar()
    lista.append(users)
    for i, lem in enumerate(lista, start=1):
        print("---Usuarios Cadastrados---- \n ")
        print("-" *33)
        print(f"Usuario {i}")
        print(f"Nome : {lem['nome']}")
        print(f"Idade : {lem['idade']}")
        print(f"E-mail : {lem['email']}")
        print("-" * 33)

def menu():
    usuarios = []
    n = input(" Olá como te chamas ? : ")
    print(f"Olá {n} Ben-vindo ao Sistema de Cadastro \n")

    print("=====MENU PRINCIPAL===== \n \n")
    while True:

        op = input("[1] Cadastrar Novo Usuario \n [2] Mostrar Usuarios Cadastrados \n [3] Sair \n").strip()
        if op == 1:
            cadastrar()
        elif op == 2 :
            usuarios_cadastrados(usuarios)   
        elif op == 3:
            print("Programa Encerrado")
            break

        else:
            print("Opção Invalida")         


if __name__=="__main__":
    menu()      


