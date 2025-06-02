from time import sleep
def cadastrar(lista):
    usuario = {}
    usuario["nome"] = input("Nome : ").strip()
    
    while True:
        idade =input("Idade : ").strip()
        if idade.isdigit():
            usuario["idade"] = int(idade)
            break
        else:
            print("Digite idade valida!")

    while True:
        email = input("E-mail: ").strip()
        if any(user['email'] == email for user in lista):
            print("Este Email já foi usado, Crie outro!")
        else:
            usuario['email'] = email
            break  
                

    print("Usuario Cadastrado com Sucesso") 

    return usuario   


def usuarios_cadastrados(lista):
    if not lista:
         
         print("\n======USUARIOS CADASTRADOS=====")
         print("Ainda não há usuários Cadastrados.\n")
         return

    print("======USUARIOS CADASTRADOS===== \n ")
    for i, us in enumerate(lista, start=1):
        print("--" * 30)
        print(f"Usuario {i}")
        print("_______________")
        print(f"Nome: {us['nome']}")
        print(f"Idade: {us['idade']}")
        print(f"E-mail: {us['email']}")
        print("--" * 30)

def menu():

    usuarios = []
    print("=====CADASTRO DE USUARIOS=====")
    n = input("Olá, como te chamas?? ")
    print(f"Bem-vindo(a) {n} ao Cadastro de usuarios")
    print("Iniciando o sistema.......")
    sleep(5)
    while True:
        print()
        print("====MENU PRINCIPAL====")
        print()
        print("[1] Cadastrar Usuário")
        print("[2] Mostrar Usuarios Cadastrados")
        print("[3] Sair")
        try:

            op = int(input("Escolhe uma Opção: ").strip())
            if op == 1:
                user = cadastrar(usuarios)
                usuarios.append(user)
            elif op == 2:
                usuarios_cadastrados(usuarios) 
                
            elif op == 3:
                print("Encerrando o Sistema......")    
                sleep(5)
                print("Sistema Encerrado")      
                break
            else:
                print("Opção invalida!")
        except ValueError:
            print("Valor invalido, Insira outro Valor!")    
            continue    

   
    

        



if __name__=="__main__":
    menu()





    