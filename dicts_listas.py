lista = []

for i in range(3):
    pessoa={}
    pessoa["nome"]= input(f"Insira o nome da pessoa {i} :  ")
    pessoa["idade"]= int(input(f"Insira a idade do {pessoa['nome']} :  "))
    pessoa["altura"] = float(input(f"Insira a Altura do {pessoa['nome']} :  "))
    lista.append(pessoa)

print("Dados das Pessoas : \n")

for pessoa in lista:
    print(f"Nome: {pessoa["nome"]}")
    print(f"Idade: {pessoa["idade"]}")
    print(f"Altura : {pessoa["altura"]}")
    print("\n")
