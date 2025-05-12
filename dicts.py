pessoa = {
    "nome" : "text",
    "idade" :00,
    "altura" : 00.00

}

print("DADOS DA PESSOA \n \n")
print("O nome da Pessoa é : ", pessoa["nome"])
print("A idade da Pessoa é : ", pessoa["idade"])
print("A altura da Pessoa é : ", pessoa["altura"])

pessoa["nome"] = "Gilson"
pessoa["idade"] = 18
pessoa["altura"] = 1.99

print("DADOS DA PESSOA \n")
print("O nome da Pessoa é : ", pessoa["nome"])
print("A idade da Pessoa é : ", pessoa["idade"])
print("A altura da Pessoa é :  ", pessoa["altura"])

pessoa["nome"] = input("Insira o nome da Pessoa :  ")
pessoa["idade"] = int(input("Insira a idade da Pessoa:  "))
pessoa["altura"] = float(input("Insira a altura da Pessoa: "))



print("DADOS DA PESSOA \n ")
print("O nome da Pessoa é : ", pessoa["nome"])
print("A idade da Pessoa é : ", pessoa["idade"])
print("A altura da Pessoa é : ", pessoa["altura"])

