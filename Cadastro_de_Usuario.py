from time import sleep
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
   

    nome = input("Qual é o seu nome ? : ")
    print(f"Olá {nome} Seje benvindo ao nosso sistema de Cadastro de Usuarios")
    print("Iniciando o Sistema.......")
    sleep(5)
    print("----CADASTRO DE USUARIOS-----")   
    while True:
        

            us = cadastrar()
            usuarios.append(us) 
            d = input("Cadastrar novo Usuario ? [S/N] : ").strip().upper()
            if d == "S":
                continue
            elif d == "N":
                break
          


    users = input("Desejas ver os Usuarios Cadastrados ? [S/N] : ").strip().upper() 
    if users == "S":
        mostrar_usuarios(usuarios)
    elif users == "N":
        print("Programa Encerrado!")
                 
            



if __name__== "__main__":
    main()




        









    
