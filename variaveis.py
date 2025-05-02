nome =""
idade= 0
Altura = 0.0
salario=0000.000
Brasileiro=""


nome = input("Insira o seu nome : \n")
idade = int (input("Insira a sua idade: \n"))
Altura = float (input("Insiara a sua altura : \n"))

print("Seus Dados : \n")
print("Nome : \t",nome)
print("Idade: \t",idade)
print("Altura: \t", Altura)

salario = float(input("Qual é o seu salario ? \n"))
Brasileiro = bool(input("Voce é Brasileiro"))

print(f"o seu salario é {salario : .2f} \n respondeu {Brasileiro}sobre ser brasileiro ou não")