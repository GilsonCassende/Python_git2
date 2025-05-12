produtos = []


for i in range(5):
    produto = {}
    produto["ID"] = i
    produto["Nome"] = input("Insira o Nome do Produto :  ")
    produto["preço"] = float(input(f"Insira o Preço do produto :  "))
    produtos.append(produto.copy())
    print()

    d = input("Desejas criar Novo Produto ? S/N :  ").upper()
    if d == "S":
          continue
    elif d == "N":
          break
print()

c = input("Queres ver os Produtos Cadastrados S/N? \n ").upper() 
print()

if c == "S":

    print("Já foram Cadastrados os Seguintes Produtos : \n")
    for produt in produtos : 
                
                print(f"ID : {produt["ID"]}")
                print(f"Nome: {produt["Nome"]}")
                print(f"Preço : {produt["preço"]}")
                print()

    qt_p = len(produtos)
    print(f"Foram Cadastrados {qt_p} Produtos ")


elif c == "N":
     print("Programa Encerrado")

        
        
         
