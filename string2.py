l = []

for i in range(19999):
    n = input("Insira um nome ou digite exite para encerrar  : \n")
   
    l.append(n)
    if n == "exite":
        print("Programa encerrado")
        break

l.pop()

    
nc = " ".join(l) #juntou os elementos da lista l
print(f"{nc} ") 
 

