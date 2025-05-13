def soma(n1,n2):
    s = n1 + n2
    print(f"O resultado é : {s}")

def Subtracao(n1,n2):
    s = n1 - n2
    print(f"O resultado é : {s}")

def multi(n1,n2):
    m = n1 * n2
    print(f"O resultado é : {m}")

def div(n1,n2):
    d = n1 / n2
    print(f"O resultado é : {d}")


op = input("Qual operação desejas efetuar ? + | - | * | /  \n")
if op == "+":
    n1 = int(input("Digite o primero numero : \n "))
    n2 = int(input("Digite o segundo numero : \n"))
    soma(n1,n2)
elif op == "-":
    n1 = int(input("Digite o primero numero : \n "))
    n2 = int(input("Digite o segundo numero : \n"))
    Subtracao(n1,n2)

elif op == "*":
    n1 = int(input("Digite o primero numero : \n "))
    n2 = int(input("Digite o segundo numero : \n"))
    multi(n1,n2)    
elif op == "/":
    n1 = int(input("Digite o primero numero : \n "))
    n2 = int(input("Digite o segundo numero : \n"))
    div(n1,n2)
else:
    print("Operação Invalida")
    


