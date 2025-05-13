def caixa_registradora(qt,pr):
    try:
        compras = int(input("Qual foi o Total de compras ? \n"))
        valor_total = (qt * pr) + compras
        print(f"O valor Total dos Produtos é : {valor_total}")

    except ValueError:
        print("Erro: Você digitou um valor inválido. Use apenas números.")

print(" \t \t CAIXA REGISTRADORA \n \n ")
try:
    nome = input("Insira o Nome do Produto: \n")
    if nome == " ":
         print("Erro: Produto sem nome")
except ValueError:
     print("Erro: Você digitou um valor inválido.")    
try:  
    qt = int(input("Insira a Quantidade do Produto:  \n"))
    pr = float(input("Insira o Preço do Produto : \n"))
except ValueError:
    
       print("Erro: Você digitou um valor inválido. Use apenas números.")  

caixa_registradora(qt,pr)
