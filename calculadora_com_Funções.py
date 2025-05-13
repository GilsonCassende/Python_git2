def calculadora(n1,n2):
    try:

        op = input("Qual operação desejas efetuar ? + | - | * | /  \n")
        if op == "+":
            soma = n1 + n2
            print(soma)
        elif op == "-":
            sub = n1 - n2
            print(sub)
        elif op == "*":
            multi = n1 * n2
            print(multi)  
        elif op == "/":
            div  = n1 / n2
            if n2 == 0:
                print("Erro de divisão por 0 ")
            print(div)
        
        
        else:
     
           print("Operação Invalida") 
    except ValueError:
        print("Erro: Você digitou um valor inválido. Use apenas números.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")   
    


n1 = int(input("Insira o Primeiro Numero : \n"))  
n2 = int(input("Insira o Segundo Numero : \n"))   

calculadora(n1,n2)

      


