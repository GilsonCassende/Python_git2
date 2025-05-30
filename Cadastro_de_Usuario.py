def cadastrar():
    usuario = {}
    usuario["nome"] = input("Nome : ")
    usuario["email"] = input("E-mail : ")
    while True:
        idade = input("Idade : ").strip()
        if idade.isdigit():
            usuario["idade"] = int(idade)
            break
        else:
            print("Digite uma idade valida!")
        
    
    return usuario

def mostrar_usuarios(lista):
    print("\t --USUARIOS CADASTRADOS-- ")
    for i, elem in enumerate(lista, start=1):
        print("-" *30)
        print(f"Usuario {i}")
        print(f"Nome : {elem['nome']}")
        print(f"E-mail : {elem['email']}")
        print(f"Idade : {elem['idade']}")
        print("-" *30)

def main():
    usuarios = []
    print("----CADASTRO DE USUARIOS-----")   
    while True:
        us = cadastrar()
        usuarios.append(us) 
        d = input("Cadastrar novo Usuario ? [S/N] : ").strip().upper()
        if d != "S":
            break
    users = input("Desejas ver os Usuarios Cadastrados ? [S/N] : ").strip().upper() 
    if users == "S":
        mostrar_usuarios(usuarios)
    else:
        print("Programa Encerrado!")



if __name__== "__main__":
    main()




        
    








    
