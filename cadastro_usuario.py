usuarios = []

print("--------CADASTRO DE USUARIOS--------")
for i in range(100):
    us = {}
    us["nome"] = input("Nome: ").strip()
    us["idade"] = input("Idade: ").strip()
    us["email"] = input("E-mail:").strip()
    usuarios.append(us)
    d = input("Cadastrar Novo Usuario ? S/N : ").upper()
    if d == "S":
        continue
    elif d == "N":
        break
    
u = input("Queres ver os Usuarios Cadastrados ? S/N : ").upper()
if u == "S":
    print(" \t Usuarios Cadastrados  \n ")
    print(f"Usuario {i}")
    for i, usu in enumerate(usuarios, start=1):
        print("-" * 30)
        print(f" Nome : {usu["nome"]} ")
        print(f"Idade : {usu["idade"]}")
        print(f" E-mail :{usu["email"]} ")
        print("-" * 30)




