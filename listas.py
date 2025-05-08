lista = []


for i in range(12934945):
    d = int(input("Digite numeros para guardar nas listas ou  0 para Encerrar \n"))
    lista.append(d)
    if d == 0:
        print("Programa Encerrado")
        break
maior = max(lista)  
menor = min(lista)  
print(f"Foram adicionadas {len(lista)}")
print(f"O Maior numero digitado é :{maior} ")
print(f"O menor numero digitado é : {menor}")